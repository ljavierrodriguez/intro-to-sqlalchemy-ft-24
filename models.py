from sqlalchemy import create_engine, Column, Integer, String, Boolean, Text, DateTime, ForeignKey
from sqlalchemy.orm import declarative_base, sessionmaker, relationship


Base = declarative_base()


# Definimos la estructura de nuestras tablas
class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    username = Column(String(120), unique=True, nullable=False)
    password = Column(String(120), nullable=False)
    active = Column(Boolean(), default=True)
    posts = relationship("Post", backref="user")


class Post(Base):
    __tablename__ = 'posts'
    id = Column(Integer, primary_key=True)
    title = Column(String(200), unique=True, nullable=False)
    users_id = Column(Integer, ForeignKey('users.id'), nullable=False) # Clave Foranea (Foreign Key)


# Conectar con la base de datos que seleccionemos: (SQLite)
engine = create_engine('sqlite:///database.db')
# engine = create_engine('mysql+pymysql://root:root@localhost:3306/dbft24')

# Crear las tablas en la base de datos
with engine.connect() as connection:
    Base.metadata.create_all(connection)


# Creamos una sesion para interactuar con la base de datos
Session = sessionmaker(bind=engine)
session = Session()


# Ejemplo de CRUD (Create, Read, Update, Delete)
# Crear un nuevo usuario
"""
# Usuario 1
user = User(username="lrodriguez", password="123456", active=False)
session.add(user) # INSERT INTO users (username, password, active) VALUES ('lrodriguez', '123456', false);
session.commit() # Confirmar los cambios en la base de datos

# Usuario 2
user = User()
user.username = "johndoe"
user.password = "123456"
user.active = True
session.add(user)
session.commit()

# Usuario 3
user = User()
user.username = "janedoe"
user.password = "123456"
user.active = True
session.add(user)
session.commit()

post = Post(title="Hola Mundo desde SQLAlchemy", users_id=1)
session.add(post)
session.commit()

"""
print("=====================================================================")

# Leer la tabla de usuarios
users = session.query(User).all() # SELECT * FROM users
#users = list(map(lambda user: user.username, users))
#print(users)
for user in users:
    print(f"id: {user.id}, username: {user.username}, password: {user.password}, active: {user.active}")
    print(f"Posts: {len(user.posts)}")
    if len(user.posts) > 0:
        for post in user.posts:
            print(post.title)

print("=====================================================================")
user = session.query(User).filter_by(id=1).first()
print(f"id: {user.id}, username: {user.username}, password: {user.password}, active: {user.active}")

print("=====================================================================")

users = session.query(User).filter_by(active=True)
for user in users:
    print(f"id: {user.id}, username: {user.username}, password: {user.password}, active: {user.active}")

print("=====================================================================")

# Actualizando un usuario
user = session.query(User).filter_by(id=1).first()
user.active = True # UPDATE users SET active = true WHERE id=1
session.commit()

print("USUARIO ACTUALIZADO")

print("=====================================================================")

users = session.query(User).filter_by(active=True)
for user in users:
    print(f"id: {user.id}, username: {user.username}, password: {user.password}, active: {user.active}")

print("=====================================================================")

# Eliminar un usuario

user = session.query(User).filter_by(username='johndoe').first()
if user:
    session.delete(user) # DELETE FROM users WHERE username = 'johndoe';
    session.commit()
    print("USUARIO ELIMINADO")
else:
    print("USUARIO NO ENCONTRADO")

print("=====================================================================")

users = session.query(User).filter_by(active=True)
for user in users:
    print(f"id: {user.id}, username: {user.username}, password: {user.password}, active: {user.active}")

print("=====================================================================")


posts = session.query(Post).all()
for post in posts:
    print(f"Title: {post.title}, Author: {post.user.username}")


# Cerrar session
session.close()