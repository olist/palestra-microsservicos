from decimal import Decimal
from django.db import migrations, models
import django.db.models.deletion


def populate_database(apps, schema_editor):
    TipoMulta = apps.get_model("core", "TipoMulta")

    TipoMulta.objects.create(descricao="Sinal Vermelho", valor=Decimal("300.00"))
    TipoMulta.objects.create(descricao="Trafegando em contra mão", valor=Decimal("200.00"))
    TipoMulta.objects.create(descricao="Estacionado em local proibido", valor=Decimal("100.00"))


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='TipoMulta',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('valor', models.DecimalField(decimal_places=2, max_digits=5)),
                ('descricao', models.CharField(max_length=255)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Multa',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('placa', models.CharField(max_length=255)),
                ('tipo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.TipoMulta')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.RunPython(populate_database),
    ]
