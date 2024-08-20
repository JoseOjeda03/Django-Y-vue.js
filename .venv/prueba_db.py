import psycopg2
conexion = psycopg2.connect(user='postgres',password='admin',host='127.0.0.1',port='5432',database='test_db')

try:
    with conexion:
        with conexion.cursor() as cursor:
            #SELECT
            # sentencia ='SELECT * FROM persona WHERE id_persona = %s'
            # id_persona=2
            # cursor.execute(sentencia,(id_persona,))
            # registros= cursor.fetchone()
            # print(registros)
            # sentencia= 'INSERT INTO persona(nombre,apellido,email) VALUES(%s,%s,%s)'
            # valores =(('carlos','lara','clara@gmail'),('gabriel','santa','santa@gmail'),('valentina','copa','copa@gmail'))
            # cursor.executemany(sentencia,valores)
            # sentencia='UPDATE persona SET nombre=%s , apellido=%s, email=%s WHERE id_persona=%s'
            # valores=(('juan','esteban','estaban@gamil',1))
            # cursor.execute(sentencia,valores)
            
            sentencia='DELETE FROM persona WHERE id_persona=%s'
            valores=(1,)
            
            cursor.execute(sentencia,valores)
            registros_isertados = cursor.rowcount
            print(f'registros INsertados: {registros_isertados}')
except Exception as e:
    print(f'Ocurrio un error: {e}')
finally:
    conexion.close()