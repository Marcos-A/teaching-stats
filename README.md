# School Evaluation Form
Form about high school's services to be asnwered by the students. Students login through their Google account. Responses are recorded in a PostgreSQL database. The application prevents responses from unauthorized students and duplicated submissions.

There're different requirements and setup instructions depending on your running setup:
A) Run from localhost
B) Run from your domain

---

## A) Run from localhost
#### Requirements
```
sudo apt install apache2
sudo apt-get install python3	
sudo apt-get install libpq-dev python-dev
sudo apt install python3-pip
pip3 install django
pip3 install psycopg2
pip3 install django-allauth
```

#### 1. Download the project to your /var/www folder.

#### 2. Migrate database info:
Run:

```
$ python manage.py makemigrations
$ python manage.py migrate
```

#### 3. Collect static:
Run `python manage.py collectstatic`

#### 4. Create superuser:
Run `$ python manage.py createsuperuser`

#### 5. Obtain your Google credentials:

    1. Visit the Google Developers Console site and log in with your Google account.
    2. Create a new project.
    3. Go to Credentials → Create credentials → OAuth client ID. 
    4. Set OAuth consent screen to External.
    5. Add App information:

```
App name:
Support email: your-email
Developer contact information: your-email
```

    6. Save and continue.
    7. Set  it up:
    
```
Application type: Web application
Name: name-of-your-project
Authorized JavaScript origins → Add URI: http://127.0.0.1:8000
Authorized redirect URIs → Add URI: http://127.0.0.1:8000/google/login/callback/
```
	
	8. Copy your Client id and Secret key

#### 6. Add your social account credentials to your project:
    1. Run: `$ python manage.py runserver`
    2. Go to http://127.0.0.1:8000/admin and log in as superuser:
    3. Go to Sites → Site → Add site. Set it up:

```
Domain name: 127.0.0.1:8000
Display name: 127.0.0.1:8000
```

    3. Go to Social accounts → Social applications → Add social application. Set it up:
    
```
Provider: Google
Name: google-api
Client id: your-client-id
Secret id: your-secret-key
```
You can leave the "Key" field empty.

    4. Add 127.0.0.1:8000 to Chosen sites and save the new settings.

#### 7. Set up home/settings.py:
1. Make sure SITE_ID has the correct id of your site. You can obtain the proper id with a simple query to your database:
`SELECT * FROM django_site WHERE name = '127.0.0.1:8000'`.
2. Set up your PostgreSQL database connection configuration:
```
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'name-of-your-database',
        'OPTIONS': {
        'options': '-c search_path=django,name-of-your-schema',
        },
        'USER': 'name-of-your-user',
        'PASSWORD': 'password-of-your-user',
        'HOST': 'name-of-your-host',
        'PORT':'your-database-connection-port',
    }
}
```

#### 8. Setup your database
    Populate the forms_enrolledstudent table with the enrolled students info.

### 9. Start Django server
Run:
`python3 manage.py startserver`

---

## B) Run from your own domain
#### Requirements
```
sudo apt install apache2 apache2-dev
sudo apt-get install libapache2-mod-wsgi-py3
sudo apt-get install python3	
sudo apt install python3-pip
pip3 install virtualenv
```

#### 1. Download the project to your /var/www folder.
1. Go to /var/www/school-form
2. Create a virtual environment: `virtualenv school-project-env`
3. Activate the new environment: `source school-project-env/bin/activate`
4. Install:

```
pip3 install django
pip3 install django-allauth
pip3 install psycopg2
```

#### 2. Migrate database info:
Run:

```
$ python manage.py makemigrations
$ python manage.py migrate
```

#### 3. Collect static:
Run `python manage.py collectstatic`

#### 4. Create superuser:
Run `$ python manage.py createsuperuser`

#### 5. Obtain your Google credentials:

    1. Visit the Google Developers Console site and log in with your Google account.
    2. Create a new project.
    3. Go to Credentials → Create credentials → OAuth client ID. 
    4. Set OAuth consent screen to External.
    5. Add App information:

