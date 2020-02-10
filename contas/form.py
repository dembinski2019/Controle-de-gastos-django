from django.forms import ModelForm
from .models import Transacao


class TransacaoForm(ModelForm):
    class Meta:
        model = Transacao
        fields = ['date', 'descricao','valor', 'observacoes', 'categoria']
