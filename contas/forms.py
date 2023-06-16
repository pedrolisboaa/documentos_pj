from django import forms
from django.core.validators import FileExtensionValidator
from .models import RecemConstruida

class RecemConstruidaForm(forms.ModelForm):
    
    documento_identidade = forms.FileField(
        widget=forms.ClearableFileInput(attrs={'accept': 'image/*,application/pdf,application/msword'}),
        validators=[FileExtensionValidator(allowed_extensions=['pdf', 'doc', 'docx', 'jpg', 'jpeg', 'png'])]
    )
    comprovante_residencia = forms.FileField(
        widget=forms.ClearableFileInput(attrs={'accept': 'image/*,application/pdf,application/msword'}),
        validators=[FileExtensionValidator(allowed_extensions=['pdf', 'doc', 'docx', 'jpg', 'jpeg', 'png'])]
    )
    irpf = forms.FileField(
        widget=forms.ClearableFileInput(attrs={'accept': 'image/*,application/pdf,application/msword'}),
        validators=[FileExtensionValidator(allowed_extensions=['pdf', 'doc', 'docx', 'jpg', 'jpeg', 'png'])]
    )
    certidao_casamento = forms.FileField(
        widget=forms.ClearableFileInput(attrs={'accept': 'image/*,application/pdf,application/msword'}),
        validators=[FileExtensionValidator(allowed_extensions=['pdf', 'doc', 'docx', 'jpg', 'jpeg', 'png'])]
    )
    contrato_constituicao = forms.FileField(
        widget=forms.ClearableFileInput(attrs={'accept': 'image/*,application/pdf,application/msword'}),
        validators=[FileExtensionValidator(allowed_extensions=['pdf', 'doc', 'docx', 'jpg', 'jpeg', 'png'])]
    )
    certidao_simplificada_junta = forms.FileField(
        widget=forms.ClearableFileInput(attrs={'accept': 'image/*,application/pdf,application/msword'}),
        validators=[FileExtensionValidator(allowed_extensions=['pdf', 'doc', 'docx', 'jpg', 'jpeg', 'png'])]
    )
    relacao_faturamento = forms.FileField(
        widget=forms.ClearableFileInput(attrs={'accept': 'image/*,application/pdf,application/msword'}),
        validators=[FileExtensionValidator(allowed_extensions=['pdf', 'doc', 'docx', 'jpg', 'jpeg', 'png'])]
    )

    class Meta:
        model = RecemConstruida
        fields = [
            'nome_completo', 
            'email', 
            'documento_identidade', 
            'comprovante_residencia', 
            'irpf', 
            'certidao_casamento', 
            'contrato_constituicao',
            'certidao_simplificada_junta',
            'relacao_faturamento'
        ]



