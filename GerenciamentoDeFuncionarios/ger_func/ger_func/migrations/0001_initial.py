# Generated by Django 3.2 on 2022-03-25 22:18

from django.db import migrations, models
import django.db.models.manager


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Funcionario',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=255)),
                ('sobrenome', models.CharField(max_length=255)),
                ('cpf', models.CharField(max_length=14)),
                ('tempo_de_servico', models.IntegerField(default=0)),
                ('remuneracao', models.DecimalField(decimal_places=2, max_digits=8)),
            ],
            managers=[
                ('objetos', django.db.models.manager.Manager()),
            ],
        ),
    ]
