# coding: utf-8
"""
    project: main
    module created: 24.02.2016
"""

from django.db import models

from Quo.constants import MILITARY_COMISSARIAT_TYPES, GRADE_TYPES, \
                          DEGREE_OF_FITNESS_TYPES, \
                          DEPARTMENT_TYPES, VUS_TYPES


class Person(models.Model):
    """Обучающийся на ВК"""
    first_name = models.CharField(u"Имя", max_length=100, default="Имя")
    middle_name = models.CharField(u"Фамилия", max_length=100, default="Отчество")
    last_name = models.CharField(u"Отчество", max_length=100, default="Фамилия")
    birth_date = models.DateField(u"Дата рождения")
    is_learning = models.BooleanField(u"Обучается ли на военной кафедре?", default=False, blank=True)

    document_number = models.CharField(u"Серия и номер документа", max_length=100, default=" ", null=True, blank=True)
    issued_by = models.CharField(u"Выдан", max_length=100, default=" ", null=True, blank=True)
    birthplace = models.CharField(u"Место рождения", max_length=100, default="Москва", null=True, blank=True)
    address = models.CharField(u"Адресс", max_length=100, default="Москва", null=True, blank=True)

    military = models.ForeignKey('MilitaryCommissariat', verbose_name=u'Военкомат', null=True, blank=True)
    grade = models.ForeignKey('Grade', verbose_name=u'Звание', null=True, blank=True)
    degree = models.ForeignKey('DegreeOfFitness', verbose_name=u'Категория годности', null=True, blank=True)
    OKSO = models.ForeignKey('OKSO', verbose_name=u'ОКСО', null=True, blank=True)
    year = models.ForeignKey('Year', verbose_name=u'Год обучения', null=True, blank=True)
    VUS = models.ForeignKey('VUS', verbose_name=u'ВУС', null=True, blank=True)
    faculty = models.ForeignKey('Faculty', verbose_name=u'Факультет', null=True)
    department = models.ForeignKey('Department', verbose_name=u'Кафедра', null=True)
    group = models.ForeignKey('Group', verbose_name=u'Группа', null=True)

    def __unicode__(self):
        return u'{} {}'.format((self.first_name or ''), (self.middle_name or ''))

    class Meta:
        verbose_name = u"Студент"
        verbose_name_plural = u"Студенты"


class MilitaryCommissariat(models.Model):
    title = models.CharField(u"Военкомат", max_length=2550,
                             choices=MILITARY_COMISSARIAT_TYPES)

    def __unicode__(self):
        return self.title

    class Meta:
        verbose_name = u"Военкомат"
        verbose_name_plural = u"Военкоматы"


class Grade(models.Model):
    grade = models.CharField(u"Направление обучения", max_length=255, choices=GRADE_TYPES)

    def __unicode__(self):
        return self.grade

    class Meta:
        verbose_name = u"Направление обучения"
        verbose_name_plural = u"Направления обучения"


class DegreeOfFitness(models.Model):
    degree_of_fitness = models.CharField(u"Группа здоровья", max_length=255,
                                         choices=DEGREE_OF_FITNESS_TYPES)

    def __unicode__(self):
        return self.degree_of_fitness

    class Meta:
        verbose_name = u"Группа здоровья"
        verbose_name_plural = u"Группы здоровья"


class Faculty(models.Model):
    faculty = models.CharField(u"Факультет", max_length=255,
                               choices=DEPARTMENT_TYPES)

    def __unicode__(self):
        return self.faculty

    class Meta:
        verbose_name = u"Факультет"
        verbose_name_plural = u"Факультеты"


class Department(models.Model):
    department = models.CharField(u"Кафедра", max_length=255,
                                  choices=((str(x), x) for x in range(1, 13)))

    def __unicode__(self):
        return self.department

    class Meta:
        verbose_name = u"Кафедра"
        verbose_name_plural = u"Кафедры"


class Group(models.Model):
    group = models.CharField(u"Группа", max_length=100, default=11)

    def __unicode__(self):
        return self.group

    class Meta:
        verbose_name = u"Группа"
        verbose_name_plural = u"Группы"


class OKSO(models.Model):
    OKSO = models.CharField(u"ОКСО", max_length=255)

    def __unicode__(self):
        return self.OKSO

    class Meta:
        verbose_name = u"код ОКСО"
        verbose_name_plural = u"коды ОКСО"


class VUS(models.Model):
    VUS = models.CharField(u"ВУС", max_length=255,
                           choices=VUS_TYPES)

    def __unicode__(self):
        return self.VUS

    class Meta:
        verbose_name = u"код ВУС"
        verbose_name_plural = u"коды ВУС"


class Year(models.Model):
    year = models.CharField(u"Год обучения", max_length=255,
                            choices=((str(x), x) for x in range(1, 4)))

    def __unicode__(self):
        return self.year

    class Meta:
        verbose_name = u"Год обучения"
        verbose_name_plural = u"Годы обучения"



