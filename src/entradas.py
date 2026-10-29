def resumo_entrada(matricula, horas=None, estado=None):
    matricula = matricula.strip()

    if matricula == "":
        matricula = "Sem identificação"

    valor_valido = (
        type(horas) is int 
        and 0 <= horas <= 24)

    estado_aceite = estado in {"ativa", "pendente"}

    return matricula, valor_valido, estado_aceite


#matricula, valor_valido, estado_aceite = resumo_entrada(
 #   "  AA-12-BB  ", 8, "ativa"
#)

#print(f"Identificação: {matricula} | Valor válido: {valor_valido} | Estado aceite: {estado_aceite}")