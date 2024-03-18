from django.shortcuts import render


notebook = [
    "1. Зустріч з клієнтом: \n"
    "Дата: 2024-03-14\n"
    "Час: 10:00 - 11:00\n"
    "Опис: Обговорення деталей щодо проведення процедур у суді.",
    "2. Покупки:"
       "Дата: 2024-03-14"
       "Продукти:"
       "- Молоко"
       "- Хліб"
       "- Яйця",
    "3. Завдання на сьогодні:"
    "\t- Підготувати звіт для збору фінансової звітності."
    "\t- Переглянути документи щодо нового проекту."
    "\t- Зателефонувати клієнту для підтвердження зустрічі.",

]

def homepage(request):
    return render(
        request=request,
        template_name='homepage.html',
        context={
            'notes': notebook
        }
    )