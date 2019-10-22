from django.contrib import admin
from .models import Post #importamos el modelo

admin.site.register(Post) #registrar el modelo para que sea visible en el admin
