from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    # path('delete/<int:widget_id>', views.WidgetDelete, name='delete_widget')
    path('widget/<int:pk>/delete/', views.WidgetDelete.as_view(), name='delete_widget'),
]