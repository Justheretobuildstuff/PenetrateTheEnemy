import subprocess

# Give User ability to add IP
# TargetIP = ('Enter Target IP:\n')
TargetIP = '10.129.41.227'

# Pinging UserInputs IP that is entered for 4 times
print(">> Pinging " + TargetIP)
ping = subprocess.run(["ping", "-c", "4", TargetIP], stdout=subprocess.DEVNULL, stderr=subprocess.STDOUT)
pr = ping.returncode
if str(pr) == "0":
    print(TargetIP + " is Online\n")
    # Ping is good, running nmap scan
    print(">> Running Nmap Scan")
    nmapScan = subprocess.Popen(["nmap", TargetIP], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    stdout, stderr = nmapScan.communicate()
    #stdout = stdout.split(b"\n")
    print(stdout)
    #for line in stdout:
        #if line.find("open"):
            #print(line)
else:
    print(TargetIP + " is Offline\n")

# print(ping.returncode)
#if ping.poll():
    #print(TargetIP" is down")
#else:
    #print(TargetIP" is up")

# Boolean to print if target IP is online or offline

# print('\nTarget is online')

# Boolean to continue if IP responded to ping