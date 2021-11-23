from django.urls import path
from crud import views
from .views import *
urlpatterns=[
      path('listar',views.Listar.as_view(),name='listar'),
      path('crear',views.Crear.as_view(),name='crear'),
      path('<int:pk>',views.VistaInd.as_view(),name='detalle'),
      path('<int:pk>/update',views.Actualizar.as_view(),name='actualizar'),
      path('<int:pk>/delete',views.Eliminar.as_view(),name='eliminar'),
      path('genpdf', views.GenPdf, name='sale_invoice_pdf'),
]