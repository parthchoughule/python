"""student={"Name":"Parth","Marks":90}
marks=student["Marks"]
if marks>80:
    print("Pass")
else:
    print("fail")
person={"Name":"Parth","Age":18}
x=person["Age"]
if x>=10:
    print("Adult")
else:
    print("Minor")
meaning={"Shubham":"sweet","Shri":"calm devotion","Parth":"Arjun"}
print(meaning["Shri"]) 
set1={1,2,3}
set2={3,4,5}
print(set1.union(set2)) 
print(set1.intscersection(set2))         
student={"Name":"Parth","Score":{"Maths":88,"Science":85}}
print(student["Score"]["Science"])
set={1,2,3,4}
set.remove(2)
print(set)
if {1,3}.issubset(set):
    print("Yes")
else:
    print("No")
name="Parth"
print(set(name))  """
list=[1,2,3,4]
set1=set(list)
print(set1)     