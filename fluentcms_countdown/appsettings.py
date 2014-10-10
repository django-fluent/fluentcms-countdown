from django.conf import settings

# Default values
_js_min = "" if settings.DEBUG else ".min"
JQUERY_PLUGIN_JS = 'fluentcms_countdown/vendor/jquery.plugin{0}.js'.format(_js_min)
JQUERY_COUNTDOWN_JS = 'fluentcms_countdown/vendor/jquery.countdown{0}.js'.format(_js_min)
JQUERY_COUNTDOWN_LOCALE_JS = 'fluentcms_countdown/vendor/jquery.countdown-{locale}.js'
COUNTDOWN_JS = 'fluentcms_countdown/countdown.js'

# Offer flexibility to make sure developers can ensure there
# is only one jQuery.plugin instance is loaded, or allow developers to choose their own scripts.
JQUERY_PLUGIN_JS = getattr(settings, 'JQUERY_PLUGIN_JS', JQUERY_PLUGIN_JS)
JQUERY_COUNTDOWN_JS = getattr(settings, 'JQUERY_COUNTDOWN_JS', JQUERY_COUNTDOWN_JS)
COUNTDOWN_JS = getattr(settings, 'COUNTDOWN_JS', COUNTDOWN_JS)
