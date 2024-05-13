first = input().split()
name_count = int(first[0])
command_count = int(first[1])
names = {}
command_name = []
command_ip = []
for i in range(name_count):
    j = input().split()
    name = j[0]
    ip = j[1]
    names[ip] = name
for i in range(command_count):
    j = input().split()
    command = j[0]
    ip = j[1].rstrip(';')
    command_name.append(command)
    command_ip.append(ip)
for name, ip in zip(command_name, command_ip):
    print(f'{name} {ip}; #{names.get(ip)}')
