"""
La pizzería Teenage Mutant Ninja Turtles ofrece pizzas vegetarianas y no vegetarianas a sus clientes. 
Los ingredientes para cada tipo de pizza aparecen a continuación.
•Ingredientes vegetarianos: Pimiento y tofu.
•Ingredientes no vegetarianos: Peperoni, Jamón y Salmón.
Escribir un programa que pregunte al usuario si quiere una pizza vegetariana o no,
y en función de su respuesta le muestre un menú con los ingredientes disponibles para que elija. Solo se puede eligir 
un ingrediente ademas de la mozzarella y el tomate que están en todas las pizzas.
Al final se debe mostrar por pantalla si la pizza elegida es vegetariana o no y todos los ingredientes que lleva.
"""
def main():
    print("Bienvenido a la pizzería Teenage Mutant Ninja Turtles.")
    tipo_pizza = input("¿Deseas una pizza vegetariana? (s/n): ")

    if tipo_pizza == "s":
        print("Ingredientes vegetarianos disponibles:")
        print("1. Pimiento")
        print("2. Tofu")
        ingrediente_elegido = int(input("Elige un ingrediente (1 o 2): "))
        pizza = "Vegetariana"
        if ingrediente_elegido == 1:
            print("La pizza:", pizza, " Contiene los ingredientes: Pimiento, mozzarella y tomate")
        else:
            print("La pizza:", pizza, " Contiene los ingredientes: Tofu, mozzarella y tomate")
    else:
        print("\nIngredientes no vegetarianos disponibles:")
        print("1. Peperoni")
        print("2. Jamón")
        print("3. Salmón")
        ingrediente_elegido = input("Elige un ingrediente (1, 2 o 3): ")
        pizza = "No vegetariana"
        if ingrediente_elegido == 1:
            print("La pizza:", pizza, " Contiene los ingredientes: Peperoni, mozzarella y tomate")
        elif ingrediente_elegido == 2:
            print("La pizza:", pizza, " Contiene los ingredientes: Jamón, mozzarella y tomate")
        else:
            print("La pizza:", pizza, " Contiene los ingredientes: Salmón, mozzarella y tomate")
            
main()