# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('fluent_contents', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='CountDownItem',
            fields=[
                ('contentitem_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='fluent_contents.ContentItem', on_delete=models.CASCADE)),
                ('title', models.CharField(max_length=200, verbose_name='Title')),
                ('until', models.DateTimeField(verbose_name='Count to')),
                ('format', models.CharField(default=b'dHMS', help_text="y=year, o=months, w=weeks, d=days, h=hours, m=minutes, s=seconds. Uppercase means it's always visible.", max_length=15, verbose_name='Format')),
                ('expiry_text', models.CharField(max_length=200, null=True, verbose_name='Expiry text', blank=True)),
            ],
            options={
                'db_table': 'contentitem_fluentcms_countdown_countdownitem',
                'verbose_name': 'Count-down timer',
                'verbose_name_plural': 'Count-down timers',
            },
            bases=('fluent_contents.contentitem',),
        ),
    ]
