# from __future__ import unicode_literals
from django.shortcuts import render
from django.http import request,HttpRequest
from django .template import loader
from django.contrib.auth.models import User
from django.db import models
from multiselectfield import MultiSelectField
import MySQLdb



database = MySQLdb.connect(host="127.0.0.1", user="root", passwd="1234", db="collage5")
print(request)
# Get the cursor, which is used to traverse the database, line by line
cursor = database.cursor()
sql = 'SELECT name FROM student_Subject'
check = cursor.execute(sql)
results = cursor.fetchall()
lis = []
for a in results:
    lis.append(a[0])
li = []
for a in lis:
    li.append( [
       a,a

    ])

def new():
    database = MySQLdb.connect(host="127.0.0.1", user="root", passwd="1234", db="collage5")

    # Get the cursor, which is used to traverse the database, line by line
    cursor = database.cursor()

    # semesters_id = request.HttpRequest('q')
    # branch_id = request.GET('branch')

    sql = ('SELECT * FROM student_Subject WHERE semester_id = 1 AND branch_id = 1')
    check = cursor.execute(sql)
    results = cursor.fetchall()
    lis = []
    for a in results:
        lis.append(a[1])
    li = []
    for a in lis:
        li.append( [
        a,a

        ])
    return li
# print(new())
BRANCH_CHOICES= [
    ('Information Technology', 'Information Technology'),
    ('Computer Engineering', 'Computer Engineering'),
    ('Production Engineering', 'Production Engineering'),
    ('Mechanical Engineering', 'Mechanical Engineering'),
    ('Chemical Engineering', 'Chemical Engineering'),
    ('Electronics & Telecommunication Engineering', 'Electronics & Telecommunication Engineering'),
    ]

BRANCH_CHOICES1= [
    ('all branch','all branch'),
    ('Information Technology', 'Information Technology'),
    ('Computer Engineering', 'Computer Engineering'),
    ('Production Engineering', 'Production Engineering'),
    ('Mechanical Engineering', 'Mechanical Engineering'),
    ('Chemical Engineering', 'Chemical Engineering'),
    ('Electronics & Telecommunication Engineering', 'Electronics & Telecommunication Engineering'),
    ]

YEAR_CHOICES= [
    ('second year', 'second year'),
    ('third year', 'third year'),
    ]

SEMISTER_CHOICES= [
    ('III', 'III'),
    ('IV', 'IV'),
    ('V', 'V'),
    ('VI', 'VI'),
    ]

EXAM_CHOICES= [
   ('CBCS', 'CBCS'),
   ('CBGS', 'CBGS'),

]

