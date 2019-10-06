''''     it is main code of one touch file it gives user information about doctor and hospital'''

exitcount='s'
password="admin"
sepc=[0,1,2,3,4,5,6,7,0,1,2,3,4,5,6,7,0,1,2,3,4,5,6,7,0,1,2,3,4,5,6,7,0,1,2,3,4,5,6,7,0,1,2,3,4,5,6,7,0]
dho=[[0,1,2,3,4],[5,6,7,8,9],[10,11,12,13,14],[15,16,17,18,19],[20,21,22,23,24],[25,26,27,28,29],[30,31,32,33,34],[35,36,37,38,39],[40,41,42,43,44],[45,46,47,48]]
dep=["ACIDENT A EMERGENCY","ANESTHETICS","CANCER","BURN CENTERS","CARDIOLOGY","DIAGNOSTIC IMAGING","GASTROENTEROLOGY","GENERAL SURGERY"]
department=[[0,1,2,3,4],[5,6,7,0,1],[2,3,4,5,6],[7,0,1,2,3],[4,5,6,7,0],[1,2,3,4,5],[6,7,0,1,2],[3,4,5,6,7],[0,1,2,3,4],[5,6,7,0]]
hospital=["MG HOSPITAL","SUBASH.C.BOSE HOSPITAL","CHANDRASHEKAR HOSPITAL","SARJONI NADIU HOSPITAL","SWAMI VIVEKANAD HOSPITAL","SADAR VALABH BHAI PATEL HOSPITAL","TATA MEMEORIAL HOSPITAL","LALA LAJPATH RAI HOSPITAL","BALGANGADHAR TILAK HOSPITAL","BIPIN CHANDRA PAL HOSPITAL"]
doctor=["Dr NISHANT EXP 9 YEARS","Dr DP  EXP 25 YEARS","Dr SEENU  EXP 8 YEARS","DR DIVESH EXP 7 YEARS","DR TUSHAR EXP 20 YEARS","DR SAMMER EXP 17 YEARS","DR ASHISH EXP 22 YEARS","DR SHEWATANK EXP 17 YEARS","DR KSHITJ EXP 7 YEARS","DR RUTH EXP 3 YEARS","DR SHIVAM MALPANI EXP 2 YEARS","DR NIRALA EXP 15 YEARS","DR VARDHIL EXP 20 YEARS","DR NAMAN EXP 11 YEARS","DR MANJOT EXP 6 YEARS","DR AKKIKUMAR EXP 2 YEARS","DR M.K EXP 39 YEARS","DR S.LEON EXP 29 YEARS","DR JOHN SNOW 9 EXP YEARS","DR TYRION 12 EXP YEARS","DR JAMIE 12 EXP YEARS","DR CERSIE 12EXP YEARS","DR SANSA 8 EXP YEARS","DR ARYA 4 EXP YEARS","DR JOJEN 3 EXP YEARS","DR MELLISENDE 6 EXP YEARS","DR ALLADIN 35 EXP YEARS","DR VIRUS 20 EXP YEARS","DR AMAN S 9 EXP YEARS","DR SHERLOCK 5 EXP YEARS","DR WASTON 3 EXP YEARS","DR N KING 9 EXP YEARS","DR DANY 5 EXP YEARS","DR DROGON 7 EXP YEARS","DR LYANNA 9 EXP YEARS","DR NED 19 EXP YEARS","DR ROGERS 25 EXP YEARS","DR CLINT 13 EXP YEARS","DR THOR 23 EXP YEARS","DR BANNER 29 EXP YEARS","DR GATES 18 EXP YEARS","DR MARK 27 EXP YEARS","DR SHELDON 27 EXP YEARS","DR RAJ 26 EXP YEARS","DR PENNY 25 EXP YEARS","DR ROSS 24 EXP YEARS","DR RACHEL 24 EXP YEARS","DR BING 23 EXP YEARS","DR MONICA 21 EXP YEARS"]
while ( exitcount != 'E' ):
 def admin():
   print("----WE WELCOMES YOU  TO ONE TOUCH HEALTH CARE SERVICES----")
   print("----ADMINISTRATOR SERVICES ARE AS FOLLOW----")
   print("---0 to add a hospital ")
   print("---1 to add doctor ")
   print("")
   cval=int(input("please select the admin service by selecting by  corresponding number in the list ----- "))
   return cval
 def user():
   print("----WE WELCOMES YOU TO ONE TOUCH HEALTH CARE SERVICES----")
   b=["ACIDENT A EMERGENCY","ANESTHETICS","CANCER","BURN CENTERS","CARDIOLOGY","DIAGNOSTIC IMAGING","GASTROENTEROLOGY","GENERAL SURGERY"]
   c=0
   for i in b:
     
     print(str(c),"--",i)
     c=c+1
   a=int(input("please select the medical service by selecting by  corresponding number in the list ----- "))
   return a
 print("for user enter U")
 print("for admin enter A")
 mainoption=input()
 if ( mainoption == 'U'):
  b=user()
  count=0
  for i in department:
    
   for j in i:
     if ( j == b ):
       print("SPECILAIST OF ",dep[int(b)]," in ",hospital[count],"are")
       for k in dho[count]:
         
        
         if (dep[sepc[k]] == dep[b]):
           print (doctor[int(k)])
   count=count+1
 if (mainoption == 'A'):
   print("Please enter admin password-----")
   passwordA=input("")
   if ( passwordA == password ):
      adminfunc=admin()
      if adminfunc == 0 :
        print ("to add hospital add its name ")
        hname=input("enter--")
        hospital.append(hname)
        print ("to add its doctor add  ")
        print ("add it format <drname> <experince years> ")
        whish="YES"
        countlocal=0
        localdr=[]
        localdep=[]
        print("code for department for doctor are as follow-")

        for i in dep:
          print(countlocal,i)
          countlocal=countlocal+1
        countlocal=0
        while whish != "N":
             
             hname=input("enter name and experince of doctor--")
             hsepc=int(input("enter department code of doctor --"))
             localdep.append(int(hsepc))
             whish=input("if to enter more press Y else N")
             sepc.append(int(hsepc))
             doctor.append(hname)
             localdr.append(len(doctor)+countlocal)
             countlocal=countlocal+1
        dho.append(localdr)
        department.append(localdep)

 print(" --------------------------------------------------------------------------")
 print(" ")
 print(" ")
 print("if want to go main screen press y ")
 print("if want exit press E ")
 exitcount=(input(""))




