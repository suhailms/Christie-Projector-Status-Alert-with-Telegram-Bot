import telnetlib
import requests
import datetime
#from termcolor import colored

TOKEN = "2000000000:Aaaaaaaabbbbbbbbbbbb5050-TY"
chatID = "-555666777"
URL = "https://api.telegram.org/bot%s/sendMessage"%TOKEN
PORT = "3002"
time = datetime.datetime.now()
now = (time.strftime("%d-%m-%Y %H:%M:%S"))
iplist = ("10.10.2.101", "10.10.2.102", "10.10.2.103", "10.10.2.104", "10.10.2.105", "10.10.2.106", "10.10.2.107", "10.10.2.108", "10.10.2.109", "10.10.2.110", "10.10.2.111", "10.10.2.112", "10.10.2.113", "10.10.2.114", "10.10.2.115", "10.10.2.116", "10.10.2.117", "10.10.2.118", "10.10.2.119", "10.10.2.120", "10.10.2.121")
prjname = ("PRJ-101", "PRJ-102", "PRJ-103", "PRJ-104", "PRJ-105", "PRJ-106", "PRJ-107", "PRJ-108", "PRJ-109", "PRJ-110", "PRJ-111", "PRJ-112", "PRJ-113", "PRJ-114", "PRJ-115", "PRJ-116", "PRJ-117", "PRJ-118", "PRJ-119", "PRJ-120", "PRJ-121")
n = 0

# use the commented codes if you are printing the output in terminal itself

def send_to_telegram(message):
	try:
		response = requests.post(URL, json={'chat_id': chatID, 'text': message})
		#print (response.text)
	except Exception as e:
		print (e)

while n<len(iplist):
	HOST = iplist[n]
	NAME0 = iplist.index(HOST)
	NAME1 = prjname[NAME0]
	try:
		tn = telnetlib.Telnet(HOST, PORT, timeout = 5)
		'''
    		print NAME1, colored("Connected", "cyan")
		tn.write(b'(PWR?)\n')
		#print (tn.read_until(b")"))
		y=tn.read_until(b")")
		if "001" in y:
			print "Powered ON"
		else:
			print "Standby Mode"
		'''
		tn.write(b'(SST+ALRM?)\n')
      		z=tn.read_until(b")")
    		if "No status items" in z:
			#print "No attention needed"
			pass
    		else:
    			#print colored("ATTENTION NEEDED", "yellow", attrs=["reverse", "blink"])
    			#print "Message:", z
			message = "%s %s %s"%(NAME1, z, now)
			send_to_telegram(message)

		tn.write(b'(SST+SIGN?013)\n')
		x=tn.read_until(b")")
		if "No Signal" in x:
			#print colored("HDMI Connection Error", "red")
			message = "%s HDMI Connection Error %s"%(NAME1, now)
			send_to_telegram(message)
		else:
			pass
			#print colored("HDMI Connected", "green")
		tn.close()

	except:
		#print NAME1, colored("No Response", "red", attrs=["reverse", "blink"])
		message = "%s Unresponsive %s"%(NAME1, now)
		send_to_telegram(message)
	n += 1

ack = "Scheduled Scanning Done at %s"%now
send_to_telegram(ack)
