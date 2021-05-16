from django import forms

# Create your forms here.

class ContactForm(forms.Form):
    first_name = forms.CharField(max_length=50, label='Имя')
    last_name = forms.CharField(max_length=50, label='Фамилия')
    middle_name = forms.CharField(max_length=50, label='Отчество')
    email = forms.EmailField(max_length=50, label='Емайл')
    phone = forms.CharField(max_length=50, label='Номер телефона')
    work_place = forms.CharField(max_length=50, label='Место работы/учебы')
    title_of_report = forms.CharField(max_length=50, label='Название доклада')
    scientific_director = forms.CharField(max_length=50, label='Научный руководитель (Ф.И.О., ученая степень и звание)')
