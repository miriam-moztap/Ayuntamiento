from django.urls import path
from .views import SingleDocumentAPIView, DocumentAPIView, TipoDocumentoListView, TipoDocumentoDetailView

urlpatterns = [
    path('', DocumentAPIView.as_view(), name='document'),
    path('<int:id>/', SingleDocumentAPIView.as_view()),
    path('tipo-documento/', TipoDocumentoListView.as_view(), name='tipo-documento-list'),
    path('tipo-documento/<int:pk>/', TipoDocumentoDetailView.as_view(), name='tipo-documento-detail'),
]
