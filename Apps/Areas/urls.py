from django.urls import path
from .views import DepartamentoListAPIView
from .views import DepartamentoListAPIView, DepartamentoDetail, DepartamentoListSubdepartamentosView

urlpatterns = [
    path('', DepartamentoListAPIView.as_view(), name='departamento-list-create'),
    path('<int:pk>/', DepartamentoDetail.as_view(), name='departamento-detail'),
    path('departamentos/', DepartamentoListSubdepartamentosView.as_view(), name='departamento-list-subdepartamentos'),

]