STATION_CHOICE= [
    ('Airoli', 'Airoli'),
    ('Ambarnath', 'Ambarnath'),
    ('Ambivli', 'Ambivli'),
    ('Andheri', 'Andheri'),
    ('APTA', 'APTA'),
    ('Asangaon', 'Asangaon'),
    ('Atgaon', 'Atgaon'),
    ('Badlapur', 'Badlapur'),
    ('Bamandongri', 'Bamandongri'),
    ('Bandra', 'Bandra'),
    ('Bhandup', 'Bhandup'),
    ('Bhayandar', 'Bhayandar'),
    ('BhivpuriRoad', 'BhivpuriRoad'),
    ('Bhiwandi', 'Bhiwandi'),
    ('Boisar', 'Boisar'),
    ('Borivali', 'Borivali'),
    ('Byculla', 'Byculla'),
    ('CBDBelapur', 'CBDBelapur'),
    ('CharniRoad', 'CharniRoad'),
    ('Chembur', 'Chembur'),
    ('ChhatrapatiShivajiTerminus','ChhatrapatiShivajiTerminus'),
    ('Chinchpokli', 'Chinchpokli'),
    ('Chunabhatti', 'Chunabhatti'),
    ('Churchgate', 'Churchgate'),
    ('CottonGreen', 'CottonGreen'),
    ('CurreyRoad', 'CurreyRoad'),
    ('Dadar', 'Dadar'),
    ('DahanuRoad', 'DahanuRoad'),
    ('Dahisar', 'Dahisar'),
    ('Dativali', 'Dativali'),
    ('DivaJunction', 'DivaJunction'),
    ('DockyardRoad', 'DockyardRoad'),
    ('Dolavli', 'Dolavli'),
    ('Dombivli', 'Dombivli'),
    ('Dronagiri', 'Dronagiri'),
    ('ElphinstoneRoad', 'ElphinstoneRoad'),
    ('Gavhan', 'Gavhan'),
    ('Ghansoli', 'Ghansoli'),
    ('Ghatkopar', 'Ghatkopar'),
    ('Goregaon', 'Goregaon'),
    ('Govandi', 'Govandi'),
    ('GrantRoad', 'GrantRoad'),
    ('GuruTeghBahadurNagar', 'GuruTeghBahadurNagar'),
    ('Jogeshwari', 'Jogeshwari'),
    ('Juchandra', 'Juchandra'),
    ('Juinagar', 'Juinagar'),
    ('Kalamboli', 'Kalamboli'),
    ('Kalwa', 'Kalwa'),
    ('Kalyan', 'Kalyan'),
    ('KamanRoad', 'KamanRoad'),
    ('Kandivali', 'Kandivali'),
    ('Kanjurmarg', 'Kanjurmarg'),
    ('Karjat', 'Karjat'),
    ('Kasara', 'Kasara'),
    ('Kelavli', 'Kelavli'),
    ('KelveRoad', 'KelveRoad'),
    ('Khadavli', 'Khadavli'),
    ('Khandeshwar', 'Khandeshwar'),
    ('KharRoad', 'KharRoad'),
    ('Kharbao', 'Kharbao'),
    ('Khardi', 'Khardi'),
    ('Kharghar', 'Kharghar'),
    ('Kharkopar', 'Kharkopar'),
    ('Khopoli', 'Khopoli'),
    ('KingsCircle', 'KingsCircle'),
    ('Kopar', 'Kopar'),
    ('KoparKhairane', 'KoparKhairane'),
    ('Kurla', 'Kurla'),
    ('LowerParel', 'LowerParel'),
    ('Lowjee', 'Lowjee'),
    ('Mahalaxmi', 'Mahalaxmi'),
    ('Mahim', 'Mahim'),
    ('Malad', 'Malad'),
    ('Mankhurd', 'Mankhurd'),
    ('Mansarovar', 'Mansarovar'),
    ('MarineLines', 'MarineLines'),
    ('Masjid', 'Masjid'),
    ('Matunga', 'Matunga'),
    ('MatungaRoad', 'MatungaRoad'),
    ('MiraRoad', 'MiraRoad'),
    ('Mulund', 'Mulund'),
    ('MumbaiCentral', 'MumbaiCentral'),
    ('Mumbra', 'Mumbra'),
    ('NAGOTHANE', 'NAGOTHANE'),
    ('Nahur', 'Nahur'),
    ('Naigaon', 'Naigaon'),
    ('Nalasopara', 'Nalasopara'),
    ('Neral', 'Neral'),
    ('Nerul', 'Nerul'),
    ('NevadeRoad', 'NevadeRoad'),
    ('Nhava-Sheva', 'Nhava-Sheva'),
    ('Nilaje', 'Nilaje'),
    ('Oshiwara', 'Oshiwara'),
    ('Palasdari', 'Palasdari'),
    ('Palghar', 'Palghar'),
    ('Panvel', 'Panvel'),
    ('Parel', 'Parel'),
    ('PEN', 'PEN'),
    ('Rabale', 'Rabale'),
    ('Ranjanpada', 'Ranjanpada'),
    ('RASAYANI', 'RASAYANI'),
    ('Roha', 'Roha'),
    ('SagarSangam', 'SagarSangam'),
    ('SandhurstRoad', 'SandhurstRoad'),
    ('Sanpada', 'Sanpada'),
    ('SantaCruz', 'SantaCruz'),
    ('Saphale', 'Saphale'),
    ('Shahad', 'Shahad'),
    ('Shelu', 'Shelu'),
    ('Sion', 'Sion'),
    ('Targhar', 'Targhar'),
    ('Thakurli', 'Thakurli'),
    ('Thane', 'Thane'),
    ('TilakNagar', 'TilakNagar'),
    ('Titwala', 'Titwala'),
    ('Turbhe', 'Turbhe'),
    ('Ulhasnagar', 'Ulhasnagar'),
    ('Umroli', 'Umroli'),
    ('Uran', 'Uran'),
    ('VadalaRoad', 'VadalaRoad'),
    ('VaitarnaRoad', 'VaitarnaRoad'),
    ('Vangani', 'Vangani'),
    ('Vangaon', 'Vangaon'),
    ('VasaiRoad', 'VasaiRoad'),
    ('Vashi', 'Vashi'),
    ('Vasind', 'Vasind'),
    ('Vidyavihar', 'Vidyavihar'),
    ('Vikhroli', 'Vikhroli'),
    ('VileParle', 'VileParle'),
    ('Virar', 'Virar'),
    ('Vithalwadi', 'Vithalwadi'),
]

