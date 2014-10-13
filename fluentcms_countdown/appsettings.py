from django.conf import settings

_js_min = "" if settings.DEBUG else ".min"

# Default values
JQUERY_PLUGIN_JS = 'fluentcms_countdown/vendor/jquery.plugin{0}.js'.format(_js_min)
JQUERY_COUNTDOWN_JS = 'fluentcms_countdown/vendor/jquery.countdown{0}.js'.format(_js_min)
JQUERY_COUNTDOWN_LOCALE_JS = 'fluentcms_countdown/vendor/jquery.countdown-{locale}.js'
COUNTDOWN_JS = 'fluentcms_countdown/countdown.js'

# Make sure only known languages are submitted to the client.
COUNTDOWN_JS_LANGUAGE_CODES = (
    'ar', 'bg', 'bn', 'bs', 'ca', 'cs', 'cy', 'da', 'de', 'el', 'es', 'et', 'fa', 'fi', 'fo', 'fr',
    'gl', 'gu', 'he', 'hr', 'hu', 'hy', 'id', 'is', 'it', 'ja', 'kn', 'ko', 'lt', 'lv', 'ml', 'ms',
    'my', 'nb', 'nl', 'pl', 'pt-BR', 'ro', 'ru', 'sk', 'sl', 'sq', 'sr-SR', 'sr', 'sv', 'th', 'tr',
    'uk', 'ur', 'uz', 'vi', 'zh-CN', 'zh-TW',
)

# Offer flexibility to make sure developers can ensure there
# is only one jQuery.plugin instance is loaded, or allow developers to choose their own scripts.
JQUERY_PLUGIN_JS = getattr(settings, 'JQUERY_PLUGIN_JS', JQUERY_PLUGIN_JS)
JQUERY_COUNTDOWN_JS = getattr(settings, 'JQUERY_COUNTDOWN_JS', JQUERY_COUNTDOWN_JS)
COUNTDOWN_JS = getattr(settings, 'COUNTDOWN_JS', COUNTDOWN_JS)
