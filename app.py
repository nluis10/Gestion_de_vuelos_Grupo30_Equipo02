from flask import Flask
from flask import render_template
from flask import redirect
from flask import request
from flask_wtf.csrf import CSRFProtect
from flask_wtf.csrf import CSRFError
import os

app=Flask(__name__)

@app.route('/login', methods=['GET', 'POST'])
def login():
    return render_template('login.html')

@app.route('/validar_login', methods=['POST'])
def validarLogin():
    if (request.method == 'POST'):
        return redirect('/')
    else:
        return "ERROR"

@app.route('/recuperar_clave', methods=['GET', 'POST'])
def recuperarClave():
    return render_template('recuperarClave.html')

@app.route('/registro', methods=['GET', 'POST'])
def registro():
    return render_template('registro.html')

@app.route('/privacidad', methods=['GET'])
def privacidad():
    return render_template('privacidad.html')

@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')

@app.route('/perfil', methods=['GET'])
def perfil():
    return render_template('perfil.html')

@app.route('/agregar_usuario', methods=['GET', 'POST'])
def agregarUsuario():
    return render_template('agregarUsuario.html')

@app.route('/validar_agregar_usuario', methods=['POST'])
def validarAgregarUsduario():
    return redirect('/perfil')

@app.route('/editar_usuario', methods=['GET', 'POST'])
def editarUsuario():
    return render_template('editarUsuario.html')

@app.route('/cambiar_clave', methods=['GET', 'POST'])
def cambiarClave():
    return render_template('cambiarClave.html')

@app.route('/vuelos_asignados', methods=['GET'])
def vuelosAsignados():
    return render_template('vuelosAsignados.html')

@app.route('/vuelos', methods=['GET'])
def vuelos():
    return render_template('vuelos.html')

@app.route('/crear_vuelo', methods=['GET', 'POST'])
def crearVuelo():
    return render_template('crearVuelo.html')

@app.route('/editar_vuelo', methods=['GET', 'POST'])
def editarVuelo():
    return render_template('editarVuelo.html')

@app.route('/eliminar_vuelo', methods=['GET', 'POST'])
def eliminarVuelo():
    return render_template('eliminarVuelo.html')

@app.route('/reservar_vuelo', methods=['GET', 'POST'])
def reservarVuelo():
    return render_template('reservarVuelo.html')

@app.route('/buscar_vuelo', methods=['GET'])
def buscarVuelo():
    return render_template('buscarVuelo.html')

@app.route('/calificar_vuelo', methods=['GET', 'POST'])
def calificarVuelo():
    return render_template('calificarVuelo.html')

@app.route('/gestion_comentario', methods=['GET', 'POST'])
def gestionComentario():
    return render_template('gestionComentario.html')

@app.route('/dashboard', methods=['GET'])
def dashboard():
    return render_template('dashboard.html')

@app.route('/dashboard_vuelos', methods=['GET'])
def dashboardVuelos():
    return render_template('dashboardVuelos.html')

@app.route('/dashboard_usuarios', methods=['GET'])
def dashboardUsuarios():
    return render_template('dashboardUsuarios.html')

@app.route('/dashboard_calificaciones', methods=['GET'])
def dashboardCalificaciones():
    return render_template('dashboardCalificaciones.html')


@app.errorhandler(CSRFError)
def handle_csrf_error(e):
    return render_template('csrfError.html', reason=e.description), 400


csrf = CSRFProtect()
csrf.init_app(app)

SECRET_KEY = os.urandom(32)
app.config['SECRET_KEY'] = SECRET_KEY

app.run(debug=True)
