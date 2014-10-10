from django.conf import settings
from django.forms import Media
from django.utils.translation import ugettext_lazy as _
from fluent_contents.extensions import ContentPlugin, plugin_pool
from .models import CountDownItem
from . import appsettings

# Make sure only known languages are submitted to the client.
JS_LANGUAGE_CODES = (
    'ar', 'bg', 'bn', 'bs', 'ca', 'cs', 'cy', 'da', 'de', 'el', 'es', 'et', 'fa', 'fi', 'fo', 'fr',
    'gl', 'gu', 'he', 'hr', 'hu', 'hy', 'id', 'is', 'it', 'ja', 'kn', 'ko', 'lt', 'lv', 'ml', 'ms',
    'my', 'nb', 'nl', 'pl', 'pt-BR', 'ro', 'ru', 'sk', 'sl', 'sq', 'sr-SR', 'sr', 'sv', 'th', 'tr',
    'uk', 'ur', 'uz', 'vi', 'zh-CN', 'zh-TW',
)




@plugin_pool.register
class CountDownPlugin(ContentPlugin):
    """
    Count-down timer for a deadline
    """
    model = CountDownItem
    render_template = "fluentcms_countdown/countdown.html"
    category = _("Sidebar widgets")

    def get_frontend_media(self, instance):
        #
        # Base scripts
        js = [
            appsettings.JQUERY_PLUGIN_JS,
            appsettings.JQUERY_COUNTDOWN_JS,
        ]

        # Localize for the given instance
        language, locale = _to_locale_name(instance.language_code)
        if locale in JS_LANGUAGE_CODES:
            js.append(appsettings.JQUERY_COUNTDOWN_LOCALE_JS.format(locale=locale))
        elif language in JS_LANGUAGE_CODES:
            js.append(appsettings.JQUERY_COUNTDOWN_LOCALE_JS.format(locale=language))

        # And the main script
        js.append(appsettings.COUNTDOWN_JS)

        # Remove any None values, allow developers to exclude scripts
        js = [file for file in js if file]

        # No CSS, provide your own styling.
        return Media(js=js)


def _to_locale_name(language_code):
    # Convert a language code (e.g. nl-nl) to a locale (nl-NL)
    # The locale uses a dash instead of _, to match the vendor filenames.
    language_code =language_code.replace('_', '-')
    if '-' in language_code:
        language, country = language_code.split()
        return language_code, "{0}-{1}".format(language, country.upper())
    else:
        return language_code, language_code
