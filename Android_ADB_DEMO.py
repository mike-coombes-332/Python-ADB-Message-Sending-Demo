import subprocess

Adb_Devices=[]
global ConStr

def Find_adb_devices():
    global Adb_Devices
    try:
           cmd='adb devices' # https://developer.android.com/studio/command-line/adb#devicestatus
           ready = 0
           process = subprocess.Popen(cmd,shell=True,stdout=subprocess.PIPE,stderr=subprocess.PIPE)	
           for line in process.stdout:
               rline = line.decode("utf-8")
                                                 #List of devices attached
		                                 #3200a745e87cb55f  device
		                                 #R9WTB0RFR6L       device
               if ((ready==1) and (len(rline)>1)):
                   Limiter2 = rline.split()
                   Adb_Devices.append(Limiter2[0])
               if (rline.find('List of devices attached')==0):
                   ready = 1
           print("ADB Devices Detected")
           print (Adb_Devices)
           print("--------------------")
           print("Ready to send messages to device")
    except:
           print("adb devices, command failed")
           

def adb_messenger(cmd,format):     
       result =[]
       global ConStr
       cmd = ConStr+cmd
       print(">>"+cmd)
       try:
           process = subprocess.Popen(cmd,shell=True,stdout=subprocess.PIPE,stderr=subprocess.PIPE)	
           for line in process.stdout:
               result.append(line)
           #print (result)
           rVal = result[0].decode("utf-8")
           #print(rVal.strip("\n"))
       except:
           errcode = process.returncode
           print("ADB Message Send Error"+str(errcode))
           if (format == 0):       
               return("")
       if (format == 0):
           return(rVal.strip("\n"))  
       return


def main() :
       global Adb_Devices
       global ConStr
       print ()
       print ("===================================")
       print ("| Python ADB Message Sending Demo |")
       print ("===================================")
       print ()
       Find_adb_devices() # Run the function to get the adb server to list the availbe devices
       choice=0
       if (len(Adb_Devices)>1):
           index=0
           valid=0
           print("Number \t Device") 
           for i in Adb_Devices:  
               print(index,"\t",i)
               index+=1
           while(valid==0): 
               try:   
                   choice=int(input("Choose which device to connect to by selecting the coresponding number "))
               except:
                   choice=-1    
               if ((choice >-1) and (choice <index)):
                   valid=1 
                   
       if (len(Adb_Devices)==0):
           print("No ADB Decive Detected")
           exit()
       print()    
           
       MyStr=Adb_Devices[choice]
       ConStr='adb -s '+MyStr+' shell '
       
       UpTime   = adb_messenger('uptime',0) 
       print("<<"+UpTime)
       print()
           
       SW_Ver = adb_messenger('getprop ro.build.version.release',0)
       print("<<"+SW_Ver)
if __name__ == '__main__':
    main()
