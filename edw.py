from termcolor import colored
import os , time , calendar
def dir(place) :
    for i in os.listdir(place) :
        print(i)
print(colored("Welcome to edw","red"))
print(colored("-"*50,"blue"),"\r")
while True :
    fun = input()
    try :
        orders = {"write :":"print(more)",
                  "open :":r"os.system(more)",
                  "go :":r"os.chdir(more),print('you are in ',os.getcwd())",
                  "where :":r"print(os.getcwd())",
                  "rename :":"os.rename(more[0:more.index(',')],more[more.index(',')+1:]),print('renamed')",
                  "rfo :":"os.rmdir(more),print('removed')",
                  "cfo :": "os.mkdir(more),print('created')",
                  "rfi :": "os.remove(more),print('removed')",
                  "cfi :": "open(more,mode='x'),print('created')",
                  "quit :":"print('goodbay'),quit()",
                  "reboot :":"print('reboot'),os.system('c:\Windows\System32\shutdown.exe /s /t 1')",
                  "dir :":"dir(more)",
                  "time :":"print(time.ctime())",
                  "clear :":"os.system('cls')",
                  "chrome :":"os.startfile('C:\Program Files\Google\Chrome\Application\chrome.exe')",
                  "exist :":"print(os.path.exists(r'{}'.format(more)))",
                  "read :":"print(os.system(f'type {more}'))",
                  "calendar :":"print(calendar.month(int(more[0:more.index(',')]),int(more[more.index(',')+1:])))",
                  'calc :':"print(eval(more))",
                  "help :":"print(list(orders.keys()))"
                  }
        g = fun[0:fun.index(":")+1]
        more = fun[fun.index(":")+2:]
        eval(orders[g])
    except NameError as msg:
        print(msg)