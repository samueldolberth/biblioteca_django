from django.contrib import admin

from .models import Autor, Emprestimo, Livro

# registrar os modelos para aparecer no admin
admin.site.register(Autor)

@admin.register(Livro)
class LivroAdmin(admin.ModelAdmin):
    list_display = ("titulo", "autor", "categoria", "ano", "disponivel")
    list_filter = ("categoria", "disponivel")
    search_fields = ("titulo", "autor")
    list_aditable = ("disponivel")


admin.site.register(Emprestimo)

