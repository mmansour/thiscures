from django.db import models
from django.db.models import Q
from mezzanine.core.models import Displayable, RichTextField
from mezzanine.generic.fields import CommentsField, RatingField
from django.utils.translation import ugettext_lazy as _


class TreatmentPage(Displayable):

    subject_data = models.TextField(blank=True, verbose_name="Subject One Causes")
    subject_data_treatment = models.TextField(blank=True, verbose_name="Subject One Treatment")
    subject_data_natural_cures = models.TextField(blank=True, verbose_name="Subject One Natural Cures")
    subject_video = models.TextField(blank=True, verbose_name="Subject One Video")
    subject_image = models.ImageField(upload_to="uploads", blank=True, null=True,)
    subject_one_ad = models.TextField(blank=True, verbose_name="Subject Ad One")
    subject_data_sources = models.TextField(blank=True, verbose_name="Data Sources")

    allow_comments = models.BooleanField(default=True)
    is_title_case = models.BooleanField(default=True)
    comments = CommentsField(verbose_name=_("Comments"))
    rating = RatingField(verbose_name=_("Rating"))

    @models.permalink
    def get_absolute_url(self):
        return ('treatment.views.treatment',
                [self.slug,])

    def __unicode__(self):
        return self.title
