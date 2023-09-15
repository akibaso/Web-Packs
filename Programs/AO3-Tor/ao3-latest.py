import os
import sys

torpath = "/root/tor/tor/tor"
torrc = '''HardwareAccel 1
#Log notice stdout
#UseBridges 1
AvoidDiskWrites 1
#DNSPort 0.0.0.0:8853
RunAsDaemon 1
MaxCircuitDirtiness 600
AllowSingleHopExits 1
UseBridge 1
Bridge 66.206.4.26:9001 BBD8F4DF8FF5C69A6A989DB8C1EE2CA7ADFE0755
Bridge 135.148.150.99:443 A06CDA7922E2522BAD37AABDB51BC953CC41BEB8
Bridge 51.81.93.108:443 24523E7B004983EC4CA5033EBC9B7293F12F237C
Bridge 23.250.14.226:443 5CDEC940C15EA7DABBFA8F58CD8945B875DA80C6
Bridge 68.67.32.31:9001 964B4E8A75263A69769541F2764563DABDD995D2
Bridge 23.175.32.11:443 56BAF2F6CAE76B1AC6C1F08C148D04C219E85E70
Bridge 15.204.141.95:8080 32742AD57C3D243DA0713BB6DFD82118DF573D2E
Bridge 23.82.136.232:443 A5424DEEDD5A913146E7177A79EE48FAF7CB861A
Bridge 66.206.4.26:9001 BBD8F4DF8FF5C69A6A989DB8C1EE2CA7ADFE0755
Bridge 135.148.52.231:443 BA6E064596B86AF9F55F0603A82C90E958E86E7A
Bridge 172.106.11.34:443 44FAD1FB2286D1680E5A3EECE5069157719F031E
Bridge 107.155.69.234:9001 EA596D84CDEF2A8DB89FF848FEA7DB4A5294A1AE
Bridge 97.113.236.133:8000 08EA5457CF66F13AC89EA74682417A6001DC61D9
Bridge 104.192.3.74:444 6ABFC90631A8CDA0C2D43D266878DBF9DC5BA485
Bridge 162.251.116.34:443 D58ABC85644F021638010310C3C4B3511A8A4142
Bridge 45.33.13.63:4001 5DA69B086B833FC1DFCF2D9C8B9C3B03137C7EFD
Bridge 195.60.166.2:9000 73A2557D2887878AD67F45372CD2D1446B92DEC3
Bridge 104.57.231.26:443 1F772DD93DA20A6745E334BAFFC7B9765876BB11
Bridge 108.54.152.215:9001 67F5AC35DBA20D22A0178BFB6F4AC076C3B16829
Bridge 62.151.177.116:443 725FDAFDEC3E6F0368941BC96A33CA3E6C8175B9
SocksPort 127.0.0.1:'''
    
def init(instances):
    if not os.path.exists("/usr/bin/ao3"):
        f = open("/usr/bin/ao3", "w")
        f.write('''#!/bin/bash
python3 /root/tor/tor.py ${1} ${2}''')
        f.close()
        os.system("chmod +x /usr/bin/ao3")
    if not os.path.exists("/root/tor/"):
        os.makedirs("/root/tor/")
        os.system("mv "+sys.argv[0]+" /root/tor/tor.py")
    if not os.path.exists("/root/tor/tor/"):
        os.system("wget https://www.torproject.org/dist/torbrowser/12.0.2/tor-expert-bundle-12.0.2-linux-x86_64.tar.gz -O /root/tor/tor.tar.gz && cd /root/tor/ && tar -xzvf /root/tor/tor.tar.gz && chmod +x /root/tor/tor/tor && rm /root/tor/tor.tar.gz")
    i=0
    instances=int(instances)
    for i in range(instances):
        os.makedirs("/root/tor/instances/"+str(i)+"/")
        tor = open("/root/tor/instances/"+str(i)+"/torrc", "w")
        torrc1 = torrc + str(6000+int(i)) + '''
PidFile /root/tor/instances/'''+str(i)+"/tor.pid"+'''
DataDirectory /root/tor/instances/'''+str(i)+'''/'''
        tor.write(torrc1)
        tor.close()
        f = open("/root/tor/instances/instances.txt", "w")
        f.write(str(instances))
        f.close()

        
