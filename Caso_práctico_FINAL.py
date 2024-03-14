#Clase en directo - Laboratorio 
#API - interfaz que nos permite interactuar con la base de datos. Tipo REST - estilo arquitectónico para diseñar sistemas distribuidos.
#Principios REST - se utilizan en alta volumetria de datos, para hacer las operaciones de la forma más simple possible, evitando sobrecargar el sistema. 
#Recursos = cualquier cosa que pueda ser nombrada o identificada. Definidos por los mapers. Definen los atributos (similar a los datos de nuestra base de SQL).
#URI - cada recurso es identificado por un URI único. /users/, /sales/...
#Método HTTP - GET, POST, PUT ,DELETE para definir operaciones sobre los recursos. Similar a lo SQL (GET = GET, POST = CREATE, PUT = UPDATE, DELETE = DELETE).
#Representaciones - se pueden representar en JSON, XML, HTML.
#Estados Stateless - cada solicitud HTTP contiene toda la información necesaria para procesar la solicitud y no se requiere ningún estado de sesión en el servidor. 
# -- MUY UTILIZADES EN DESARROLLO DE APLICACIONES WEB Y MÓVILES--

#Creación de una API - es la parte más relacionada con INGENIERO DE DATOS, el nivel de ANALISTA DE DATOS, seria la parte siguiente, es decir trabajar con los datos ya acabados.

#127.0.0.1 - - [12/Mar/2024 10:54:12] "GET /clients HTTP/1.1" 404 -
#127.0.0.1 - - [12/Mar/2024 10:54:12] "GET /favicon.ico HTTP/1.1" 404 -

#from flask import Flask, jsonify
#from flask_restx import Api, Resource, fields
#from sqlalchemy import create_engine, MetaData, Table, select
#from sqlalchemy.exc import SQLAlchemyError

#pip install Flask Flask-SQLAlchemy flask-restx
#pip install psycopg2-binary
#pip install Flask sqlalchemy flask-restx

from flask import Flask, request
from flask_restx import Api, Resource, fields
from sqlalchemy import create_engine, MetaData, select, insert, update, delete
from sqlalchemy.exc import SQLAlchemyError

app = Flask(__name__)

# Initialize Flask-Restx API
api = Api(app, version='1.0', title='API de Usuarios', description='Una API para gestionar usuarios')

# Create a database engine
db_uri = 'postgresql://postgres:1234@localhost:5432/flask'
engine = create_engine(db_uri)

# Reflect the existing 'users' table
metadata = MetaData()
try:
    metadata.reflect(bind=engine)
    users_table = metadata.tables['User']
except SQLAlchemyError as e:
    print(f"Error reflecting table: {e}")


# Define API input/output model
user_model = api.model('User', {
    'id': fields.Integer(readonly=True, description='El ID del usuario'),
    'username': fields.String(required=True, description='El nombre de usuario'),
    'email': fields.String(required=True, description='La dirección de correo electrónico del usuario')
})

class UserResource(Resource):
    @api.doc(description='Obtener un usuario por su ID', responses={404: 'Usuario no encontrado'})
    @api.marshal_with(user_model)
    def get(self, user_id):
        # Create a database connection
        with engine.connect() as connection:
            # Construct the select query with explicit column names
            query = select(
                users_table.c.id,
                users_table.c.username,
                users_table.c.email
            ).where(users_table.c.id == user_id)
            
            # Execute the query and fetch the result
            result = connection.execute(query).fetchone()

            # If user exists, return user data
            if result:
                return result
            else:
                api.abort(404, 'Usuario no encontrado')


    @api.doc(description='Actualizar un usuario existente', responses={200: 'Usuario actualizado', 404: 'Usuario no encontrado'})
    @api.expect(user_model)
    def put(self, user_id):
        # Extract user data from request
        updated_user_data = request.json
        
        # Create a database connection
        with engine.connect() as connection:
            # Construct the update query
            query = update(users_table).where(users_table.c.id == user_id).values(
                username=updated_user_data['username'],
                email=updated_user_data['email']
            )
            
            # Execute the update query
            result = connection.execute(query)

            connection.commit()

        
        if result.rowcount == 0:
            return {'message': 'Usuario no encontrado'}, 404
        else:
            return {'message': 'Usuario actualizado'}, 200

    @api.doc(description='Eliminar un usuario existente', responses={204: 'Usuario eliminado', 404: 'Usuario no encontrado'})
    def delete(self, user_id):
        # Create a database connection
        with engine.connect() as connection:
            # Construct the delete query
            query = delete(users_table).where(users_table.c.id == user_id)
            
            # Execute the delete query
            result = connection.execute(query)
            
            connection.commit()
        
        if result.rowcount == 0:
            return {'message': 'Usuario no encontrado'}, 404
        else:
            return {'message': 'Usuario eliminado'}, 204

class UsersResource(Resource):

    @api.doc(description='Obtener todos los usuarios', responses={404: 'Usuarios no encontrados'})
    @api.marshal_with(user_model, as_list=True)
    def get(self):
        # Create a database connection
        with engine.connect() as connection:
            # Construct the select query to fetch all records
            query = select(
                users_table.c.id,
                users_table.c.username,
                users_table.c.email
            )
            
            # Execute the query and fetch all results
            results = connection.execute(query).fetchall()

            # If users exist, return user data
            if results:
                return results
            else:
                api.abort(404, 'Usuarios no encontrados')

                

    @api.doc(description='Crear un nuevo usuario', responses={201: 'Usuario creado'})
    @api.expect(user_model)
    def post(self):
        # Extract user data from request
        new_user_data = request.json
        
        # Create a database connection
        with engine.connect() as connection:
            try:
                # Construct the insert query
                query = insert(users_table).values(
                    username=new_user_data['username'],
                    email=new_user_data['email']
                )
                
                # Execute the insert query
                connection.execute(query)
                connection.commit()

                
                return {'message': 'Usuario creado'}, 201
            except Exception as e:
                return {'error': str(e)}, 500


api.add_resource(UserResource, '/users/<int:user_id>')
api.add_resource(UsersResource, '/users')

if __name__ == '__main__':
    app.run(debug=True)