from django.urls import path
from django.conf.urls.static import static
from django.conf import settings

from .views import turn_point_list, turn_point_detail, make_photos, make_two, make_three, status_point_detail, image_list, image_detail

app_name = 'api'

urlpatterns = [
    path('turn_point_list/', turn_point_list),
    path('turn_point/<int:pk>', turn_point_detail),

    path('make_photos/', make_photos, name='make_photos'),
    path('make_two/', make_two, name='make_two'),
    path('make_three/', make_three, name='make_three'),

    path('status_point_detail/<int:pk>', status_point_detail, name='status_point_detail'),

    path('image_list/', image_list, name='image_list'),
    path('image_detail/<int:pk>', image_detail, name='image_detail'),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)