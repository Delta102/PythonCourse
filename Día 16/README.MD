## Guardar instalaciones en Requeriments.txt
pip freeze > Requeriments.txt

## Instalar virtualenv
```
pip install virtualenv
```
## Configurar entorno virtual
```
virtualenv env
```
## Activar entorno Virtual
```
env/Scripts/activate.bat
```
## Instalar django
```
pip install django
```
## Levantar django
```
django-admin startproject "nombre del proyecto"
```
## Iniciar servidor (En la carpeta del proyecto)
```
python manage.py runserver
```
## Crear migrations
```
python manage.py makemigrations
```
## Crear migraciones
```
python manage.py migrate
```
## Crear Superusuario
```
python manage.py createsuperuser
```
## Crear carpeta de modelos, views, urls, migraciones, etc  (En Proyecto)
```
python manage.py startapp "Nombre de Carpeta"
```
## Colocar el nombre de la carpeta creada desde start app
```
src\MiProyecto\MiProyecto\settings.py> INSTALLED_APPS = [...., ']
```
## Instalar django rest-framework
```
pip install djangorestframework
pip install markdown
pip install django-filter.
```
Archivo: setting.py
```
INSTALLED_APPS{
    ...,
    'rest_framework',
}
```
## Crear git por primera vez
```
git init
git add .
git commit -m "first commit"
git remote add origin https://github.com/Delta102/Netflix_Code_Python

git push origin master
```
## Subir código
```
git add .
git commit -m "mensaje"
git push origin master
```
## Instalar Autenticacion (Simple JWT)
```
pip install djangorestframework-simplejwt
``` 
Configuración
```
REST_FRAMEWORK={
    ...
    'DEFAULT_AUTHENTICATION_CLASSES':(
        ...
        'rest_framework_simplejwt.authentication.JWTAuthentication',
    )
    ...
}
```
Url-Main
```
from rest_framework_simplejwt.views import(
    TokenObtainPairView,
    TokenRefreshView,
)
```
```
urlpatterns=[
    ...
    path('api/token/',TokenObtainPairView.as_view(),name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(),name='token_refresh'),
    ...
]
```
## Instalar Angular
```
npm install -g @angular/cli
``` 
## Crear Proyecto
```
ng new "nombre del proyecto"
```