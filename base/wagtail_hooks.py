from django.utils.html import format_html, format_html_join
from django.templatetags.static import static
from django.forms.widgets import Select

from wagtail import hooks
from wagtail.snippets.models import register_snippet
from wagtail.snippets.views.snippets import SnippetViewSet
from wagtail.admin.panels import FieldPanel, PublishingPanel, PageChooserPanel

from base.models import Menu, Article, Profile, Experience

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
        FieldPanel("anchor", icon="link"),
        FieldPanel("link_text", icon="title"),
        PublishingPanel(),
    ]


class ArticleViewSet(SnippetViewSet):
    model = Article

    panels = [
        FieldPanel("name"),
        FieldPanel("hero", icon="image"),
        FieldPanel("paragraph", icon="doc-empty"),
        FieldPanel("link_type", icon="link", widget=Select(attrs={'data-controller': 'conditional-snippet-link'})),
        PageChooserPanel("page_link", "basic.ArticlePage", icon="doc-empty"),
        FieldPanel("url", icon="link-external"),
        FieldPanel("link_text", icon="title"),
        FieldPanel("date", icon="date"),
        FieldPanel("reading_time", icon="time"),
        PublishingPanel(),
    ]


class ProfileViewSet(SnippetViewSet):
    model = Profile

    panels = [
        FieldPanel("name"),
        FieldPanel("image", icon="image"),
        FieldPanel("about_me", icon="doc-empty"),
        FieldPanel("social_links", icon="link"),
        PublishingPanel(),
    ]


class ExperienceViewSet(SnippetViewSet):
    model = Experience

    panels = [
        FieldPanel("name"),
        FieldPanel("company"),
        FieldPanel("from_date", icon="date"),
        FieldPanel("to_date", icon="date"),
        FieldPanel("current", icon="pick"),
        FieldPanel("link_type", icon="link", widget=Select(attrs={'data-controller': 'conditional-snippet-link'})),
        FieldPanel("page_link", icon="doc-empty"),
        FieldPanel("url", icon="link-external"),
        FieldPanel("link_text", icon="title"),
        FieldPanel("paragraph", icon="doc-empty"),
        PublishingPanel(),
    ]


register_snippet(MenuViewSet)
register_snippet(ArticleViewSet)
register_snippet(ProfileViewSet)
register_snippet(ExperienceViewSet)