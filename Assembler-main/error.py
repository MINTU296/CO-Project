operation=[]
reg=["R0","R1","R2","R3","R4","R5","R6"]

typeA=["add","sub","mul","xor","or","and"]
typeB =["mov","rs","ls"]
typeC = ["mov","div","not","cmp"]
typeD=["ld","st"]
typeE =["je","jlt","jgt","jmp"]




no_of_line=0
print("begin")
with open("test.txt", 'r') as f:
    for line in f:
        no_of_line+=1

f.close()
i=0

label_index=[]
labels=[]
label_flag=False


var=[]
var_flag=True



with open("test.txt", 'r') as f:
    for line in f:
     operation.append(line.strip().split(' '))
    
        
     i+=1
       
     if(operation[i-1][0]=='/' and operation[i-1][1]=='/'):
        continue

     if(len(operation[i-1])==0):
        continue
     if(operation[i-1][0]=="var"):
         if(len(operation[i-1])==2 and var_flag==True ):
             var.append(operation[i-1][1])
         else:
            var_flag=False
            print(i,"invalid flag")
     

     else:

        if(len(operation[i-1])==1 and label_flag==False and operation[i-1][0]!="hlt"):
            if(len(operation[i-1][0])<7):
                    print(i,"Missing label name")
                    exit()

            if "label" not in operation[i-1][0]:
                print(i,"typo in label")
                
                str=list(operation[i-1][0])
                if(str[-1]==":"):
                    print(i,"Missing label semicolon")
                exit()
            else:
                labelname=list(operation[i-1][0])
                labelname.pop()
                x="".join([str(i) for i in labelname])
                labels.append(x)
                
                label_index.append(i-1)
                label_flag=True
                continue
        elif(len(operation[i-1])==1 and label_flag==True):
            if operation[i-1][0]=="hlt":
                label_flag=False
            else:
                print(i,"Missing hlt instruction in label")
                exit()
        if(i==no_of_line):
            if(len(operation[no_of_line-1])!=1 or operation[no_of_line-1][0]=="hlt"):
                continue
            else:
                print("hlt not being used as the last instruction")
                break

        #errors for type A
        elif(operation[i-1][0] in typeA):
            if(len(operation[i-1])!=4):
                print(i,"Missing operand in type A")
                exit()
            if(operation[i-1][1] not in reg):
                print(i,"Invalid register name in type A")
                exit()
            
            if(operation[i-1][2] not in reg):
                print(i,"Invalid 1stoperand in type A")
                exit()
            if(operation[i-1][3] not in reg and operation[i-1][3] not in var):
                print(i,"Invalid 2ndoperand in type A")
                exit()
        

        #errors for mov instruction
        elif(operation[i-1][0]=="mov"):
            if(len(operation[i-1])!=3):
                print(i,"invalid operand in mov instruction")
                exit()
            if(operation[i-1][1] not in reg):
                print(i,"invalid register given in mov")
                exit()
            if(operation[i][2].startswith('$')):
                if(int(operation[i-1][2][1:]) not in range(0,128)):
                    print("invalid immediate value for mov")
                    exit()
        
            elif((operation[i-1][2] not in reg) and (operation[i-1][2] not in var) ):#
                
                print("ivalid operand for mov")
                exit()
        #errors for type B except mov
        elif(operation[i-1][0] in typeB):
            if(len(operation[i-1])!=3):
                print(i,"Missing operand in type B")
                exit()
            if(operation[i-1][1] not in reg):
                print(i,"Invalid register name in type B")
                exit()
            if(operation[i][2].startswith('$')):
                if(int(operation[i-1][2][1:]) not in range(0,128)):
                    print("invalid immediate value for mov")
                    exit()
            
            elif((operation[i-1][2] not in reg) and (operation[i-1][2] not in var) ):#
                print(i,"invalid operand 2 for type B")
                exit()
        #errors for type C
        elif(operation[i-1][0] in typeC):
            if(len(operation[i-1])!=3):
                print(i,"Missing operand in type C")
                exit()
            if(operation[i-1][1] not in reg):
                print(i,"Invalid register name in type C")
                exit()
            if(operation[i][2].startswith('$')):
                if(int(operation[i-1][2][1:]) not in range(0,128)):
                    print("invalid immediate value for mov")
                    exit()
            
            elif(operation[i-1][2] not in reg and (operation[i-1][2] not in var)):
                print(i,"Invalid operand for type c")
                exit()
        #errors for type D
        elif(operation[i-1][0] in typeD):
            if(len(operation[i-1])!=3):
                print(i,"Missing operand in type D")
                exit()
            if(operation[i-1][1] not in reg):
                print(i,"Invalid register name in type D")
                exit()
            if(operation[i-1][2] not in labels):
                print(i,"only labels can be passed as mem_address")
                exit()
        #errors for type E
        elif(operation[i-1][0] in typeE):
            if(len(operation[i-1])!=2):
                print(i,"Missing operand in type E")
                exit()
            if(operation[i-1][1] not in labels):
                print(i,"invalid label name for type E")
                exit()
        


        

                
print("error free")
error_free=1
        
