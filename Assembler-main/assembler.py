import sys

# Rest of the code...


# no_of_line = 0

# i = 0
# reg=["R0","R1","R2","R3","R4","R5","R6"]

# typeA1=["add","sub","mul","xor","or","and"]
# typeB1 =["mov","rs","ls"]
# typeC1 = ["mov","div","not","cmp"]
# typeD1=["ld","st"]
# typeE1 =["je","jlt","jgt","jmp"]


# label_index = []
# labels = []
# label_flag = False

# var = []
# var_flag = True
# error_free = 1
# operation1=[]
# code=[]
# for ele in sys.stdin:
#      code.append(ele.strip())       
#      operation1.append(ele.strip().split())
#      i+=1
       
#      if(operation1[i-1][0][0]=='/' and operation1[i-1][0][1]=='/'):
#         continue

#      if(len(operation1[i-1])==0):
#         continue
#      if(operation1[i-1][0]=="var"):
#          if(len(operation1[i-1])==2 and var_flag==True ):
#              var.append(operation1[i-1][1])
#          else:
#             var_flag=False
#             sys.stdout.write("invalid flag")
     

#      else:

#         if(len(operation1[i-1])==1 and label_flag==False and operation1[i-1][0]!="hlt"):
#             if(len(operation1[i-1][0])<7):
#                     sys.stdout.write("Missing label name")
#                     exit()

#             if "label" not in operation1[i-1][0]:
#                 sys.stdout.write("typo in label")
                
#                 str=list(operation1[i-1][0])
#                 if(str[-1]==":"):
#                     sys.stdout.write("Missing label semicolon")
#                 exit()
#             else:
#                 labelname=list(operation1[i-1][0])
#                 labelname.pop()
#                 x="".join([str(i) for i in labelname])
#                 labels.append(x)
                
#                 label_index.append(i-1)
#                 label_flag=True
#                 continue
#         elif(len(operation1[i-1])==1 and label_flag==True):
#             if operation1[i-1][0]=="hlt":
#                 label_flag=False
#             else:
#                 sys.stdout.write("Missing hlt instruction in label")
#                 exit()
#         if(i==no_of_line):
#             if(len(operation1[no_of_line-1])!=1 or operation1[no_of_line-1][0]=="hlt"):
#                 continue
#             else:
#                 sys.stdout.write("hlt not being used as the last instruction")
#                 break

#         #errors for type A
#         elif(operation1[i-1][0] in typeA1):
#             if(len(operation1[i-1])!=4):
#                 sys.stdout.write("Missing operand in type A")
#                 exit()
#             if(operation1[i-1][1] not in reg):
#                 sys.stdout.write("Invalid register name in type A")
#                 exit()
            
#             if(operation1[i-1][2] not in reg):
#                 sys.stdout.write("Invalid 1stoperand in type A")
#                 exit()
#             if(operation1[i-1][3] not in reg and operation1[i-1][3] not in var):
#                 sys.stdout.write("Invalid 2ndoperand in type A")
#                 exit()
        

#         #errors for mov instruction
#         elif(operation1[i-1][0]=="mov"):
#             if(len(operation1[i-1])!=3):
#                 sys.stdout.write(i,"invalid operand in mov instruction")
#                 exit()
#             if(operation1[i-1][1] not in reg):
#                 sys.stdout.write("invalid register given in mov")
#                 exit()
#             if(operation1[i-1][2].startswith('$')):
#                 if(int(operation1[i-1][2][1:]) not in range(0,128)):
#                     sys.stdout.write("invalid immediate value for mov")
#                     exit()
        
#             elif((operation1[i-1][2] not in reg) and (operation1[i-1][2] not in var) ):#
                
#                 sys.stdout.write("ivalid operand for mov")
#                 exit()
#         #errors for type B except mov
#         elif(operation1[i-1][0] in typeB1):
#             if(len(operation1[i-1])!=3):
#                 sys.stdout.write("Missing operand in type B")
#                 exit().write
#             if(operation1[i-1][1] not in reg):
#                 sys.stdout.write("Invalid register name in type B")
#                 exit()
#             if(operation1[i][2].startswith('$')):
#                 if(int(operation1[i-1][2][1:]) not in range(0,128)):
#                     sys.stdout.write("invalid immediate value for mov")
#                     exit()
            
#             elif((operation1[i-1][2] not in reg) and (operation1[i-1][2] not in var) ):#
#                 sys.stdout.write("invalid operand 2 for type B")
#                 exit()
#         #errors for type C
#         elif(operation1[i-1][0] in typeC1):
#             if(len(operation1[i-1])!=3):
#                 sys.stdout.write("Missing operand in type C")
#                 exit()
#             if(operation1[i-1][1] not in reg):
#                 sys.stdout.write("Invalid register name in type C")
#                 exit()
#             if(operation1[i-1][2].startswith('$')):
#                 if(int(operation1[i-1][2][1:]) not in range(0,128)):
#                     sys.stdout.write("invalid immediate value for mov")
#                     exit()
            
#             elif(operation1[i-1][2] not in reg and (operation1[i-1][2] not in var)):
#                 sys.stdout.write("Invalid operand for type c")
#                 exit()
#         #errors for type D
#         elif(operation1[i-1][0] in typeD1):
#             if(len(operation1[i-1])!=3):
#                 sys.stdout.write("Missing operand in type D")
#                 exit()
#             if(operation1[i-1][1] not in reg):
#                 sys.stdout.write("Invalid register name in type D")
#                 exit()
#             if(operation1[i-1][2] not in labels):
#                 sys.stdout.write("only labels can be passed as mem_address")
#                 exit()
#         #errors for type E
#         elif(operation1[i-1][0] in typeE1):
#             if(len(operation1[i-1])!=2):
#                 sys.stdout.write("Missing operand in type E")
#                 exit()
#             if(operation1[i-1][1] not in labels):
#                 sys.stdout.write("invalid label name for type E")
#                 exit()





