from django.db import models

class Persona(models.Model):
    """Model definition fos Persona."""

    nombre = models.CharField(verbose_name="Nombre completo", max_length=50)
    edad = models.IntegerField(verbose_name="Edad")
    email = models.EmailField(verbose_name="Correo electronico", max_length=254)

    class Meta:
        """Meta definition fos Persona."""

        verbose_name = 'Persona'
        verbose_name_plural = 'Personas'

    def __str__(self):
        """Unicode representation os Persona."""
        return f"{self.nombre} - {self.email}"


