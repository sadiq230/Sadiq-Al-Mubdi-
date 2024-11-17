import ipaddress as i
class subnet:
    def __init__(self,network_address,prefix):
        self.network=i.IPv4Network(f'{network_address}/{prefix}',strict=False)
        self.prefix=prefix
        self.subnets=[]
    def divide_by_subnet_count(self,subnet_count):
        prefix=self.network.prefixlen+(subnet_count-1).bit_length()
        self.subnets=list(self.network.subnets(new_prefix=prefix))
        print("divided successfuly ('_')")
    
    def divide_by_host_number(self,hosts_number):
        for i in range(1,33):
            if 2**i >= hosts_number:
                n_prefix=32-i
                break
        self.subnets=list(self.network.subnets(new_prefix=n_prefix))
        print("divided successfuly ('_')")

    def display_networks(self):
        for i,sub in enumerate(self.subnets):
            print('='*80)
            print(f' NETWORK {i+1} '.center(80,'='))
            print('='*80)
            print(f'address : {sub.network_address}')
            print(f'broadcast :{sub.broadcast_address}')
            print(f'hosts range :{sub.network_address+1} - {sub.broadcast_address-1}')
            print(f'prefix : /{sub.prefixlen}')
            print(f'subnet mask :{sub.netmask}')
            print(f'magic number:{self.magic_number(sub.prefixlen)}')
            print(f'available hosts :{self.magic_number(sub.prefixlen)-2}')
    

    def display_specific_network(self,net_number):
        for i,sub in enumerate(self.subnets):
            if i==net_number-1:
                print('='*80)
                print(f' NETWORK {i+1} '.center(80,'='))
                print('='*80)
                print(f'address : {sub.network_address}')
                print(f'broadcast :{sub.broadcast_address}')
                print(f'hosts range :{sub.network_address+1} - {sub.broadcast_address-1}')
                print(f'prefix : /{sub.prefixlen}')
                print(f'subnet mask :{sub.netmask}')
                print(f'magic number:{self.magic_number(sub.prefixlen)}')
                print(f'available hosts :{self.magic_number(sub.prefixlen)-2}')
    @staticmethod
    def magic_number(prefixlen):
        number=2**(32-prefixlen)
        return number

while True:
    print('\n1. divide by sunets count \n2. divide by hosts number\n0.exit ')
    choice=int(input('enter your choice >> '))
    if choice==0:
        break
    
    elif choice==1:
        network_address = input('enter network ip exam(192.168.10.0) >> ')

        sub=network_address.split('.') 
        if len(sub) !=4 :
            print('invalid ip address please try again ')
            input('press enter to continue...')
            continue

        for i in range(len(sub)):
            if int(sub[i]) > 255 or int(sub[i]) < 0:
                verify=False
                break
        if verify==False:
            print('invalid ip address please try again ')
            input('press enter to continue...')
            continue

        prefix = int(input('enter prefix beween (1-32) >> '))
        subnet_count = int(input('enter the number of subnets >> '))
        network = subnet(network_address,prefix)
        network.divide_by_subnet_count(subnet_count)
        c=input('display details (y/n) ')
        if c=='y':
            print('\na. display all networks\nb.display specific network \n')
            ch=input('enter your choice >> ')
            if ch=='a':
                network.display_networks()
                input('press enter to continue...')
            elif ch=='b':
                net_number=int(input('enter the network number >> '))
                network.display_specific_network(net_number)
                input('press enter to continue...')
            else:
                print("invalid choice please try again ('_')")
                input('press enter to continue...')
        else:
            continue
    elif choice==2:
        network_address = input('enter network ip exam(192.168.10.0) >> ')
        sub=network_address.split('.') 
        if len(sub) !=4 :
            print('invalid ip address please try again ')
            input('press enter to continue...')
            continue

        for i in range(len(sub)):
            if int(sub[i]) > 255 or int(sub[i]) < 0:
                verify=False
                break
        if verify==False:
            print('invalid ip address please try again ')
            input('press enter to continue...')
            continue


        prefix = int(input('enter prefix (1-32)>> '))
        hosts_number=int(input('enter the hosts number >> '))
        network = subnet(network_address,prefix)
        network.divide_by_host_number(hosts_number)
        c=input('display details (y/n) ')
        if c=='y':
            print('\na. display all networks\nb.display specific network \n')
            ch=input('enter your choice >> ')
            if ch=='a':
                network.display_networks()
                input('press enter to continue...')
            elif ch=='b':
                net_number=int(input('enter the network number >> '))
                network.display_specific_network(net_number)
                input('press enter to continue...')
            else:
                print("invalid choice please try again ('_')")
                input('press enter to continue...')
        else:
            continue


        
    else :
        print("invalid choice please try again ('_')")
        input('press enter to continue...')


