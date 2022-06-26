from klass import individual, breeding


f1 = individual(input("Fist paren gen:"))
f2 = individual(input("Second paren gen:"))
g1 = breeding(f1.genom,f2.genom)


print(g1)
