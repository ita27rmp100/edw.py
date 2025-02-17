commands={"write$":"callback(more)",
        "open$":r"os.system(more),callback('opened'+more)",
        "go$":r"os.chdir(more),callback('you are in ',os.getcwd())",
        "where$":r"callback(os.getcwd())",
        "rename$":"os.rename(more[0:more.index(',')],more[more.index(',')+1:]),callback('renamed to'+more[more.index(',')+1:])",
        "rfo$":"os.rmdir(more),callback('removed'+more)",
        "cfo$": "os.mkdir(more),print('created folder with name : '+more)",
        "rfi$": "os.remove(more),print('removed'+more)",
        "cfi$": "open(more,mode='x'),print('created file with name : '+more)",
        "quit$":"callback('goodbye'),quit()",
        "reboot$":"callback('reboot'),os.system('c:\Windows\System32\shutdown.exe /s /t 1')",
        "dir$":"callback(listdir(more))",
        "time$":"callback(time.ctime())",
        "clear$":"os.system('cls'),callback('')",
        "chrome$":"os.startfile('C:\Program Files\Google\Chrome\Application\chrome.exe'),callback('google chrome opened')",
        "exist$":"callback(os.path.exists(r'{}'.format(more)))",
        "read$":"callback(os.system(f'type {more}'))",
        "calendar$":"callback(calendar.month(int(more[0:more.index(',')]),int(more[more.index(',')+1:])))",
        'calc$':"calback(eval(more))",
        "help$":"calback(list(orders.keys()))",
        # from here the new commands
        "redirect$":"open(more,mode='w').write(prevCommand['input']+'\n'+prevCommand['output'])",
        "redirect -ow$":"open(more,mode='a').write(prevCommand['input']+'\n'+prevCommand['output'])",
        "save$":"open(more,mode='a).write(sheet)",
        "history$":"callback(displayHis())",
        "delhis$":"db.execute(delete from history)",
        "chtime$":"callback(os.system('time'))",
        "restart$":"restart()", # supported only for windows and linux
        "sysinfo$":"callback(infoSys(more))"
    }
greeting = """
#  .............._............................_..................._......................
#  __......_____|.|.___.___.._.__.___...___..|.|_.___.....___..__|.__......___.__.._..._.
#  \.\./\././._.|.|/.__/._.\|.'_.`._.\./._.\.|.__/._.\.../._.\/._`.\.\./\./.|.'_.\|.|.|.|
#  .\.V..V.|..__|.|.(_|.(_).|.|.|.|.|.|..__/.|.||.(_).|.|..__|.(_|.|\.V..V._|.|_).|.|_|.|
#  ..\_/\_/.\___|_|\___\___/|_|.|_|.|_|\___|..\__\___/...\___|\__,_|.\_/\_(_|..__/.\__,.|
#  .........................................................................|_|....|___/.
"""