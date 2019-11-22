# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2019-09-24 16:16
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import multiselectfield.db.fields


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0118_auto_20190924_2117'),
    ]

    operations = [
        migrations.CreateModel(
            name='Subject_multiple',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', multiselectfield.db.fields.MultiSelectField(choices=[['Applied Mathmatics III', 'Applied Mathmatics III'], ['Database Management System', 'Database Management System'], ['Applied Mathmatics IV', 'Applied Mathmatics IV'], ['Computer Network', 'Computer Network'], ['Data Structure & Algorithm', 'Data Structure & Algorithm'], ['Object Oriented Programming', 'Object Oriented Programming'], ['Principles of Analog & Digital', 'Principles of Analog & Digital'], ['Computer Organization and Architecture', 'Computer Organization and Architecture'], ['Automata Theory', 'Automata Theory'], ['Web Programming', 'Web Programming'], ['Information Theory and Coding', 'Information Theory and Coding'], ['Computer Graphics and Virtual Reality', 'Computer Graphics and Virtual Reality'], ['Operating Systems', 'Operating Systems'], ['Microcontroller and Embedded Systems', 'Microcontroller and Embedded Systems'], ['Advanced Database Management Systems', 'Advanced Database Management Systems'], ['Open Source Technologies', 'Open Source Technologies'], ['Business Communication and Ethics*', 'Business Communication and Ethics*'], ['Software Engineering', 'Software Engineering'], ['Distributed Systems', 'Distributed Systems'], ['System & Web Security', 'System & Web Security'], ['Data Mining & Business Intelligence', 'Data Mining & Business Intelligence'], ['Advance Internet Technology', 'Advance Internet Technology'], ['Object Oriented Programming Methodolgy*', 'Object Oriented Programming Methodolgy*'], ['Data Structures', 'Data Structures'], ['Digital Logic Design and Analysis', 'Digital Logic Design and Analysis'], ['Discrete Structures', 'Discrete Structures'], ['Electronic Circuits and Communication Fundamentals', 'Electronic Circuits and Communication Fundamentals'], ['Analysis of Algorithms', 'Analysis of Algorithms'], ['Computer Organization and Architecture*', 'Computer Organization and Architecture*'], ['Data Base Management systems', 'Data Base Management systems'], ['Theoretical Computer Science', 'Theoretical Computer Science'], ['Computer Graphics', 'Computer Graphics'], ['Microprocessor', 'Microprocessor'], ['Operating Systems', 'Operating Systems'], ['Structured and Object Oriented Analysis and Design', 'Structured and Object Oriented Analysis and Design'], ['Computer Networks', 'Computer Networks'], ['Web Technologies Laboratory', 'Web Technologies Laboratory'], ['Business Communication and Ethics', 'Business Communication and Ethics'], ['System Programming and Compiler Construction', 'System Programming and Compiler Construction'], ['Software Engineering', 'Software Engineering'], ['Distributed Databases', 'Distributed Databases'], ['Mobile Communication and Computing', 'Mobile Communication and Computing'], ['Network Programming Laboratory', 'Network Programming Laboratory']], max_length=1210, null=True)),
                ('branch', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='student.Branch')),
                ('semester', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='student.Semester')),
                ('year', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='student.Year')),
            ],
        ),
        migrations.RemoveField(
            model_name='atktmodel',
            name='subject',
        ),
    ]
