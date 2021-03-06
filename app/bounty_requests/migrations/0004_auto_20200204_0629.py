# Generated by Django 2.2.4 on 2020-02-04 06:29

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0079_auto_20200204_0629'),
        ('bounty_requests', '0003_auto_20191001_0748'),
    ]

    operations = [
        migrations.AddField(
            model_name='bountyrequest',
            name='title',
            field=models.CharField(default='', max_length=1000),
        ),
        migrations.AddField(
            model_name='bountyrequest',
            name='token_name',
            field=models.CharField(default='ETH', help_text='token in which the requested bounty is to be funded', max_length=50),
        ),
        migrations.AddField(
            model_name='bountyrequest',
            name='tribe',
            field=models.ForeignKey(help_text='tribe which is being requested to fund the issue', null=True, on_delete=django.db.models.deletion.SET_NULL, to='dashboard.Profile'),
        ),
        migrations.AlterField(
            model_name='bountyrequest',
            name='amount',
            field=models.FloatField(help_text='amount for which the requested bounty is to be funded', validators=[django.core.validators.MinValueValidator(1.0)]),
        ),
        migrations.AlterField(
            model_name='bountyrequest',
            name='comment',
            field=models.TextField(help_text='description from the requestor to justify the bounty request', max_length=500),
        ),
        migrations.AlterField(
            model_name='bountyrequest',
            name='github_org_email',
            field=models.CharField(blank=True, max_length=255),
        ),
        migrations.AlterField(
            model_name='bountyrequest',
            name='github_org_name',
            field=models.CharField(blank=True, max_length=50),
        ),
        migrations.AlterField(
            model_name='bountyrequest',
            name='github_url',
            field=models.CharField(help_text='github url of suggested bounty', max_length=255),
        ),
        migrations.AlterField(
            model_name='bountyrequest',
            name='requested_by',
            field=models.ForeignKey(help_text='profile submitting the bounty request', null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='bounty_requests', to='dashboard.Profile'),
        ),
        migrations.AlterField(
            model_name='bountyrequest',
            name='status',
            field=models.CharField(choices=[('o', 'open'), ('c', 'closed'), ('f', 'funded')], db_index=True, default='o', help_text='status of the bounty request', max_length=1),
        ),
    ]
