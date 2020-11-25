from flask import Flask, render_template, request, redirect, url_for
import sqlite3

app = Flask(__name__)
db = sqlite3.connect('data.db', check_same_thread=False)
@app.route('/')
def Index():
    return render_template('Index.html')
@app.route('/Contacto', methods=['GET','POST'])
def Contacto():
    if request.method=='GET':
        return render_template('Contacto.html')
    nombres=request.form.get('nombres')
    apellidos=request.form.get('apellidos')
    email=request.form.get('email')
    celular=request.form.get('celular')
    return 'Guardando Información'+'\n'+nombres+'\n'+apellidos+'\n'+email+'\n'+celular+'\n'+email


@app.route('/Usuarios')
def Usuarios():
    Usuarios = db.execute('select * from Usuarios')
    Usuarios = Usuarios.fetchall()
    return render_template('Usuarios/Listar.html', Usuarios=Usuarios)

@app.route('/Usuarios/Crear', methods=['GET','POST'])
def Crear_Usuarios():
    if request.method == 'GET':
        return render_template('Usuarios/Crear.html')
    
    Nombres=request.form.get('Nombres')
    Apellidos=request.form.get('Apellidos')
    Email=request.form.get('Email')
    Contraseña=request.form.get('Contraseña')
    
    cursor=db.cursor()
    
    cursor.execute("""INSERT INTO Usuarios(
            Nombres,
            Apellidos, 
            Email,
            Contraseña
        )values (?,?,?,?)
    """, (Nombres,Apellidos,Email,Contraseña))
    
    db.commit()
    
    return redirect(url_for('Usuarios'))

@app.route('/Usuarios/Eliminar', methods=['GET','POST'])
def Eliminar():
    if request.method == 'GET':
        return render_template('Usuarios/Actualizar.html')
    
    Id=request.form.get('Id')
    cursor = db.cursor()
    cursor.execute("""DELETE FROM Usuarios where Id=?""",(Id))
    
    db.commit()
    
    return redirect(url_for('Usuarios'))
    

@app.route('/Usuarios/Editar', methods=['GET','POST'])
def Editar():
    if request.method == 'GET':
        return render_template('Usuarios/Editar.html')
    
    Id=request.form.get('Id')
    Nuevos_Nombres=request.form.get('Nombres')
    Nuevos_Apellidos=request.form.get('Apellidos')
    Nuevo_Email=request.form.get('Email')
    Nueva_Contraseña=request.form.get('Email')
    cursor = db.cursor()
    cursor.execute("""UPDATE Usuarios SET
                Nombres=?,
                Apellidos=?, 
                Email=?,
                Contraseña=?
                WHERE Id=?
    """,(Nuevos_Nombres,Nuevos_Apellidos,Nuevo_Email,Nueva_Contraseña,Id))
    db.commit()
    
    return redirect(url_for('Usuarios'))

app.run(debug=True)
