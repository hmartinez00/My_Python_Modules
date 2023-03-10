import socket
import urllib.request

url = 'google.com'
external = 'https://ident.me'

# nombre de la maquina
hostname = socket.gethostname()

# ip privada
ip_address1 = socket.gethostbyname(hostname)

# ip external server
# ip_address2 = socket.getaddrinfo(url, 80)

# ip publica
external_ip = urllib.request.urlopen(external).read().decode('utf8')

msg = \
f'Hostname: {hostname}\n' + \
f'Ip privada: {ip_address1}\n' + \
f'IP publica: {external_ip}'
# f'Ip Servidor externo: {ip_address2}\n' + \

print(msg)