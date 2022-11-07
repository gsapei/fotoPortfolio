@echo off
if exist venv (
    cmd /k "cd /d ./venv/scripts & activate &  python ../../manage.py runserver & cd.. & cd.. & exit"
) else (
    echo Debe instalar un entorno virtual con django en este directorio...
    echo PASOS:
    echo  -  pip install venv
    echo  -  python -m venv venv
    echo  -  ./venv/scripts/activate
    echo  -  pip install django
    echo  -  pip install pillow
)
