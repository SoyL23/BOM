from db.db import db
from models.country_model import Country
from models.state_model import State
from models.city_model import City
from models.role_model import Role

capitales_colombia = {

    "Amazonas": "Leticia",
    "Antioquia": "Medellín",
    "Arauca": "Arauca",
    "Atlántico": "Barranquilla",
    "Bolívar": "Cartagena",
    "Boyacá": "Tunja",
    "Caldas": "Manizales",
    "Caquetá": "Florencia",
    "Casanare": "Yopal",
    "Cauca": "Popayán",
    "Cesar": "Valledupar",
    "Chocó": "Quibdó",
    "Córdoba": "Montería",
    "Cundinamarca": "Bogotá",
    "Guainía": "Puerto Inírida",
    "Guaviare": "San José del Guaviare",
    "Huila": "Neiva",
    "La Guajira": "Riohacha",
    "Magdalena": "Santa Marta",
    "Meta": "Villavicencio",
    "Nariño": "Pasto",
    "Norte de Santander": "Cúcuta",
    "Putumayo": "Mocoa",
    "Quindío": "Armenia",
    "Risaralda": "Pereira",
    "San Andrés y Providencia": "San Andrés",
    "Santander": "Bucaramanga",
    "Sucre": "Sincelejo",
    "Tolima": "Ibagué",
    "Valle del Cauca": "Cali",
    "Vaupés": "Mitú",
    "Vichada": "Puerto Carreño"
}

roles_educativos = {
    "Administrador": "Administrar usuarios, cursos y contenido, generar informes",
    "Profesor": "Crear y gestionar cursos, calificar tareas, interactuar con alumnos",
    "Alumno": "Tomar cursos, enviar tareas, participar en foros",
    "Tutor": "Brindar apoyo académico y motivacional a los alumnos",
    "Coordinador Académico": "Coordinar planes de estudio, asignar profesores",
    "Soporte Técnico": "Resolver problemas técnicos de la plataforma",
    "Diseñador Instruccional": "Diseñar material educativo y cursos",
    "Investigador": "Realizar investigaciones académicas",
    "Director/Administrador de la Institución": "Supervisar el funcionamiento general de la institución educativa"
}

for key, value in roles_educativos.items():
   role = Role(name=key, description=f'Para usuarios {key} en el sistema', functions=f'{value}')
   with db.session.begin():
      db.session.add(role)
      db.session.commit()
      db.session.close()

country = Country(name='Colombia', description='Para Usuarios y empresas residentes en Colombia', code='COL')
with db.session.begin():
   db.session.add(country)
   db.session.commit()
   db.session.close()

for key, value in capitales_colombia.items():
   with db.session.begin():
      state = State(name=key, description=f'Para Usuarios y empresas residentes en {key}, Colombia', code='', country_id=1)
      db.session.add(state)
      db.session.commit()
      db.session.close()
      
for key, value in capitales_colombia.items():
   with db.session.begin():
      state = db.session.query(State).filter(State.name == key).first()
      city = City(name=value, description=f'Para Usuarios y empresas residentes en {value}, {key}', code='', state_id=state.id)
      db.session.add(city)
      db.session.commit()
      db.session.close()
   
