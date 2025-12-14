from app import db

class Albums(db.Model):
    __tablename__ = 'albums'
    id = db.Column(db.String, primary_key=True)
    titulo = db.Column(db.String)
    artista = db.Column(db.String)
    fecha_lanzamiento = db.Column(db.Date)
    genero = db.Column(db.String)
    descripcion = db.Column(db.String)

    def to_dict(self):
        return{
            'id':self.id,
            'titulo':self.titulo,
            'artista':self.artista,
            'fecha_lanzamiento':self.fecha_lanzamiento,
            'genero':self.genero,
            'descripcion' : self.descripcion,
        }