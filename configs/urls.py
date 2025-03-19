from django.urls import path
# from cars.views import CarsDetailView, CarListCreateView, CarsTestView
# from cars.models import CarsModel
from cars.views import CarCrud, CarsTestView

urlpatterns = [
    path('cars', CarsTestView.as_view()),
    path('cars/<int:pk>',CarCrud.as_view())
]
