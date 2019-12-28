from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Squirrel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('longitude', models.FloatField(help_text='Longitude')),
                ('latitude', models.FloatField(help_text='Latitude')),
                ('unique_squirrel_id', models.CharField(help_text='Unique_squirrel_id', max_length=50)),
                ('shift', models.CharField(choices=[('AM', 'AM'), ('PM', 'PM'), ('', '')], default='', max_length=2)),
                ('date', models.DateField(help_text='Date')),
                ('hectare_squirrel_number', models.CharField(help_text='The number of squirrels per hectare', max_length=10)),
                ('age', models.CharField(choices=[('Adult', 'Adult'), ('Juvenile', 'JUVENILE'), ('', '')], default='', help_text='Age of the squirrel', max_length=10)),
                ('primary_fur_color', models.CharField(choices=[('Gray', 'Gray'), ('Cinnamon', 'Cinnamon'), ('Black', 'Black'), ('', '')], default='', help_text='Primary fur color', max_length=10)),
                ('location', models.CharField(choices=[('ground plane', 'ground plane'), ('above ground', 'above ground'), ('', '')], default='', help_text='Location of the squirrel', max_length=20)),
                ('specific_location', models.CharField(help_text='Specific Location', max_length=30)),
                ('running', models.BooleanField(default=False)),
                ('chasing', models.BooleanField(default=False)),
                ('climbing', models.BooleanField(default=False)),
                ('eating', models.BooleanField(default=False)),
                ('foraging', models.BooleanField(default=False)),
                ('other_activities', models.CharField(help_text='Other activities squirrel is doing except those mentioned', max_length=30)),
                ('kuks', models.BooleanField(default=False)),
                ('quaas', models.BooleanField(default=False)),
                ('moans', models.BooleanField(default=False)),
                ('tail_flags', models.BooleanField(default=False)),
                ('tail_twitches', models.BooleanField(default=False)),
                ('approaches', models.BooleanField(default=False)),
                ('indifferent', models.BooleanField(default=False)),
                ('runs_from', models.BooleanField(default=False)),
            ],
        ),
    ]