LAST_STATION_CHOICE=[

    ('',''),
    ('Dombivli','Dombivli')
]
LAST_TICKET_TYPE_CHOICE=[
    ('I','I'),
    ('II','II'),
]
LAST_TICKET_PERIOD_CHOICE=[
    ('monthly','monthly'),
    ('quaterly','quaterly'),
]

YEARS= [x for x in range(2010,2019)]

IT_FE_1_CHOICE= [
    ('Applied Physics – I','Applied Physics – I'),
    ('Applied Mathematics – I', 'Applied Mathematics – I'),
    ('Applied Chemistry – I	', 'Applied Chemistry – I'),
    ('Engineering Mechanics', 'Engineering Mechanics'),
    ('Introduction to Computers and Auto CAD', 'Introduction to Computers and Auto CAD'),
    ('Environmental Studies', 'Environmental Studies'),
    ]

IT_FE_2_CHOICE = [
    ('Applied Mathematics – II', 'Applied Mathematics – II'),
    ('Applied Physics – II', 'Applied Physics – II'),
    ('Applied Chemistry – II	', 'Applied Chemistry – II'),
    ('Introduction to Programming', 'Introduction to Programming'),
    ('Engineering Mechanics', 'Engineering Mechanics'),
    ('Electrical Science', 'Electrical Science'),

]

IT_FE_3_CHOICE = [
    ('Applied Mathematics III', 'Applied Mathematics III'),
    ('Logic Design', 'Logic Design'),
    ('Data Structures & Analysis', 'Data Structures & Analysis'),
    ('Database Management System', 'Database Management System'),
    ('Principle of Communications 2', 'Principle of Communications 2'),
    ]

IT_FE_4_CHOICE = [
    ('Applied Mathematics-IV', 'Applied Mathematics-IV'),
    ('Computer Networks', 'Computer Networks'),
    ('Operating Systems', 'Operating Systems'),
    ('Computer Organization and Architecture', 'Computer Organization and Architecture'),
    ('Automata Theory', 'Automata Theory'),
    ]

IT_FE_5_CHOICE = [
    ('Microcontroller and Embedded Programming', 'Microcontroller and Embedded Programming'),
    ('Internet Programming', 'Internet Programming'),
    ('Advanced Data Management Technology', 'Advanced Data Management Technology'),
    ('Cryptography & Network Security', 'Cryptography & Network Security'),
    ('E-Commerce & E-Business', 'E-Commerce & E-Business'),

    ]
IT_FE_6_CHOICE = [
    ('Software Engineering with Project Management', 'Software Engineering with Project Management'),
    ('Data Mining and Business Intelligence', 'Data Mining and Business Intelligence'),
    ('Cloud Computing & Services', 'Cloud Computing & Services'),
    ('Wireless Networks', 'Wireless Networks'),
    ('Digital Forensics', 'Digital Forensics'),

    ]




