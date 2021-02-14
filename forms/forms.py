from django import forms
from django.utils.safestring import mark_safe


class EvaluateSchoolESOBatx(forms.Form):
    question1 = forms.IntegerField(label=mark_safe("<p>Creus que les relacions entre les persones del centre són bones?<br>" +
                                                   "<small><i>Resposta obligatòria.</i></small></p>"),
                                   required=True,
                                   widget=forms.RadioSelect(
                                   attrs={'class':'form-control', 'class':'form-check-inline'},
                                   choices=[('1', 1), ('2', 2), ('3', 3),('4', 4), ('5', 5), ('6', 6),
                                            ('7', 7), ('8', 8), ('9', 9), ('10', 10)]))

    question2 = forms.IntegerField(label=mark_safe("<p>T'identifiques amb el centre?<br>" +
                                                   "<small><i>Resposta obligatòria.</i></small></p>"),
                                   required=True,
                                   widget=forms.RadioSelect(
                                   attrs={'class':'form-control', 'class':'form-check-inline'},
                                   choices=[('1', 1), ('2', 2), ('3', 3),('4', 4), ('5', 5), ('6', 6),
                                            ('7', 7), ('8', 8), ('9', 9), ('10', 10)]))

    question3 = forms.IntegerField(label=mark_safe("<p>Es resolen correctament els conflictes de convivència?<br>" +
                                                   "<small><i>Resposta obligatòria.</i></small></p>"),
                                   required=True,
                                   widget=forms.RadioSelect(
                                   attrs={'class':'form-control', 'class':'form-check-inline'},
                                   choices=[('1', 1), ('2', 2), ('3', 3),('4', 4), ('5', 5), ('6', 6),
                                            ('7', 7), ('8', 8), ('9', 9), ('10', 10)]))

    question4 = forms.IntegerField(label=mark_safe("<p>T'agraden les activitats extraescolars que es fan dins i fora del centre? " +
                                                   "(Xerrades, competicions esportives, sortides, etc.)<br>" +
                                                   "<small><i>Resposta obligatòria.</i></small></p>"),
                                   required=True,
                                   widget=forms.RadioSelect(
                                   attrs={'class':'form-control', 'class':'form-check-inline'},
                                   choices=[('1', 1), ('2', 2), ('3', 3),('4', 4), ('5', 5), ('6', 6),
                                            ('7', 7), ('8', 8), ('9', 9), ('10', 10)]))

    question5 = forms.IntegerField(label=mark_safe("<p>Estàs globalment satisfet de la teva estada al centre?<br>" +
                                                   "<small><i>Resposta obligatòria.</i></small></p>"),
                                   required=True,
                                   widget=forms.RadioSelect(
                                   attrs={'class':'form-control', 'class':'form-check-inline'},
                                   choices=[('1', 1), ('2', 2), ('3', 3),('4', 4), ('5', 5), ('6', 6),
                                            ('7', 7), ('8', 8), ('9', 9), ('10', 10)]))
    
    opinion = forms.CharField(label=mark_safe("<p>Si us plau, fes una proposta per millorar algun d'aquests aspectes.<br>" +
                                              "<small><i>Opcional, però molt important si penses que hi ha coses que cal canviar." +
                                              "Extensió màxima: 280 caràcters.</i></small></p>"),
                              max_length=280,
                              required=False,
                              widget=forms.Textarea(
                              attrs={'class':'form-control',
                                     'placeholder':"Escriu aquí la teva opinió. " +
                                                   "Extensió màxima: 280 caràcters."},)
                              )


