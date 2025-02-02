from django.db import models

class Municipio(models.Model):
    nome = models.CharField(max_length=100)

    def __str__(self):
        return self.nome


class Pessoa(models.Model):
    tipo_doc = models.CharField(max_length=50)
    doc_ident = models.CharField(max_length=50, primary_key=True)
    id_mun = models.ForeignKey(Municipio, on_delete=models.CASCADE, related_name="pessoas")
    nome = models.CharField(max_length=255)
    dt_nac = models.DateField(null=True, blank=True)
    email = models.EmailField(null=True, blank=True)
    ddd = models.CharField(max_length=5, null=True, blank=True)
    celular = models.CharField(max_length=15, null=True, blank=True)
    nacionalidade = models.CharField(max_length=100, null=True, blank=True)

    def __str__(self):
        return self.nome
    
    


class Endereco(models.Model):
    id_pes = models.OneToOneField(Pessoa, on_delete=models.CASCADE, primary_key=True, related_name="endereco")
    logradouro = models.CharField(max_length=255)
    numero = models.CharField(max_length=10)
    bairro = models.CharField(max_length=100)
    cep = models.CharField(max_length=20)

    def __str__(self):
        return f"{self.logradouro}, {self.numero}"
    
class PessoaFisica(Pessoa):
    cpf = models.CharField(max_length=14, unique=True)
    rg = models.CharField(max_length=20, unique=True, null=True, blank=True)
    affiliation_pai = models.CharField(max_length=255, null=True, blank=True)
    affiliaton_mae = models.CharField(max_length=255, null=True, blank=True)
    pis = models.CharField(max_length=11, unique=True, null=True, blank=True)

    ESCOLHER_GENERO = [(0, 'Não Informado'),(1, 'Masculino'),(2, 'Feminino'),(3, 'Outro'), ] #levar como opção
    genero = models.IntegerField(choices= ESCOLHER_GENERO, null=True, blank=True)


    def __str__(self):
        return f"{self.nome} - CPF: {self.cpf}"
    
    def get_cpf(self):
        return self.cpf

    def set_cpf(self, cpf):
        self.cpf = cpf
        self.save()

    def get_rg(self):
        return self.rg

    def set_rg(self, rg):
        self.rg = rg
        self.save()  

    def get_name(self):
        return self.nome 

    def set_name(self, nome):
        self.nome = nome
        self.save()

    def get_gender(self):
        return self.genero

    def set_gender(self, genero):
        self.genero = genero
        self.save()

    def get_birthday(self):
        return self.dt_nac

    def set_birthday(self, dt_nac):
        self.dt_nac = dt_nac
        self.save()
    
    def get_affiliation(self):
        return {"pai": self.filiacao_pai, "mae": self.filiacao_mae}

    def set_affiliation(self, pai: str, mae: str):
        self.filiacao_pai = pai
        self.filiacao_mae = mae
        self.save()
    
    def get_nacionality(self):
        return self.nacionalidade
    
    def set_nacionality(self, nacionalidade):
        self.nacionalidade = nacionalidade
        self.save()

    def get_pis(self):
        return self.pis

    def set_pis(self, pis: str):
        self.pis = pis
        self.save()
