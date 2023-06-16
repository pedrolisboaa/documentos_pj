from django.db import models
from django.utils import timezone

# Create your models here.


class RecemConstruida(models.Model):
    tipo_empresa = models.CharField(max_length=100, default='Recém Construída')
    nome_completo = models.CharField(verbose_name='Nome Completo', max_length=250)
    email = models.EmailField(verbose_name='Email')
    documento_identidade = models.FileField(upload_to='documentacao/%Y/%m')
    comprovante_residencia = models.FileField(upload_to='documentacao/%Y/%m')
    irpf = models.FileField(upload_to='documentacao/%Y/%m')
    certidao_casamento = models.FileField(upload_to='documentacao/%Y/%m')
    contrato_constituicao = models.FileField(upload_to='documentacao/%Y/%m')
    certidao_simplificada_junta = models.FileField(upload_to='documentacao/%Y/%m')
    relacao_faturamento = models.FileField(upload_to='documentacao/%Y/%m')
    data_recebimento_documentacao = models.DateTimeField(default=timezone.now)


    def __str__(self):
        return self.nome_completo
    

class Mei(models.Model):
    tipo_empresa = models.CharField(max_length=100, default='MEI')
    nome_completo = models.CharField(verbose_name='Nome Completo', max_length=250)
    email = models.EmailField(verbose_name='Email')
    documento_identidade = models.FileField(upload_to='documentacao/%Y/%m')
    comprovante_residencia = models.FileField(upload_to='documentacao/%Y/%m')
    irpf = models.FileField(upload_to='documentacao/%Y/%m')
    certidao_casamento = models.FileField(upload_to='documentacao/%Y/%m')
    requerimento_empresario = models.FileField(upload_to='documentacao/%Y/%m')
    simei = models.FileField(upload_to='documentacao/%Y/%m')
    data_recebimento_documentacao = models.DateTimeField(default=timezone.now)


    def __str__(self):
        return self.nome_completo
    

class Simples(models.Model):
    tipo_empresa = models.CharField(max_length=100, default='Simples')
    nome_completo = models.CharField(verbose_name='Nome Completo', max_length=250)
    email = models.EmailField(verbose_name='Email')
    documento_identidade = models.FileField(upload_to='documentacao/%Y/%m')
    comprovante_residencia = models.FileField(upload_to='documentacao/%Y/%m')
    irpf = models.FileField(upload_to='documentacao/%Y/%m')
    certidao_casamento = models.FileField(upload_to='documentacao/%Y/%m')

    alteracao_contratual = models.FileField(upload_to='documentacao/%Y/%m')
    certidao_simplificada = models.FileField(upload_to='documentacao/%Y/%m')
    extrato_simples = models.FileField(upload_to='documentacao/%Y/%m')
    faturamento = models.FileField(upload_to='documentacao/%Y/%m')
    data_recebimento_documentacao = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.nome_completo


class LucroReal(models.Model):
    tipo_empresa = models.CharField(max_length=100, default='Lucro Real / Presumido')
    nome_completo = models.CharField(verbose_name='Nome Completo', max_length=250)
    email = models.EmailField(verbose_name='Email')
    documento_identidade = models.FileField(upload_to='documentacao/%Y/%m')
    comprovante_residencia = models.FileField(upload_to='documentacao/%Y/%m')
    irpf = models.FileField(upload_to='documentacao/%Y/%m')
    certidao_casamento = models.FileField(upload_to='documentacao/%Y/%m')

    alteracao_contratual = models.FileField(upload_to='documentacao/%Y/%m')
    certidao_simplificada = models.FileField(upload_to='documentacao/%Y/%m')
    balanco_dre = models.FileField(upload_to='documentacao/%Y/%m')
    faturamento = models.FileField(upload_to='documentacao/%Y/%m')
    ecf = models.FileField(upload_to='documentacao/%Y/%m')

    data_recebimento_documentacao = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.nome_completo


class Associacao(models.Model):
    tipo_empresa = models.CharField(max_length=100, default='Associações e Sindicatos')
    nome_completo = models.CharField(verbose_name='Nome Completo', max_length=250)
    email = models.EmailField(verbose_name='Email')
    documento_identidade = models.FileField(upload_to='documentacao/%Y/%m')
    comprovante_residencia = models.FileField(upload_to='documentacao/%Y/%m')
    irpf = models.FileField(upload_to='documentacao/%Y/%m')
    certidao_casamento = models.FileField(upload_to='documentacao/%Y/%m')

    estatuto_social = models.FileField(upload_to='documentacao/%Y/%m')
    ata_constituicao = models.FileField(upload_to='documentacao/%Y/%m')
    ata_eleicao = models.FileField(upload_to='documentacao/%Y/%m')
    faturamento = models.FileField(upload_to='documentacao/%Y/%m')
    

    data_recebimento_documentacao = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.nome_completo


class Condominio(models.Model):
    tipo_empresa = models.CharField(max_length=100, default='Associações e Sindicatos')
    nome_completo = models.CharField(verbose_name='Nome Completo', max_length=250)
    email = models.EmailField(verbose_name='Email')
    documento_identidade = models.FileField(upload_to='documentacao/%Y/%m')
    comprovante_residencia = models.FileField(upload_to='documentacao/%Y/%m')
    irpf = models.FileField(upload_to='documentacao/%Y/%m')
    certidao_casamento = models.FileField(upload_to='documentacao/%Y/%m')

    convencao = models.FileField(upload_to='documentacao/%Y/%m')
    ata = models.FileField(upload_to='documentacao/%Y/%m')
    faturamento = models.FileField(upload_to='documentacao/%Y/%m')
    

    data_recebimento_documentacao = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.nome_completo


class Cooperativa(models.Model):
    tipo_empresa = models.CharField(max_length=100, default='Associações e Sindicatos')
    nome_completo = models.CharField(verbose_name='Nome Completo', max_length=250)
    email = models.EmailField(verbose_name='Email')
    documento_identidade = models.FileField(upload_to='documentacao/%Y/%m')
    comprovante_residencia = models.FileField(upload_to='documentacao/%Y/%m')
    irpf = models.FileField(upload_to='documentacao/%Y/%m')
    certidao_casamento = models.FileField(upload_to='documentacao/%Y/%m')

    estatudo_social = models.FileField(upload_to='documentacao/%Y/%m')
    ata_fundacao = models.FileField(upload_to='documentacao/%Y/%m')
    ata_eleicao = models.FileField(upload_to='documentacao/%Y/%m')
    certidao_simplificada = models.FileField(upload_to='documentacao/%Y/%m')
    balanco_dre = models.FileField(upload_to='documentacao/%Y/%m')
    faturamento = models.FileField(upload_to='documentacao/%Y/%m')
   

    data_recebimento_documentacao = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.nome_completo

