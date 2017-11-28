from django.conf.urls import url, include
from rest_framework import routers
from nature_cards_rest.viewsets import UserViewSet, NatureCardsViewSet, NatureImagesViewSet

router = routers.DefaultRouter()
router.register(r'cards', NatureCardsViewSet, 'cards')
router.register(r'images', NatureImagesViewSet, 'images')
router.register(r'users', UserViewSet, 'userlist')

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    url(r'^', include(router.urls)),
]