# Generated by Django 5.1.5 on 2025-02-02 23:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('faqs', '0004_language'),
    ]

    operations = [
        migrations.AddField(
            model_name='faq',
            name='languages',
            field=models.ManyToManyField(related_name='faqs', to='faqs.language'),
        ),
    ]
