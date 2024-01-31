from django.urls import path
from crmapp import views as v

urlpatterns = [
    path('', v.home, name='home'),
    
    # CRUD
    path('dashboard', v.dashboard, name='dashboard'),
    path('<user_id>/create_record', v.create_record, name='create_record'),
    path('update_record/<int:pk>', v.update_record, name='update_record'),
    path('record/<int:pk>', v.signular_record, name='record'),
    path('delete_record/<int:pk>/', v.delete_record, name='delete_record'),
]
