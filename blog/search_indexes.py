from haystack import indexes
from .models import Article


class ArticleIndex(indexes.SearchIndex, indexes.Indexable):
    text = indexes.CharField(document=True, use_template=True)
    auteur = indexes.CharField(model_attr='auteur')
    categorie = indexes.CharField(model_attr='categorie')
    contenu = indexes.CharField(model_attr='contenu')
    tags = indexes.MultiValueField(model_attr='tags__nom')
    auteurs_commentaires = indexes.MultiValueField(model_attr='commentaires__auteur__full_name')

    def get_model(self):
        return Article

    def index_queryset(self, using=None):
        """Used when the entire index for model is updated."""
        return self.get_model().objects.all()
