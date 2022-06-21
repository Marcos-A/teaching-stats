from django import forms
from django.utils.safestring import mark_safe

from forms.helpers import get_question_statement


class EvaluateSchoolESOBatx(forms.Form):
    question1 = forms.IntegerField(label=mark_safe("<p>" + get_question_statement(1, 'Numeric', 'ESO', 'Centre') + "<br>" +
                                                   "<small><i>Resposta obligatòria.</i></small></p>"),
                                   required=True,
                                   widget=forms.RadioSelect(
                                   attrs={'class':'form-control', 'class':'form-check-inline'},
                                   choices=[('1', 1), ('2', 2), ('3', 3),('4', 4), ('5', 5), ('6', 6),
                                            ('7', 7), ('8', 8), ('9', 9), ('10', 10)]))

    question2 = forms.IntegerField(label=mark_safe("<p>" + get_question_statement(2, 'Numeric', 'ESO', 'Centre') + "<br>" +
                                                   "<small><i>Resposta obligatòria.</i></small></p>"),
                                   required=True,
                                   widget=forms.RadioSelect(
                                   attrs={'class':'form-control', 'class':'form-check-inline'},
                                   choices=[('1', 1), ('2', 2), ('3', 3),('4', 4), ('5', 5), ('6', 6),
                                            ('7', 7), ('8', 8), ('9', 9), ('10', 10)]))

    question3 = forms.IntegerField(label=mark_safe("<p>" + get_question_statement(3, 'Numeric', 'ESO', 'Centre') + "<br>" +
                                                   "<small><i>Resposta obligatòria.</i></small></p>"),
                                   required=True,
                                   widget=forms.RadioSelect(
                                   attrs={'class':'form-control', 'class':'form-check-inline'},
                                   choices=[('1', 1), ('2', 2), ('3', 3),('4', 4), ('5', 5), ('6', 6),
                                            ('7', 7), ('8', 8), ('9', 9), ('10', 10)]))

    question4 = forms.IntegerField(label=mark_safe("<p>" + get_question_statement(4, 'Numeric', 'ESO', 'Centre') + "<br>" +
                                                   "<small><i>Resposta obligatòria.</i></small></p>"),
                                   required=True,
                                   widget=forms.RadioSelect(
                                   attrs={'class':'form-control', 'class':'form-check-inline'},
                                   choices=[('1', 1), ('2', 2), ('3', 3),('4', 4), ('5', 5), ('6', 6),
                                            ('7', 7), ('8', 8), ('9', 9), ('10', 10)]))

    question5 = forms.IntegerField(label=mark_safe("<p>" + get_question_statement(5, 'Numeric', 'ESO', 'Centre') + "<br>" +
                                                   "<small><i>Resposta obligatòria.</i></small></p>"),
                                   required=True,
                                   widget=forms.RadioSelect(
                                   attrs={'class':'form-control', 'class':'form-check-inline'},
                                   choices=[('1', 1), ('2', 2), ('3', 3),('4', 4), ('5', 5), ('6', 6),
                                            ('7', 7), ('8', 8), ('9', 9), ('10', 10)]))
    
    opinion = forms.CharField(label=mark_safe("<p>" + get_question_statement(6, 'Text', 'ESO', 'Centre') + "<br>" +
                                              "<small><i>Opcional, però molt important si penses que hi ha coses que cal canviar. " +
                                              "Extensió màxima: 280 caràcters.</i></small></p>"),
                              max_length=280,
                              required=False,
                              widget=forms.Textarea(
                              attrs={'class':'form-control',
                                     'placeholder':"Escriu aquí la teva opinió. " +
                                                   "Extensió màxima: 280 caràcters."},)
                              )


