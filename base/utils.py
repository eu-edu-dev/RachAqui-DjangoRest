from django.core.exceptions import ValidationError
import re

LIST_OF_COUNTY = [
    ('AC', 'Acre'),
    ('AL', 'Alagoas'),
    ('AP', 'Amapá'),
    ('AM', 'Amazonas'),
    ('BA', 'Bahia'),
    ('CE', 'Ceará'),
    ('DF', 'Distrito Federal'),
    ('ES', 'Espírito Santo'),
    ('GO', 'Goiás'),
    ('MA', 'Maranhão'),
    ('MT', 'Mato Grosso'),
    ('MS', 'Mato Grosso do Sul'),
    ('MG', 'Minas Gerais'),
    ('PR', 'Paraná'),
    ('PB', 'Paraíba'),
    ('PA', 'Pará'),
    ('PE', 'Pernambuco'),
    ('PI', 'Piauí'),
    ('RJ', 'Rio de Janeiro'),
    ('RN', 'Rio Grande do Norte'),
    ('RS', 'Rio Grande do Sul'),
    ('RO', 'Rondônia'),
    ('RR', 'Roraima'),
    ('SC', 'Santa Catarina'),
    ('SE', 'Sergipe'),
    ('SP', 'São Paulo'),
    ('TO', 'Tocantins'),
    ('EX', 'Exterior'),
]

TRUE_OR_FALSE_CHOICES = [
    ('F', False),
    ('T', True),
]


def validate_cpf(cpf):
    # Remove formatting characters
    cpf = re.sub(r'[.-]', '', cpf)

    # Check if the CPF has 11 digits
    if not cpf.isdigit() or len(cpf) != 11:
        raise ValidationError('Invalid CPF')


def validate_cnpj(cnpj):
    # Remove formatting characters
    cnpj = re.sub(r'[./-]', '', cnpj)

    # Check if the CNPJ has 14 digits
    if not cnpj.isdigit() or len(cnpj) != 14:
        raise ValidationError('Invalid CNPJ')


def validate_cep(cep):
    # Remove formatting characters
    cep = re.sub(r'[^0-9]', '', cep)

    # Check if the CEP has 8 digits
    if not cep.isdigit() or len(cep) != 8:
        raise ValidationError('Invalid CEP')


def validate_phone(phone):
    # Remove formatting characters
    phone = re.sub(r'[^0-9]', '', phone)
