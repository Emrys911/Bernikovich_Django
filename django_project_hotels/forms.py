from django import forms
from django.core.exceptions import ValidationError


# Валидатор для проверки возраста
def validate_age(value):
    if not 18 <= value <= 90:
        raise ValidationError('Возраст должен быть от 18 до 90 лет.')


class UserForm(forms.Form):
    name = forms.CharField(label='Имя', max_length=100)
    age = forms.IntegerField(label='Возраст', validators=[validate_age])

    # Дополнительные настройки с помощью Crispy Forms
    def __init__(
            self,
            data=None,
            files=None,
            auto_id="id_%s",
            prefix=None,
            initial=None,
            error_class=ErrorList,
            label_suffix=None,
            empty_permitted=False,
            field_order=None,
            use_required_attribute=None,
            renderer=None,
    ):
        super().__init__(data, files, auto_id, prefix, initial, error_class, label_suffix, empty_permitted, field_order,
                         use_required_attribute, renderer)
        self.helper = None

    def init(self, *args, **kwargs):
        super(UserForm, self).init(*args, **kwargs)
        self.helper = FormHelper(self)
        self.helper.form_method = 'post'
        self.helper.layout = Layout(
            'name',
            'age',
            Submit('submit', 'Добавить пользователя')
        )
