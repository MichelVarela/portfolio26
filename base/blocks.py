from wagtail.blocks import (
    CharBlock,
    ChoiceBlock,
    StructBlock,
    RichTextBlock,
    ListBlock,
    PageChooserBlock,
    URLBlock,
    StreamBlock,
    DateBlock,
    BooleanBlock,
)
from wagtail.snippets.blocks import SnippetChooserBlock
from wagtail.images.blocks import ImageChooserBlock
from wagtail.documents.blocks import DocumentChooserBlock
from wagtail.embeds.blocks import EmbedBlock
from django.core.validators import EmailValidator
from wagtail.fields import NoFutureDateValidator

from base.choices import SIZE_CHOICES, GAP_CHOICES, GAP_X_CHOICES, GAP_Y_CHOICES, PADDING_TOP_CHOICES, PADDING_BOTTOM_CHOICES

class LinkBlock(StructBlock):
    link_type = ChoiceBlock(
        choices=[
            ("internal", "Internal"),
            ("external", "External"),
            ("mailto", "Mailto"),
            ("phone", "Phone"),
            ("image", "Image"),
            ("document", "Document"),
            ("anchor", "Anchor"),
        ],
        default="internal",
        required=True,
    )
    page_link = PageChooserBlock(required=False)
    url = URLBlock(required=False)
    mailto = CharBlock(validators=[EmailValidator()], required=False)
    phone = CharBlock(required=False)
    image = ImageChooserBlock(required=False)
    document = DocumentChooserBlock(required=False)
    anchor = CharBlock(required=False)
    link_text = CharBlock(required=True)
    
    class Meta:
        template = "blocks/link.html"
        icon = "link"
        label = "Link"
        preview_value = {"link_type": "internal", "page_link": "https://www.google.com", "url": "https://www.google.com", "mailto": "https://www.google.com", "phone": "https://www.google.com", "asset": "https://www.google.com", "anchor": "https://www.google.com", "link_text": "John Doe"}
        preview_template = "blocks/previews/link.html"
        form_classname = 'link-block struct-block'
        form_attrs = {'data-controller': 'conditional-link'}


class FormEmbedBlock(StructBlock):
    form_page = PageChooserBlock(required=True, page_type="basic.FormPage")
    
    class Meta:
        template = "blocks/form_embed.html"
        icon = "form"
        label = "Form Embed"
        preview_value = {"form_page": "https://www.google.com"}
        preview_template = "blocks/previews/form_embed.html"
        form_classname = 'form-embed-block struct-block'
    

class ProfileCardBlock(StructBlock):
    image = ImageChooserBlock(required=True)
    name = CharBlock(required=True)
    about_me = CharBlock(required=True)
    social_links = ListBlock(StructBlock(
        [
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
        ]
    ))
    
    class Meta:
        template = "blocks/profile_card.html"
        icon = "user"
        label = "Profile Card"
        preview_value = {"image": "https://via.placeholder.com/150", "name": "John Doe"}
        preview_template = "blocks/previews/profile_card.html"


class ProjectCardBlock(StructBlock):
    image = ImageChooserBlock(required=True)
    heading = CharBlock(required=True)
    subheading = CharBlock(required=True)
    link = LinkBlock(required=True)
    
    class Meta:
        template = "blocks/project_card.html"
        icon = "folder-inverse"
        label = "Project Card"
        preview_value = {"image": "https://via.placeholder.com/150", "heading": "John Doe"}
        preview_template = "blocks/previews/project_card.html"


class ExperienceCardBlock(StructBlock):
    heading = CharBlock(required=True)
    paragraph = RichTextBlock(required=True)
    link = LinkBlock(required=True)
    from_date = DateBlock(required=True, validators=[NoFutureDateValidator()])
    to_date = DateBlock(required=True, validators=[NoFutureDateValidator()])
    current = BooleanBlock(required=False)
    
    class Meta:
        template = "blocks/experience_card.html"
        icon = "folder-open-1"
        label = "Experience Card"
        preview_value = {"heading": "John Doe", "paragraph": "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nullam nec metus vel ante convallis finibus. Nullam nec metus vel ante convallis finibus. Nullam nec metus vel ante convallis finibus.", "link": {"link_type": "internal", "page_link": "https://www.google.com", "url": "https://www.google.com", "mailto": "https://www.google.com", "link_text": "John Doe"}, "from_date": "2022-01-01", "to_date": "2022-01-01", "current": True}
        preview_template = "blocks/previews/experience_card.html"


