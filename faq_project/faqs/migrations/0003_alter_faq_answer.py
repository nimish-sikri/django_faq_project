# Generated by Django 5.1.5 on 2025-02-02 23:24

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('faqs', '0002_remove_faq_answer_bn_remove_faq_answer_hi_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='faq',
            name='answer',
            field=ckeditor.fields.RichTextField(),
        ),
    ]