class EvaluateSchoolCF(forms.Form):
    question1 = forms.IntegerField(label=mark_safe("<p>Creus que les relacions entre les persones del centre són bones?<br>" +
                                                   "<small><i>Resposta obligatòria.</i></small></p>"),
                                   required=True,
                                   widget=forms.RadioSelect(
                                   attrs={'class':'form-control', 'class':'form-check-inline'},
                                   choices=[('1', 1), ('2', 2), ('3', 3),('4', 4), ('5', 5), ('6', 6),
                                            ('7', 7), ('8', 8), ('9', 9), ('10', 10)]))
         
    question2 = forms.IntegerField(label=mark_safe("<p>T'identifiques amb el centre?<br>" +
                                                   "<small><i>Resposta obligatòria.</i></small></p>"),
                                   required=True,
                                   widget=forms.RadioSelect(
                                   attrs={'class':'form-control', 'class':'form-check-inline'},
                                   choices=[('1', 1), ('2', 2), ('3', 3),('4', 4), ('5', 5), ('6', 6),
                                            ('7', 7), ('8', 8), ('9', 9), ('10', 10)]))
         
    question3 = forms.IntegerField(label=mark_safe("<p>Es resolen correctament els conflictes de convivència?<br>" +
                                                   "<small><i>Resposta obligatòria.</i></small></p>"),
                                   required=True,
                                   widget=forms.RadioSelect(
                                   attrs={'class':'form-control', 'class':'form-check-inline'},
                                   choices=[('1', 1), ('2', 2), ('3', 3),('4', 4), ('5', 5), ('6', 6),
                                            ('7', 7), ('8', 8), ('9', 9), ('10', 10)]))
         
    question4 = forms.IntegerField(label=mark_safe("<p>Funcionen bé els serveis de borsa de treball i biblioteca?<br>" +
                                                   "<small><i>Resposta obligatòria.</i></small></p>"),
                                   required=True,
                                   widget=forms.RadioSelect(
                                   attrs={'class':'form-control', 'class':'form-check-inline'},
                                   choices=[('1', 1), ('2', 2), ('3', 3),('4', 4), ('5', 5), ('6', 6),
                                            ('7', 7), ('8', 8), ('9', 9), ('10', 10)]))
         
    question5 = forms.IntegerField(label=mark_safe("<p>T'agraden les activitats extraescolars que es fan dins i fora del centre? " +
                                                   "(Xerrades, competicions esportives, sortides, etc.)<br>" +
                                                   "<small><i>Resposta obligatòria.</i></small></p>"),
                                   required=True,
                                   widget=forms.RadioSelect(
                                   attrs={'class':'form-control', 'class':'form-check-inline'},
                                   choices=[('1', 1), ('2', 2), ('3', 3),('4', 4), ('5', 5), ('6', 6),
                                            ('7', 7), ('8', 8), ('9', 9), ('10', 10)]))

    question6 = forms.IntegerField(label=mark_safe("<p>Estàs globalment satisfet de la teva estada al centre?<br>" +
                                                   "<small><i>Resposta obligatòria.</i></small></p>"),
                                   required=True,
                                   widget=forms.RadioSelect(
                                   attrs={'class':'form-control', 'class':'form-check-inline'},
                                   choices=[('1', 1), ('2', 2), ('3', 3),('4', 4), ('5', 5), ('6', 6),
                                   ('7', 7), ('8', 8), ('9', 9), ('10', 10)]))
         
    opinion = forms.CharField(label=mark_safe("<p>Si us plau, fes una proposta per millorar algun d'aquests aspectes.<br>" +
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
    question1 = forms.IntegerField(label=mark_safe("<p>Valora el grau d'atenció que has rebut i la capacitat d'escoltar del tutor.<br>" +
                                                   "<small><i>Resposta obligatòria.</i></small></p>"),
                                   required=True,
                                   widget=forms.RadioSelect(
                                   attrs={'class':'form-control', 'class':'form-check-inline'},
                                   choices=[('1', 1), ('2', 2), ('3', 3),('4', 4), ('5', 5), ('6', 6),
                                            ('7', 7), ('8', 8), ('9', 9), ('10', 10)]))
         
    question2 = forms.IntegerField(label=mark_safe("<p>Valora el grau de disponibilitat del tutor.<br>" +
                                                   "<small><i>Resposta obligatòria.</i></small></p>"),
                                   required=True,
                                   widget=forms.RadioSelect(
                                   attrs={'class':'form-control', 'class':'form-check-inline'},
                                   choices=[('1', 1), ('2', 2), ('3', 3),('4', 4), ('5', 5), ('6', 6),
                                            ('7', 7), ('8', 8), ('9', 9), ('10', 10)]))
         
    question3 = forms.IntegerField(label=mark_safe("<p>Penses que el tutor t'ha mantingut prou informat? " +
                                                   "(De dates del curs, informació relativa al cicle, activitats de l'institut, beques, etc.)<br>" +
                                                   "<small><i>Resposta obligatòria.</i></small></p>"),
                                   required=True,
                                   widget=forms.RadioSelect(
                                   attrs={'class':'form-control', 'class':'form-check-inline'},
                                   choices=[('1', 1), ('2', 2), ('3', 3),('4', 4), ('5', 5), ('6', 6),
                                            ('7', 7), ('8', 8), ('9', 9), ('10', 10)]))

    opinion = forms.CharField(label=mark_safe("<p>Si us plau, fes una proposta per millorar la tutoria.<br>" +
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
    question1 = forms.IntegerField(label=mark_safe("<p>Valora el grau d'atenció que has rebut i la capacitat d'escoltar del tutor.<br>" +
                                                   "<small><i>Resposta obligatòria.</i></small></p>"),
                                   required=True,
                                   widget=forms.RadioSelect(
                                   attrs={'class':'form-control', 'class':'form-check-inline'},
                                   choices=[('1', 1), ('2', 2), ('3', 3),('4', 4), ('5', 5), ('6', 6),
                                            ('7', 7), ('8', 8), ('9', 9), ('10', 10)]))
         
    question2 = forms.IntegerField(label=mark_safe("<p>Valora el grau de disponibilitat del tutor.<br>" +
                                                   "<small><i>Resposta obligatòria.</i></small></p>"),
                                   required=True,
                                   widget=forms.RadioSelect(
                                   attrs={'class':'form-control', 'class':'form-check-inline'},
                                   choices=[('1', 1), ('2', 2), ('3', 3),('4', 4), ('5', 5), ('6', 6),
                                            ('7', 7), ('8', 8), ('9', 9), ('10', 10)]))
         
    question3 = forms.IntegerField(label=mark_safe("<p>Penses que el tutor t'ha mantingut prou informat? " +
                                                   "(De dates del curs, informació relativa al cicle, activitats de l'institut, beques, etc.)<br>" +
                                                   "<small><i>Resposta obligatòria.</i></small></p>"),
                                   required=True,
                                   widget=forms.RadioSelect(
                                   attrs={'class':'form-control', 'class':'form-check-inline'},
                                   choices=[('1', 1), ('2', 2), ('3', 3),('4', 4), ('5', 5), ('6', 6),
                                            ('7', 7), ('8', 8), ('9', 9), ('10', 10)]))

    question4 = forms.IntegerField(label=mark_safe("<p>Valora l'orientació rebuda sobre les sortides acadèmiques i professionals en acabar el cicle. " +
                                                   "(Accés a la universitat, altres CFGS, etc.)<br>" +
                                                   "<small><i>Resposta obligatòria.</i></small></p>"),
                                   required=True,
                                   widget=forms.RadioSelect(
                                   attrs={'class':'form-control', 'class':'form-check-inline'},
                                   choices=[('1', 1), ('2', 2), ('3', 3),('4', 4), ('5', 5), ('6', 6),
                                            ('7', 7), ('8', 8), ('9', 9), ('10', 10)]))

    opinion = forms.CharField(label=mark_safe("<p>Si us plau, fes una proposta per millorar la tutoria.<br>" +
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

    question1 = forms.IntegerField(label=mark_safe("<p>Avalua la metodologia d'aprenentatge, l'organització de la classe i l'assistència rebuda.<br>" +
                                                   "<small><i>Resposta obligatòria.</i></small></p>"),
                                   required=True,
                                   widget=forms.RadioSelect(
                                   attrs={'class':'form-control', 'class':'form-check-inline'},
                                   choices=[('1', 1), ('2', 2), ('3', 3),('4', 4), ('5', 5), ('6', 6),
                                            ('7', 7), ('8', 8), ('9', 9), ('10', 10)]))
         
    question2 = forms.IntegerField(label=mark_safe("<p>Penses que la manera d'avaluar és l'adequada?<br>" +
                                                   "<small><i>Resposta obligatòria.</i></small></p>"),
                                   required=True,
                                   widget=forms.RadioSelect(
                                   attrs={'class':'form-control', 'class':'form-check-inline'},
                                   choices=[('1', 1), ('2', 2), ('3', 3),('4', 4), ('5', 5), ('6', 6),
                                            ('7', 7), ('8', 8), ('9', 9), ('10', 10)]))
         
    question3 = forms.IntegerField(label=mark_safe("<p>Penses que el que has après pot ser útil a la teva futura vida professional?<br>" +
                                                   "<small><i>Resposta obligatòria.</i></small></p>"),
                                   required=True,
                                   widget=forms.RadioSelect(
                                   attrs={'class':'form-control', 'class':'form-check-inline'},
                                   choices=[('1', 1), ('2', 2), ('3', 3),('4', 4), ('5', 5), ('6', 6),
                                            ('7', 7), ('8', 8), ('9', 9), ('10', 10)]))

    question4 = forms.IntegerField(label=mark_safe("<p>Penses que el material triat pel professor és l'adequat? " + 
                                                   "(Llibre o apunts, Moodle, activitats, transparències, videotutorials...)<br>" +
                                                   "<small><i>Resposta obligatòria.</i></small></p>"),
                                   required=True,
                                   widget=forms.RadioSelect(
                                   attrs={'class':'form-control', 'class':'form-check-inline'},
                                   choices=[('1', 1), ('2', 2), ('3', 3),('4', 4), ('5', 5), ('6', 6),
                                            ('7', 7), ('8', 8), ('9', 9), ('10', 10)]))

    opinion = forms.CharField(label=mark_safe("<p>Si us plau, fes una proposta per millorar la tutoria.<br>" +
                                              "<small><i>Opcional, però molt important si penses que hi ha coses que cal canviar. " +
                                              "Extensió màxima: 280 caràcters.</i></small></p>"),
                              max_length=280,
                              required=False,
                              widget=forms.Textarea(
                              attrs={'class':'form-control',
                                     'placeholder':"Escriu aquí la teva opinió. " +
                                                   "Extensió màxima: 280 caràcters."},)
                              )