class EvaluateSchoolCF(forms.Form):
    question1 = forms.IntegerField(label=mark_safe("<p>" + get_question_statement(1, 'Numeric', 'Cicles Formatius', 'Centre') + "<br>" +
                                                   "<small><i>Resposta obligatòria.</i></small></p>"),
                                   required=True,
                                   widget=forms.RadioSelect(
                                   attrs={'class':'form-control', 'class':'form-check-inline'},
                                   choices=[('1', 1), ('2', 2), ('3', 3),('4', 4), ('5', 5), ('6', 6),
                                            ('7', 7), ('8', 8), ('9', 9), ('10', 10)]))
         
    question2 = forms.IntegerField(label=mark_safe("<p>" + get_question_statement(2, 'Numeric', 'Cicles Formatius', 'Centre') + "<br>" +
                                                   "<small><i>Resposta obligatòria.</i></small></p>"),
                                   required=True,
                                   widget=forms.RadioSelect(
                                   attrs={'class':'form-control', 'class':'form-check-inline'},
                                   choices=[('1', 1), ('2', 2), ('3', 3),('4', 4), ('5', 5), ('6', 6),
                                            ('7', 7), ('8', 8), ('9', 9), ('10', 10)]))
         
    question3 = forms.IntegerField(label=mark_safe("<p>" + get_question_statement(3, 'Numeric', 'Cicles Formatius', 'Centre') + "<br>" +
                                                   "<small><i>Resposta obligatòria.</i></small></p>"),
                                   required=True,
                                   widget=forms.RadioSelect(
                                   attrs={'class':'form-control', 'class':'form-check-inline'},
                                   choices=[('1', 1), ('2', 2), ('3', 3),('4', 4), ('5', 5), ('6', 6),
                                            ('7', 7), ('8', 8), ('9', 9), ('10', 10)]))
         
    question4 = forms.IntegerField(label=mark_safe("<p>" + get_question_statement(4, 'Numeric', 'Cicles Formatius', 'Centre') + "<br>" +
                                                   "<small><i>Resposta obligatòria.</i></small></p>"),
                                   required=True,
                                   widget=forms.RadioSelect(
                                   attrs={'class':'form-control', 'class':'form-check-inline'},
                                   choices=[('1', 1), ('2', 2), ('3', 3),('4', 4), ('5', 5), ('6', 6),
                                            ('7', 7), ('8', 8), ('9', 9), ('10', 10)]))
         
    question5 = forms.IntegerField(label=mark_safe("<p>" + get_question_statement(5, 'Numeric', 'Cicles Formatius', 'Centre') + "<br>" +
                                                   "<small><i>Resposta obligatòria.</i></small></p>"),
                                   required=True,
                                   widget=forms.RadioSelect(
                                   attrs={'class':'form-control', 'class':'form-check-inline'},
                                   choices=[('1', 1), ('2', 2), ('3', 3),('4', 4), ('5', 5), ('6', 6),
                                            ('7', 7), ('8', 8), ('9', 9), ('10', 10)]))

    question6 = forms.IntegerField(label=mark_safe("<p>" + get_question_statement(6, 'Numeric', 'Cicles Formatius', 'Centre') + "<br>" +
                                                   "<small><i>Resposta obligatòria.</i></small></p>"),
                                   required=True,
                                   widget=forms.RadioSelect(
                                   attrs={'class':'form-control', 'class':'form-check-inline'},
                                   choices=[('1', 1), ('2', 2), ('3', 3),('4', 4), ('5', 5), ('6', 6),
                                   ('7', 7), ('8', 8), ('9', 9), ('10', 10)]))
         
    opinion = forms.CharField(label=mark_safe("<p>" + get_question_statement(7, 'Text', 'Cicles Formatius', 'Centre') + "<br>" +
                                              "<small><i>Opcional, però molt important si penses que hi ha coses que cal canviar. " +
                                              "Extensió màxima: 280 caràcters.</i></small></p>"),
                              max_length=280,
                              required=False,
                              widget=forms.Textarea(
                              attrs={'class':'form-control',
                                     'placeholder':"Escriu aquí la teva opinió. " +
                                                   "Extensió màxima: 280 caràcters."},)
                              )
         

