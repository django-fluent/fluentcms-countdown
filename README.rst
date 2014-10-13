fluentcms-countdown
===================

A plugin for django-fluent-contents_ to show a countdown timer on a website.

It's based on the jQuery plugin found at: http://keith-wood.name/countdown.html

Installation
============

First install the module, preferably in a virtual environment. It can be installed from PyPI::

    pip install fluentcms-countdown


Backend Configuration
---------------------

First make sure the project is configured for django-fluent-contents_.

Then add the following settings::

    INSTALLED_APPS += (
        'fluentcms_countdown',
    )

The database tables can be created afterwards::

    ./manage.py syncdb

Now, the ``CountDownPlugin`` can be added to your ``PlaceholderField``
and ``PlaceholderEditorAdmin`` admin screens.


Frontend Configuration
----------------------

Make sure that all plugin media files are exposed by django-fluent-contents_::

    {% load frontend_contents_tags %}

    {% render_content_items_media %}

This tag should be placed at the bottom of the page, after all plugins are rendered.
For more configuration options - e.g. integration with django-compressor -
see the `template tag documentation <http://django-fluent-contents.readthedocs.org/en/latest/templatetags.html#frontend-media>`_.

CSS Code
~~~~~~~~

The stylesheet code is purposefully left out, since authors typically like to provide their own styling.

To get started quickly, include ``fluentcms_countdown/vendor/jquery.countdown.css`` in your site.

JavaScript Code
~~~~~~~~~~~~~~~

No configuration is required for the JavaScript integration,

By default, the plugin includes all required JavaScript code to run the timer.

The includes can be customized however, using the following settings::

    JQUERY_PLUGIN_JS = 'fluentcms_countdown/vendor/jquery.plugin.min.js'

    JQUERY_COUNTDOWN_JS = 'fluentcms_countdown/vendor/jquery.countdown.min.js'

    JQUERY_COUNTDOWN_LOCALE_JS = 'fluentcms_countdown/vendor/jquery.countdown-{locale}.js'

    COUNTDOWN_JS = 'fluentcms_countdown/countdown.js'

For example, if another plugin also uses ``jquery.plugin.js``, redefine the setting, so both plugins use the same file::

    JQUERY_PLUGIN_JS = 'mysite/vendor/jquery.plugin.min.js'

If a value is defined as ``None``, it will be excluded from the frontend media.

HTML code
~~~~~~~~~

If needed, the HTML code can be overwritten by redefining ``fluentcms_countdown/countdown.html``.
Any ``data-...`` attributes on the ``countdown`` element will be read by the JavaScript code;
this can be used to provide custom settings to the countdown init script.

Contributing
------------

If you like this module, forked it, or would like to improve it, please let us know!
Pull requests are welcome too. :-)

.. _django-fluent-contents: https://github.com/edoburu/django-fluent-contents
