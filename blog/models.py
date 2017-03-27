from django.db import models


class Auteur(models.Model):
    prenom = models.CharField(max_length=100, null=False, blank=False)
    nom = models.CharField(max_length=100, null=False, blank=False)
    email = models.CharField(max_length=100, null=False, blank=False)

    def __unicode__(self):
        return "%s %s" % (self.prenom, self.nom)

    def full_name(self):
        return "%s %s" % (self.prenom, self.nom)


class Categorie(models.Model):
    nom = models.CharField(max_length=100)

    def __unicode__(self):
        return self.nom


class Tag(models.Model):
    nom = models.CharField(max_length=100)

    def __unicode__(self):
        return self.nom


class Article(models.Model):
    auteur = models.ForeignKey('Auteur', related_name='articles')
    categorie = models.ForeignKey('Categorie', related_name='articles')
    tags = models.ManyToManyField('Tag')
    titre = models.CharField(max_length=100)
    contenu = models.TextField()

    def __unicode__(self):
        return self.titre


class Commentaire(models.Model):
    auteur = models.ForeignKey('Auteur', related_name='commentaires')
    article = models.ForeignKey('Article', related_name='commentaires')
    contenu = models.TextField()

    def __unicode__(self):
        return "Commentaite #%s" % (self.id)
