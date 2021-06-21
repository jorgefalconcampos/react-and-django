# Create/activate the virtual enviroment:

## ◼️ Create
Run the command 
```
python -m venv ${virtualEnvName}
```
where **${virtualEnvName}** is the desired name for your virtual enviroment

## ◼️ Activate
Once created, (at project root level) activate the virtual env with the command 
```
source ${virtualEnvName}/Scripts/activate}
```
where **${virtualEnvName}** is the name you given to your virtual enviroment


<p>&nbsp;</p><p>&nbsp;</p>


# Create/set up the project/app:

## ◼️ Project

Once the the virtual enviroment is activated, run:
```
django-admin startproject ${projectName} .
```
where **${projectName}** is the name you want to give to your project 

⚠ IMPORTANT! notice the dot ( . ) at the end of the command


## ◼️ App
At project root level,  run this command:
```
python manage.py startapp ${appName}
```
where **${appName}** is the name you want to give to your app.

Do not forgot to add this app to your **INSTALLED_APPS** variable inside `${projectName}/settings.py`


<p>&nbsp;</p><p>&nbsp;</p>


# Generate and apply migrations

Whenever you make changes to the models, you should:

1) Generate a migrations file with: 
```
python manage.py makemigrations ${yourApp}
```

2) Then, apply the migrations to the DB with: 
```
python manage.py migrate ${yourApp}
```


In both commands, **${yourApp}** is the name of the Django app