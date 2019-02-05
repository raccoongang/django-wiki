from wiki.models import URLPath
from wiki.views.article import Dir


class CategoryListView(Dir):

    def get_queryset(self):
        qs = super().get_queryset()
        if self.urlpath.root_type == URLPath.NPB:
            return qs.filter(item_type=URLPath.CATEGORY, root_type=URLPath.NPB)
        else:
            return qs.filter(item_type=URLPath.CATEGORY, root_type=URLPath.WIKI)

    def get_template_names(self):
        return ["wiki/wiki_home.html"]
