from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Field, Submit
from crispy_forms.bootstrap import FieldWithButtons, StrictButton
from django import forms


class FeedbackForm(forms.Form):
    hotel_name = forms.CharField(label='Название отеля', widget=forms.Textarea)
    feedback = forms.CharField(label='Отзыв', widget=forms.Textarea(attrs={'rows': 4}))

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
        super(FeedbackForm, self).init(*args, **kwargs)
        self.helper = FormHelper(self)
        self.helper.form_method = 'post'
        self.helper.layout = Layout(
            Field('hotel_name', rows='1', css_class='mb-3', wrapper_class='col-md-6'),
            Field('feedback', css_class='mb-3', wrapper_class='col-md-6'),
            FieldWithButtons(
                Field('submit', css_class='btn btn-primary'),
                StrictButton('Отмена', css_class='btn btn-secondary', type='reset')
            )
        )
        self.helper.form_class = 'form-horizontal'
        self.helper.label_class = 'col-md-2'
        self.helper.field_class = 'col-md-10'
        self.helper.use_custom_control = True
        self.helper.template_pack = 'bootstrap5'
