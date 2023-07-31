```python
from django.db import migrations, models
import django.db.models.deletion

class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name='CrewMember',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('status', models.CharField(max_length=200)),
                ('availability_date', models.DateField()),
                ('gender', models.CharField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='Cert',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('issuing_authority', models.CharField(max_length=200)),
                ('expiry_date', models.DateField()),
                ('validity_days', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Qualification',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('required_certificates', models.ManyToManyField(to='crew_assignment_app.Cert')),
            ],
        ),
        migrations.CreateModel(
            name='Ship',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('ship_code', models.CharField(max_length=200)),
                ('brand', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Positions',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('position_code', models.CharField(max_length=200)),
                ('name', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Assignment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('start_date', models.DateField()),
                ('end_date', models.DateField()),
                ('crewmember', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='crew_assignment_app.CrewMember')),
                ('ship', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='crew_assignment_app.Ship')),
                ('position', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='crew_assignment_app.Positions')),
            ],
        ),
        migrations.CreateModel(
            name='ShipCrewAllowance',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ship_code', models.CharField(max_length=200)),
                ('quantity', models.IntegerField()),
                ('position', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='crew_assignment_app.Positions')),
            ],
        ),
        migrations.AddField(
            model_name='crewmember',
            name='certificates',
            field=models.ManyToManyField(to='crew_assignment_app.Cert'),
        ),
        migrations.AddField(
            model_name='crewmember',
            name='position',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='crew_assignment_app.Positions'),
        ),
        migrations.AddField(
            model_name='crewmember',
            name='qualifications',
            field=models.ManyToManyField(to='crew_assignment_app.Qualification'),
        ),
    ]
```