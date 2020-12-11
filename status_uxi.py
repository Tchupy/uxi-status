#!/usr/bin/python3

import requests

class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

################################################
#
#       MENU
#
################################################
def menu():
    # function names that will be send as a result
    switch = {
    '1': components,
    '2': status,
    '3': maintenance,
    '9': leave
    }
    
    # Menu string
    choice = '0'
    choice = input("""
    
    *****************
    
    1 - Display all components status
    2 - Display global status
    3 - Display validated schedule maintenance
    9 - Quit
    
    Your choice : """)
    
    return switch.get(choice, lambda: menu())


################################################
#
#      COMPONENTS
#
################################################

def components(url):
    
    req=requests.request("GET",url)
    status_value=req.json()

    # display results
    title=("Aruba " + bcolors.OKCYAN + "User Experience Insight" + bcolors.ENDC + " status" )
    print("\n" + title.center(76) + "\n")
    for k in status_value['components']:
         print("        " + k['name'].ljust(21), " ===> ".center(10), end=' ')
         if (k['status'] == 'operational'):
            print(bcolors.OKGREEN + k['status'].ljust(12) + bcolors.ENDC)
         elif (k['status'] == 'degraded_performance'):  
            print(bcolors.WARNING + k['status'].ljust(12) + bcolors.ENDC)
         elif (k['status'] == 'partial_outage'):  
            print(bcolors.FAIL + k['status'].ljust(12) + bcolors.ENDC)
         elif (k['status'] == 'major_outage'):  
            print(bcolors.FAIL + k['status'].ljust(12) + bcolors.ENDC)
    return


def maintenance(url):
    return


################################################
#
#       STATUS
#
################################################

def status(url):
    
    req=requests.request("GET",url)
    status_value=req.json()

    # display results
    # "All Systems Operational", "Partial System Outage", "Major Service Outage".
    title=("Aruba " + bcolors.OKCYAN + "User Experience Insight" + bcolors.ENDC + " status" )
    #print("\n" + title.center(60) + "\n")
    #print(status_value['status']['description'])

    if (status_value['status']['description'] == "All Systems Operational"):
       value=(bcolors.OKGREEN + status_value['status']['description'] + bcolors.ENDC)
    elif (status_value['status']['description'] == "Partial System Outage "):
       value=(bcolors.WARNING + status_value['status']['description'] + bcolors.ENDC)
    elif (status_value['status']['description'] == "Major System Outage"):
       value=(bcolors.FAIL+ status_value['status']['description'] + bcolors.ENDC)
    print("\n" + title.rjust(50) + " ==> " +value + "\n")
    return

################################################
#
#       quit
#
################################################

def leave():
    # function to exit script
    print('Leaving..')
    pass

################################################
#
#    MAIN FUNCTION
#
################################################

def main():
    # define URL & URI
    baseurl='http://status.capenetworks.com/api/v2/'
    compourl='components.json'
    statusurl='status.json'

#    while True:
#        # Display menu
#        action = menu()
#        print(action)    
#        # call function
#        action(baseurl)
#    return
    choice = '0'
    while choice != '9': 
        # Menu string
        choice = input("""
        
        *****************
        
        1 - Display all components status
        2 - Display global status
        3 - Display validated schedule maintenance
        9 - Quit
        
        Your choice : """)

        if (choice == '1'):
            components(baseurl+compourl)
        elif (choice== '2'):
            status(baseurl+statusurl)
        elif (choice == '3'):
            maintenance()
        elif (choice == '9'):
            leave();
    return

if __name__ == "__main__":
    main()
