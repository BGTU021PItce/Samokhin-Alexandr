print("введите кол-во секунд")
z=int(input())
x=z//3600
z=z-x*3600
y=z//60
z=z-y*60
print(x, "часов ",y, "минут", z," секунд")
input()