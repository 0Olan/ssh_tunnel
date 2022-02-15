#!/usr/bin/env python3

from os import system

users = []
passwords = []
servers = []
expire_date = []

f = open('./list_sshs.csv',"r")
D= []

for line in f:
    if line.strip() != '':
        D.append(line.strip())
    
for i in range(len(D)):
    users.append(D[i].split(",")[0])
    passwords.append(D[i].split(",")[1])
    servers.append(D[i].split(",")[2])
    expire_date.append(D[i].split(",")[3])


def Finder():
    coms = []
    for i in range(j):
    
        user = users[i]
        password = passwords[i]
        server = servers[i]
        date = expire_date[i]
        # torify 
        command = "sshpass -p \'" + password + "\' ssh -ND "+ str(port) +" " + user + "@" + server + " # " + date +"\n"
        coms.append(command)

    for i in range(j):
        print(str(i+1)+"- " +coms[i])

    print(seprator)
    return coms


print("")
port = int(input("Port [8080] ~~> ") or 8080)

j = len(D)
seprator = "-------------------------------------------------------------------------------"
print("")

def main():
    system("clear")
    coms = Finder()
    which_one = int(input("  Which One: "))
    print("")
    print("~~> "+coms[which_one-1])
    system(coms[which_one-1])
    mp3_command = "mpg123 ./Ding_Dong.mp3 > /dev/null 2>&1 & "
    system(mp3_command)
    system("clear")
    print("")
    print(seprator)
    
while True:
    try:
        main()
    except:
        pass
