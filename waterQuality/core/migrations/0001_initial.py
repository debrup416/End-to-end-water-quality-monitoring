# Generated by Django 4.0.1 on 2022-01-25 18:24

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Water',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ph', models.DecimalField(decimal_places=12, max_digits=24)),
                ('Hardness', models.DecimalField(decimal_places=12, max_digits=24)),
                ('Solids', models.DecimalField(decimal_places=12, max_digits=24)),
                ('Chloramines', models.DecimalField(decimal_places=12, max_digits=24)),
                ('Sulfate', models.DecimalField(decimal_places=12, max_digits=24)),
                ('Conductivity', models.DecimalField(decimal_places=12, max_digits=24)),
                ('Organic_carbon', models.DecimalField(decimal_places=12, max_digits=24)),
                ('Trihalomethanes', models.DecimalField(decimal_places=12, max_digits=24)),
                ('Turbidity', models.DecimalField(decimal_places=12, max_digits=24)),
            ],
        ),
    ]
