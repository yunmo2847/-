import turtle
import random
color = ['red','blue','yellow','green','purple','pink','orange']
t_list = [[],[],[],[]]
for i in range(4):
	for j in range(3):
		t=turtle.Turtle()
		t_list[i].append(t)
for i in range(4):
        for j in range(3):
                asdf = random.choice(color)
                t_list[i][j].color(asdf)
                t_list[i][j].lt(i*90)
                t_list[i][j].fd(100*(j+1))

for i in range(4):
        for j in range(3):
                asdf = random.choice(color)
                t_list[i][j].color(asdf)
                t_list[i][j].lt(135)
                t_list[i][j].fd(2**0.5*(100*(j+1)))
