from django.utils.html import format_html, format_html_join
from django.templatetags.static import static
from django.forms.widgets import Select

from wagtail import hooks
from wagtail.snippets.models import register_snippet
from wagtail.snippets.views.snippets import SnippetViewSet
from wagtail.admin.panels import FieldPanel, PublishingPanel 

from base.models import Menu, Article

@hooks.register('insert_global_admin_css')
def global_admin_css():
    return format_html('<link rel="stylesheet" href="{}">', static('css/admin.css'))


@hooks.register('insert_editor_js')
def editor_js():
    # add more controller code as needed
    js_files = ['js/conditional-link-controller.js', 'js/conditional-snippet-link-controller.js']
    return format_html_join('\n', '<script src="{0}"></script>',
        ((static(filename),) for filename in js_files)
    )


class MenuViewSet(SnippetViewSet):
    model = Menu
    

    panels = [
        FieldPanel("name"),
        FieldPanel("icon", icon="pick"),
        FieldPanel("link_type", icon="link", widget=Select(attrs={'data-controller': 'conditional-snippet-link'})),
        FieldPanel("page_link", icon="doc-empty"),
        FieldPanel("url", icon="link-external"),
        FieldPanel("mailto", icon="mail"),
        FieldPanel("link_text", icon="title"),
        PublishingPanel(),
    ]


class ArticleViewSet(SnippetViewSet):
    model = Article

    panels = [
        FieldPanel("name"),
        FieldPanel("image", icon="image"),
        FieldPanel("paragraphs", icon="doc-empty"),
        FieldPanel("link_type", icon="link", widget=Select(attrs={'data-controller': 'conditional-snippet-link'})),
        FieldPanel("page_link", icon="doc-empty"),
        FieldPanel("url", icon="link-external"),
        FieldPanel("mailto", icon="mail"),
        FieldPanel("link_text", icon="title"),
        FieldPanel("date", icon="date"),
        FieldPanel("reading_time", icon="time"),
        PublishingPanel(),
    ]

# Instead of using @register_snippet as a decorator on the model class,
# register the snippet using register_snippet as a function and pass in
# the custom SnippetViewSet subclass.
register_snippet(MenuViewSet)
register_snippet(ArticleViewSet)