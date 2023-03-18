# Dictionary Practice

def main():
    while True:
        print("---\nPort Lookup. Type 'list' to see all. Type 'exit' to quit.")
        user_input = input("Please enter which protocol to search for : ").lower()
        if user_input == 'exit':
            break
        if user_input in ports().keys():
            port = ports()[user_input]
            print(f'Protocol : {user_input} | Port : {port}')
        elif user_input == 'list':
            for key in ports():
                print(f'{key} : {ports()[key]}')
        else:
            print('Lookup failed.')


def ports():
    port = {'echo': '7',
            'ftp-data': '20',
            'ftp': '21',
            'ssh': '22',
            'scp': '22',
            'telnet': '23',
            'smtp': '25',
            'dns': '53',
            'tftp': '69',
            'http': '80',
            'kerberos': '88',
            'kerberos-pw': '464',
            'tsap': '102',
            'pop3': '110',
            'epmap': '135',
            'netbios-ns': '137',
            'netbios-ssn': '139',
            'imap4': '143',
            'https': '443',
            'smtps': '465',
            'smpt-ems': '587',
            'dcom': '593',
            'ldaps': '636',
            'ldap': '389',
            'exchange': '691',
            'vmware-server': '902',
            'vmware-server2': '8222',
            'ftps': '990',
            'imap4s': '993',
            'pop3s': '995',
            'rpc': '1025',
            'openvpn': '1194',
            'waste': '1337',
            'vqp': '1589',
            'steam': '1725',
            'cpanel': '2082',
            'radsec': '2083',
            'oracledb': '2483',
            'oracledbs': '2484',
            'symantec': '2967',
            'xbox': '3074',
            'mysql': '3306',
            'wow': '3724',
            'googledesktop': '4664',
            'postgresql': '5432',
            'rfb': '5900',
            'vnc': '5900',
            'irc': '6665',
            'irc2': '6669',
            'hpopenview': '381',
            'hpopenview2': '383',
            'bittorrent': '6881',
            'bittorrent2': '6999',
            'quicktime': '6970',
            'kasperskytcp': '8086',
            'kaspeerskyudp': '8087',
            'pdl': '9100',
            'backupexec': '10000',
            'netbus': '12345',
            'sub7': '27374',
            'backorifice': '18006'}
    return port


if __name__ == '__main__':
    main()