class EvaluateCounselingCF1(forms.Form):
    question1 = forms.IntegerField(label=mark_safe("<p>" + get_question_statement(1, 'Numeric', 'Cicles Formatius', 'Tutoria 1r CF') + "<br>" +
                                                   "<small><i>Resposta obligatòria.</i></small></p>"),
                                   required=True,
                                   widget=forms.RadioSelect(
                                   attrs={'class':'form-control', 'class':'form-check-inline'},
                                   choices=[('1', 1), ('2', 2), ('3', 3),('4', 4), ('5', 5), ('6', 6),
                                            ('7', 7), ('8', 8), ('9', 9), ('10', 10)]))
         
    question2 = forms.IntegerField(label=mark_safe("<p>" + get_question_statement(2, 'Numeric', 'Cicles Formatius', 'Tutoria 1r CF') + "<br>" +
                                                   "<small><i>Resposta obligatòria.</i></small></p>"),
                                   required=True,
                                   widget=forms.RadioSelect(
                                   attrs={'class':'form-control', 'class':'form-check-inline'},
                                   choices=[('1', 1), ('2', 2), ('3', 3),('4', 4), ('5', 5), ('6', 6),
                                            ('7', 7), ('8', 8), ('9', 9), ('10', 10)]))
         
    question3 = forms.IntegerField(label=mark_safe("<p>" + get_question_statement(3, 'Numeric', 'Cicles Formatius', 'Tutoria 1r CF') + "<br>" +
                                                   "<small><i>Resposta obligatòria.</i></small></p>"),
                                   required=True,
                                   widget=forms.RadioSelect(
                                   attrs={'class':'form-control', 'class':'form-check-inline'},
                                   choices=[('1', 1), ('2', 2), ('3', 3),('4', 4), ('5', 5), ('6', 6),
                                            ('7', 7), ('8', 8), ('9', 9), ('10', 10)]))

    opinion = forms.CharField(label=mark_safe("<p>" + get_question_statement(4, 'Text', 'Cicles Formatius', 'Tutoria 1r CF') + "<br>" +
                                              "<small><i>Opcional, però molt important si penses que hi ha coses que cal canviar. " +
                                              "Extensió màxima: 280 caràcters.</i></small></p>"),
                              max_length=280,
                              required=False,
                              widget=forms.Textarea(
                              attrs={'class':'form-control',
                                      'placeholder':"Escriu aquí la teva opinió. " +
                                                    "Extensió màxima: 280 caràcters."},)
                              )
         

