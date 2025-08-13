stud_marks={'asha':'25','badsha':'34','clesha':'42','smasha':'77','trisha':'89'}
name=input("enter the name of the student:")
try: 
   print(name,"secured ",stud_marks[name]+" marks")
except KeyError:
   print("student not found!")    