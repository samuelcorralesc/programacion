
a, comando = {"1": 0, "2": 0, "3": 0}, 0
while comando != "4":
   comando = input()
   if comando in a.keys():
       a[comando] += 1
print("MUITO OBRIGADO\nAlcool: {}\nGasolina: {}\nDiesel: {}".format(a["1"], a["2"],
                                                                   a["3"]))
