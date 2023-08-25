p_id =["P01","P23","P93","P42","P09","P87"]
pro=["VSCode","Eclipse","Chrome","JDK","CMD","NotePad"]
Stime=[100,234,189,9,7,23] 
pri=["MID","MID","High","High","High","Low"]
spid = sorted(p_id)
st=sorted(Stime)
spri=sorted(pri)
print("1. Sort by P_ID\n2. Sort by Start Time\n3. Sort by Priority")
print("Choose a sorting option")
ch=int(input())
if ch==1:
 for x in spid:
  print(x)
elif ch==2:
  for x in st:
   print(x)
elif ch==3:
  for x in spri:
   print(x)
else:
  print("Invalid Choice")