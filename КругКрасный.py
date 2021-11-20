import turtle

_list = list(map(int,input().split()))

for i in _list:
    turtle.circle(i)
m = 0
while _list != 0:
    if i > m:
        m = i
        turtle.color('red')
        turtle.circle(m)

turtle.mainloop()