file = open (  "OFL.txt" , 'r')
if FileNotFoundError == True:
    print("The requested file dosent exist.")
else:    
    print("Reading file content\nline 1:",file.readlines(10),"\n line 2:",file.      readlines(5))