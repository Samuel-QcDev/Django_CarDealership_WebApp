from django.db import models
from django.utils.timezone import now


# Create your models here.

# <HINT> Create a Car Make model `class CarMake(models.Model)`:
# - Name
# - Description
# - Any other fields you would like to include in car make model
# - __str__ method to print a car make object

# Car Make model
class CarMake(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(null=False, max_length=30)
    description = models.CharField(max_length=1000,null=True)

    def __str__(self):
        return "Name: " + self.name + "," + \
               "Description: " + self.description

# <HINT> Create a Car Model model `class CarModel(models.Model):`:
# - Many-To-One relationship to Car Make model (One Car Make has many Car Models, using ForeignKey field)
# - Name
# - Dealer id, used to refer a dealer created in cloudant database
# - Type (CharField with a choices argument to provide limited choices such as Sedan, SUV, WAGON, etc.)
# - Year (DateField)
# - Any other fields you would like to include in car model
# - __str__ method to print a car make object
# Car model
class CarModel(models.Model):
    SUV = 'Suv'
    SEDAN = 'Sedan'
    WAGON = 'Wagon'
    COUPE = 'Coupe'
    SPORT = 'Sport'
    HATCHBACK = 'Hatchback'
    CONVERTIBLE = 'Convertible'
    MINIVAN = 'Minivan'
    CAR_TYPES = [
        (SEDAN, 'Sedan'),
        (SUV, 'SUV'),
        (WAGON, 'Wagon'),
        (COUPE, 'Coupe'),
        (SPORT, 'Sport'),
        (HATCHBACK, 'Hatchback'),
        (CONVERTIBLE, 'Convertible'),
        (MINIVAN, 'Minivan'), 
    ]
    id = models.AutoField(primary_key=True)
    name = models.CharField(null=False, max_length=100, default='Car Model')
    type = models.CharField(max_length=15, choices=CAR_TYPES)
    year = models.CharField(max_length=10,default='year')
    make = models.ForeignKey(CarMake, null=False, on_delete=models.CASCADE)

    def __str__(self):
        return  self.name + ", " + \
                self.type + ", " + \
                self.year

# <HINT> Create a plain Python class `CarDealer` to hold dealer data


# <HINT> Create a plain Python class `DealerReview` to hold review data