code = []
# with open("ans.txt", "r") as f:
#     for line in f:
for line in sys.stdin:
    code.append(line.strip())

# Register addresses
rig={"R0":"000","R1":"001","R2":"010","R3":"011","R4":"100","R5":"101","R6":"110","FLAGS":"111"}
reg={"R0":"000","R1":"001","R2":"010","R3":"011","R4":"100","R5":"101","R6":"110"}
# operation codes

operation={ "add":"00000", "sub":"00001", "mov1":"00010","mov2":"00011", "ld":"00100", "st":"00101", "mul":"00110","div":"00111","rs":"01000","ls":"01001", "xor":"01010","or":"01011", "and":"01100","not":"01101","cmp":"01110","jmp":"01111", "jlt":"11100", "jgt":"11101","je":"11111", "hlt":"11010", "addf":"10000", "subf":"10001", "movf":"10010"}

# code for type of instruction
typ={"add":"A","sub":"A","mov1":"B","mov2":"C","ld":"D","st":"D", "mul":"A","div":"C","rs":"B","ls":"B", "xor":"A","or":"A","and":"A","not":"C","cmp":"C","jmp":"E","jlt":"E","jgt":"E","je":"E","hlt":"F","addf":"A","subf":"A","movf":"B"}

variable=[]
label={}
labels = {}
variables = {}

# function to convert decimal to binary
def get_binary(n):
    return format(int(n), '07b')

# function for floating point conversion
def float_to_binary(my_number):
    places = 5
    my_number = float(my_number)
    whol, dec = str(my_number).split(".")
    dec = int(dec)
    whol = int(whol)
    res = bin(whol).lstrip("0b") + "."

    for _ in range(places):
        if dec != 0:
            dec *= 2
            whol = dec // 10
            dec %= 10
            res += str(whol)
        else:
            break

    d = ''.join(res.split('.'))
    d = d[:places] + "0" * max(0, places - len(d))
    tt = min(len(res.split('.')[0][1:]), 7)
    g = bin(tt)[2:].rjust(3, '0')

    return g + d

  
# function for type A
def typeA(value, r1, r2, r3):
    machine_code = operation.get(value)
    i = 0
    while i < 2:
        machine_code += "0"
        i += 1
    machine_code += rig.get(r1) + rig.get(r2) + rig.get(r3)
    
    return machine_code


# function for type B
def typeB(value, r1, n):
    a = get_binary(n)
    machine_code = operation.get(value)
    i = 0
    while i < 1:
        machine_code += "0"
        i += 1
    machine_code += rig.get(r1) + a
    return machine_code

def typeC(value, r1, r2):
    machine_code = operation.get(value)
    
    i=0
    while i<5:
        machine_code+="0"
        i+=1
    machine_code+=rig.get(r1)+rig.get(r2)
    return machine_code

# function for type D
def typeD(value, r1, var):
    machine_code = operation.get(value)
    i=0
    while i<1:
        machine_code+="0"
        i+=1
    machine_code+=rig.get(r1)+get_binary(variables[var])
    return  machine_code

    
# function for type E
def typeE(value, label):
    machine_code = operation.get(value)
    i=0
    while i<4:
        machine_code+="0"
        i+=1
    machine_code+=get_binary(labels[label+':'])
    return machine_code


# function for type F
def typeF(value):
    machine_code = operation.get(value)
    while(len(machine_code)<16):
        machine_code+="0"
    return machine_code






address = -1
for line in code:

    if len(line) == 0:
        continue

    line_list = list(line.split())

    if line_list[0] == "mov":
        if line_list[2][0] == "$":
            line_list[0] = "mov1"
        else:
            line_list[0] = "mov2"

    if (line_list[0] in operation and line_list[0] != "hlt"):
        address += 1

    elif (line_list[0] == "hlt"):
        address += 1
        labels[line_list[0]] = address

    elif (line_list[0][-1] == ":"):
        address += 1
        labels[line_list[0]] = address


for line in code:
    if (len(line) == 0):
        continue
    line_list = list(line.split())
    if line_list[0] == "var":
        address += 1
        variables[line_list[1]] = address


for line in code:
    
    if(len(line) == 0):
        continue

    line_list = list(line.split())


    if(len(line_list) > 1 and line_list[0] in labels):
        line_list.pop(0)

    if line_list[0] == "mov":
        if line_list[2][0] == "$":
            line_list[0] = "mov1"
        else:
            line_list[0] = "mov2"

    if line_list[0] in operation.keys():
      

        if typ[line_list[0]][0] == "A":

            sys.stdout.write(typeA(line_list[0], line_list[1], line_list[2],line_list[3])+"\n")

        elif typ[line_list[0]][0] == "B":
            

            sys.stdout.write(typeB(line_list[0], line_list[1], line_list[2][1:])+"\n")

        elif typ[line_list[0]][0] == "C":

            sys.stdout.write(typeC(line_list[0], line_list[1], line_list[2])+"\n")

        elif typ[line_list[0]] == "D":
            sys.stdout.write(typeD(line_list[0], line_list[1], line_list[2])+"\n")
            

        elif typ[line_list[0]][0] == "E":

            sys.stdout.write(typeE(line_list[0], line_list[1])+"\n")

        elif typ[line_list[0]][0] == "F":

            sys.stdout.write(typeF(line_list[0])+"\n") 


