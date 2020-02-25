a=open("archivo.txt","w")
for x in range(256):
	if x <128 or x>159:
		a.write(chr(x)+ "="+str(x))
		a.write("\n")
a.close()