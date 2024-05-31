from django.urls import path
from .views import EmpresaListView, EmpresaDetailView, UsuarioListView, UsuarioDetailView, ConsumoListView, ConsumoDetailView, BalonesListView, BalonesDetailView

urlpatterns = [
    path('empresas/', EmpresaListView.as_view(), name='empresa-list'),
    path('empresas/<int:empresa_id>/', EmpresaDetailView.as_view(), name='empresa-detail'),
    path('usuarios/', UsuarioListView.as_view(), name='usuario-list'),
    path('usuarios/<int:usuario_id>/', UsuarioDetailView.as_view(), name='usuario-detail'),
    path('consumos/', ConsumoListView.as_view(), name='consumo-list'),
    path('consumos/<int:consumo_id>/', ConsumoDetailView.as_view(), name='consumo-detail'),
    path('balones/', BalonesListView.as_view(), name='balones-list'),
    path('balones/<int:balones_id>/', BalonesDetailView.as_view(), name='balones-detail'),
]