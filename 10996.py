menu = []
for i in range(5):
    menu.append(int(input()))
array = [sum([x,y])-50 for x in menu[:3] for y in menu[3:]]
print(min(array))