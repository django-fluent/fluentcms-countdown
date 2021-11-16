from datetime import datetime, timedelta, timezone

from django.test import TestCase
from fluent_contents.tests.factories import create_content_item
from fluent_contents.tests.utils import render_content_items

from fluentcms_countdown.models import CountDownItem


class ButtonTests(TestCase):
    """
    Testing private notes
    """

    def test_primary(self):
        """
        Test the standard button
        """
        item = create_content_item(
            CountDownItem, title="Until 2030", until=datetime(2030, 1, 1, 10, 0, 0, tzinfo=timezone(timedelta(hours=5))),
        )
        self.assertHTMLEqual(
            render_content_items([item]).html,
            '<div class="countdown" data-until="2030-01-01 05:00:00+00:00" data-expiry-text="null">'
            '  <p>Until 2030</p>'
            '  <span class="timer"></span>'
            '</div>'
        )
