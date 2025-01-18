#path = "C:\Program Files (x86)\VMware\VMware Workstation"
vms = "C:\\Users\\UserDirName\\Documents\\Virtual Machines"
fileT = "C:\\Users\\UserDirName\\Desktop\\all type of files"

# part 1 :
import os
subfolders = [ vmf.name for vmf in os.scandir(vms) if vmf.is_dir() ]
print("List of Available Guest Machines ")
print()
for i in range(len(subfolders)):
    print(subfolders[i])
print()

import subprocess
proc = subprocess.Popen('vmrun list', shell=True, stdin=subprocess.PIPE, stdout=subprocess.PIPE)
out, erp = proc.communicate() #its will return tuple of pair.
print(out.decode("utf-8") )

# part 2 :
print("Choose your file")
print()
lis = os.listdir(fileT)
for i in lis:
    print(i)
print()
filename = input("Enter the name here it should be exact including extension =>  ")
print()
flag=0
if filename in lis:
    for j in lis:
        if filename == j:
            name, ext = os.path.splitext(filename)
    files_extensions = {".docx":"Office 2010 Word Document",".pdf":"PDF Document",".xlsx":"Office 2010 Excel Sheet",".pptx":"Office 2010 PowerPoint",
                         ".ppt":"PowerPoint",".xls":"Excel Sheet",".doc":"Word Document",".elf":"Executable and Linkable Format",
                         ".pe32":"Portable Executable 32 Bit File",".pe32+":"Portable Executable 64 Bit File",".csv":"CSV File"}
    for key, value in files_extensions.items():
        if ext == key:
            print("The Input file is of format : "+value)
    if flag == 0:
        print("File Identification Done !!")
        print()
else:
    print("file doesn't exists")

#part 3 :
'''
print("Powering on vm")
print()
if ext in files_extensions.keys():
    #only start vm
    on = input("Enter your choice : press 1 for Windows 10, press 2 for Kaali, press 3 for Remnux : ")
    vmNo = ["1","2","3"]
    if on in vmNo:
        if on == "1":
            proc = subprocess.Popen('vmrun -T ws start "C:\\Users\\UserDirName\\Documents\\Virtual Machines\\Windows 10 x64\\Windows 10 x64.vmx"', shell=True, stdin=subprocess.PIPE, stdout=subprocess.PIPE)
            out, erp = proc.communicate()
            print(out.decode("utf-8"))
        elif on == "2":
            proc = subprocess.Popen('vmrun -T ws start "C:\\Users\\UserDirName\\Documents\\Virtual Machines\\Kaali\\Kaali.vmx"', shell=True, stdin=subprocess.PIPE, stdout=subprocess.PIPE)
            out, erp = proc.communicate()
            print(out.decode("utf-8"))
        elif on == "3":
            proc = subprocess.Popen('vmrun -T ws start "C:\\Users\\UserDirName\\Documents\\Virtual Machines\\remnux-v7-focal\\remnux-v7-focal.vmx"', shell=True, stdin=subprocess.PIPE, stdout=subprocess.PIPE)
            out, erp = proc.communicate()
            print(out.decode("utf-8"))
    else:
        print("Vm not exists")'''          
print("Running appropriate selected vm , Done !!")
print()

#start vm with pass and execute program
'''program="notepad.exe \"C:\\Users\\VMUserDirName\\Desktop\\testing\\hie.txt"
proc = subprocess.Popen('vmrun -T ws -gu guestUser -gp guestPassword runProgramInGuest "C:\\Users\\UserDirName\\Documents\\Virtual Machines\\Windows 10 x64\\Windows 10 x64.vmx" -activeWindow -interactive {0}"'.format(program), shell=True, stdin=subprocess.PIPE, stdout=subprocess.PIPE)
out, erp = proc.communicate()
print(out.decode("utf-8"))'''

'''#vmrun -gu guestUser -gp guestPassword runProgramInGuest "C:\\Users\\UserDirName\\Documents\\Virtual Machines\\Windows 10 x64\\Windows 10 x64.vmx" -activeWindow -interactive cmd.exe
proc = subprocess.Popen('vmrun -gu guestUser -gp guestPass runProgramInGuest "C:\\Users\\UserDirName\\Documents\\Virtual Machines\\Windows 10 x64\\Windows 10 x64.vmx" -activeWindow -interactive notepad.exe', shell=True, stdin=subprocess.PIPE, stdout=subprocess.PIPE)
out, erp = proc.communicate()
print(out.decode("utf-8"))'''
    
