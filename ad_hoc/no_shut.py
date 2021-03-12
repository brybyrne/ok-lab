from netmiko import ConnectHandler

switch = {
    'device_type': 'cisco_ios',
    'host': '10.15.255.6',
    'username': 'netman',
    'password': 'C1sco,123',
}

net_connect = ConnectHandler(**switch)

config_commands = [ 'interface GigabitEthernet1/0/10',
                    'no shutdown' 
                    ]

output = net_connect.send_config_set(config_commands)

print(output)