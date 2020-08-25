# Generated by Django 2.2.4 on 2020-08-14 00:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ptokens', '0007_auto_20200731_0901'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ptokenevent',
            name='event',
            field=models.CharField(choices=[('mint_ptoken', 'Mint tokens'), ('burn_ptoken', 'Burn tokens'), ('edit_price_ptoken', 'Update price token')], max_length=20),
        ),
    ]