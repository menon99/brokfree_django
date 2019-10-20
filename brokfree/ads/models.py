from django.db import models

class property(models.Model):
    lattitude=models.DecimalField(max_digits=8,decimal_places=5)
    longitude = models.DecimalField(max_digits=8, decimal_places=5)
    name=models.CharField(max_length=100)
    address=models.CharField(max_length=150)
    description=models.CharField(max_length=254)
    location=models.CharField(max_length=30)
    FURNISHING=(
        ('Full','Fully furnished'),
        ('Semi','Semi furnished'),
        ('Unfurnished','Unfurnished')
    )
    furnishing=models.CharField(max_length=5,choices=FURNISHING)
    FACING=(
        ('North','North'),
        ('South','South'),
        ('East','East'),
        ('West','West'),
        ('NA','NA')
    )
    facing=models.CharField(max_length=5,choices=FACING)
    WATER=(
        ('Corporation','Corporation'),
        ('Borewell','Borewell'),
        ('Both','Both'),
        ('NA','NA')
    )
    water=models.CharField(max_length=15,choices=WATER)
    bathroom=models.DecimalField(max_digits=1,decimal_places=0)
    bedroom = models.DecimalField(max_digits=1, decimal_places=0)
    CHOICE=(
        ('Yes','Yes'),
        ('No','No')
    )
    security = models.CharField(max_length=3, choices=CHOICE)
    non_veg = models.CharField(max_length=3, choices=CHOICE)
    lift = models.CharField(max_length=3, choices=CHOICE)
    AC = models.CharField(max_length=3, choices=CHOICE)
    swimming_pool = models.CharField(max_length=3, choices=CHOICE)
    servant_room = models.CharField(max_length=3, choices=CHOICE)
    gas_pipe = models.CharField(max_length=3, choices=CHOICE)
    sewage_trt = models.CharField(max_length=3, choices=CHOICE)
    v_parking = models.CharField(max_length=3, choices=CHOICE)
    gym = models.CharField(max_length=3, choices=CHOICE)
    club = models.CharField(max_length=3, choices=CHOICE)
    child_play_area = models.CharField(max_length=3, choices=CHOICE)
    park = models.CharField(max_length=3, choices=CHOICE)
    house_keeping = models.CharField(max_length=3, choices=CHOICE)
    internet = models.CharField(max_length=3, choices=CHOICE)
    intercom= models.CharField(max_length=3, choices=CHOICE)
    fire_safe= models.CharField(max_length=3, choices=CHOICE)
    shopping= models.CharField(max_length=3, choices=CHOICE)
    water_harv= models.CharField(max_length=3, choices=CHOICE)
    power_back= models.CharField(max_length=3, choices=CHOICE)
    rent=models.DecimalField(max_digits=7,decimal_places=0)
    deposit=models.DecimalField(max_digits=7,decimal_places=0)
    builtup=models.DecimalField(max_digits=7,decimal_places=0,default=0)
    btype=models.CharField(max_length=20)
    tenants=models.CharField(max_length=20)
    possession=models.CharField(max_length=15)
    parking=models.CharField(max_length=20)
    age=models.CharField(max_length=20)
    balcony=models.DecimalField(max_digits=1,decimal_places=0)

    def __str__(self):
        return self.address


