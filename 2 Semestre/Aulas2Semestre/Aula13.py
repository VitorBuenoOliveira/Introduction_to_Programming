def herdeiros(familia):
    def encontrar_herdeiros(familia, pai):
        herdeiros = [p['nome'] for p in familia if p['pai'] == pai]
        if not herdeiros:
            return ""
        herdeiros_str = '   -> '.join(herdeiros)
        for herdeiro in herdeiros:
            descendentes = encontrar_herdeiros(familia, herdeiro)
            if descendentes:
                herdeiros_str += " -> " + descendentes
        return herdeiros_str

    return encontrar_herdeiros(familia, None)

minhaFamilia = [
    {'nome': 'Eduardo', 'pai': None},
    {'nome': 'Lucas', 'pai': 'Eduardo'},
    {'nome': 'Pedro', 'pai': 'Lucas'},
    {'nome': 'João', 'pai': 'Pedro'},
]

print(herdeiros(minhaFamilia))  # 'Eduardo -> Lucas -> Pedro -> João'
