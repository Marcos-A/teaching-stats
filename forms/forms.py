from typing import List
from django import forms
from .models import Evaluation
from django.utils.safestring import mark_safe
from django.contrib.auth.models import User


class EvaluateSchool(forms.Form):
     item1 = forms.IntegerField(label=mark_safe("<p>Creus que les relacions entre les persones del centre són bones?<br>" +
                                                "<small><i>Resposta obligatòria.</i></small></p>"),
                                widget=forms.RadioSelect(
                                   attrs={'class':'form-control', 'class':'form-check-inline'},
                                   choices=[('1', 1), ('2', 2), ('3', 3),('4', 4), ('5', 5), ('6', 6),
                                            ('7', 7), ('8', 8), ('9', 9), ('10', 10)]))
     item2 = forms.IntegerField(label=mark_safe("<p>T'identifiques amb el centre?<br>" +
                                                "<small><i>Resposta obligatòria.</i></small></p>"),
                                widget=forms.RadioSelect(
                                   attrs={'class':'form-control', 'class':'form-check-inline'},
                                   choices=[('1', 1), ('2', 2), ('3', 3),('4', 4), ('5', 5), ('6', 6),
                                            ('7', 7), ('8', 8), ('9', 9), ('10', 10)]))
     item3 = forms.IntegerField(label=mark_safe("<p>Es resolen correctament els conflictes de convivència?<br>" +
                                                "<small><i>Resposta obligatòria.</i></small></p>"),
                                widget=forms.RadioSelect(
                                   attrs={'class':'form-control', 'class':'form-check-inline'},
                                   choices=[('1', 1), ('2', 2), ('3', 3),('4', 4), ('5', 5), ('6', 6),
                                            ('7', 7), ('8', 8), ('9', 9), ('10', 10)]))
     item4 = forms.IntegerField(label=mark_safe("<p>T'agraden les activitats extraescolars que es fan dins i fora del centre? " +
                                                "(Xerrades, competicions esportives, sortides, etc.)<br>" +
                                                "<small><i>Resposta obligatòria.</i></small></p>"),
                                widget=forms.RadioSelect(
                                   attrs={'class':'form-control', 'class':'form-check-inline'},
                                   choices=[('1', 1), ('2', 2), ('3', 3),('4', 4), ('5', 5), ('6', 6),
                                            ('7', 7), ('8', 8), ('9', 9), ('10', 10)]))
     item5 = forms.IntegerField(label=mark_safe("<p>Estàs globalment satisfet de la teva estada al centre?<br>" +
                                                "<small><i>Resposta obligatòria.</i></small></p>"),
                                widget=forms.RadioSelect(
                                   attrs={'class':'form-control', 'class':'form-check-inline'},
                                   choices=[('1', 1), ('2', 2), ('3', 3),('4', 4), ('5', 5), ('6', 6),
                                            ('7', 7), ('8', 8), ('9', 9), ('10', 10)]))
     opinion = forms.CharField(label=mark_safe("<p>Si us plau, fes una proposta per millorar algun d'aquests aspectes.<br>" +
                                               "<small><i>Opcional, però molt important si penses que hi ha coses a millorar. " +
                                               "Extensió màxima: 280 caràcters.</i></small></p>"),
                               max_length=280,
                               required=False,
                               widget=forms.Textarea(
                                 attrs={'class':'form-control',
                                        'placeholder':"Escriu aquí la teva opinió. " +
                                                      "Extensió màxima: 280 caràcters."},
                               ))
     
     def record_evaluation(self, timestamp, level, classgroup):
          new_evaluation = Evaluation(timestamp=timestamp,
                                      level=level,
                                      classgroup=classgroup,
                                      item1=self.data['item1'],
                                      item2=self.data['item2'],
                                      item3=self.data['item3'],
                                      item4=self.data['item4'],
                                      item5=self.data['item5'],
                                      opinion=self.data['opinion'])
          new_evaluation.save()
