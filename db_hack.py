from random import choice

from django.core.exceptions import MultipleObjectsReturned, ObjectDoesNotExist

from datacenter.models import (Chastisement, Commendation, Lesson, Mark,
                               Schoolkid)


def get_schoolkid(name):
    try:
        return Schoolkid.objects.filter(full_name__contains=name).get()
    except ObjectDoesNotExist:
        print("Ученик с таким именем не найден.")
    except MultipleObjectsReturned:
        print(
            "Учеников с таким именем слишком много.",
            "Попробуйте добавить фамилию или отчество."
        )


def fix_marks(schoolkid):
    bad_marks = Mark.objects.filter(schoolkid=schoolkid, points__lt=4)
    for mark in bad_marks:
        mark.points = 5
        mark.save()


def remove_chastisements(schoolkid):
    chastisements = Chastisement.objects.filter(schoolkid=schoolkid)
    for chastisement in chastisements:
        chastisement.delete()


def create_commendation(schoolkid, subject_title):
    commendation_texts = (
        "Молодец!",
        "Отлично!",
        "Хорошо!",
        "Приятно удивил!",
        "Великолепно!",
        "Очень хороший ответ!",
        "Замечательно!",
        "Так держать!",
        "Я тобой горжусь!",  
        "С каждым разом получается всё лучше!",
    )
    lessons = Lesson.objects.filter(
        year_of_study=schoolkid.year_of_study,
        group_letter=schoolkid.group_letter,
        subject__title=subject_title
    )
    if not lessons:
        print(
            f"Уроков по предмету '{subject_title}' не найдено.",
            "Проверьте название предмета.",
            "Название должно быть с заглавной буквы.",
        )
        return
    random_lesson = choice(lessons)
    commendation = Commendation.objects.create(
        text=choice(commendation_texts),
        created=random_lesson.date,
        schoolkid=schoolkid,
        subject=random_lesson.subject,
        teacher=random_lesson.teacher
    )
    commendation.save()
    return commendation
