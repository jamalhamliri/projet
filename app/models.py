"""
Module models.py pour la gestion des Models de l'application.
"""
from django.db import models


class ArticleType(models.Model):
    """
    Model for storing types of articles.
    """
    name = models.CharField(max_length=50)

    def __str__(self):
        """
        Return the name of the article type.
        """
        return str(self.name)


class Article(models.Model):
    """
    Model for storing articles.
    """
    title = models.CharField(max_length=200)
    content = models.TextField(blank=True)
    publication_date = models.DateTimeField(auto_now_add=True)
    fichier = models.FileField(upload_to='media/fichier/', blank=True)
    image = models.ImageField(upload_to='media/article_photos/', blank=True)
    article_type = models.ForeignKey(ArticleType, on_delete=models.CASCADE)

    def __str__(self):
        """
        Return the title of the article.
        """
        return str(self.title)

    @property
    def image_url(self):
        """
        Return the URL of the image.
        """
        try:
            url = self.image.url
        except Exception as e:
            url = ''
            print(e)
        return url

    @property
    def fichier_url(self):
        """
        Return the URL of the fichier.
        """
        try:
            url = self.fichier.url
        except Exception as e:
            url = ''
            print(e)
        return url


class Slide(models.Model):
    """
    Model for storing slides.
    """
    titre = models.CharField(max_length=200, blank=True)
    image = models.ImageField(upload_to='media/slide/', blank=True)
    date_expiration = models.DateField()
    add_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        """
        Return the title of the slide.
        """
        return str(self.titre)

    @property
    def image_url(self):
        """
        Return the URL of the image.
        """
        try:
            url = self.image.url
        except Exception as e:
            url = ''
            print(e)
        return url


class Events(models.Model):
    """
    Model for storing events.
    """
    title = models.CharField(max_length=200)
    description = models.CharField(max_length=255, blank=True)
    date_event = models.DateField()
    duree = models.CharField(max_length=200)

    def __str__(self):
        """
        Return the title of the event.
        """
        return str(self.title)


class Niveau(models.Model):
    """
    Model for storing education levels.
    """
    niveau = models.CharField(max_length=250)

    def __str__(self):
        return str(self.niveau)


class Filiere(models.Model):
    """
    Model for storing study programs.
    """
    filiere = models.CharField(max_length=250)

    def __str__(self):
        return str(self.filiere)


class EmploisTemps(models.Model):
    """
    Model for storing class schedules.
    """
    niveau = models.ForeignKey(Niveau, on_delete=models.CASCADE)
    filiere = models.ForeignKey(Filiere, on_delete=models.CASCADE)
    emplois_du_temps = models.FileField(upload_to='media/emplois_du_temps/')

    @property
    def fichier_url(self):
        """
        Property that returns the URL
        of the emploi_du_temps file,
        or an empty string if not available.
        """
        try:
            url = self.emplois_du_temps.url
        except Exception as e:
            url = ''
            print(e)
        return url
