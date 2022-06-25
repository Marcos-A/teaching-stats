from django import forms
from django.utils.safestring import mark_safe
from forms.helpers import get_questions_type_and_statement_by_level_and_topic


class EvaluateSchoolESOBatx(forms.Form):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        
        questions_type_and_statement_list = get_questions_type_and_statement_by_level_and_topic('ESO', 'Centre')

        for sort, question_tuple in enumerate(questions_type_and_statement_list, start=1):
            question_type = question_tuple[0]
            question_statement = question_tuple[1]
            # Required numeric question
            if question_type == 'Numeric':
                self.fields['question{}'.format(sort)] = forms.IntegerField(label=mark_safe("<br><li><p>" + question_statement + "<br>" +
                                                    "<small><i>Resposta obligatòria.</i></small></p></li>"),
                                    required=True,
                                    widget=forms.RadioSelect(
                                    attrs={'class':'form-control', 'class':'form-check-inline', 'required':'required'},
                                    choices=[('1', 1), ('2', 2), ('3', 3),('4', 4), ('5', 5), ('6', 6),
                                                ('7', 7), ('8', 8), ('9', 9), ('10', 10)]))
            # Non-required text question
            else:
                self.fields['question{}'.format(sort)] = forms.CharField(label=mark_safe("<br><li><p>" + question_statement + "<br>"
                                                            "<small><i>Opcional, però molt important si penses que hi ha coses que cal canviar. " +
                                                            "Extensió màxima: 280 caràcters.</i></small></p></li>"),
                                            max_length=280,
                                            required=False,
                                            widget=forms.Textarea(
                                            attrs={'class':'form-control',
                                                    'placeholder':"Escriu aquí la teva opinió. " +
                                                                "Extensió màxima: 280 caràcters."},)
                                            )


class EvaluateSchoolCF(forms.Form):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        
        questions_type_and_statement_list = get_questions_type_and_statement_by_level_and_topic('Cicles Formatius', 'Centre')

        for sort, question_tuple in enumerate(questions_type_and_statement_list, start=1):
            question_type = question_tuple[0]
            question_statement = question_tuple[1]
            # Required numeric question
            if question_type == 'Numeric':
                self.fields['question{}'.format(sort)] = forms.IntegerField(label=mark_safe("<br><li><p>" + question_statement + "<br>" +
                                                    "<small><i>Resposta obligatòria.</i></small></p></li>"),
                                    required=True,
                                    widget=forms.RadioSelect(
                                    attrs={'class':'form-control', 'class':'form-check-inline', 'required':'required'},
                                    choices=[('1', 1), ('2', 2), ('3', 3),('4', 4), ('5', 5), ('6', 6),
                                                ('7', 7), ('8', 8), ('9', 9), ('10', 10)]))
            # Non-required text question
            else:
                self.fields['question{}'.format(sort)] = forms.CharField(label=mark_safe("<br><li><p>" + question_statement + "<br>"
                                                            "<small><i>Opcional, però molt important si penses que hi ha coses que cal canviar. " +
                                                            "Extensió màxima: 280 caràcters.</i></small></p></li>"),
                                            max_length=280,
                                            required=False,
                                            widget=forms.Textarea(
                                            attrs={'class':'form-control',
                                                    'placeholder':"Escriu aquí la teva opinió. " +
                                                                "Extensió màxima: 280 caràcters."},)
                                            )
     