class ArticleCardBlock(StructBlock):
    article = SnippetChooserBlock(required=True, target_model="base.Article")
    
    class Meta:
        template = "blocks/article_card.html"
        icon = "draft"
        label = "Article Card"
        preview_value = {"article": "https://www.google.com"}
        preview_template = "blocks/previews/article_card.html"
        form_classname = 'article-card-block struct-block'


class ToolCardBlock(StructBlock):
    image = ImageChooserBlock(required=True)
    heading = CharBlock(required=True)
    subheading = CharBlock(required=True)
    link = LinkBlock(required=True)    
    
    class Meta:
        template = "blocks/tool_card.html"
        icon = "pick"
        label = "Tool Card"
        preview_value = {"image": "https://via.placeholder.com/150", "heading": "John Doe", "subheading": "John Doe", "link": {"link_type": "internal", "page_link": "https://www.google.com", "url": "https://www.google.com", "mailto": "https://www.google.com", "link_text": "John Doe"}}
        preview_template = "blocks/previews/tool_card.html"
        form_classname = 'tool-card-block struct-block'


class InformativeNumber(StructBlock):
    number = CharBlock(required=True)
    title = CharBlock(required=True)
    
    class Meta:
        template = "blocks/informative_number.html"
        icon = "superscript"
        label = "Informative Number"
        preview_value = {"number": "10", "title": "Years of Experience"}
        preview_template = "blocks/previews/informative_number.html"


class CardSkillBlock(StructBlock):
    title = CharBlock(required=True)
    link = LinkBlock(required=True)
    background = ChoiceBlock(
        choices=[
            ("bg-portfolio-orange", "Orange"),
            ("bg-portfolio-green", "Green"),
        ],
        default="bg-portfolio-orange",
        required=True,
    )
    icon = ChoiceBlock(
        choices=[
            ("dynamic", "Dynamic"),
            ("square", "Square"),
        ],
        default="dynamic",
        required=True,
    )
    
    class Meta:
        template = "blocks/card_skill.html"
        icon = "user"
        label = "Card Skill"
        preview_value = {"title": "John Doe", "background": "orange", "icon": "dynamic", "page_link": "https://www.google.com", "url_link": "https://www.google.com"}
        preview_template = "blocks/previews/card_skill.html"


class HeadingWithTwoLinesBlock(StructBlock):
    line_one = CharBlock(required=True)
    line_two = CharBlock(required=True)
    size = ChoiceBlock(
        choices=[
            ("h2", "H2"),
            ("h3", "H3"),
            ("h4", "H4"),
            ("h5", "H5"),
            ("h6", "H6"),
        ],
        default="h2",
        required=True,
    )
    text_align = ChoiceBlock(
        choices=[
            ("text-left", "left"),
            ("text-center", "center"),
            ("text-right", "right"),
        ],
        default="text-left",
        required=True,
    )
    
    class Meta:
        template = 'blocks/heading_with_two_lines.html'
        icon = "title"
        label = "Heading with Two Lines"
        preview_value = {"line_one": "Healthy bread types", "line_two": "Healthy bread types", "size": "h2", "text_align": "left"}
        preview_template = "blocks/previews/heading_with_two_lines.html"
        form_classname = 'heading-with-two-lines-block struct-block'


class HeadingBlock(StructBlock):
    heading_text = CharBlock(required=True)
    size = ChoiceBlock(
        choices=[
            ("h2", "H2"),
            ("h3", "H3"),
            ("h4", "H4"),
            ("h5", "H5"),
            ("h6", "H6"),
        ],
        default="h2",
        required=True,
    )
    text_align = ChoiceBlock(
        choices=[
            ("text-left", "left"),
            ("text-center", "center"),
            ("text-right", "right"),
        ],
        default="text-left",
        required=True,
    )

    class Meta:
        template = 'blocks/heading.html'
        icon = "title"
        label = "Heading"
        preview_value = {"heading_text": "Healthy bread types", "size": "h2", "text_align": "left"}
        description = "A heading with level two, three, four, five or six"
        preview_template = "blocks/previews/heading.html"
        form_classname = 'heading-block struct-block'


