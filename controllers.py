from models import db, Juego

# LISTAR TODOS LOS JUEGOS
def obtener_juegos():
    return Juego.query.all()


# OBTENER UN JUEGO POR ID
def obtener_juego(id):
    return Juego.query.get(id)


# AGREGAR JUEGO
def agregar_juego(nombre, genero, precio):
    nuevo_juego = Juego(
        nombre=nombre,
        genero=genero,
        precio=precio
    )
    db.session.add(nuevo_juego)
    db.session.commit()


# ACTUALIZAR JUEGO
def actualizar_juego(id, nombre, genero, precio):
    juego = Juego.query.get(id)
    juego.nombre = nombre
    juego.genero = genero
    juego.precio = precio
    db.session.commit()


# ELIMINAR JUEGO
def eliminar_juego(id):
    juego = Juego.query.get(id)
    db.session.delete(juego)
    db.session.commit()