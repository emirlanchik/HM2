todays = ["osh," "bishkek", "kol", "jalal_abad", "talas",]

print ("Day" + (" "*12) + "High Temperature")
print ("-"*30)
temperature = []
temp = 0
spaces = 0

for i,x in enumerate(todays):
    temp_input = input ("Enter the temperature for" +x+str(":"))
    temperature.append(int(temp_input))
    spaces = 15-len(x)
    print (x," "*spaces,temperature[i])

avg= sum(temperature)//len(todays)


print ("средний показатель температупы КР на сегодня", avg,  "°c")