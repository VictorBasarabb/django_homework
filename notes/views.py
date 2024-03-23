from django.shortcuts import render

from notes.models import Category, Note


category1 = Category.objects.create(title='Work')
category2 = Category.objects.create(title='Personal')
category3 = Category.objects.create(title='Study')

note1 = Note.objects.create(title='Meeting', text='Meeting with client', category=category1)
note2 = Note.objects.create(title='Groceries', text='Buy milk and bread', category=category2)
note3 = Note.objects.create(title='Study Python', text='Learn Django framework', category=category3)
note4 = Note.objects.create(title='Exercise', text='Go for a run', category=category2)
note5 = Note.objects.create(title='Shopping', text='Buy clothes', category=category2)


def homepage(request):
    notes = Note.objects.all()
    return render(
        request=request,
        template_name='homepage.html',
        context={'notes': notes}
    )