class Branch(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name
class Year(models.Model):
    name = models.CharField(max_length=30,null=True)

    def __str__(self):
        return self.name
class Semester(models.Model):
    year = models.ForeignKey(Year, on_delete=models.CASCADE)
    name = models.CharField(max_length=30,null=True)

    def __str__(self):
        return self.name

class Subject(models.Model):
    branch = models.ForeignKey(Branch, on_delete=models.CASCADE, null=True)
    year = models.ForeignKey(Year, on_delete=models.CASCADE, null=True)
    semester = models.ForeignKey(Semester, on_delete=models.CASCADE)
    name = models.CharField(max_length=100,null=True)

    def __str__(self):
        return self.name

class Subject_multiple(models.Model):
    branch = models.ForeignKey(Branch, on_delete=models.CASCADE, null=True)
    year = models.ForeignKey(Year, on_delete=models.CASCADE, null=True)
    semester = models.ForeignKey(Semester, on_delete=models.CASCADE, null=True)
    name = MultiSelectField(choices=li,null=True)

    def __str__(self):
        return str(self.name)





class UserProfileModel(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE,related_name='profile')

    full_name=models.CharField(max_length=50, null=True )
    gender = models.CharField(max_length=8,choices=(('Male','Male'),('Female','Female')),blank=True)
    age = models.PositiveIntegerField(blank=True,null=True)
    admission_no=models.CharField(max_length=60,null=True)
    mobile_no=models.CharField(max_length=12, null=True )
    birth_date = models.DateField(blank=True, null=True )
    current_year=models.CharField(max_length=20, null=True )
    category=models.CharField(max_length=20, null=True )
    address=models.CharField(max_length=200, null=True)
    branch=models.CharField(choices=BRANCH_CHOICES,max_length=100, null=True)
    image=models.ImageField(upload_to='profile_image',blank=True)
    roll_no=models.PositiveIntegerField(blank=True,null=True)
    def __str__(self):
        return self.user.username




class examformmodel(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE,null=True)

    month = models.CharField(max_length=50)
    roll_no = models.IntegerField(default=0,null=True)

    branch = models.ForeignKey(Branch, on_delete=models.SET_NULL, null=True)
    year = models.ForeignKey(Year, on_delete=models.SET_NULL, null=True)
    semester = models.ForeignKey(Semester, on_delete=models.CASCADE, null=True)
    # subject = models.ForeignKey(Subject, on_delete=models.CASCADE, null=True)
    status = models.IntegerField(
        choices=((1, "Approved"), (2, 'Rejected'), (3, 'Pending')),
        default=3,
    )



    def __str__(self):
        return self.user.username

class atktmodel(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE, null=True)
    month = models.CharField(max_length=50)
    roll_no = models.IntegerField(default=0,null=True)
    branch = models.ForeignKey(Branch, on_delete=models.SET_NULL, null=True)
    year = models.ForeignKey(Year, on_delete=models.SET_NULL, null=True)
    semester = models.ForeignKey(Semester, on_delete=models.CASCADE, null=True)
    # subject = MultiSelectField(Subject,null=True)
    # subject = models.ManyToManyField(Subject)
    last_seat_no=models.CharField(max_length=30,null=True, blank=True)
    IT_FE_1 = MultiSelectField(choices=IT_FE_1_CHOICE,null=True , blank=True)
    IT_FE_2 = MultiSelectField(choices=IT_FE_2_CHOICE, null=True , blank=True)
    IT_FE_3 = MultiSelectField(choices=IT_FE_3_CHOICE, null=True, blank=True)
    IT_FE_4 = MultiSelectField(choices=IT_FE_4_CHOICE, null=True, blank=True)
    IT_FE_5 = MultiSelectField(choices=IT_FE_5_CHOICE, null=True, blank=True)
    IT_FE_6 = MultiSelectField(choices=IT_FE_6_CHOICE, null=True, blank=True)
    status = models.IntegerField(
        choices=((1, "Approved"), (2, 'Rejected'), (3, 'Pending')),
        default=3,
    )
    def __str__(self):
        return self.user.username

class regularrevalutionmodel(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE, null=True)
    month = models.CharField(max_length=50)
    roll_no = models.IntegerField(default=0,null=True)

    branch = models.ForeignKey(Branch, on_delete=models.SET_NULL, null=True)
    year = models.ForeignKey(Year, on_delete=models.SET_NULL, null=True)
    semester = models.ForeignKey(Semester, on_delete=models.CASCADE, null=True)
    last_seat_no=models.CharField(max_length=30,null=True)
    status = models.IntegerField(
        choices=((1, "Approved"), (2, 'Rejected'), (3, 'Pending')),
        default=3,
    )
    def __str__(self):
        return self.user.username

class atktrevalutionmodel(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE, null=True)
    month = models.CharField(max_length=50)
    roll_no = models.IntegerField(default=0,null=True)

    branch = models.ForeignKey(Branch, on_delete=models.SET_NULL, null=True)
    year = models.ForeignKey(Year, on_delete=models.SET_NULL, null=True)
    semester = models.ForeignKey(Semester, on_delete=models.CASCADE, null=True)
    last_seat_no=models.CharField(max_length=30,null=True)

    status = models.IntegerField(
        choices=((1, "Approved"), (2, 'Rejected'), (3, 'Pending')),
        default=3,
    )
    def __str__(self):
        return self.user.username

class regularphotocopymodel(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE, null=True)
    month = models.CharField(max_length=50)
    roll_no = models.IntegerField(default=0,null=True)

    branch = models.ForeignKey(Branch, on_delete=models.SET_NULL, null=True)
    year = models.ForeignKey(Year, on_delete=models.SET_NULL, null=True)
    semester = models.ForeignKey(Semester, on_delete=models.CASCADE, null=True)
    last_seat_no=models.CharField(max_length=30,null=True)
    status = models.IntegerField(
        choices=((1, "Approved"), (2, 'Rejected'), (3, 'Pending')),
        default=3,
    )
    def __str__(self):
        return self.user.username

class atktphotocopymodel(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE, null=True)
    month = models.CharField(max_length=50)
    roll_no = models.IntegerField(default=0,null=True)

    branch = models.ForeignKey(Branch, on_delete=models.SET_NULL, null=True)
    year = models.ForeignKey(Year, on_delete=models.SET_NULL, null=True)
    semester = models.ForeignKey(Semester, on_delete=models.CASCADE, null=True)
    last_seat_no=models.CharField(max_length=30,null=True)
    status = models.IntegerField(
        choices=((1, "Approved"), (2, 'Rejected'), (3, 'Pending')),
        default=3,
    )
    def __str__(self):
        return self.user.username

class examcelladmin(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE, null=True)
    full_name=models.CharField(max_length=50, null=True )
    image=models.ImageField(upload_to='profile_image',blank=True)
    mobile_no=models.CharField(max_length=12, null=True )
    address=models.CharField(max_length=200, null=True)

    def __str__(self):
        return self.user.username

class uploadresultmodel(models.Model):
    branch = models.CharField(choices=BRANCH_CHOICES,max_length=200, null=True)
    semester = models.CharField(choices=SEMISTER_CHOICES, max_length=200, null=True)
    result = models.FileField(upload_to='documents', null=True, blank=True)

    def __str__(self):
        return self.branch

class uploadnoticemodel(models.Model):
    branch = models.CharField(choices=BRANCH_CHOICES1,max_length=200, null=True)
    notice = models.TextField(max_length=500)
    image = models.ImageField(upload_to='notice_image',blank=True)
    date = models.DateField(auto_now=True)


    def __str__(self):
        return self.branch


class consessionadmin(models.Model):	
    user = models.OneToOneField(User,on_delete=models.CASCADE, null=True)
    full_name=models.CharField(max_length=50, null=True )
    image=models.ImageField(upload_to='profile_image',blank=True)
    mobile_no=models.CharField(max_length=12, null=True )
    address=models.CharField(max_length=200, null=True)
    def __str__(self):
        return self.user.username

class consessionformmodel(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE, null=True)
    last_ticket_from = models.CharField(max_length=50,choices=LAST_STATION_CHOICE)
    last_ticket_to = models.CharField(max_length=50,choices=STATION_CHOICE)
    last_ticket_type = models.CharField(max_length=50,choices=LAST_TICKET_TYPE_CHOICE)
    last_ticket_period = models.CharField(max_length=50,choices=LAST_TICKET_PERIOD_CHOICE)
    last_certificate_no = models.CharField(max_length=50)
    last_ticket_no = models.CharField(max_length=50)
    from_date = models.DateField(null=True)
    status = models.IntegerField(
        choices=((1, "Accepted"), (2, 'Rejected'), (3, 'Pending')),
        default=3,
    )
    def __str__(self):
        return self.user.username

class newconsessionformmodel(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE, null=True)
    ticket_from = models.CharField(max_length=50,choices=LAST_STATION_CHOICE)
    ticket_to = models.CharField(max_length=50,choices=STATION_CHOICE)
    ticket_type = models.CharField(max_length=50,choices=LAST_TICKET_TYPE_CHOICE)
    ticket_period = models.CharField(max_length=50,choices=LAST_TICKET_PERIOD_CHOICE)

    from_date = models.DateField(null=True)
    status = models.IntegerField(
        choices=((1, "Accepted"), (2, 'Rejected'), (3, 'Pending')),
        default=3,
    )
    def __str__(self):
        return self.user.username















