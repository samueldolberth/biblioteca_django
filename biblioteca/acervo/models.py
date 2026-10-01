from django.db import models

class Autor(models.Model):
    nome = models.CharField(max_length=100)
    ano_nascimento = models.IntegerField(null=True, blank=True)
    nacionalidade = models.CharField(max_length=50)

    def __str__(self):
        return self.nome

class Livro(models.Model):
    titulo = models.CharField(max_length=120)
    autor = models.ForeignKey(Autor, on_delete=models.CASCADE)
    categoria = models.CharField(max_length=50)
    ano = models.IntegerField()
    disponivel = models.BooleanField(default=True)

    def __str__(self):
        return self.titulo

class Emprestimo(models.Model):
    livro = models.ForeignKey(Livro, on_delete=models.CASCADE)
    data_emprestimo = models.DateField(auto_now_add=True)
    data_devolucao = models.DateField(null=True, blank=True)

    def __str__(self):
        return f"Empréstimo de {self.livro.titulo} em {self.data_emprestimo}"