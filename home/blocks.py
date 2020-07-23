from wagtail.core import blocks


class CourseBlock(blocks.StructBlock):
    """Block for courses"""

    institution = blocks.CharBlock(required=True, help_text="Intitutição")
    courses = blocks.ListBlock(blocks.CharBlock(required=True, help_text="Curso", icon='plus'),
     required=True)
    note = blocks.CharBlock(required=True, help_text="Descreva o estado ou nota final")
    begining_date = blocks.DateBlock(required=True, help_text="Data de Incio")
    finishing_date = blocks.DateBlock(required=False, help_text="Data de Término")


    class Meta:  # noqa
        template = "streams/course_block.html"
        icon = "fa-book"
        label = "Curso Formal"

class FreeCourseBlock(blocks.StructBlock):
    """Block for free courses"""

    institution = blocks.CharBlock(required=True, help_text="Intitutição")
    courses = blocks.ListBlock(blocks.CharBlock(required=True, help_text="Curso"))


    class Meta:  # noqa
        template = "streams/free_course_block.html"
        icon = "fa-group"
        label = "Curso Livre"

class JobBlock(blocks.StructBlock):
    """Block for job experience"""

    institution = blocks.CharBlock(required=True, help_text="Intitutição")
    job = blocks.CharBlock(required=True, help_text="Título")
    description = blocks.TextBlock(required=True, help_text="Descreva o trabalho")
    begining_date = blocks.DateBlock(required=True, help_text="Data de Incio")
    finishing_date = blocks.DateBlock(required=False, help_text="Data de Término")


    class Meta:  # noqa
        template = "streams/job_block.html"
        icon = "fa-building"
        label = "Experiência profissional"
