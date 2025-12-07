from django.db import models
from django.contrib.contenttypes.fields import GenericRelation
from wagtail.models import PreviewableMixin, DraftStateMixin, LockableMixin, RevisionMixin, WorkflowMixin
from wagtail.search import index
from wagtail.fields import RichTextField, NoFutureDateValidator, StreamField
from wagtail.blocks import ChoiceBlock, StructBlock
from base.blocks import LinkBlock


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
            ("anchor", "Anchor"),
        ],
        default="internal",
    )
    page_link = models.ForeignKey('wagtailcore.Page', null=True, blank=True, on_delete=models.CASCADE, related_name="+",)
    url = models.URLField(null=True, blank=True)
    anchor = models.CharField(max_length=255, null=True, blank=True)
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


class Article(WorkflowMixin, DraftStateMixin, LockableMixin, RevisionMixin, index.Indexed, PreviewableMixin, models.Model):
    name = models.CharField(max_length=255)
    hero = models.ForeignKey('wagtailimages.Image', null=True, blank=True, on_delete=models.SET_NULL, related_name='+')
    paragraph = RichTextField(blank=True)
    link_type = models.CharField(
        max_length=10,
        choices=[
            ("internal", "Internal"),
            ("external", "External"),
        ],
        default="internal",
    )
    page_link = models.ForeignKey('wagtailcore.Page', null=True, blank=True, on_delete=models.CASCADE, related_name="+", )
    url = models.URLField(null=True, blank=True)
    link_text = models.CharField(max_length=255)
    date = models.DateField(null=True, blank=True, validators=[NoFutureDateValidator()])
    reading_time = models.CharField(max_length=255)

    # Generic relations
    _revisions = GenericRelation("wagtailcore.Revision", related_query_name="article")
    workflow_states = GenericRelation(
        "wagtailcore.WorkflowState",
        content_type_field="base_content_type",
        object_id_field="object_id",
        related_query_name="article",
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
        return "tags/previews/article.html"

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = "Article"
        verbose_name_plural = "Articles"


class Profile(WorkflowMixin, DraftStateMixin, LockableMixin, RevisionMixin, index.Indexed, PreviewableMixin, models.Model):
    image = models.ForeignKey('wagtailimages.Image', null=True, blank=True, on_delete=models.SET_NULL, related_name='+')
    name = models.CharField(max_length=255)
    about_me = models.TextField(null=True, blank=True)
    social_links = StreamField([
        ("social_link", StructBlock([
            ("icon", ChoiceBlock(
                choices=[
                    ("email", "Email"),
                    ("linkedin", "LinkedIn"),
                    ("github", "GitHub"),
                ],
                default="email",
                required=True,
            )),
            ("link", LinkBlock(required=True)),
        ]))
    ], null=True, blank=True)

    # Generic relations
    _revisions = GenericRelation("wagtailcore.Revision", related_query_name="profile")
    workflow_states = GenericRelation(
        "wagtailcore.WorkflowState",
        content_type_field="base_content_type",
        object_id_field="object_id",
        related_query_name="profile",
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
        return "tags/previews/profile.html"

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = "Profile"
        verbose_name_plural = "Profiles"


class Experience(WorkflowMixin, DraftStateMixin, LockableMixin, RevisionMixin, index.Indexed, PreviewableMixin, models.Model):
    name = models.CharField(max_length=255)
    company = models.CharField(max_length=255)
    from_date = models.DateField(null=True, blank=True, validators=[NoFutureDateValidator()])
    to_date = models.DateField(null=True, blank=True, validators=[NoFutureDateValidator()])
    current = models.BooleanField(default=False)
    link_type = models.CharField(
        max_length=10,
        choices=[
            ("internal", "Internal"),
            ("external", "External"),
        ],
        default="internal",
    )
    page_link = models.ForeignKey('wagtailcore.Page', null=True, blank=True, on_delete=models.CASCADE, related_name="+", )
    url = models.URLField(null=True, blank=True)
    link_text = models.CharField(max_length=255)
    paragraph = models.TextField(null=True, blank=True)

    # Generic relations
    _revisions = GenericRelation("wagtailcore.Revision", related_query_name="experience")
    workflow_states = GenericRelation(
        "wagtailcore.WorkflowState",
        content_type_field="base_content_type",
        object_id_field="object_id",
        related_query_name="experience",
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
        return "tags/previews/experience.html"

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = "Experience"
        verbose_name_plural = "Experiences"
    