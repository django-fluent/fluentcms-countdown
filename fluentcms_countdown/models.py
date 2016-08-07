from django.db import models
from django.utils.six import python_2_unicode_compatible
from django.utils.translation import ugettext_lazy as _
from django.utils.timezone import utc
from fluent_contents.models import ContentItem


@python_2_unicode_compatible
class CountDownItem(ContentItem):
    """
    Count-down timer to a deadline
    """
    title = models.CharField(_("Title"), max_length=200)

    until = models.DateTimeField(_("Count to"))
    format = models.CharField(_("Format"), max_length=15, default='dHMS', help_text=_("y=year, o=months, w=weeks, d=days, h=hours, m=minutes, s=seconds. Uppercase means it's always visible."))
    expiry_text = models.CharField(_("Expiry text"), max_length=200, blank=True, null=True)

    class Meta:
        verbose_name = _("Count-down timer")
        verbose_name_plural = _("Count-down timers")

    def __str__(self):
        return self.title

    @property
    def until_utc(self):
        # Provide 'until' format in UTC for templates
        return self.until.astimezone(utc)
