from django.db import models
from django.contrib.contenttypes.fields import GenericRelation
from wagtail.models import PreviewableMixin, DraftStateMixin, LockableMixin, RevisionMixin, WorkflowMixin
from wagtail.search import index


class Menu(WorkflowMixin, DraftStateMixin, LockableMixin, RevisionMixin, index.Indexed, PreviewableMixin, models.Model):
    name = models.CharField(max_length=255)
    icon = models.CharField(
        max_length=15,
        choices=[
            ('home', 'Home'),
            ('folder', 'Folder'),
            ('briefcase', 'Briefcase'),
            ('tool', 'Tool'),
            ('contact', 'Contact'),
        ],
        default='home'
    )
    link_type = models.CharField(
        max_length=10,
        choices=[
            ("internal", "Internal"),
            ("external", "External"),
            ("mailto", "Mailto"),
        ],
        default="internal",
    )
    page_link = models.ForeignKey('wagtailcore.Page', null=True, blank=True, on_delete=models.CASCADE)
    url = models.URLField(null=True, blank=True)
    mailto = models.EmailField(null=True, blank=True)
    link_text = models.CharField(max_length=255)

    # Generic relations
    _revisions = GenericRelation("wagtailcore.Revision", related_query_name="menu")
    workflow_states = GenericRelation(
        "wagtailcore.WorkflowState",
        content_type_field="base_content_type",
        object_id_field="object_id",
        related_query_name="menu",
        for_concrete_model=False,
    )

    search_fields = [
        index.SearchField('name'),
        index.AutocompleteField('name'),
    ]

    @property
    def revisions(self):
        return self._revisions.all()

    def get_preview_template(self, request, mode_name):
        return "tags/previews/menu.html"

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = "Menu Item"
        verbose_name_plural = "Menu Items"