# workshops/views.py
from rest_framework import viewsets
from .models import Workshop
from .serializers import WorkshopSerializer
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response


from users.permissions import IsAdmin
from users.permissions import IsTrainer
from rest_framework.decorators import action

class WorkshopViewSet(viewsets.ModelViewSet):
    queryset = Workshop.objects.all()
    serializer_class = WorkshopSerializer
    permission_classes = [IsAuthenticated]

class AdminWorkshopViewSet(viewsets.ModelViewSet):
    queryset = Workshop.objects.all()
    serializer_class = WorkshopSerializer
    permission_classes = [IsAdmin]

    @action(detail=True, methods=['get'])
    def participants(self, request, pk=None):
        workshop = self.get_object()
        enrollments = workshop.enrollment_set.all()
        participants = [enrollment.participant.username for enrollment in enrollments]
        return Response({'participants': participants})

class TrainerWorkshopViewSet(viewsets.ReadOnlyModelViewSet):
    serializer_class = WorkshopSerializer
    permission_classes = [IsTrainer]

    def get_queryset(self):
        return Workshop.objects.filter(trainer=self.request.user)

    @action(detail=True, methods=['get'])
    def participants(self, request, pk=None):
        workshop = self.get_object()
        enrollments = workshop.enrollment_set.all()
        participants = [enrollment.participant.username for enrollment in enrollments]
        return Response({'participants': participants})