class EvaluateCounselingCF1(forms.Form):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        
        questions_type_and_statement_list = get_questions_type_and_statement_by_level_and_topic('Cicles Formatius', 'Tutoria 1r CF')

        for sort, question_tuple in enumerate(questions_type_and_statement_list, start=1):
            question_type = question_tuple[0]
            question_statement = question_tuple[1]
            # Required numeric question
            if question_type == 'Numeric':
                self.fields['question{}'.format(sort)] = forms.IntegerField(label=mark_safe("<br><li><p>" + question_statement + "<br>" +
                                                    "<small><i>Resposta obligatòria.</i></small></p></li>"),
                                    required=True,
                                    widget=forms.RadioSelect(
                                    attrs={'class':'form-control', 'class':'form-check-inline', 'required':'required'},
                                    choices=[('1', 1), ('2', 2), ('3', 3),('4', 4), ('5', 5), ('6', 6),
                                                ('7', 7), ('8', 8), ('9', 9), ('10', 10)]))
            # Non-required text question
            else:
                self.fields['question{}'.format(sort)] = forms.CharField(label=mark_safe("<br><li><p>" + question_statement + "<br>"
                                                            "<small><i>Opcional, però molt important si penses que hi ha coses que cal canviar. " +
                                                            "Extensió màxima: 280 caràcters.</i></small></p></li>"),
                                            max_length=280,
                                            required=False,
                                            widget=forms.Textarea(
                                            attrs={'class':'form-control',
                                                    'placeholder':"Escriu aquí la teva opinió. " +
                                                                "Extensió màxima: 280 caràcters."},)
                                            )


class EvaluateCounselingCF2(forms.Form):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        
        questions_type_and_statement_list = get_questions_type_and_statement_by_level_and_topic('Cicles Formatius', 'Tutoria 2n CF')

        for sort, question_tuple in enumerate(questions_type_and_statement_list, start=1):
            question_type = question_tuple[0]
            question_statement = question_tuple[1]
            # Required numeric question
            if question_type == 'Numeric':
                self.fields['question{}'.format(sort)] = forms.IntegerField(label=mark_safe("<br><li><p>" + question_statement + "<br>" +
                                                    "<small><i>Resposta obligatòria.</i></small></p></li>"),
                                    required=True,
                                    widget=forms.RadioSelect(
                                    attrs={'class':'form-control', 'class':'form-check-inline', 'required':'required'},
                                    choices=[('1', 1), ('2', 2), ('3', 3),('4', 4), ('5', 5), ('6', 6),
                                                ('7', 7), ('8', 8), ('9', 9), ('10', 10)]))
            # Non-required text question
            else:
                self.fields['question{}'.format(sort)] = forms.CharField(label=mark_safe("<br><li><p>" + question_statement + "<br>"
                                                            "<small><i>Opcional, però molt important si penses que hi ha coses que cal canviar. " +
                                                            "Extensió màxima: 280 caràcters.</i></small></p></li>"),
                                            max_length=280,
                                            required=False,
                                            widget=forms.Textarea(
                                            attrs={'class':'form-control',
                                                    'placeholder':"Escriu aquí la teva opinió. " +
                                                                "Extensió màxima: 280 caràcters."},)
                                            )


class EvaluateSubjectCF(forms.Form):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # Remove ":"" as label suffix
        self.label_suffix = ""  

        questions_type_and_statement_list = get_questions_type_and_statement_by_level_and_topic('Cicles Formatius', 'Assignatura')
        
        for sort, question_tuple in enumerate(questions_type_and_statement_list, start=1):
            question_type = question_tuple[0]
            question_statement = question_tuple[1]
            # Required numeric question
            if question_type == 'Numeric':
                self.fields['question{}'.format(sort)] = forms.IntegerField(label=mark_safe("<br><li><p>" + question_statement + "<br>" +
                                                    "<small><i>Resposta obligatòria.</i></small></p></li>"),
                                    required=True,
                                    widget=forms.RadioSelect(
                                    attrs={'class':'form-control', 'class':'form-check-inline', 'required':'required'},
                                    choices=[('1', 1), ('2', 2), ('3', 3),('4', 4), ('5', 5), ('6', 6),
                                                ('7', 7), ('8', 8), ('9', 9), ('10', 10)]))
            # Non-required text question
            else:
                self.fields['question{}'.format(sort)] = forms.CharField(label=mark_safe("<br><li><p>" + question_statement + "<br>"
                                                            "<small><i>Opcional, però molt important si penses que hi ha coses que cal canviar. " +
                                                            "Extensió màxima: 280 caràcters.</i></small></p></li>"),
                                            max_length=280,
                                            required=False,
                                            widget=forms.Textarea(
                                            attrs={'class':'form-control',
                                                    'placeholder':"Escriu aquí la teva opinió. " +
                                                                "Extensió màxima: 280 caràcters."},)
                                            )
