from django.contrib import admin

# Register your models here.
from nature_cards_rest.models import NatureImage, NatureCard

admin.site.register(NatureCard)
admin.site.register(NatureImage)
