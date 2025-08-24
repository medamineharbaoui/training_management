# enrollments/views.py
from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.decorators import action
from users.permissions import IsParticipant
from workshops.models import Workshop
from .models import Enrollment
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated

class ParticipantEnrollmentViewSet(viewsets.ViewSet):
    permission_classes = [IsParticipant]

    def list(self, request):
        workshops = Workshop.objects.all()
        return Response([{'id': w.id, 'title': w.title, 'trainer': w.trainer.username} for w in workshops])

    @action(detail=True, methods=['post'])
    def enroll(self, request, pk=None):
        workshop = Workshop.objects.get(pk=pk)
        enrollment, created = Enrollment.objects.get_or_create(participant=request.user, workshop=workshop)
        if not created:
            return Response({'detail': 'Already enrolled'}, status=status.HTTP_400_BAD_REQUEST)
        return Response({'detail': 'Enrolled successfully'})
    
class CheckEnrollmentView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, workshop_id):
        user_id = request.query_params.get("userId")
        if not user_id:
            return Response({"error": "userId is required"}, status=status.HTTP_400_BAD_REQUEST)

        enrolled = Enrollment.objects.filter(
            participant_id=user_id,
            workshop_id=workshop_id
        ).exists()

        return Response({"isEnrolled": enrolled})