# Generated by Django 3.2.3 on 2023-04-01 13:52

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='ad',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category', models.CharField(choices=[('TA', 'Tanks'), ('HE', 'Healers'), ('DD', 'DD (?)'), ('TR', 'Traders'), ('GM', 'Guild Masters'), ('QG', 'Quest Givers'), ('BM', 'Blacksmiths'), ('LM', 'Leather Makers'), ('PM', 'Potion Makers'), ('SM', 'Spell Masters')], default='TA', max_length=2)),
                ('posted', models.DateTimeField(auto_now_add=True)),
                ('content', models.TextField()),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='response',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('posted', models.DateTimeField(auto_now_add=True)),
                ('text', models.TextField()),
                ('ad', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ads.ad')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
