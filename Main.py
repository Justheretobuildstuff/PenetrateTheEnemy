import subprocess

# Give User ability to add IP
# TargetIP = ('Enter Target IP:\n')
TargetIP = '10.129.41.227'

# Pinging UserInputs IP that is entered for 4 times
print("Pinging " + TargetIP)
ping = subprocess.run(["ping", "-c", "4", TargetIP], stdout=subprocess.DEVNULL, stderr=subprocess.STDOUT)

if str(ping.returncode) == "0":
    print(TargetIP + " is Online")
else:
    print(TargetIP + " is Offline")

# print(ping.returncode)
#if ping.poll():
    #print(TargetIP" is down")
#else:
    #print(TargetIP" is up")

# Boolean to print if target IP is online or offline

# print('\nTarget is online')

# Boolean to continue if IP responded to ping