class ParagraphBlock(StructBlock):
    content = RichTextBlock()

    class Meta:
        template = "blocks/paragraph.html"
        icon = "doc-full"
        label = "Paragraph"
        preview_value = {"content": "<p>Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.</p>"}
        preview_template = "blocks/previews/paragraph.html"


class ImageBlock(StructBlock):
    image = ImageChooserBlock(required=True)
    caption = CharBlock(required=False)
    attribution = CharBlock(required=False)

    class Meta:
        template = "blocks/image.html"
        icon = "image"
        label = "Image"
        preview_value = {"caption": "A beautiful scenery", "attribution": "Photo by John Doe"}
        preview_template = "blocks/previews/image.html"


class VideoBlock(StructBlock):
    video = EmbedBlock()

    class Meta:
        template = "blocks/video.html"
        icon = "media"
        label = "Video"
        preview_value = {"video": "https://www.youtube.com/watch?v=dQw4w9WgXcQ"}
        preview_template = "blocks/previews/video.html"


class SpacerBlock(StructBlock):
    height = ChoiceBlock(
        choices=SIZE_CHOICES,
        default="h-6",
        required=True,
    )

    class Meta:
        template = "blocks/spacer.html"
        icon = "collapse-up"
        label = "Spacer"
        preview_value = {"height": "h-6"}
        preview_template = "blocks/previews/spacer.html"


class ButtonAreaBlock(StructBlock):
    buttons = ListBlock(LinkBlock())
    direction = ChoiceBlock(
        choices=[
            ("horizontal", "Horizontal"),
            ("vertical", "Vertical"),
        ],
        default="horizontal",
        required=True,
    )
    gap = ChoiceBlock(
        choices=GAP_CHOICES,
        default="gap-0",
        required=True,
    )

    class Meta:
        template = "blocks/button_area.html"
        icon = "grip"
        label = "Button Area"
        preview_value = {
            "direction": "horizontal",
            "gap": "gap-0",
            "buttons": [
                {"text": "Primary Action", "url_link": "https://example.com"},
                {"text": "Secondary Action", "url_link": "https://example.com"},
            ]
        }
        preview_template = "blocks/previews/button_area.html"


class BoxBlock(StructBlock):
    direction = ChoiceBlock(
        choices=[
            ("flex-col", "Vertical"),
            ("flex-row", "Horizontal"),
        ],
        default="flex-row",
        required=True,
    )
    vertical_alignment = ChoiceBlock(
        choices=[
            ("items-start", "Start"),
            ("items-center", "Center"),
            ("items-end", "End"),
        ],
        default="items-start",
        required=True,
    )
    horizontal_alignment = ChoiceBlock(
        choices=[
            ("justify-start", "Start"),
            ("justify-center", "Center"),
            ("justify-end", "End"),
            ("justify-between", "Between"),
            ("justify-around", "Around"),
            ("justify-evenly", "Evenly"),
        ],
        default="justify-start",
        required=True,
    )
    gap = ChoiceBlock(
        choices=GAP_CHOICES,
        default="gap-0",
        required=True,
    )
    content = StreamBlock(
        [
            ("informative_number", InformativeNumber()),
            ("card_skill", CardSkillBlock()),
            ("tool_card", ToolCardBlock()),
        ]
    )

    class Meta:
        template = "blocks/box.html"
        icon = "radio-empty"
        label = "Box"
        preview_value = {
            "vertical_alignment": "flex-row",
            "horizontal_alignment": "justify-start",
            "gap": "gap-0",
            "content": [
                {"type": "informative_number", "value": {"number": "10", "title": "Years of Experience"}},
            ]
        }
        preview_template = "blocks/previews/box.html"
        form_classname = 'box-block struct-block'


class BoxGridBlock(StructBlock):
    layout = ChoiceBlock(
        choices=[
            ("grid-cols-1", "Full"),
            ("lg:grid-cols-2", "2 Columns"),
            ("md:grid-cols-3", "3 Columns"),
            ("md:grid-cols-4", "4 Columns"),
            ("lg:grid-cols-[1fr_2fr]", "4/8 Columns"),
            ("lg:grid-cols-[2fr_1fr]", "8/4 Columns"),
        ],
        default="grid-cols-1",
        required=True,
    )
    gap = ChoiceBlock(
        choices=GAP_CHOICES,
        default="gap-0",
        required=True,
    )
    content = StreamBlock(
        [
            ("informative_number", InformativeNumber()),
            ("card_skill", CardSkillBlock()),
            ("tool_card", ToolCardBlock()),
        ]
    )

    class Meta:
        template = "blocks/box_grid.html"
        icon = "radio-full"
        label = "Box Grid"
        preview_value = {
            "layout": "grid-cols-1",
            "gap": "gap-0",
            "content": [
                {"type": "informative_number", "value": {"number": "10", "title": "Years of Experience"}},
            ]
        }
        preview_template = "blocks/previews/box_grid.html"
        form_classname = 'box-grid-block struct-block'


