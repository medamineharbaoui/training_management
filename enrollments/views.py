# enrollments/views.py
from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.decorators import action
from users.permissions import IsParticipant
from workshops.models import Workshop
from .models import Enrollment

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
