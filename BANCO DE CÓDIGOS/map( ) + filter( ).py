estoque = [
    {'Item01': 'Camisa Nike', 'Preco':39.90},
    {'Item02': 'Camisa Adidas', 'Preco':37.90},
    {'Item03': 'Moletom 00', 'Preco':79.90},
    {'Item04': 'Calca Jeans', 'Preco': 69.90},
    {'Item05': 'Tenis AllStar', 'Preco': 59.90}
]

precos06 = list(map(lambda p: p['Preco'],
                    filter(lambda p: p['Preco'], estoque)))

print(f'Preços de estoque (Map + Filter) {precos06}')