#part 4

#CopyFileFromHostToGuest
#vmrun -gu guestUser -gp guestPassword copyFileFromHostToGuest Ubuntu16.vmwarevm/Ubuntu16.vmx ~/img.db /tmp/img.db

proc = subprocess.Popen('vmrun -gu VMUserDirName -gp VMPassword copyFileFromHostToGuest "C:\\Users\\UserDirName\\Documents\\Virtual Machines\\Windows 10 x64\\Windows 10 x64.vmx" "C:\\Users\\UserDirName\\Desktop\\all type of files\\{0}" "C:\\Users\\VMUserDirName\\Desktop\\testing\\{1}"'.format(filename,filename), shell=True, stdin=subprocess.PIPE, stdout=subprocess.PIPE)
out, erp = proc.communicate()
print(out.decode("utf-8"))

print("copy file from host to guest is done")
print()

#executing copied file in vm
#P.O.:file execution is only supporting to open in notepad, working on other editors also

files_Indecation = {".txt":"notepad.exe",".pdf":"msedge.exe",".ppt":"wordpad.exe",".pptx":"wordpad.exe",".xlsx":"wordpad.exe",".xls":"wordpad.exe",".doc":"wordpad.exe",".docx":"wordpad.exe"}

for key, value in files_Indecation.items():
    if ext == key:
        promo = value
        break

program="{0} \"C:\\Users\\VMUserDirName\\Desktop\\testing\\{1}".format(promo,filename)

proc = subprocess.Popen('vmrun -T ws -gu VMUserDirName -gp VMPassword runProgramInGuest "C:\\Users\\UserDirName\\Documents\\Virtual Machines\\Windows 10 x64\\Windows 10 x64.vmx" -activeWindow -interactive {0}"'.format(program), shell=True, stdin=subprocess.PIPE, stdout=subprocess.PIPE)
out, erp = proc.communicate()

print("execute copied file from host to guest in vm is done")
print()


#part 5
#listSnapshots
#vmrun snapshot Ubuntu16.vmwarevm/Ubuntu16.vmx mySnapshot
snappyVM = input("enter your choice to choose the which vm's snapshot you want to figure out => 1 for windows 10, 2 for kaali , 3 for remnux : ")
print()
vmNo = ["1","2","3"]
if snappyVM in vmNo:
    if snappyVM == "1":
        snap = "C:\\Users\\UserDirName\\Documents\\Virtual Machines\\Windows 10 x64\\Windows 10 x64.vmx"
    elif snappyVM == "2":
        snap = "C:\\Users\\UserDirName\\Documents\\Virtual Machines\\Kaali\\Kaali.vmx"
    elif snappyVM == "3":
        snap = "C:\\Users\\UserDirName\\Documents\\Virtual Machines\\remnux-v7-focal\\remnux-v7-focal.vmx"
else:
    print("VM not exists")

proc = subprocess.Popen('vmrun snapshot {0} mynewSnapshot'.format(snap), shell=True, stdin=subprocess.PIPE, stdout=subprocess.PIPE)
out, erp = proc.communicate()

#part 6: power off
print("Powering off vm")
print()
off = input("Enter your choice : press 1 for Windows 10, press 2 for Kaali, press 3 for Remnux : ")
vmNo = ["1","2","3"]
if off in vmNo:
    if off == "1":
        proc = subprocess.Popen('vmrun -T ws suspend "C:\\Users\\UserDirName\\Documents\\Virtual Machines\\Windows 10 x64\\Windows 10 x64.vmx"', shell=True, stdin=subprocess.PIPE, stdout=subprocess.PIPE)
        out, erp = proc.communicate()
        print(out.decode("utf-8"))
    elif off == "2":
        proc = subprocess.Popen('vmrun -T ws suspend "C:\\Users\\UserDirName\\Documents\\Virtual Machines\\Kaali\\Kaali.vmx"', shell=True, stdin=subprocess.PIPE, stdout=subprocess.PIPE)
        out, erp = proc.communicate()
        print(out.decode("utf-8"))
    elif off == "3":
        proc = subprocess.Popen('vmrun -T ws suspend "C:\\Users\\UserDirName\\Documents\\Virtual Machines\\remnux-v7-focal\\remnux-v7-focal.vmx"', shell=True, stdin=subprocess.PIPE, stdout=subprocess.PIPE)
        out, erp = proc.communicate()
        print(out.decode("utf-8"))
else:
    print("Vm not exists")    

