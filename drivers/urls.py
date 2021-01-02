from django.urls import path


from .views import drivers_list, add_driver, driver_details

urlpatterns = [
    path('drivers/', drivers_list, name='drivers_list'),
    path('drivers/add', add_driver, name='add_driver'),
    path('drivers/details/<int:pk>', driver_details, name='driver_details'),

]