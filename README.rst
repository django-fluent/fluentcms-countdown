fluentcms-countdown
===================

A plugin for django-fluent-contents_ to show a countdown timer on a website.

Installation
============

First install the module, preferably in a virtual environment. It can be installed from PyPI::

    pip install fluentcms-countdown

Configuration
-------------

Next, create a project which uses the module::

    cd ..
    django-admin.py startproject fluentdemo

It should have the following settings::

    INSTALLED_APPS += (
        'fluent_contents',
        'fluentcms_countdown',
    )

The database tables can be created afterwards::

    ./manage.py syncdb

Now, the ``CountDownPlugin`` can be added to your ``PlaceholderField``
and ``PlaceholderEditorAdmin`` admin screens.

Finally, you'll have to add some CSS to the website.
This is purposefully left out.


Contributing
------------

If you like this module, forked it, or would like to improve it, please let us know!
Pull requests are welcome too. :-)

.. _django-fluent-contents: https://github.com/edoburu/django-fluent-contents
