import sqlite3
from datetime import datetime, timedelta

# Conectar con la base de datos y crear las tablas si no existen
conn = sqlite3.connect('personas.db')
c = conn.cursor()
c.execute('''CREATE TABLE IF NOT EXISTS personas (id INTEGER PRIMARY KEY, nombre TEXT)''')
c.execute('''CREATE TABLE IF NOT EXISTS inactividad (persona_id INTEGER, inicio TEXT, fin TEXT)''')

# Agregar personas y periodos de inactividad a las tablas
personas = [('Juan',), ('Pedro',), ('María',), ('Luisa',)]
c.executemany('INSERT INTO personas(nombre) VALUES (?)', personas)

inactividad = [(1, '2023-07-01', '2023-07-07'), (2, '2023-05-01', '2023-05-15'), (3, '2023-09-01', '2023-09-30')]
c.executemany('INSERT INTO inactividad(persona_id, inicio, fin) VALUES (?, ?, ?)', inactividad)

# Obtener todas las fechas del año
fecha_inicio = datetime(2023, 1, 1)
fecha_fin = datetime(2023, 12, 31)
fechas = [fecha_inicio + timedelta(days=d) for d in range((fecha_fin - fecha_inicio).days + 1)]

# Seleccionar un par de personas para cada semana del año
for fecha in fechas:
    semana_inicio = fecha - timedelta(days=fecha.weekday())
    semana_fin = semana_inicio + timedelta(days=6)
    
    c.execute('''SELECT id FROM personas
                 WHERE id NOT IN (SELECT persona_id FROM inactividad
                                  WHERE inicio <= ? AND fin >= ?)''', (semana_inicio, semana_fin))
    personas_disponibles = c.fetchall()
    
    if len(personas_disponibles) >= 2:
        id1, id2 = personas_disponibles[0][0], personas_disponibles[1][0]
        c.execute('INSERT INTO asignacion(persona1_id, persona2_id, inicio, fin) VALUES (?, ?, ?, ?)',
                  (id1, id2, semana_inicio, semana_fin))
        print(f'Asignación realizada para la semana del {semana_inicio:%d-%m-%Y} al {semana_fin:%d-%m-%Y}: '
              f'{c.execute("SELECT nombre FROM personas WHERE id=?", (id1,)).fetchone()[0]} '
              f'y {c.execute("SELECT nombre FROM personas WHERE id=?", (id2,)).fetchone()[0]}')
    else:
        print(f'No hay suficientes personas disponibles para la semana del {semana_inicio:%d-%m-%Y} al {semana_fin:%d-%m-%Y}')

# Guardar los cambios en la base de datos y cerrar la conexión
conn.commit()
conn.close()
