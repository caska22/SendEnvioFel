import socket


def conexion():

    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.settimeout(5)
    try:
        s.connect(("www.google.com", 80))
    except (socket.gaierror, socket.timeout):
        return False
    else:
        s.close()
        return True
