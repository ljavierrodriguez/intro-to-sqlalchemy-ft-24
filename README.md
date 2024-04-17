# Crear un entorno virtual usando "pipenv"

- Crear un entorno virtual con una version especifica de python

```shell
pipenv --python=3.12
```

- Activa y Crear el entorno virtual usando la version por defecto de python o la seleccionada en el paso anterior

```shell
pipenv shell
```

# Database URI SQLAlchemy

```text
Nota: dialect+driver://<user>:<pass>@<host>:<port>/<database-name>
```

MySQL: 
```text
mysql+pymysql://root:root@localhost:3306/prueba
```

PostgreSQL:
```text
postgresql+psycopg2://postgres:postgres@localhost:5432/prueba
```

SQLite:
```text
sqlite:///database.db
```
