def listar():
    for chave in agenda:
        for valor in agenda[chave]:
            print(valor)
        print()

agenda = {
    "a": ["ane"] ,
    "b": ["bruna", "bianca"],
    "c": ["camilo"]
}

entrada = input("Digite o seu contato: ") # ana
inicial = entrada[0] # "a"

agenda[inicial].append(entrada)

listar()

contato_remove = input("Digite o contato para remover: ")
inicial_de_quem_eu_quero_remover = contato_remove[0]

agenda[inicial_de_quem_eu_quero_remover].remove(contato_remove)

listar()
