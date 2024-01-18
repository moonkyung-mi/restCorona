from django.db import models


class CoFacility(models.Model):
    loc = models.TextField(db_column='LOC', blank=True, null=True)  # Field name made lowercase.
    fac_popu = models.BigIntegerField(db_column='FAC_POPU', blank=True, null=True)  # Field name made lowercase.
    qur_rate = models.TextField(db_column='QUR_RATE', blank=True, null=True)  # Field name made lowercase.
    std_day = models.TextField(db_column='STD_DAY', blank=True, null=True)  # Field name made lowercase.
    cf_idx = models.BigIntegerField(db_column='CF_IDX', primary_key=True,)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'co_facility'


class CoPopuDensity(models.Model):
    loc = models.TextField(db_column='LOC', blank=True, null=True)  # Field name made lowercase.
    popu_density = models.BigIntegerField(blank=True, null=True)
    qur_rate = models.TextField(db_column='QUR_RATE', blank=True, null=True)  # Field name made lowercase.
    std_day = models.TextField(db_column='STD_DAY', blank=True, null=True)  # Field name made lowercase.
    cp_idx = models.BigIntegerField(db_column='CP_IDX',primary_key=True,)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'co_popu_density'


class CoVaccineThird(models.Model):
    loc = models.TextField(db_column='LOC', blank=True, null=True)  # Field name made lowercase.
    std_day = models.TextField(db_column='STD_DAY', blank=True, null=True)  # Field name made lowercase.
    third_rate = models.BigIntegerField(db_column='Third_RATE', blank=True, null=True)  # Field name made lowercase.
    qur_rate = models.TextField(db_column='QUR_RATE', blank=True, null=True)  # Field name made lowercase.
    cv_idx = models.BigIntegerField(db_column='CV_IDX', primary_key=True,)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'co_vaccine_third'


class CoWeekday(models.Model):
    index = models.TextField()
    fri = models.FloatField(db_column='FRI', blank=True, null=True)  # Field name made lowercase.
    mon = models.FloatField(db_column='MON', blank=True, null=True)  # Field name made lowercase.
    sat = models.FloatField(db_column='SAT', blank=True, null=True)  # Field name made lowercase.
    sun = models.FloatField(db_column='SUN', blank=True, null=True)  # Field name made lowercase.
    the = models.FloatField(db_column='THE', blank=True, null=True)  # Field name made lowercase.
    tue = models.FloatField(db_column='TUE', blank=True, null=True)  # Field name made lowercase.
    wed = models.FloatField(db_column='WED', blank=True, null=True)  # Field name made lowercase.
    std_day = models.TextField(db_column='STD_DAY', primary_key=True,)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'co_weekday'