from flask import Flask
from flask import render_template, request
from flaskext.mysql import MySQL
from datetime import datetime
    

app = Flask(__name__)

mysql = MySQL()
app.config ['MYSQL_DATABASE_HOST'] = 'localhost'
app.config ['MYSQL_DATABASE_USER'] = 'root'
app.config ['MYSQL_DATABASE_PASSWORD'] = ''
app.config ['MYSQL_DATABASE_DB'] = 'crudcleintes'
mysql.init_app(app)

    


@app.route('/')
def index():
    sql="INSERT INTO `clientes` (`id`, `nombre_apellido`, `direccion`, `mail`, `telefono`) VALUES (NULL, 'aaleellm', 'mcewkmkweº¡', 'ddjoidqwoij', 'sdoiwjoi');"
    conn = mysql.connect()
    cursor = conn.cursor()
    cursor.execute(sql)
    conn.commit()

    return render_template ('empleados/index.html')

@app.route('/create')
def create():
 
    return render_template ('empleados/create.html')
    
@app.route('/store', methods=['post'])
def storage():
    _nombre = request.form ['txtnombre']
    _correo = request.form ['txtcorreo']
    _foto = request.files ['txtfoto']

    sql="INSERT INTO `clientes` (`id`, `nombre_apellido`, `direccion`, `mail`, `telefono`) VALUES (NULL, %s, %s, %s, %s);"
    datos = (_nombre, _correo, _foto.filename)

    conn = mysql.connect()
    cursor = conn.cursor()
    cursor.execute(sql, datos)
    conn.commit()

    return render_template ('empleados/index.html')


if __name__ == '__main__':
    app.run(debug=True)