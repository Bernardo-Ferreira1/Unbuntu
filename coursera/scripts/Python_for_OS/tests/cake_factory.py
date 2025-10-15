#!/bin/env/python3

from typing import List


class CakeFactory:
 def __init__(self, cake_type: str, size: str):
   self.cake_type = cake_type       # Tipo de bolo (ex: chocolate, vanilla)
   self.size = size                 # Tamanho do bolo (small, medium, large)
   self.toppings = []               # Lista de coberturas extras

   # Preço base depende do tipo e tamanho
   self.price = 10 if self.cake_type == "chocolate" else 8
   # Acrescenta custo dependendo do tamanho
   self.price += 2 if self.size == "medium" else 4 if self.size == "large" else 0

 def add_topping(self, topping: str):
     self.toppings.append(topping)  # Adiciona cobertura
     self.price += 1                # Cada cobertura custa +1

 def check_ingredients(self) -> List[str]:
     # Ingredientes básicos
     ingredients = ['flour', 'sugar', 'eggs']
     # Se for chocolate, usa cacau; caso contrário, baunilha
     ingredients.append('cocoa') if self.cake_type == "chocolate" else ingredients.append('vanilla extract')
     # Adiciona as coberturas escolhidas
     ingredients += self.toppings
     return ingredients

 def check_price(self) -> float:
     return self.price


# Exemplo de uso:
cake = CakeFactory("chocolate", "medium")
cake.add_topping("sprinkles")
cake.add_topping("cherries")
cake_ingredients = cake.check_ingredients()
cake_price = cake.check_price()

cake_ingredients, cake_price


import unittest                                # importa o framework de testes do Python

class TestCakeFactory(unittest.TestCase):     # define uma classe de testes; herda de unittest.TestCase
    def test_create_cake(self):                # qualquer método que comece por "test_" é um caso de teste
        cake = CakeFactory("vanilla", "small") # cria uma instância do objeto que estamos a testar
        # verifica se o atributo cake_type tem o valor esperado
        self.assertEqual(cake.cake_type, "vanilla")
        # verifica se o atributo size tem o valor esperado
        self.assertEqual(cake.size, "small")
        # verifica se o preço inicial foi calculado corretamente (8)
        self.assertEqual(cake.price, 8)  # comentário explicativo no próprio teste

    def test_add_topping(self):
        cake = CakeFactory("chocolate", "large")  # cria um bolo chocolate large
        cake.add_topping("sprinkles")             # adiciona uma cobertura
        # confirma que "sprinkles" está presente na lista de toppings do bolo
        self.assertIn("sprinkles", cake.toppings)

    def test_check_ingredients(self):
        cake = CakeFactory("chocolate", "medium")  # cria um bolo chocolate medium
        cake.add_topping("cherries")               # adiciona "cherries" como topping
        ingredients = cake.check_ingredients()     # obtém a lista de ingredientes
        # verifica que 'cocoa' (cacau) está entre os ingredientes para bolo de chocolate
        self.assertIn("cocoa", ingredients)
        # verifica que o topping adicionado aparece nos ingredientes
        self.assertIn("cherries", ingredients)
        # verifica que 'vanilla extract' não aparece (porque não é vanilla)
        self.assertNotIn("vanilla extract", ingredients)

    def test_check_price(self):
        cake = CakeFactory("vanilla", "large")  # cria vanilla large
        cake.add_topping("sprinkles")            # 1º topping (+1)
        cake.add_topping("cherries")             # 2º topping (+1)
        price = cake.check_price()               # obtém o preço final
        # verifica que o preço coincide com o cálculo esperado: 8 (vanilla) +4 (large) +2 (2 toppings) = 14
        self.assertEqual(price, 14)

# carrega e executa os testes definidos na classe TestCakeFactory e imprime o resultado no terminal
unittest.TextTestRunner().run(
    unittest.TestLoader().loadTestsFromTestCase(TestCakeFactory)
)
