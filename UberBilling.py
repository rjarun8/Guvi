starting=int(input("enter starting kilometer"))
end=int(input("enter ending kilometer"))
ride_type=int(input("Select the destination :\n Enter '1' for micro \n Enter '2' for mini \n Enter '3' for prime \n Enter '4' for suv\n"))

total=int(end-starting)

dic={1:1.5,2:2.5,3:3.5,4:4.5}

x= lambda ride_type,total: float(dic.get(ride_type)) * total

print(x(ride_type,total))

