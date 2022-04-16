from django.db import models

machines=(
        (0,'Granos'),
        (1,'Granos chicos'),
        (2,'Mayor capacidad'),
        (3, 'Maquina estandar')
 )

class Maquina(models.Model):
    Id_Machine = models.BigAutoField(primary_key=True, null=False)
    User_id= models.BigIntegerField("user_id", null=True, blank=False)
    Address=models.CharField("Address", max_length=200, null=True, blank=False)
    Type_Machine=models.CharField("Machine_type", choices=machines, max_length=50, null=True, blank=False)
    Date_Create=models.DateField("Date_create", auto_now_add=True)
    Is_activate=models.BooleanField(verbose_name="maquina activa", default=False)
    Balance_Machine=models.BigIntegerField(null=False, blank=False)