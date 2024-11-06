from django.db import models

class BotUser(models.Model):
    user_id = models.CharField(max_length=120)
    name = models.CharField(max_length=120)
    username = models.CharField(max_length=120, null=True, blank=True)
    number = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.name)


# Create your models here.
class Catalog(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Carads(models.Model):
    id = models.AutoField(primary_key=True)
    catalog = models.ForeignKey(Catalog, on_delete=models.CASCADE, related_name='car_ads')
    name = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    pozitsiya = models.IntegerField()
    year = models.IntegerField()
    color = models.CharField(max_length=50)
    oil = models.TextField()
    mileage = models.IntegerField()
    description = models.TextField()
    status = models.BooleanField(default=False)  # Tasdiqlash holati
    created_by = models.CharField(max_length=20)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
    
class CarImage(models.Model):
    car = models.ForeignKey(Carads, related_name='img', on_delete=models.CASCADE)
    img = models.ImageField(upload_to='car/')

    def __str__(self):
        return f"Image for {self.car}"


class Houseads(models.Model):
    id = models.AutoField(primary_key=True)
    catalog = models.ForeignKey(Catalog, on_delete=models.CASCADE, related_name='house_ads')
    name = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    area = models.DecimalField(max_digits=10, decimal_places=2)
    rooms = models.IntegerField()
    location = models.TextField()
    description = models.TextField()
    status = models.BooleanField(default=False)
    created_by = models.CharField(max_length=20)
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.name


class HouseImage(models.Model):
    house = models.ForeignKey(Houseads, related_name='img', on_delete=models.CASCADE)
    img = models.ImageField(upload_to='house/')

    def __str__(self):
        return f"Image for {self.house}"



class Feedback(models.Model):
    user_id = models.CharField(max_length=120,null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    body = models.CharField(max_length=120, null=True, blank=True)

    def __str__(self):
        return str(self.body)  