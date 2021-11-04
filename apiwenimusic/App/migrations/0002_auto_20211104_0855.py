# Generated by Django 3.2.9 on 2021-11-04 11:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('App', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Artista',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Playlist',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('namePlaylist', models.CharField(max_length=100)),
            ],
        ),
        migrations.DeleteModel(
            name='Usuario',
        ),
        migrations.RenameField(
            model_name='music',
            old_name='titulo',
            new_name='nameMusic',
        ),
        migrations.AddField(
            model_name='playlist',
            name='musicas',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='musicas', to='App.music'),
        ),
        migrations.AlterField(
            model_name='music',
            name='artista',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='artista', to='App.artista'),
        ),
    ]
