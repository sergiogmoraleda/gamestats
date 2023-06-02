# DJANGO - GRAPHQL -SQLITE3 API
#### Guía de ejecución paso a paso
1. Abre tu terminal o línea de comandos.
2. Clona el repositorio de GitHub utilizando el siguiente comando:
   git clone <URL_del_repositorio>
   Reemplaza <URL_del_repositorio> con la URL del repositorio que deseas clonar.
3. Navega al directorio del repositorio clonado:
   cd tu_repositorio
4. Crea un entorno virtual (opcional pero recomendado) ejecutando el siguiente comando:
   python3 -m venv venv
5. Activa el entorno virtual:
   - En macOS/Linux:
     source venv/bin/activate
   - En Windows:
     venv\Scripts\activate
6. Instala las dependencias necesarias utilizando pip:
   pip install -r requirements.txt
7. Realiza las migraciones de la base de datos:
   python manage.py migrate
8. Crea un superusuario para acceder al panel de administración de Django:
   python manage.py createsuperuser
   Sigue las instrucciones para ingresar un nombre de usuario, correo electrónico y contraseña.
9. Inicia el servidor de desarrollo:
   python manage.py runserver
10. Ctrl + Click en la url que te aparece y entraras en una pestaña de navegador. Si añades "/graphql/" a la ruta se te abrirá GraphiQL, donde se pueden ver las diferentes querys y mutation que han sido creadas y probadas.


