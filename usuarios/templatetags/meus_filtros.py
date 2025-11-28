from django import template

register = template.Library()

@register.filter
def dict_get(d, key):
    if not d:
        return 0
    return d.get(key, 0)

@register.filter
def tipos_por_aluno(confirmacoes_rota, aluno_id):
    """
    confirmacoes_rota: dict {aluno_id: set([...])}
    """
    if not confirmacoes_rota:
        return set()
    return confirmacoes_rota.get(aluno_id, set())