class ColumnBlock(StructBlock):
    layout = ChoiceBlock(
        choices=[
            ("col-span-full", "Full"),
            ("col-auto", "Auto"),
        ],
        default="col-auto",
        required=True,
    )
    content = StreamBlock(
        [
            ("heading", HeadingBlock()),
            ("paragraph", ParagraphBlock()),
            ("image", ImageBlock()),
            ("video", VideoBlock()),
            ("spacer", SpacerBlock()),
            ("button_area", ButtonAreaBlock()),
            ("profile_card", ProfileCardBlock()),
            ("heading_with_two_lines", HeadingWithTwoLinesBlock()),
            ("informative_number", InformativeNumber()),
            ("box", BoxBlock()),
            ("box_grid", BoxGridBlock()),
            ("project_card", ProjectCardBlock()),
            ("experience_card", ExperienceCardBlock()),
            ("tool_card", ToolCardBlock()),
            ("article_card", ArticleCardBlock()),
            ("form_embed", FormEmbedBlock()),
        ],
        required=True,
    )

    class Meta:
        template = "blocks/column.html"
        icon = "grip"
        label = "Column"
        preview_value = {
            "layout": "col-auto",
            "content": [
                {"type": "paragraph", "value": {"content": "<p>Column content goes here.</p>"}},
            ]
        }
        preview_template = "blocks/previews/column.html"


class ContainerBlock(StructBlock):
    layout = ChoiceBlock(
        choices=[
            ("grid-cols-1", "Full"),
            ("md:grid-cols-[repeat(1,_34.625rem)] lg:grid-cols-[repeat(1,_28.5rem)] xl:grid-cols-[repeat(1,_36rem)] 3xl:grid-cols-[repeat(1,_47.25rem)]", "Small"),
            ("lg:grid-cols-[repeat(1,_39rem)] xl:grid-cols-[repeat(1,_49rem)] 3xl:grid-cols-[repeat(1,_64rem)]", "Medium"),
            ("lg:grid-cols-[repeat(1,_49.5rem)] xl:grid-cols-[repeat(1,_62rem)] 3xl:grid-cols-[repeat(1,_80.75rem)]", "Large"),
            ("lg:grid-cols-2", "2 Columns"),
            ("md:grid-cols-3", "3 Columns"),
            ("md:grid-cols-4", "4 Columns"),
            ("lg:grid-cols-[1fr_2fr]", "4/8 Columns"),
            ("lg:grid-cols-[2fr_1fr]", "8/4 Columns"),
        ],
        default="grid-cols-1",
        required=True,
    )
    gap_x = ChoiceBlock(
        choices=GAP_X_CHOICES,
        default="gap-x-0",
        required=True,
    )
    gap_y = ChoiceBlock(
        choices=GAP_Y_CHOICES,
        default="gap-y-0",
        required=True,
    )
    padding_top = ChoiceBlock(
        choices=PADDING_TOP_CHOICES,
        default="none",
        required=True,
    )
    padding_bottom = ChoiceBlock(
        choices=PADDING_BOTTOM_CHOICES,
        default="none",
        required=True,
    )
    columns = ListBlock(ColumnBlock())

    class Meta:
        template = "blocks/container.html"
        icon = "folder"
        label = "Container"
        preview_value = {
            "layout": "lg:grid-cols-2",
            "gap_x": "gap-x-0",
            "gap_y": "gap-y-0",
            "padding_top": "none",
            "padding_bottom": "none",
            "columns": [
                {
                    "layout": "full",
                    "content": [{"type": "paragraph", "value": {"content": "<p>Left column</p>"}}]
                },
                {
                    "layout": "full",
                    "content": [{"type": "paragraph", "value": {"content": "<p>Right column</p>"}}]
                }
            ]
        }
        preview_template = "blocks/previews/container.html"
        form_classname = 'container-block struct-block'