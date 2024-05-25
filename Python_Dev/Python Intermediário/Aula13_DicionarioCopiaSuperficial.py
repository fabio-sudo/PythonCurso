import copy

# Criando um dicionário original
original_dict = {
    'key1': 1,
    'key2': 2,
    'list_key': [0, 1, 2],#Lisa dentro do dicionario
}

# Fazendo uma cópia superficial do dicionário original
copied_dict = original_dict.copy()

# Alterando um valor no dicionário copiado
copied_dict['key1'] = 100

# Alterando um valor na lista dentro do dicionário copiado
copied_dict['list_key'][1] = 999

# Imprimindo os dicionários original e copiado
print("Original Dictionary:", original_dict)
print("Copied Dictionary:", copied_dict)