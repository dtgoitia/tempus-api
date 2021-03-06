# Generated by Django 3.0.3 on 2020-02-24 20:13

import django.core.validators
import django.db.models.deletion
from django.db import migrations, models

import src.plan.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Exercise',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField(help_text='Short name for the user to identify the exercise.')),
                ('description', models.TextField(default='', help_text='Optional space for details about the exercise, technique, caveats...')),
                ('exercise_type', models.CharField(choices=[('WORK', 'Work'), ('REST', 'Rest'), ('PREP', 'Preparation')], max_length=4)),
            ],
        ),
        migrations.CreateModel(
            name='Plan',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField(help_text='Short name for the user to identify the plan.')),
                ('description', models.TextField(blank=True, default='', help_text='Optional space for a longer description of what the plan is about.')),
                ('created', models.DateTimeField(help_text='Moment at which the plan was created in the client. This time has nothing to do with when was the plan saved in the backend.')),
                ('last_updated', models.DateTimeField(help_text='Moment at which the plan was update for last time in the client. This time has nothing to do with when was the plan updated in the backend.')),
            ],
        ),
        migrations.CreateModel(
            name='Session',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField(help_text='Short name for the user to identify the session.')),
                ('description', models.TextField(blank=True, default='', help_text='Short description for the user to get a better understanding of what the session is about.')),
                ('notes', models.TextField(blank=True, default='', help_text='Optional space for notes like: what went well/bad, injuries, why the session was aborted...')),
                ('start', models.DateTimeField(help_text='Moment at which the session started.', validators=[src.plan.models.is_not_future_datetime])),
            ],
        ),
        migrations.CreateModel(
            name='Record',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('start', models.DateTimeField(help_text='Moment at which the execution of the exercise started.', validators=[src.plan.models.is_not_future_datetime])),
                ('end', models.DateTimeField(help_text='Moment at which the execution of the exercise finished.', validators=[src.plan.models.is_not_future_datetime])),
                ('reps', models.IntegerField(default=0, help_text='Amount of times the execise was repeated during the record.', validators=[django.core.validators.MinValueValidator(0)])),
                ('exercise', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='+', to='plan.Exercise')),
                ('session', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='records', to='plan.Session')),
            ],
        ),
        migrations.CreateModel(
            name='Loop',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rounds', models.IntegerField(default=1, help_text='Amount of times that the whole block of child Goals under the Loop will be executed.', validators=[src.plan.models.is_positive_number])),
                ('loop_index', models.IntegerField(help_text='Position of the Loop inside the parent Plan.', validators=[django.core.validators.MinValueValidator(0)])),
                ('description', models.TextField(default='', help_text='Optional description for a group of goals.')),
                ('plan', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='loops', to='plan.Plan')),
            ],
        ),
        migrations.CreateModel(
            name='Goal',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('goal_index', models.IntegerField(help_text='Position of the Goal inside the parent Loop.', validators=[django.core.validators.MinValueValidator(0)])),
                ('duration', models.IntegerField(help_text='Time allocated to execute the Exercise.', null=True, validators=[src.plan.models.is_positive_number])),
                ('repetitions', models.IntegerField(help_text='Amount of times the Exercise should be repeated during a single execution of the Goal.', null=True, validators=[src.plan.models.is_positive_number])),
                ('pause', models.BooleanField(default=False, help_text='Specifies if the goal waits for users approval to run or not.')),
                ('exercise', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='+', to='plan.Exercise')),
                ('loop', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='goals', to='plan.Loop')),
            ],
        ),
    ]
