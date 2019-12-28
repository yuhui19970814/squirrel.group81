from django.db import models

# Create your models here.
from django.utils.translation import gettext as _
from django.utils import timezone

class squirrels(models.Model):
   
    
    Longitude= models.DecimalField(max_digits=10,decimal_places=10)
    
    Latitude=models.DecimalField(max_digits=10,decimal_places=10)
    
    Unique_Squirrel_ID=models.CharField(max_length=30,unique=True)
    
    AM,PM='AM','PM'
    
    Shift=models.CharField(max_length=30, choices=((AM,'AM'),(PM,'PM'),),)
    
    Date=models.DateField(blank=True,null=True,max_length=30,default=timezone.now)
    
    adult,juvenile='Adult','Juvenile'
    age_choices=((adult,"Adult"),(juvenile, "Juvenile"),)
    Age=models.CharField(max_length=30,choices=age_choices,default=adult)
    
    gray,cinnamon,black='Gray','Cinnamon','Black'
    fur_choices=((gray,"Gray"),(cinnamon, "Cinnamon"),(black,"Black"),)
    Primary_fur_color=models.CharField(max_length=30,choices=fur_choices,default=gray)
    
    ground_plane,above_ground="Ground Plane","Above Ground"
    location_choices=((ground_plane,"Ground Plane"),(above_ground,"Above Ground"),)    
    Location=models.CharField(max_length=30,choices=location_choices,default=ground_plane)
    
    Specific_location=models.CharField(max_length=30,blank=True)
    
    Running=models.NullBooleanField(help_text='run')
    
    Chasing=models.NullBooleanField(help_text='Chase')
    
    Climbing=models.NullBooleanField(help_text='Climb')
    
    Eating=models.NullBooleanField(help_text='Eat')
    
    Foraging=models.NullBooleanField(help_text='Forage')
    
    Other_Activities=models.CharField(help_text='Others',max_length=30,)
    
    Kuks=models.NullBooleanField(help_text='Kuks')
    
    Quaas=models.NullBooleanField(help_text='Quaas')
    
    Moans=models.NullBooleanField(help_text='Moans')
    
    Tail_flags=models.NullBooleanField(help_text='Tailflags')
    
    Tail_twitches=models.NullBooleanField(help_text='Tail twitches')
    
    Approaches=models.NullBooleanField(help_text='Approaches')
    
    Indifferent=models.NullBooleanField(help_text='Indifferent')
    
    Runs_from=models.NullBooleanField(help_text='Runs from')
   
    def __str__(self):
        return self.Unique_Squirrel_ID
