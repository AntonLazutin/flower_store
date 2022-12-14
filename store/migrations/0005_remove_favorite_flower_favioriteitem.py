# Generated by Django 4.1.3 on 2022-12-03 14:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0004_favorite'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='favorite',
            name='flower',
        ),
        migrations.CreateModel(
            name='FavioriteItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('favorite', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='favorite_items', to='store.favorite')),
                ('item', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='favorite_items', to='store.flower')),
            ],
        ),
    ]
