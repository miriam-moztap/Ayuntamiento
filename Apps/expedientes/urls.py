from django.urls import path
from .views import ExpedienteAPIView, SingleExpedienteAPIGetUpdateDeleteView

urlpatterns = [
    path('', ExpedienteAPIView.as_view(), name='expediente'),
    
    path('<int:id>/', SingleExpedienteAPIGetUpdateDeleteView.as_view()),

]