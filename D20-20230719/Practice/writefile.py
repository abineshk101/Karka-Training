# To write a file
file=open("/home/abinesh/Documents/karka",'w')
file.write("Address:205/9A,Thanunadar compund,Vattavilai\nPincode:629002")
file.close()

# To read a file 
file=open("/home/abinesh/Documents/karka",'r')
print(file.read(7))

