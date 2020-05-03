from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Proprietario",
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ("nome", models.CharField(max_length=255)),
                ("email", models.EmailField(max_length=254)),
            ],
            options={"abstract": False},
        ),
        migrations.CreateModel(
            name="Carro",
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ("placa", models.CharField(max_length=255)),
                ("modelo", models.CharField(max_length=255)),
                (
                    "proprietario",
                    models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to="core.Proprietario"),
                ),
            ],
            options={"abstract": False},
        )
    ]
