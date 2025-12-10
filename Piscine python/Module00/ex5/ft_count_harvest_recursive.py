
# def ft_count_harvest_recursive():
#     try:
#         days = int(input("Days until harvest: "))
#         if days == 0:
#             print("Harvest time!")
#             return
#         else:
#             print("Day ", days)
#             ft_count_harvest_recursive(days - 1)
#     except ValueError:
#         print("We only count time in numbers of days!")

# ft_count_harvest_recursive()





#         def cuenta_atras_recursiva(n):
#     # Caso base: cuando n llega a 0, la recursión termina
#     if n == 0:
#         print("¡Tiempo agotado!")
#         return
#     else:
#         # Paso recursivo: imprime el número y se llama a sí misma con n-1
#         print(n)
#         cuenta_atras_recursiva(n - 1)

# # Llamada inicial para empezar la cuenta desde 5
# cuenta_atras_recursiva(5)