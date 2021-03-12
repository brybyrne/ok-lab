from netmiko import ConnectHandler

switch = {
    'device_type': 'cisco_ios',
    'host': '10.15.255.6',
    'username': 'username',
    'password': 'password',
}

net_connect = ConnectHandler(**switch)

config_commands = [ 'interface GigabitEthernet1/0/10',
                    'shutdown' 
                    ]

output = net_connect.send_config_set(config_commands)

print(output)