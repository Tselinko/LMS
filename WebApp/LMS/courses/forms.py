from django import forms
from .models import StudentsHomeworks, Materials, Homeworks


class AddHomeworkForm(forms.ModelForm):
    class Meta:
        model = StudentsHomeworks
        fields = ('material', )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs['class'] = 'form-control'


class MaterialForm(forms.ModelForm):
    class Meta:
        model = Materials
        fields = ('title', 'description', 'material_сontent',)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs['class'] = 'form-control'


class HomeworkForm(forms.ModelForm):
    class Meta:
        model = Homeworks
        fields = ('title', 'description', 'date_of_beggining', 'deadline',)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs['class'] = 'form-control'

