from django.db import models
from modelcluster.fields import ParentalKey
from wagtail.models import Page
from wagtail.fields import StreamField, RichTextField
from wagtail.admin.panels import FieldPanel, TabbedInterface, TitleFieldPanel, ObjectList
from wagtail.contrib.forms.models import AbstractEmailForm, AbstractFormField
from wagtail.admin.panels import (
    FieldPanel, FieldRowPanel,
    InlinePanel, MultiFieldPanel
)
from base.blocks import ContainerBlock

class BasicPage(Page):
    body = StreamField(
        [
            ("container", ContainerBlock()),
        ],
        blank=True,
    )

    content_panels = Page.content_panels + [
        FieldPanel("body"),
    ]

    subpage_types = ["basic.BasicPage", "basic.FormPage", "basic.ArticlePage"]


class FormField(AbstractFormField):
    page = ParentalKey('FormPage', on_delete=models.CASCADE, related_name='form_fields')

    field_width = models.CharField(
        max_length=15,
        choices=[
            ('col-span-1', 'Auto'),
            ('col-span-full', 'Full'),
        ],
        default='col-span-1'
    )

    panels = AbstractFormField.panels + [
        FieldPanel('field_width'),
    ]


class FormPage(AbstractEmailForm):
    thank_you_heading = models.CharField(blank=True)
    thank_you_text = RichTextField(blank=True)

    content_panels = [
        InlinePanel('form_fields', icon="form"),
    ]

    success_panels = [
        FieldPanel('thank_you_heading', icon="title"),
        FieldPanel('thank_you_text', icon="doc-full"),
    ]

    email_panels = [
        MultiFieldPanel([
            FieldRowPanel([
                FieldPanel('from_address', classname="col6"),
                FieldPanel('to_address', classname="col6"),
            ]),
            FieldPanel('subject'),
        ], heading="Email Configuration", icon="mail"),
    ]

    edit_handler = TabbedInterface([
        ObjectList(AbstractEmailForm.content_panels + content_panels, heading='Content'),
        ObjectList(success_panels, heading='Success'),
        ObjectList(email_panels, heading='Email'),
        ObjectList(AbstractEmailForm.promote_panels, heading='Promote'),
    ])

    subpage_types = []


class ArticlePage(Page):
    article = models.ForeignKey(
        'base.Article',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+'
    )

    content_panels = Page.content_panels + [
        FieldPanel("article"),
    ]

    subpage_types = []