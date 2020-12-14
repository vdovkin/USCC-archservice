from django.db import models


class Standart(models.Model):
    title = models.CharField(max_length=200)
    standart_type = models.CharField(max_length=200)
    elements_type = models.CharField(max_length=200)
    number = models.CharField(max_length=100)

    def __str__(self):
        return self.title


class I_Beam(models.Model):
    standart = models.ForeignKey(Standart, on_delete=models.DO_NOTHING, blank=True)
    title = models.CharField(max_length=10)
    h = models.DecimalField(max_digits=5, decimal_places=1) # height
    b = models.DecimalField(max_digits=5, decimal_places=1) # leg width
    s = models.DecimalField(max_digits=3, decimal_places=1) # waist thickness
    t = models.DecimalField(max_digits=3, decimal_places=1) # averange leg thickness
    A = models.DecimalField(max_digits=6, decimal_places=2) #  Sectional Area
    P = models.DecimalField(max_digits=5, decimal_places=2) #  Weight per meter
    Iy = models.DecimalField(max_digits=10, decimal_places=3) # Moment of Inertia - horizontal axis
    Wy = models.DecimalField(max_digits=10, decimal_places=3) # Elastic Section Modulus - horizontal axis
    Sy = models.DecimalField(max_digits=10, decimal_places=3) # First moment of area - horizontal axis
    i_y = models.DecimalField(max_digits=4, decimal_places=1) # Radius of gyration- horizontal axis
    Iz = models.DecimalField(max_digits=10, decimal_places=3) # Moment of Inertia - vertical axis
    Wz = models.DecimalField(max_digits=10, decimal_places=3) # Elastic Section Modulus - vertical axis
    i_z = models.DecimalField(max_digits=4, decimal_places=1) # Radius of gyration- vertical axis

    def __str__(self):
        return "Двотавр " + str(self.title)




