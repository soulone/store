from django.contrib import admin

# Register your models Productos
from .models import Producto

admin.site.register(Producto)

# Register your models Admins.
from .models import Admin

admin.site.register(Admin)
