from flask import Blueprint, render_template, request, redirect, url_for
from app import db
from app.models import Albums


alb_bp = Blueprint ('albums',__name__)



@alb_bp.route('/')
def index():
    albums = Albums.query.all()
    return render_template('index.html', albums = albums)

@alb_bp.route('/new',methods=['GET','POST'])
def create_album():
     if request.method == 'POST':
         #Agregar Alumno 
         id = request.form['id']
         titulo = request.form['titulo']
         artista = request.form['artista']
         fecha_lanzamiento = request.form['fecha_lanzamiento']
         genero = request.form['genero']
         descripcion = request.form['descripcion']

         nvo_album = Albums(id = id, titulo = titulo,artista = artista, fecha_lanzamiento = fecha_lanzamiento, genero = genero, descripcion = descripcion)

         db.session.add(nvo_album)
         db.session.commit()
         return redirect(url_for('albums.index'))
     #Aqui sigue si es GET
     return render_template('create_album.html')

@alb_bp.route('/update/<string:id>', methods=['GET','POST'])
def update_album(id):
    album = Albums.query.get(id)

    if request.method == 'POST':
        album.titulo = request.form['titulo']
        album.artista = request.form['artista']
        album.fecha_lanzamiento = request.form['fecha_lanzamiento']
        album.genero = request.form['genero']
        album.descripcion = request.form['descripcion']
        db.session.commit()
        return redirect(url_for('index'))
    return render_template('update_album.html',album = album)