```
App name:
Support email: your-email
Developer contact information: your-email
```

    6. Save and continue.
    7. Set  it up (change http:// with https:// when applicable):
    
```
Application type: Web application
Name: name-of-your-project
Authorized JavaScript origins → Add URI: http://your-domain.com
Authorized redirect URIs → Add URI: http://your-domain.com/google/login/callback/
```
	
	8. Copy your Client id and Secret key

#### 6. Add your social account credentials to your project:
    1. Run: `$ python manage.py runserver`
    2. Go to http://your-domain.com/admin and log in as superuser
    3. Go to Sites → Site → Add site. Set it up:

```
Domain name: your-domain.com
Display name: your-domain.com
```

    3. Go to Social accounts → Social applications → Add social application. Set it up:
    
```
Provider: Google
Name: google-api
Client id: your-client-id
Secret id: your-secret-key
```
You can leave the "Key" field empty.

    4. Add your domain to Chosen sites and save the new settings.

#### 7. Set up home/wsgi.py

```
import os
import sys

from django.core.wsgi import get_wsgi_application

sys.path.append('/var/www/school-project')
sys.path.append('/var/www/school-project/home')

# Replace the Python version in the line below as needed 
sys.path.append('/var/www/school-project/school-project-env/lib/python3.8/site-packages') 
 
os.environ.setdefault('DJANGO_SETTINGS_MODULE', "home.settings") 

try: 
    application = get_wsgi_application() 
except Exception: 
    # Error loading applications 
    if 'mod_wsgi' in sys.modules: 
        traceback.print_exc() 
        os.kill(os.getpid(), signal.SIGINT) 
        time.sleep(2.5)
```


#### 8. Set up home/settings.py:
1. In case you're hosting the application from your domain, add it to the list of ALLOWED_HOSTS like: `ALLOWED_HOSTS = ['mydomain.com']`; separate them with commas if there's more than one. Adding a dot like in '.mydomain.com' will work as a wildcard to include multiple subdomains.
2. Set up your PostgreSQL database connection configuration:
```
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'name-of-your-database',
        'OPTIONS': {
        'options': '-c search_path=django,name-of-your-schema',
        },
        'USER': 'name-of-your-user',
        'PASSWORD': 'password-of-your-user',
        'HOST': 'name-of-your-host',
        'PORT':'your-database-connection-port',
    }
}
```
3. Make sure SITE_ID has the correct id of your site. You can obtain the proper id with a simple query to your database:
`SELECT * FROM django_site WHERE name = 'your-domain.com'`.

#### 9. Setup your database
    Populate the forms_enrolledstudent table with the enrolled students info.

#### 10. Setup your Apache server
    1. Create your VirtualHost configuration file at /etc/apache2/sites-available and save it as school-form.conf:
    
```
<VirtualHost *:80>
	ServerName your-domain.com
	ServerAlias www.your-domain.com

	ServerAdmin admin@your-domain.com
	DocumentRoot /var/www/school-form

	ErrorLog /var/www/school-form/log/error.log
	CustomLog /var/www/school-form/log/access.log combined

	LoadModule wsgi_module /usr/lib/apache2/modules/mod_wsgi.so

	# WSGI configuration
	WSGIScriptAlias / /var/www/school-form/home/wsgi.py 

	# Adjust the following line to match your Python path 
	WSGIDaemonProcess your-domain.com threads=15 python-path=/var/www/school-project/school-project-env python-path=/var/www/school-form
	WSGIProcessGroup your-domain.com

	<Directory /var/www/school-form/home> 
		#Order deny,allow
		#Allow from all
		#AllowOverride all 
		Require all granted 
		#Options FollowSymlinks
	</Directory> 

	<Directory /var/www/school-form/home> 
		<Files wsgi.py>
			Require all granted
		</Files>
	</Directory> 
 
	Alias /static/ /var/www/school-form/static/
 
	<Directory /var/www/school-form/static> 
 		Require all granted 
	</Directory>

</VirtualHost>
```

    2. To enable your configuration file, run: `sudo a2ensite school-form.conf`.
    3. Restart the server: `sudo systemctl restart apache2`
    