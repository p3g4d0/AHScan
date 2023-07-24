import socket

print(f"""
______  __  __      ____                               
/\  _  \/\ \/\ \    /\  _`\                             
\ \ \L\ \ \ \_\ \   \ \,\L\_\    ___     __      ___    
 \ \  __ \ \  _  \   \/_\__ \   /'___\ /'__`\  /' _ `\  
  \ \ \/\ \ \ \ \ \    /\ \L\ \/\ \__//\ \L\.\_/\ \/\ \ 
   \ \_\ \_\ \_\ \_\   \ `\____\ \____\ \__/.\_\ \_\ \_\
    
                                                        
                                                        """)

# Función para escanear el puerto
def scan_port(host, port):
    try:
        # Crear un objeto socket
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        
        # Configurar un tiempo de espera de conexión
        s.settimeout(5)
        
        # Intentar conectar al puerto
        result = s.connect_ex((host, port))
        
        # Si el puerto está abierto, mostrarlo en la consola
        if result == 0:
            print(f"El puerto {port} está abierto")
        
        # Cerrar la conexión
        s.close()
        
    except socket.error as e:
        print(f"Error al escanear el puerto {port}: {e}")


# Pedir al usuario la URL o la dirección IP
host = input("Ingrese la URL o la dirección IP del sitio web: ")
print(f"Escaneando puertos abiertos en {host}...\n")

# Puertos comunes para escanear
common_ports = [21, 22, 23, 25, 53, 80, 443, 3389]

# Escanear los puertos comunes
for port in common_ports:
    scan_port(host, port)
