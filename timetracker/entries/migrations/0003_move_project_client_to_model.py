# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations

def rewrite_client_str_to_client_model(apps, schema_editor):
    Client = apps.get_model("entries", "Client")
    Project = apps.get_model("entries", "Project")
    
    # For each project, get the text version of the client name, and
    # see if there's already a corresponding Client.  If not, create it.
    # Then set the client property to be the new or existing Client.
    for project in Project.objects.all():
        # Is there an existing client of this name?
        try:
            c = Client.objects.get(name=project.client_as_str)
        except Client.DoesNotExist:
            # No, so create it
            c = Client(name=project.client_as_str)
            c.save()
        project.client = c
        project.save()

def rewrite_client_model_to_client_str(apps, schema_editor):
    Client = apps.get_model("entries", "Client")
    Project = apps.get_model("entries", "Project")
    
    # For each project, set the text version of the client name to
    # the name from the Client instance.
    for project in Project.objects.all():
        project.client_as_str = project.client.name
        # Must have this or delete of clients cascades to products
        project.client = None
        project.save()

    # Now delete all clients.    
    Client.objects.all().delete()

class Migration(migrations.Migration):

    dependencies = [
        ('entries', '0002_auto_20150723_0819'),
    ]

    # Switch from a charfield-based client, to a model-based one.
    operations = [
        # Move the existing client field to the side
        migrations.RenameField(
            model_name='project',
            old_name='client',
            new_name='client_as_str',
        ),
        # Create the client model
        migrations.CreateModel(
            name='Client',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, auto_created=True, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
            ],
        ),
        # Create a client field in the project.  Note it allows null, as
        # a way of avoiding to specify what the default value is.
        migrations.AddField(
            model_name='project',
            name='client',
            field=models.ForeignKey(null=True, to='entries.Client'),
        ),
        # Do the conversion from text to model instance.
        migrations.RunPython(
            rewrite_client_str_to_client_model,
            rewrite_client_model_to_client_str,
        ),
        # Now we can disallow null.
        migrations.AlterField(
            model_name='project',
            name='client',
            field=models.ForeignKey(to='entries.Client'),
        ),
        # And remove the text version of the client
        migrations.RemoveField(
            model_name='project',
            name='client_as_str',
        ),
    ]
