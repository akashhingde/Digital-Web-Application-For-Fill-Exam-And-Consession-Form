# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2019-04-20 16:16
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('student', '0088_consessionformmodel_date'),
    ]

    operations = [
        migrations.CreateModel(
            name='newconsessionformmodel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ticket_from', models.CharField(choices=[('', ''), ('Dombivli', 'Dombivli')], max_length=50)),
                ('ticket_to', models.CharField(choices=[('Airoli', 'Airoli'), ('Ambarnath', 'Ambarnath'), ('Ambivli', 'Ambivli'), ('Andheri', 'Andheri'), ('APTA', 'APTA'), ('Asangaon', 'Asangaon'), ('Atgaon', 'Atgaon'), ('Badlapur', 'Badlapur'), ('Bamandongri', 'Bamandongri'), ('Bandra', 'Bandra'), ('Bhandup', 'Bhandup'), ('Bhayandar', 'Bhayandar'), ('BhivpuriRoad', 'BhivpuriRoad'), ('Bhiwandi', 'Bhiwandi'), ('Boisar', 'Boisar'), ('Borivali', 'Borivali'), ('Byculla', 'Byculla'), ('CBDBelapur', 'CBDBelapur'), ('CharniRoad', 'CharniRoad'), ('Chembur', 'Chembur'), ('ChhatrapatiShivajiTerminus', 'ChhatrapatiShivajiTerminus'), ('Chinchpokli', 'Chinchpokli'), ('Chunabhatti', 'Chunabhatti'), ('Churchgate', 'Churchgate'), ('CottonGreen', 'CottonGreen'), ('CurreyRoad', 'CurreyRoad'), ('Dadar', 'Dadar'), ('DahanuRoad', 'DahanuRoad'), ('Dahisar', 'Dahisar'), ('Dativali', 'Dativali'), ('DivaJunction', 'DivaJunction'), ('DockyardRoad', 'DockyardRoad'), ('Dolavli', 'Dolavli'), ('Dombivli', 'Dombivli'), ('Dronagiri', 'Dronagiri'), ('ElphinstoneRoad', 'ElphinstoneRoad'), ('Gavhan', 'Gavhan'), ('Ghansoli', 'Ghansoli'), ('Ghatkopar', 'Ghatkopar'), ('Goregaon', 'Goregaon'), ('Govandi', 'Govandi'), ('GrantRoad', 'GrantRoad'), ('GuruTeghBahadurNagar', 'GuruTeghBahadurNagar'), ('Jogeshwari', 'Jogeshwari'), ('Juchandra', 'Juchandra'), ('Juinagar', 'Juinagar'), ('Kalamboli', 'Kalamboli'), ('Kalwa', 'Kalwa'), ('Kalyan', 'Kalyan'), ('KamanRoad', 'KamanRoad'), ('Kandivali', 'Kandivali'), ('Kanjurmarg', 'Kanjurmarg'), ('Karjat', 'Karjat'), ('Kasara', 'Kasara'), ('Kelavli', 'Kelavli'), ('KelveRoad', 'KelveRoad'), ('Khadavli', 'Khadavli'), ('Khandeshwar', 'Khandeshwar'), ('KharRoad', 'KharRoad'), ('Kharbao', 'Kharbao'), ('Khardi', 'Khardi'), ('Kharghar', 'Kharghar'), ('Kharkopar', 'Kharkopar'), ('Khopoli', 'Khopoli'), ('KingsCircle', 'KingsCircle'), ('Kopar', 'Kopar'), ('KoparKhairane', 'KoparKhairane'), ('Kurla', 'Kurla'), ('LowerParel', 'LowerParel'), ('Lowjee', 'Lowjee'), ('Mahalaxmi', 'Mahalaxmi'), ('Mahim', 'Mahim'), ('Malad', 'Malad'), ('Mankhurd', 'Mankhurd'), ('Mansarovar', 'Mansarovar'), ('MarineLines', 'MarineLines'), ('Masjid', 'Masjid'), ('Matunga', 'Matunga'), ('MatungaRoad', 'MatungaRoad'), ('MiraRoad', 'MiraRoad'), ('Mulund', 'Mulund'), ('MumbaiCentral', 'MumbaiCentral'), ('Mumbra', 'Mumbra'), ('NAGOTHANE', 'NAGOTHANE'), ('Nahur', 'Nahur'), ('Naigaon', 'Naigaon'), ('Nalasopara', 'Nalasopara'), ('Neral', 'Neral'), ('Nerul', 'Nerul'), ('NevadeRoad', 'NevadeRoad'), ('Nhava-Sheva', 'Nhava-Sheva'), ('Nilaje', 'Nilaje'), ('Oshiwara', 'Oshiwara'), ('Palasdari', 'Palasdari'), ('Palghar', 'Palghar'), ('Panvel', 'Panvel'), ('Parel', 'Parel'), ('PEN', 'PEN'), ('Rabale', 'Rabale'), ('Ranjanpada', 'Ranjanpada'), ('RASAYANI', 'RASAYANI'), ('Roha', 'Roha'), ('SagarSangam', 'SagarSangam'), ('SandhurstRoad', 'SandhurstRoad'), ('Sanpada', 'Sanpada'), ('SantaCruz', 'SantaCruz'), ('Saphale', 'Saphale'), ('Shahad', 'Shahad'), ('Shelu', 'Shelu'), ('Sion', 'Sion'), ('Targhar', 'Targhar'), ('Thakurli', 'Thakurli'), ('Thane', 'Thane'), ('TilakNagar', 'TilakNagar'), ('Titwala', 'Titwala'), ('Turbhe', 'Turbhe'), ('Ulhasnagar', 'Ulhasnagar'), ('Umroli', 'Umroli'), ('Uran', 'Uran'), ('VadalaRoad', 'VadalaRoad'), ('VaitarnaRoad', 'VaitarnaRoad'), ('Vangani', 'Vangani'), ('Vangaon', 'Vangaon'), ('VasaiRoad', 'VasaiRoad'), ('Vashi', 'Vashi'), ('Vasind', 'Vasind'), ('Vidyavihar', 'Vidyavihar'), ('Vikhroli', 'Vikhroli'), ('VileParle', 'VileParle'), ('Virar', 'Virar'), ('Vithalwadi', 'Vithalwadi')], max_length=50)),
                ('ticket_type', models.CharField(choices=[('I', 'I'), ('II', 'II')], max_length=50)),
                ('ticket_period', models.CharField(choices=[('monthly', 'monthly'), ('quaterly', 'quaterly')], max_length=50)),
                ('from_date', models.DateField(auto_now_add=True)),
                ('date', models.DateField(null=True)),
                ('status', models.IntegerField(choices=[(1, 'Accepted'), (2, 'Rejected'), (3, 'Pending')], default=3)),
                ('user', models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