class EvaluateCounselingCF2(forms.Form):
    question1 = forms.IntegerField(label=mark_safe("<p>" + get_question_statement(1, 'Numeric', 'Cicles Formatius', 'Tutoria 2n CF') + "<br>" +
                                                   "<small><i>Resposta obligatòria.</i></small></p>"),
                                   required=True,
                                   widget=forms.RadioSelect(
                                   attrs={'class':'form-control', 'class':'form-check-inline'},
                                   choices=[('1', 1), ('2', 2), ('3', 3),('4', 4), ('5', 5), ('6', 6),
                                            ('7', 7), ('8', 8), ('9', 9), ('10', 10)]))
         
    question2 = forms.IntegerField(label=mark_safe("<p>" + get_question_statement(2, 'Numeric', 'Cicles Formatius', 'Tutoria 2n CF') + "<br>" +
                                                   "<small><i>Resposta obligatòria.</i></small></p>"),
                                   required=True,
                                   widget=forms.RadioSelect(
                                   attrs={'class':'form-control', 'class':'form-check-inline'},
                                   choices=[('1', 1), ('2', 2), ('3', 3),('4', 4), ('5', 5), ('6', 6),
                                            ('7', 7), ('8', 8), ('9', 9), ('10', 10)]))
         
    question3 = forms.IntegerField(label=mark_safe("<p>" + get_question_statement(3, 'Numeric', 'Cicles Formatius', 'Tutoria 2n CF') + "<br>" +
                                                   "<small><i>Resposta obligatòria.</i></small></p>"),
                                   required=True,
                                   widget=forms.RadioSelect(
                                   attrs={'class':'form-control', 'class':'form-check-inline'},
                                   choices=[('1', 1), ('2', 2), ('3', 3),('4', 4), ('5', 5), ('6', 6),
                                            ('7', 7), ('8', 8), ('9', 9), ('10', 10)]))

    question4 = forms.IntegerField(label=mark_safe("<p>" + get_question_statement(4, 'Numeric', 'Cicles Formatius', 'Tutoria 2n CF') + "<br>" +
                                                   "<small><i>Resposta obligatòria.</i></small></p>"),
                                   required=True,
                                   widget=forms.RadioSelect(
                                   attrs={'class':'form-control', 'class':'form-check-inline'},
                                   choices=[('1', 1), ('2', 2), ('3', 3),('4', 4), ('5', 5), ('6', 6),
                                            ('7', 7), ('8', 8), ('9', 9), ('10', 10)]))

    opinion = forms.CharField(label=mark_safe("<p>" + get_question_statement(5, 'Text', 'Cicles Formatius', 'Tutoria 2n CF') + "<br>" +
                                              "<small><i>Opcional, però molt important si penses que hi ha coses que cal canviar. " +
                                              "Extensió màxima: 280 caràcters.</i></small></p>"),
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

        # Custom error message for empty required responses
        for field in self.fields.values():
            field.error_messages = {'required':'SI US PLAU, NO DEIXIS LA PREGUNTA SENSE RESPOSTA!'}

    question1 = forms.IntegerField(label=mark_safe("<p>" + get_question_statement(1, 'Numeric', 'Cicles Formatius', 'Assignatura') + "<br>" +
                                                   "<small><i>Resposta obligatòria.</i></small></p>"),
                                   required=True,
                                   widget=forms.RadioSelect(
                                   attrs={'class':'form-control', 'class':'form-check-inline', 'required':'required'},
                                   choices=[('1', 1), ('2', 2), ('3', 3),('4', 4), ('5', 5), ('6', 6),
                                            ('7', 7), ('8', 8), ('9', 9), ('10', 10)]))
         
    question2 = forms.IntegerField(label=mark_safe("<p>" + get_question_statement(2, 'Numeric', 'Cicles Formatius', 'Assignatura') + "<br>" +
                                                   "<small><i>Resposta obligatòria.</i></small></p>"),
                                   required=True,
                                   widget=forms.RadioSelect(
                                   attrs={'class':'form-control', 'class':'form-check-inline', 'required':'required'},
                                   choices=[('1', 1), ('2', 2), ('3', 3),('4', 4), ('5', 5), ('6', 6),
                                            ('7', 7), ('8', 8), ('9', 9), ('10', 10)]))
         
    question3 = forms.IntegerField(label=mark_safe("<p>" + get_question_statement(3, 'Numeric', 'Cicles Formatius', 'Assignatura') + "<br>" +
                                                   "<small><i>Resposta obligatòria.</i></small></p>"),
                                   required=True,
                                   widget=forms.RadioSelect(
                                   attrs={'class':'form-control', 'class':'form-check-inline', 'required':'required'},
                                   choices=[('1', 1), ('2', 2), ('3', 3),('4', 4), ('5', 5), ('6', 6),
                                            ('7', 7), ('8', 8), ('9', 9), ('10', 10)]))

    question4 = forms.IntegerField(label=mark_safe("<p>" + get_question_statement(4, 'Numeric', 'Cicles Formatius', 'Assignatura') + "<br>" +
                                                   "<small><i>Resposta obligatòria.</i></small></p>"),
                                   required=True,
                                   widget=forms.RadioSelect(
                                   attrs={'class':'form-control', 'class':'form-check-inline', 'required':'required'},
                                   choices=[('1', 1), ('2', 2), ('3', 3),('4', 4), ('5', 5), ('6', 6),
                                            ('7', 7), ('8', 8), ('9', 9), ('10', 10)]))

    opinion = forms.CharField(label=mark_safe("<p>" + get_question_statement(5, 'Text', 'Cicles Formatius', 'Assignatura') + "<br>"
                                              "<small><i>Opcional, però molt important si penses que hi ha coses que cal canviar. " +
                                              "Extensió màxima: 280 caràcters.</i></small></p>"),
                              max_length=280,
                              required=False,
                              widget=forms.Textarea(
                              attrs={'class':'form-control',
                                     'placeholder':"Escriu aquí la teva opinió. " +
                                                   "Extensió màxima: 280 caràcters."},)
                              )
