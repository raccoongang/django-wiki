from wiki.models import URLPath
from wiki.views.article import Dir


class CategoryListView(Dir):

    def get_queryset(self):
        qs = super().get_queryset()
        return qs.filter(item_type=URLPath.CATEGORY)

    def get_template_names(self):
        return ["wiki/wiki_home.html"]