def reinit(instances):
    os.system("rm -rf /root/tor/instances/")
    i=0
    instances=int(instances)
    for i in range(instances):
        os.makedirs("/root/tor/instances/"+str(i)+"/")
        tor = open("/root/tor/instances/"+str(i)+"/torrc", "w")
        torrc1 = torrc + str(6000+int(i)) + '''
PidFile /root/tor/instances/'''+str(i)+"/tor.pid"+'''
DataDirectory /root/tor/instances/'''+str(i)+'''/'''
        tor.write(torrc1)
        tor.close()
        f = open("/root/tor/instances/instances.txt", "w")
        f.write(str(instances))
        f.close()


def start():
    i=0
    try:
        f = open("/root/tor/instances/instances.txt", "r")
        instances = int(f.read())
        f.close()
    except:
        print("No instances.txt file found. Please run 'python tor.py init <instances>'")
        exit()
    for i in range(instances):
        os.system("bash -c '"+torpath+" -f /root/tor/instances/"+str(i)+"/torrc > /root/tor/instances/"+str(i)+"/tor.log' &")

def stop():
    i=0
    try:
        f = open("/root/tor/instances/instances.txt", "r")
        instances = int(f.read())
        f.close()
    except:
        print("No instances.txt file found. Please run 'python tor.py init <instances>'")
        exit()
    for i in range(instances):
        os.system("kill `cat /root/tor/instances/"+str(i)+"/tor.pid`")

def watchlog(i):
    os.system("tail -f /root/tor/instances/"+str(i)+"/tor.log")

def gost(instances):
    if not os.path.exists("/root/tor/gost"):
        os.system("wget https://github.com/go-gost/gost/releases/download/v3.0.0-rc5/gost_3.0.0-rc5_linux_amd64.tar.gz && tar -xzvf gost_3.0.0-rc5_linux_amd64.tar.gz && mv gost_3.0.0-rc5_linux_amd64/gost /root/tor/gost && rm -rf gost_3.0.0-rc5_linux_amd64* && chmod +x /root/tor/gost")
    a = '''services:'''
    b = '''
    chains:'''
    i=0
    for i in range(instances):
        a = a + '''
- name: service-'''+str(int(i))+'''
  addr: :'''+str(61000+int(i))+'''
  handler:
    type: tcp
    chain: chain-'''+str(int(i))+'''
  listener:
    type: tcp
  forwarder:
    nodes:
    - name: target-0
      addr: archiveofourown.org:443'''
    b = b + '''
- name: chain-'''+str(int(i))+'''
  hops:
  - name: hop-'''+str(int(i))+'''
    nodes:
    - name: node-'''+str(int(i))+'''
      addr: 127.0.0.1:'''+str(int(i)+6000)+'''
      connector:
        type: socks5
      dialer:
        type: tcp'''
    all = a+b
    #print(all)
    with open("/root/tor/1.yaml","w") as f:
        f.write(all)
        print("启动命令：/root/tor/gost -C /root/tor/1.yaml")



try:  
    if sys.argv[1] == "start":
        start()
    elif sys.argv[1] == "stop":
        stop()
    elif sys.argv[1] == "init":
        try:
            print(sys.argv[2])
            init(str(sys.argv[2]))
        except:
            print("Usage: ao3 or python tor.py start|stop|init <instance>|reinit <instance>|log <instance>")
    elif sys.argv[1] == "reinit":
        try:
            print(sys.argv[2])
            reinit(str(sys.argv[2]))
        except:
            print("Usage: ao3 or python tor.py start|stop|init <instance>|reinit <instance>|log <instance>")
    elif sys.argv[1] == "gost":
        try:
            gost(int(sys.argv[2]))
        except:
            print("Usage: ao3 or python tor.py start|stop|init <instance>|reinit <instance>|log <instance>")
    elif sys.argv[1] == "watchlog" or sys.argv[1] == "tail" or sys.argv[1] == "log":
        watchlog(sys.argv[2])
    else:
        print("Usage: ao3 or python tor.py start|stop|init <instance>|reinit <instance>|log <instance>")
except:
    print("Usage: ao3 or python tor.py start|stop|init <instance>|reinit <instance>|log <instance>")
