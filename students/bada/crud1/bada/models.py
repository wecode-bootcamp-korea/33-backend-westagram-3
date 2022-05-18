from django.db import models

class Menu(models.Model):
    name = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now=True)

    class Meta:
            db_table = "menu"

class Category(models.Model):
    name = models.CharField(max_length=50)
    menu = models.ForeignKey('Menu', on_delete=models.CASCADE) # menu_id_id
    created_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = "categories"

class Drink(models.Model):
    korean_name = models.CharField(max_length=50)
    english_name = models.CharField(max_length=50)
    description = models.TextField(max_length=50)
    category = models.ForeignKey('Category', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now=True)

    class Meta:
            db_table = "drink"

class Image(models.Model):
    image_url = models.CharField(max_length=2000)
    drink = models.ForeignKey('Drink', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now=True)

    class Meta:
            db_table = "images"

class Allergy_Drink(models.Model):
    drink = models.ForeignKey('Drink', on_delete=models.CASCADE)
    allergy = models.ForeignKey('Allergy', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now=True)

    class Meta:
            db_table = "allergy_drink"

class Allergy(models.Model):
    name = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = "allergy"

class Nutrition(models.Model):
    # django model decimal
    one_serving_kca = models.DecimalField(max_digits = 10, decimal_places = 2)
    sodium_mg = models.DecimalField(max_digits = 10, decimal_places = 2)
    saturated_fat_g = models.DecimalField(max_digits = 10, decimal_places = 2)
    sugars_g = models.DecimalField(max_digits = 10, decimal_places = 2)
    protein_g = models.DecimalField(max_digits = 10, decimal_places = 2)
    caffeine_mg = models.DecimalField(max_digits = 10, decimal_places = 2)
    drink = models.ForeignKey('Drink', on_delete=models.CASCADE)
    size = models.ForeignKey('Size', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = "nutritions"

class Size(models.Model):
    name = models.CharField(max_length=50)
    size_ml = models.CharField(max_length=50)
    size_fluid_ounce = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = "sizes"
