from rest_framework import viewsets, filters
from rest_framework import permissions
from nature_cards_rest.serializers import UserSerializer, NatureCardSerializer, NatureImageSerializer # import our serializer
from nature_cards_rest.models import NatureCard, NatureImage # import our model
from django.contrib.auth.models import User
from nature_cards_rest.permissions import IsOwner, IsCardOwner, IsStaffOrTargetUser
from rest_framework.permissions import AllowAny

class UserViewSet(viewsets.ModelViewSet):
    """
    This viewset automatically provides `list` and `detail` actions.
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer
    def get_permissions(self):
        #allow non-authenticated user to create via POST
        return (AllowAny() if self.request.method == 'POST' else IsStaffOrTargetUser()),

class NatureCardsViewSet(viewsets.ModelViewSet):
    """
    This viewset automatically provides `list`, `create`, `retrieve`,
    `update` and `destroy` actions.
    """
    #queryset = NatureCard.objects.all()
    serializer_class = NatureCardSerializer
    permission_classes = (permissions.IsAuthenticated, IsOwner,)

    def get_queryset(self):
        """
        This view should return a list of all the cards
        for the currently authenticated user.
        """
        user = self.request.user
        return NatureCard.objects.filter(owner=user)

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

class NatureImagesViewSet(viewsets.ModelViewSet):
    #queryset = NatureImage.objects.all()
    serializer_class = NatureImageSerializer
    permission_classes = (permissions.IsAuthenticated, IsCardOwner,)

    def get_queryset(self):
        """
        This view should return a list of all the images
        for the currently authenticated user.
        """
        user = self.request.user
        return NatureImage.objects.filter(card__owner=user)


