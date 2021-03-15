from django.forms import ModelForm
import requests
from .models import Comentario

class FormComentario(ModelForm):
    def clean(self):
        raw_data = self.data
        recaptcha_resp = raw_data.get('g-recaptcha-response')

        if not recaptcha_resp:
            self.add_error(\
                'comentario',
                'Marque o recaptcha.'
            )

        # https://www.google.com/recaptcha/api/siteverify
        # secret_key
        # resposta captcha

        recaptcha_req = requests.post(
            'https://www.google.com/recaptcha/api/siteverify',
            data={
                'secret': '6LeCrYAaAAAAAOP9w4IhHeID0J-ytwpY4JWmNF1O',
                'response' : recaptcha_resp
            }
        )
        recaptcha_result = recaptcha_req.json()

            

        cleaned_data = self.cleaned_data
        nome = cleaned_data.get('nome_comentario')
        email = cleaned_data.get('email_comentario')
        comentario = cleaned_data.get('comentario')

        if len(nome) < 5:
            self.add_error(\
                    'nome_comentario',
                    'Nome precisa ter mais que 5 caracteres.'
                )


    class Meta:
        model = Comentario
        fields = ('nome_comentario', 'email_comentario', 'comentario')



