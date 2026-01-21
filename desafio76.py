"""Crie um programa que tenha uma tupla única com nomes de produtos e seus respectivos preços, na sequência. No final, mostre uma listagem de preços, organizando os dados em forma tabular (alinhando o texto à esquerda e o preço à direita)."""

import pandas as pd
produtos = [
  ('Coca', 7.49),
  ('U.F.O.', 5.49),
  ('Banana', 5.50),
  ('Mamão Formosa', 3.50)
  ] 

tabela = pd.DataFrame(produtos, columns=["Produto", "Preço"])
print(tabela)