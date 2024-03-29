import os
from General_Utilities.option_list import option_list
from General_Utilities.control_rutas import setting_routes


class laravel_orders():
    '''
    Clase de compendio de ordenes para proyectos laravel.

    La creacion de proyectos requiere conexion a internet!
    '''

    def __init__(self):
        '''
        Inicializa la instancia.

        Se abre un explorador de archivos. Hay que localizarlo en la carpeta de proyectos. 
        '''
        import tkinter as tk
        from tkinter import filedialog
        # Seleccionando el directorio
        root = tk.Tk()
        root.withdraw()
        dir_path = filedialog.askdirectory()
        self.base_path = setting_routes('dir')[0]
        self.dir_path = dir_path
        self.orders = {
             # Crea un nuevo proyecto de Laravel en un directorio específico.
            'new'       : 'laravel new', 
             # Inicia el servidor de desarrollo de Laravel.
            'serve'     : 'php artisan serve', 
             # Ejecuta las migraciones pendientes para actualizar la base de datos.
            'migrate'   : 'php artisan migrate', 
             # Revierte la última migración realizada.
            'rollback'  : 'php artisan migrate:rollback', 
             # Revierte todas las migraciones realizadas.
            'reset'     : 'php artisan migrate:reset', 
             # Revierte y vuelve a ejecutar todas las migraciones.
            'refresh'   : 'php artisan migrate:refresh', 
             # Muestra el estado actual de todas las migraciones.
            'status'    : 'php artisan migrate:status', 
             # Ejecuta los seeders registrados para poblar la base de datos.
            'seed'      : 'php artisan db:seed', 
             # Crea un nuevo modelo en la carpeta "app" de tu proyecto.
            'model'     : 'php artisan make:model', 
             # Crea un nuevo archivo de migración en la carpeta "database/migrations".
            'migration' : 'php artisan make:migration', 
             # Crea un nuevo archivo de seeder en la carpeta "database/seeds".
            'seeder'    : 'php artisan make:seeder', 
             # Crea una nueva factory en la carpeta "database/factories".
            'factory'   : 'php artisan make:factory', 
             # Crea un nuevo controlador en la carpeta "app/Http/Controllers".
            'controller': 'php artisan make:controller', 
             # Crea una nueva clase de recurso en la carpeta "app/Http/Resources".
            'resource'  : 'php artisan make:resource', 
             # Crea una nueva clase de request en la carpeta "app/Http/Requests".
            'request'   : 'php artisan make:request', 
             # Crea un nuevo middleware.
            'middleware': 'php artisan make:middleware', 
             # Crea un nuevo compnente livewire.
            'livewire_component': 'php artisan make:livewire', 
             # Crea una clase para la generacion de mail.
            'mail'  : 'php artisan make:mail',
             # Muestra la lista actualizada de rutas del sistema".
            'route' : 'php artisan route:list', 
             # Instalará el paquete breeze para gestionar autenticaciones.
            'Auth_breeze_package'   : 'composer require laravel/breeze --dev',
             # Instalará el paquete jetstream para gestionar autenticaciones.
            'Auth_jetstream_package': 'composer require laravel/jetstream',
             # Instalará el paquete livewire para renderizado parcial en el proyecto.
            'livewire'  : 'composer require livewire/livewire',
             # Instalará el paquete telegram-bot en el proyecto.
            'telegram'  : 'composer require telegram-bot/api',
             # Instalará el scafolding.
            'breeze_install'        : 'php artisan breeze:install',
             # Instalará el scafolding.
            'jetstream_install'     : 'php artisan jetstream:install',
             # Instalará npm para vizualizacion del scafolding.
            'npm_install': 'npm install',
             # Iniciara node para la adecuada ejecuacion de los frontales.
            'npm_run_dev': 'npm run dev',
             # genera un link simbolico...
            'storagelink': 'php artisan storage:link',
        }

        self.conn_project()


    def action(self, key, value=None):
        '''
        Metodo de aplicacion de acciones
        '''
        os.chdir(self.project_path)
        if value != None:
            value = value
            order = self.orders[key] + ' ' + value
        else:
            order = self.orders[key]
        os.system(order)
        os.chdir(self.base_path)


    def attributes(self):
        '''
        main_description: attributes.
        '''
        print(
            '\n'.join(
                [
                    self.base_path,
                    self.dir_path,
                    self.project_name,
                    self.project_path,
                    ''
                ]
            ),
            self.orders
        )


    def location(self):
        '''
        main_description: location.
        '''
        dir = os.getcwd()
        print(dir)


    def laravel_new(self):
        '''
        main_description: laravel new.
        '''
        self.project_name = input('proyect name: ')
        self.project_path = os.path.join(self.dir_path, self.project_name)
        order = f'laravel new {self.project_name}'
        os.chdir(self.dir_path)
        os.system(order)

        # Creando database
        try:
            self.create_database()
        except:
            print("Error al conectar DB.")

    
    def conn_project(self):
        '''
        main_description: conn project.
        '''
        proyectos_laravel = []
        for raiz, directorios, archivos in os.walk(self.dir_path):
            for directorio in directorios:
                ruta_completa = os.path.join(raiz, directorio)
                if os.path.isdir(ruta_completa):
                    archivos_proyecto = os.listdir(ruta_completa)
                    if 'artisan' in archivos_proyecto:
                        proyectos_laravel.append(ruta_completa)

        if len(proyectos_laravel)>0:
            print("Se encontraron los siguientes proyectos Laravel:")
            self.project_path = option_list(proyectos_laravel)
            print(self.project_path)

            self.project_name = os.path.basename(self.project_path)

        else:
            print("No se encontraron proyectos Laravel en el directorio general.")


    def create_database(self):
        '''
        main_description: create database.
        '''
        import mysql.connector
        # Instanciamos
        cnx = mysql.connector.connect(
            host = 'localhost',
            user = 'root',
            password = ''
        )
        # Verificamos el estado
        if cnx.is_connected():
            # Creamos el cursor para poder enviar las querys
            curs = cnx.cursor()
            # Diseñamos la query
            print(f'Creando database: {self.project_name}')
            sql = f'CREATE DATABASE {self.project_name}'
            # Ejecutamos la query
            curs.execute(sql)
            # Cerramos el cursor
            curs.close()
            # Cerramos la conexion
            cnx.close()
        # Verificamos el estado
        if not cnx.is_connected():
            print('Conexion cerrada.')


    def model_list(self):
        '''
        main_description: model_list.
        '''
        directorio = os.path.join(self.project_path, 'app', 'Models')

        # Verificar si el directorio existe
        if not os.path.isdir(directorio):
            print("El directorio no existe.")
            return []
        
        # Obtener todos los archivos del directorio
        archivos = os.listdir(directorio)
        
        # Lista para almacenar los nombres de los modelos
        modelos = []
        
        # Recorrer cada archivo del directorio
        for archivo in archivos:
            # Verificar si el archivo es un modelo (termina con ".php" y no es "Model.php")
            if archivo.endswith(".php") and archivo != "Model.php":
                # Agregar el nombre del modelo a la lista
                modelos.append(archivo[:-4])
        
        # Verificar si se encontraron modelos
        if len(modelos) == 0:
            print("No se encontraron modelos en el directorio.")
        
        # print(modelos)

        return modelos

    def middleware_list(self):
        '''
        main_description: middleware_list.
        '''
        directorio = os.path.join(self.project_path, 'app', 'http' , 'middleware')

        # Verificar si el directorio existe
        if not os.path.isdir(directorio):
            print("El directorio no existe.")
            return []
        
        # Obtener todos los archivos del directorio
        archivos = os.listdir(directorio)
        
        # Lista para almacenar los nombres de los middlewares
        middlewares = []
        
        # Recorrer cada archivo del directorio
        for archivo in archivos:
            # Verificar si el archivo es un middleware (termina con ".php" y no es "middleware.php")
            if archivo.endswith(".php") and archivo != "middleware.php":
                # Agregar el nombre del middleware a la lista
                middlewares.append(archivo[:-4])
        
        # Verificar si se encontraron middlewares
        if len(middlewares) == 0:
            print("No se encontraron middlewares en el directorio.")
        
        # print(middlewares)

        return middlewares


    def serve(self):
        '''
        main_description: serve.
        '''
        self.action('serve')

    def makemodel(self):
        '''
        main_description: makemodel.
        '''
        model_name = input('model name: ').capitalize()
        self.action('model', model_name + ' --migration')

    def makemigration(self):
        '''
        main_description: makemigration.
        Aca hay que poner el nombre. No completa el nombre por defecto.
        '''
        migration_name = input('migration name: ')
        self.action('migration', migration_name)

    def makeseeder(self):
        '''
        main_description: makeseeder.
        '''
        seeder_name = option_list(self.model_list()) + 'Seeder'
        self.action('seeder', seeder_name)    

    def makefactory(self):
        '''
        main_description: makefactory.
        '''
        factory_name = option_list(self.model_list()) + 'Factory'
        self.action('factory', factory_name)    

    def makecontroller(self):
        '''
        main_description: makecontroller.
        '''
        controller_name = input('controller name: ').capitalize()
        self.action('controller', controller_name  + 'Controller')

    def makecontroller_model(self):
        '''
        main_description: makecontroller_model.
        '''
        controller_name = option_list(self.model_list()) + 'Controller'
        self.action('controller', controller_name)

    def makecontroller_middleware(self):
        '''
        main_description: makecontroller_middleware.
        '''
        controller_name = option_list(self.middleware_list()) + 'Controller'
        self.action('controller', controller_name)

    def makeresource(self):
        '''
        main_description: makeresource.
        '''
        resource_name = option_list(self.model_list()) + 'Resource'
        self.action('resource', resource_name)

    def makecontroller_resource(self):
        '''
        main_description: makecontroller_resource.
        '''
        controller_name = option_list(self.model_list()) + 'Controller'
        self.action('controller', controller_name + ' --resource')

    def makemiddleware(self):
        '''
        main_description: makemiddleware.
        '''
        middleware_name = input('middleware name: ').capitalize()
        self.action('middleware', middleware_name)

    def makerequest(self):
        '''
        main_description: makerequest.
        '''
        request_name = input('request name: ')
        self.action('request', request_name)

    def makerequest_model(self):
        '''
        main_description: makerequest_model.
        '''
        request_name = option_list(self.model_list()) + 'Request'
        self.action('request', request_name)

    def livewire_component(self):
        '''
        main_description: livewire_component.
        '''
        livewire_component_name = input('livewire component name: ')
        self.action('livewire_component', livewire_component_name)

    def telegram(self):
        '''
        main_description: telegram.
        '''
        self.action('telegram')

    def mail(self):
        '''
        main_description: mail.
        '''
        mail_name = input('mail class name: ').capitalize()
        self.action('mail', mail_name + 'Mail')

    def routelist(self):
        '''
        main_description: routelist.
        '''
        self.action('route')

    def migrate(self):
        '''
        main_description: migrate.
        '''
        self.action('migrate')

    def rollback(self):
        '''
        main_description: rollback.
        '''
        self.action('rollback')

    def reset(self):
        '''
        main_description: reset.
        '''
        self.action('reset')

    def refresh(self):
        '''
        main_description: refresh.
        '''
        self.action('refresh')

    def dbseed(self):
        '''
        main_description: dbseed.
        '''
        self.action('seed')

    def Auth_breeze_package(self):
        '''
        main_description: Auth_breeze_package.
        '''
        self.action('Auth_breeze_package')

    def Auth_jetstream_package(self):
        '''
        main_description: Auth_jetstream_package.
        '''
        self.action('Auth_jetstream_package')

    def breeze_install(self):
        '''
        main_description: breeze_install.
        '''
        self.action('breeze_install')

    def jetstream_install(self):
        '''
        main_description: jetstream_install.
        '''
        opt = ['livewire', 'inertia', 'inertia --teams']
        stack = option_list(opt)
        self.action('jetstream_install', stack)

    def npm_install(self):
        '''
        main_description: npm_install.
        '''
        self.action('npm_install')

    def npm_run_dev(self):
        '''
        main_description: npm_run_dev.
        '''
        self.action('npm_run_dev')

    def livewire(self):
        '''
        main_description: livewire.
        '''
        self.action('livewire')

    def storagelink(self):
        '''
        main_description: storagelink.
        '''
        self.action('storagelink')

    def newview(self):
        '''
        main_description: newview.
        '''
        view_name = input('view name: ')
        view_path = os.path.join(self.project_path, 'resources', 'views', view_name + '.blade.php')
        with open(view_path, 'w', encoding='utf-8') as view:
            content = f'''<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{view_name}</title>
</head>
<body>
    
</body>
</html>
'''
            view.write(content)
            view.close()


