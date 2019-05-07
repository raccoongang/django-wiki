from wiki.models import URLPath
from django.views.generic.detail import DetailView
from django.views.generic.base import View
from wiki.core.paginator import WikiPaginator
from django.http import JsonResponse, Http404, HttpResponseBadRequest
from django.views.decorators.http import require_http_methods
from taggit.models import Tag
from unidecode import unidecode
from django.template.defaultfilters import slugify
from django.contrib import messages
from django.utils.translation import gettext_lazy as _


class TagIndexView(DetailView):
    template_name = 'wiki/tag.html'
    model = Tag
    context_object_name = 'tag'
    slug_url_kwarg = 'slug'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        root = self.kwargs.get('path')
        if root not in [URLPath.WIKI, URLPath.NPB]:
            raise Http404("Page does not exist")

        context['categories'] = URLPath.objects.filter(
            tags__slug=self.object.slug, root_type=root, item_type=URLPath.CATEGORY
        )
        context['articles'] = URLPath.objects.filter(
            tags__slug=self.object.slug, root_type=root, item_type=URLPath.ARTICLE
        )
        return context


@require_http_methods(["POST"])
def update_tag(request):
    instance = request.POST.get('instance', '')
    if not instance:
        return HttpResponseBadRequest()
    try:
        urlpath = URLPath.objects.get(slug=instance)
    except URLPath.DoesNotExist:
        return HttpResponseBadRequest()

    urlpath.tags.clear()
    tag_list = request.POST.get('tags', None)
    if tag_list:
        tag_slugs = tag_list.split(',')
    else:
        tag_slugs = []

    for tag_slug in tag_slugs:
        try:
            tag = Tag.objects.get(slug=tag_slug)
        except Tag.DoesNotExist:
            slug = slugify(unidecode(tag_slug))
            tag = Tag.objects.create(name=tag_slug, slug=slug)
        urlpath.tags.add(tag)
    return JsonResponse({'success': 'OK'})
