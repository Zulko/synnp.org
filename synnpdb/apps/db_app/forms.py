""" Basic models, such as user profile """

import models
from django import forms

from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Div, Submit, HTML, Button, Row, Field, Fieldset
from crispy_forms.bootstrap import AppendedText, PrependedText, FormActions

#from django_summernote.widgets import SummernoteWidget, SummernoteInplaceWidget

# PEOPLE

class AssayForm(forms.ModelForm):
    class Meta:
        model = models.Assay
        fields = ['author', 'results_summary', 'content']
        widgets = {
             'content': forms.widgets.Textarea(attrs={
                'class':'summernoteTextarea'
            }),
            "results_summary":forms.widgets.Textarea(attrs={
                'class':'form-control',
                'lines':1
            })
        }

    def __init__(self, *args, **kwargs):

        # If you pass FormHelper constructor a form instance
        # It builds a default layout with all its fields
        super(AssayForm, self).__init__(*args, **kwargs)

        self.helper = FormHelper(self)
        self.helper.form_method = 'post'

        self.helper.form_class = 'form-horizontal'
        self.helper.label_class = 'col-lg-2'
        self.helper.field_class = 'col-lg-8'

        super(AssayForm, self).__init__(*args, **kwargs)

        self.helper.add_input(Submit('upload', 'Upload file'))
        self.helper.add_input(Submit('save', 'Save changes'))
        self.helper.add_input(Submit('cancel', 'Cancel'))
    # helper = FormHelper()
    # helper.form_class = 'form-horizontal'
    # helper.layout = Layout(
    #     Fieldset(
    #             Field('result_summary', css_class='input-xlarge'),
    #             Field('content', css_class='summernoteTextarea')
    #     ),
    #     FormActions(
    #         Submit('save_changes', 'Save changes', css_class="btn-primary"),
    #         Submit('cancel', 'Cancel')
    #     )
    # )
