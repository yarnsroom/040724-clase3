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

print("**Welcome to the Teenage Mutan Ninja Turtles Pizzas**")
answer="y"
while answer=="y":

    type= int(input("Pleas choose the type of pizza: 1-vegetarian. 2-Not vegetarian: "))
    if type==1:
        option = int(input("please choose one ingredient: 1-Pimiento. 2-Tofu (All pizzas come whith Mozarella and tomato): "))
        if option==1:
            pizza=  "Vegetarian"
            ingredient = "Pimiento"
        elif option==2:
            pizza=  "Vegetarian"
            ingredient = "Tofu"
    elif type==2:
        option = int(input("please choose one ingredient: 1-Peperoni. 2-Jamon. 3-Salmon (All pizzas come whith Mozarella and tomato): "))
        if option==1:
            pizza=  "Not Vegetarian"
            ingredient = "Peperoni"
        elif option==2:
            pizza=  "Not Vegetarian"
            ingredient = "Jamon"
        elif option==3:
            pizza=  "Not Vegetarian"
            ingredient = "Salmon"
    print("The pizza is: ", pizza," and his ingredients are: Mozarella, tomato and", ingredient)
    answer=input("Would you like another pizza? Yes(y), no(n): ")
print("")
print("**End of Program!**")