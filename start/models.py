from django.contrib.auth.models import User
from django.db import models


# Статусы -----------------------------------------------
from HR_CRM_System.settings import MEDIA_ROOT


class DenialStatus(models.Model):
    CHOICES = (
        ('Активный', 'Активный'),
        ('Отказ рекрутёра', 'Отказ рекрутёра'),
        ('Отказ соискателя', 'Отказ соискателя'),
        ('Отказ заказчика', 'Отказ заказчика'),
    )
    status = models.CharField(choices=CHOICES, max_length=300)

    class Meta:
        db_table = 'denialStatus'
        verbose_name = 'DenialStatus'
        verbose_name_plural = 'DenialStatus'

class CallStatus(models.Model):
    CHOICES = (
        ('Состоялось', 'Состоялось'),
        ('Перезвонить', 'Перезвонить'),
        ('Недозвон', 'Недозвон')
    )
    status = models.CharField(choices=CHOICES, max_length=300)

    class Meta:
        db_table = 'callStatus'
        verbose_name = 'CallStatus'
        verbose_name_plural = 'CallStatus'


class MeetStatus(models.Model):
    CHOICES = (
        ('Запланировано', 'Запланировано'),
        ('Состоялось', 'Состоялось'),
        ('Не состоялось', 'Не состоялось')
    )
    status = models.CharField(choices=CHOICES, max_length=300)

    class Meta:
        db_table = 'meetStatus'
        verbose_name = 'MeetStatus'
        verbose_name_plural = 'MeetStatus'


class MeetEmpStatus(models.Model):
    CHOICES = (
        ('Состоялось', 'Состоялось'),
        ('Перезвонить', 'Перезвонить'),
        ('Недозвон', 'Недозвон')
    )
    status = models.CharField(choices=CHOICES, max_length=300)

    class Meta:
        db_table = 'meetEmpStatus'
        verbose_name = 'MeetEmpStatus'
        verbose_name_plural = 'MeetEmpStatus'


class TestStatus(models.Model):
    CHOICES = (
        ('В работе', 'В работе'),
        ('Не выполнено', 'Не выполнено'),
        ('Отказ от выполнения', 'Отказ от выполнения'),
        ('Выполнено', 'Выполнено'),
    )
    status = models.CharField(choices=CHOICES, max_length=300)

    class Meta:
        db_table = 'testStatus'
        verbose_name = 'TestStatus'
        verbose_name_plural = 'TestStatus'

class StatusJob(models.Model):
    CHOICES = (
        ('Открыта', 'Открыта'),
        ('Закрыта', 'Закрыта'),
        ('Заморожена', 'Заморожена')
    )
    status = models.CharField(choices=CHOICES, max_length=300)

    class Meta:
        db_table = 'statusjob'
        verbose_name = 'StatusJob'
        verbose_name_plural = 'StatusJob'

        def __str__(self):
            return self.status


# Сущности ----------------------------------------------

class Job(models.Model):
    name = models.TextField()
    salary = models.IntegerField()
    expirence = models.IntegerField()
    employment = models.TextField()
    definition = models.TextField(null=True)
    id_status = models.ForeignKey('StatusJob',on_delete=models.DO_NOTHING,db_column='id_status')
    user = models.ForeignKey(User,on_delete=models.DO_NOTHING)

    class Meta:
        db_table = 'jobs'
        verbose_name = 'Job'
        verbose_name_plural = 'Jobs'

    # def save(self, *args, **kwargs):
    #     self.id_status = StatusJob.objects.get(pk=0)
    #     super().save(*args,**kwargs)
def userCV_directory_path(instance, filename):
    return 'candidate/CV/' + filename

def userPhoto_directory_path(instance, filename):
    # путь, куда будет осуществлена загрузка MEDIA_ROOT/user_<id>/<filename>
    return 'candidate/photo/' + filename

class Candidate(models.Model):
    name = models.TextField()
    phone = models.TextField()
    email = models.EmailField()
    sex = models.TextField()
    photo = models.ImageField(upload_to=userPhoto_directory_path)
    birthdate = models.DateField()
    cv = models.FileField(upload_to=userCV_directory_path)

    class Meta:
        db_table = 'candidates'
        verbose_name = 'Candidate'
        verbose_name_plural = 'Candidates'

class JobSeek(models.Model):
    job = models.ForeignKey('Job',on_delete=models.DO_NOTHING, db_column='job')
    candidate = models.ForeignKey('Candidate',on_delete=models.DO_NOTHING,db_column='candidate')
    offer = models.IntegerField()
    offer_definition = models.TextField()
    release_date = models.DateField()
    denial_status = models.ForeignKey('DenialStatus',on_delete=models.DO_NOTHING, db_column='denial_status')
    call_status = models.ForeignKey('CallStatus',on_delete=models.DO_NOTHING, db_column='call_status')
    call_status_defenition = models.TextField(null=True)
    test_status = models.ForeignKey('TestStatus',on_delete=models.DO_NOTHING, db_column='test_status')
    test_status_defenition = models.TextField(null=True)
    meet_status = models.ForeignKey('MeetStatus',on_delete=models.DO_NOTHING, db_column='meet_status')
    meet_status_defenition = models.TextField(null=True)
    meetemp_status = models.ForeignKey('MeetEmpStatus',on_delete=models.DO_NOTHING, db_column='meetemp_status')
    meetemp_status_defenition = models.TextField(null=True)

    class Meta:
        db_table = 'jobseek'
        verbose_name = 'JobSeek'
        verbose_name_plural = 'JobSeek'


class ActionHistory(models.Model):
    job_seek = models.ForeignKey('JobSeek',on_delete=models.DO_NOTHING, db_column='job_seek')
    action_name = models.TextField()
    value_before = models.TextField()
    value_after = models.TextField()
    data = models.DateField()

    class Meta:
        db_table = 'actionHistory'
        verbose_name = 'ActionHistory'
        verbose_name_plural = 'ActionHistory'
