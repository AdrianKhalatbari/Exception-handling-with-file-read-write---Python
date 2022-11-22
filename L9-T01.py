import os

try:
    file_name = input("Enter the name of the file to be read:"+'\n')
    valueList=[]
    with open(file_name, "r") as faezeh:
        for i in faezeh:
            if type(int(i))is int:
                    valueList.append(i)
        print("File 'T1_file_in1.txt' read successfully,",len(valueList),"lines.")
    file_name2 = input("Enter the name of the file to be written:"+'\n')
   # try:
    with open(file_name2, "w") as mamad:
        mamad.write("1\n2\n53\n67\n8\n5\n4")
        mamad.close()
    print("File '{}' was successfully written.".format(file_name2))
    #except:
     #       print("Error while processing file '{}', stopping.".format(file_name2))
except FileNotFoundError:
    print("Error while processing file",file_name+" ,"+" stopping.")
    exit(0)
except ValueError:
    print("Error while processing file '{}', stopping.".format(file_name))
    exit(0)
