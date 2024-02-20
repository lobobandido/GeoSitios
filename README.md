# GeoSitios
proyecto de prueba para capturar geolocalización de Sitio(puntos de servicio)

Proyecto de E-Commerce con Django

primera etapa

contenido del repositorio+++++

configuración Proyecto base configuración de la base de datos configuración de tablas para categorías productos y creación del panel de control

Este proyecto es un e-commerce con los siguientes avances: se creo un entorno virtual, se crean las dependencias, conectamos la base de datos, creamos una app web, dentro de esta app web configuramos 2 modelos (categoría y productos) y por último se creo el panel de administración.

comandos : python -m venv venv-----creamos entorno virtual

source venv/Scripts/activate------ activamos entorno virtual

django-admin startproyect aarshop esto genera 2 carpetas (settings.py urls.py )

python manage.py start app web (creamos nuestra app web)

python manage.py runserver iniciamos nuestro server

git status para ver cambios en nuestro proyecto

git add . area de trabajo (cache de git)

git commit -m deja un comentrio en en el proyecto "proyecto inicial

git push origin main manda cambios al repositorio

python manage.py migrate

python manage.py create superuser
