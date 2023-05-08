import json

f=open('Technitians.json')
Technitians_data=json.load(f)

def 
List=Technitians_data['Technitians']
#print(List)
#print(List[2]["id"])
print(len(List))
i=0
find=False
while(i<len(List) and find==False):
    if List[i]["id"]=="3428A":
        find=True
        index=i
        print("index: "+str(index))
        print(i)
        Technitian=List[index]
        print(Technitian['process'])
    i=i+1
        
print("i is:"+str(i))
if find==False:
    Print("Tecnico no registrado")
        
        
    
    
