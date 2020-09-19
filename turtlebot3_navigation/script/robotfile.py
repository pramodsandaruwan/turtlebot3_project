
file1 = open("myfile.txt","r+")  
  
#print "Output:"
#print file1.read() 
myarray = file1.read()
print "Output: Goto "+myarray[0]
print "In navigating state..."
#print myarray
file1.seek(0)
file1.close()


file1 = open("myfile.txt","w") 
file1.write("Navigating...") 
file1.close()