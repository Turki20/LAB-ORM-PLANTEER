# Generated by Django 5.2.4 on 2025-07-16 07:44

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Plant',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('about', models.TextField()),
                ('used_for', models.TextField()),
                ('image', models.ImageField(upload_to='images/')),
                ('category', models.CharField(choices=[('decorative', 'Decorative Plants'), ('indoor', 'Indoor Plants'), ('outdoor', 'Outdoor Plants'), ('flowering', 'Flowering Plants'), ('medicinal', 'Medicinal Plants'), ('aromatic', 'Aromatic Plants'), ('edible', 'Edible Plants'), ('climbing', 'Climbing Plants'), ('succulent', 'Succulent Plants'), ('rare', 'Rare Plants'), ('air', 'Air Plants'), ('aquatic', 'Aquatic Plants'), ('carnivorous', 'Carnivorous Plants'), ('perennial', 'Perennial Plants'), ('seasonal', 'Seasonal Plants')])),
                ('is_edible', models.BooleanField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
