from django.urls import path
from . import api_view


app_name = 'property'

urlpatterns = [
    path('api/list', api_view.PropertyApiList.as_view(), name='PropertyApiList'),
    path('api/list/ar', api_view.PropertyApiListAr.as_view(), name='PropertyApiListAr'),
    path('api/list/<int:pk>', api_view.PropertyApiDetail.as_view(), name='PropertyApiDetail'),
    path('api/list/ar/<int:pk>', api_view.PropertyApiDetailAR.as_view(), name='PropertyApiDetailAr'),
    path('api/category', api_view.Categories.as_view(), name='Categories'),
    path('api/category/ar', api_view.CategoriesAR.as_view(), name='CategoriesAr'),
    path('api/places', api_view.Places.as_view(), name='places'),
    path('api/places/ar', api_view.PlacesAR.as_view(), name='placesAR'),
    path('api/filtering/<str:slug>', api_view.TripsByFilters.as_view(), name='PropertyByCategory'),
    path('api/filtering/ar/<str:slug>', api_view.TripsByFiltersAR.as_view(), name='PropertyByCategoryAr'),
    path('api/inquiry', api_view.Inquiry.as_view(), name='inquiry'),
    path('api/visa', api_view.VisaSubmit.as_view(), name='visa'),
    path('api/list/<int:pk>/reservation', api_view.Reservation.as_view(), name='reservation'),
    path('api/ar/<int:pk>/reservation', api_view.Reservation.as_view(), name='reservationAR'),
    path('api/list/<int:pk>/review', api_view.Review.as_view(), name='review'),
    path('api/list/<int:pk>/fav', api_view.AddFavorite.as_view(), name='favorite'),
    path('dashboard', api_view.Dashboard.as_view(), name='dashboard'),
    path('dashboard/reservations/<int:pk>', api_view.delete_reservations, name='delete_reservations'),
    path('dashboard/reviews/<int:pk>', api_view.delete_review, name='delete_reviews'),
    path('dashboard/favorites/<int:pk>', api_view.delete_favorite, name='delete_favorites'),
]