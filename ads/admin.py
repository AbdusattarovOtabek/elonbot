from django.contrib import admin
from django.core.exceptions import ValidationError
from django.forms import BaseInlineFormSet
from .models import Carads, Houseads, Catalog, CarImage, HouseImage, BotUser, Feedback
# Register your models here.
admin.site.register(Catalog)
admin.site.register(BotUser)
admin.site.register(Feedback)
class CarImageInline(admin.TabularInline):  
    model = CarImage
    extra = 1  
    max_num = 4  

    def get_max_num(self, request, obj=None, **kwargs):
        """
        Har bir mahsulot uchun maksimal ruxsat etilgan rasmlar sonini 4 ta qilib belgilaydi.
        """
        if obj and obj.img.count() >= 4:
            return 0  
        return self.max_num

@admin.register(Carads)
class CarAdmin(admin.ModelAdmin):
    inlines = [CarImageInline]
    list_display = ['name', 'price', 'year', 'color', 'mileage']
    search_fields = ['name']
    list_filter = ['year', 'color']

    def save_related(self, request, form, formsets, change):
        """
        Admin panelda mahsulotga bog'liq rasmlar sonini cheklash.
        """
        super().save_related(request, form, formsets, change)
        if form.instance.img.count() > 4:
            raise ValidationError("You can only upload up to 4 images for a product!")
        
class HouseImageInline(admin.TabularInline):
    model = HouseImage
    extra = 1  
    max_num = 4  # Admin panelda maksimal 4 ta rasm qo'shish mumkin

    # get_max_num metodida to'g'ri ishlatish
    def get_max_num(self, request, obj=None, **kwargs):
        """
        Har bir uy e'loniga maksimal 4 ta rasm ruxsat etiladi.
        """
        if obj and obj.img.count() >= 4:
            return 0  # 4 tadan oshsa, yangi rasm qo'shish mumkin bo'lmaydi
        return self.max_num
        
@admin.register(Houseads)
class HouseAdmin(admin.ModelAdmin):
    inlines = [HouseImageInline]
    list_display = ['name', 'price', 'area', 'rooms']
    search_fields = ['name']
    list_filter = ['rooms']

    def save_related(self, request, form, formsets, change):
        """
        Admin panelda mahsulotga bog'liq rasmlar sonini cheklash.
        """
        super().save_related(request, form, formsets, change)
        if form.instance.img.count() > 4:
            raise ValidationError("You can only upload up to 4 images for a product!")
        

