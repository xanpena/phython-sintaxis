# -+- coding: utf-8 -*-

clients = ['Juan', 'Pablo']

def add_client(client_name):
    global clients
    if client_name not in clients:
        clients.append(client_name)
    else:
        print('Ese cliente ya existe')


def list_clients():
    global clients
    for idx, client in enumerate(clients):
        print('{}: {}'.format(idx, client))


def update_client(client_name, updated_client_name):
    global clients
    if search_client(client_name) == True:
        index = clients.index(client_name)
        clients[index] = updated_client_name
    else:
        _get_client_not_found()

def delete_client(client_name):
    global clients
    if search_client(client_name) == True:
        clients.remove(client_name)
    else:
        _get_client_not_found()

def search_client(client_name):
    global clients
    if client_name in clients:
        return True
    else:
        return False

def _get_client_name():
    client_name = None

    while not client_name:
        client_name = raw_input('Inserta el nombre del cliente: ')

    return client_name

def _get_client_not_found():
    print('Cliente no encontrado')

def _get_command():
    command = None

    while not command:
        command = input()

    if command not in range(7):
        print('Comando no permitido')
        command = _get_command()
        
    return command


def _print_menu():
    print('-'*50)
    print('Que quieres hacer hoy?:')
    print(u'[1]. Añadir cliente')
    print('[2]. Editar cliente')
    print('[3]. Eliminar cliente')
    print('[4]. Buscar cliente')
    print('[5]. Listar clientes')
    print('[6]. Salir')


if __name__ == '__main__':
    
    print('BIENVENIDOS A PYSHOP')
    print('-'*50)
    while True:
        _print_menu()

        command = _get_command()

        if command == 1:
            client_name = _get_client_name()
            add_client(client_name)
            list_clients()
        elif command == 2:
            client_name = _get_client_name()
            updated_client_name = raw_input('Inserta el nuevo nombre del cliente: ')
            update_client(client_name, updated_client_name)
            list_clients()
        elif command == 3:
            client_name = _get_client_name()
            delete_client(client_name)
            list_clients()
        elif command == 4:
            client_name = _get_client_name()

            if search_client(client_name) == True:
                print('Cliente encontrado')
            else:
                print('Cliente no encontrado')
        elif command == 5:
            list_clients()
        elif command == 6:
            print('FIN')
            break
        