from netmiko import ConnectHandler

# Replace host, username, password. Assumes a Priv15 username/password
switch = {
    'device_type': 'cisco_ios',
    'host': '10.15.255.6',
    'username': 'username',
    'password': 'password',
}

net_connect = ConnectHandler(**switch)

config_commands = [ 'interface GigabitEthernet1/0/10',
                    'no shutdown' 
                    ]

output = net_connect.send_config_set(config_commands)

# Echos out the commands sent to the switch. Comment out to suppress
print(output)
