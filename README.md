# Teaching-Stats
App that offers a form about high school's services, counseling and enrolled subjects to be answered by the students. Students log in through their Google account. Responses are recorded in a PostgreSQL database, where all the master data is stored. The application prevents responses from unauthorized students and duplicated submissions. Only the student's enrolled subjects are presented for their evaluation. The application provides access to statistical results powered by Metabase for authorized staff.

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
pip3 install django==4.0.1
pip3 install django-allauth==0.47.0
pip3 install psycopg2-binary==2.9.3
```

#### 1. Download the project to your /var/www folder.

#### 2. Set up your database connection:
1. Make sure you have a database created with PostgreSQL featuring 3 different schemas: "master", "public" and "reports".
2. At /home/settings.py set up your PostgreSQL database connection configuration:    

```
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'name-of-your-database',
        'OPTIONS': {
        'options': '-c search_path=django,public',
        },
        'USER': 'name-of-your-user',
        'PASSWORD': 'password-of-your-user',
        'HOST': 'name-of-your-host',
        'PORT':'your-database-connection-port',
        'CONN_MAX_AGE': 0,
    },
    'master': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'name-of-your-database',
        'OPTIONS': {
        'options': '-c search_path=django,master',
        },
        'USER': 'name-of-your-user',
        'PASSWORD': 'password-of-your-user',
        'HOST': 'name-of-your-host',
        'PORT':'your-database-connection-port',
        'CONN_MAX_AGE': 0,
    },
    'reports': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'name-of-your-database',
        'OPTIONS': {
        'options': '-c search_path=django,reports',
        },
        'USER': 'name-of-your-user',
        'PASSWORD': 'password-of-your-user',
        'HOST': 'name-of-your-host',
        'PORT':'your-database-connection-port',
        'CONN_MAX_AGE': 0,
    }
}
```

#### 3. Migrate database info:
Run:

```
$ python manage.py makemigrations
$ python manage.py migrate
```

#### 4. Set up database:
Run `python dbsetup.py`

#### 5. Collect static:
Run `python manage.py collectstatic`

#### 6. Create superuser:
Run `$ python manage.py createsuperuser`

#### 7. Obtain your Google credentials:

    1. Visit the Google Developers Console site and log in with your Google account.
    2. Create a new project.
    3. Go to Credentials → Create credentials → OAuth client ID. 
    4. Set OAuth consent screen to External.
    5. Add App information:

```
App name: school-form
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

#### 8. Add your social account credentials to your project:
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

#### 9. Set up /home/settings.py:
    1. Add your secret key. You can generate one running from your terminal the following instruction: `python -c 'from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())`.
    2. Add 127.0.0.1 between single quotes to the list of ALLOWED_HOSTS, e.g. `ALLOWED_HOSTS = ['127.0.0.1']`; separate them with commas if there's more than one. Adding a dot like in '.mydomain.com' will work as a wildcard to include multiple subdomains.
    3. Make sure SITE_ID has the correct id of your site. You can obtain the proper id with a simple query to your database: `SELECT * FROM django_site WHERE name = '127.0.0.1:8000'`.

#### 10. Populate the database
You can use the following repositories for that purpose:

- [https://github.com/Marcos-A/teaching-stats-db-population](https://github.com/Marcos-A/teaching-stats-db-population)
- [https://github.com/Marcos-A/teaching-stats-import-students](https://github.com/Marcos-A/teaching-stats-import-students)

#### 11. Add your Metabase shared dashboards
Make sure to add your shared links to the following files:
- /templates/analytics/adm_analytics.html
- /templates/analytics/counseling_analytics.html
- /templates/analytics/inf_analytics.html
- /templates/analytics/school_analytics.html
- /templates/analytics/subject_analytics.html

In case your site is delivered through HTTPS, make sure your Metabase server operates from a HTTPS address as well, otherwise the iFrames will be blocked.

#### 12. Start Django server
Run:
`python3 manage.py runserver`

#### 13. Access

- Access forms from:
http://127.0.0.1:8000
- Access analytics from:
http://127.0.0.1:8000/resultats

#### 14. Open/close surveys
Follow the instructions at /social_app/urls.py to open surveys during surveying season or closing them afterwards.

---

## B) Run from your own domain
#### Requirements
```
sudo apt install apache2 apache2-dev
sudo apt-get install python3
sudo apt-get install libapache2-mod-wsgi-py3
sudo apt install virtualenv
```

#### 1. Download the project to your /var/www folder.
1. Go to /var/www/enquestes
2. Create a virtual environment: `virtualenv enquestes-env`
3. Activate the new environment: `source enquestes-env/bin/activate`
4. Install:

```
pip install django==4.0.1
pip install django-allauth==0.47.0
pip install psycopg2-binary==2.9.3
```

#### 2. Set up your database connection:
1. Make sure you have a database created with PostgreSQL featuring 3 different schemas: "master", "public" and "reports".
2. At /home/settings.py set up your PostgreSQL database connection configuration:    

```
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'name-of-your-database',
        'OPTIONS': {
        'options': '-c search_path=django,public',
        },
        'USER': 'name-of-your-user',
        'PASSWORD': 'password-of-your-user',
        'HOST': 'name-of-your-host',
        'PORT':'your-database-connection-port',
        'CONN_MAX_AGE': 0,
    },
    'master': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'name-of-your-database',
        'OPTIONS': {
        'options': '-c search_path=django,master',
        },
        'USER': 'name-of-your-user',
        'PASSWORD': 'password-of-your-user',
        'HOST': 'name-of-your-host',
        'PORT':'your-database-connection-port',
        'CONN_MAX_AGE': 0,
    },
    'reports': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'name-of-your-database',
        'OPTIONS': {
        'options': '-c search_path=django,reports',
        },
        'USER': 'name-of-your-user',
        'PASSWORD': 'password-of-your-user',
        'HOST': 'name-of-your-host',
        'PORT':'your-database-connection-port',
        'CONN_MAX_AGE': 0,
    }
}
```

#### 3. Migrate database info:
Run:

```
$ python manage.py makemigrations
$ python manage.py migrate
```

#### 4. Set up database:
Run `$ python dbsetup.py`

#### 5. Collect static:
Run `$ python manage.py collectstatic`

#### 6. Create superuser:
Run `$ python manage.py createsuperuser`

#### 7. Obtain your Google credentials:

    1. Visit the Google Developers Console site and log in with your Google account.
    2. Create a new project.
    3. Go to Credentials → Create credentials → OAuth client ID. 
    4. Set OAuth consent screen to External.
    5. Add App information:

```
App name: school-form
Support email: your-email
Developer contact information: your-email
```

    6. Save and continue.
    7. Set  it up (change http:// with https:// when applicable):
    
```
Application type: Web application
Name: name-of-your-project
Authorized JavaScript origins → Add URI: http://127.0.0.1:8000
Authorized redirect URIs → Add URI: http://your-domain.com/google/login/callback/
```
	
    8. Copy your Client id and Secret key

#### 8. Add your social account credentials to your project:
    1. Run: `$ python manage.py runserver`
    2. Go to http://your-domain.com/admin and log in as superuser
    3. Go to Sites → Site → Add site. Set it up:

```
Domain name: your-domain.com
Display name: your-domain.com
```

    4. Go to Social accounts → Social applications → Add social application. Set it up:
    
```
Provider: Google
Name: google-api
Client id: your-client-id
Secret id: your-secret-key
```
You can leave the "Key" field empty.

    5. Add your domain to Chosen sites and save the new settings.

#### 9. Set up /home/wsgi.py

```
import os
import sys

sys.path.append('/var/www/enquestes')
sys.path.append('/var/www/enquestes/home')

# Replace the Python version in the line below as needed 
sys.path.append('/var/www/enquestes/enquestes-env/lib/python3.8/site-packages') 
 
os.environ.setdefault('DJANGO_SETTINGS_MODULE', "home.settings") 

from django.core.wsgi import get_wsgi_application

try: 
    application = get_wsgi_application() 
except Exception: 
    # Error loading applications 
    if 'mod_wsgi' in sys.modules: 
        traceback.print_exc() 
        os.kill(os.getpid(), signal.SIGINT) 
        time.sleep(2.5)
```


#### 10. Set up /home/settings.py:
    1. Add your secret key. You can generate one running from your terminal the following instruction: `python -c 'from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())`.
    2. Add your domain between single quotes to the list of ALLOWED_HOSTS, e.g. `ALLOWED_HOSTS = ['mydomain.com']`; separate them with commas if there's more than one. Adding a dot like in '.mydomain.com' will work as a wildcard to include multiple subdomains.
    3. Make sure SITE_ID has the correct id of your site. You can obtain the proper id with a simple query to your database: `SELECT * FROM django_site WHERE name = 'your-domain.com'`.
    
#### 11. Populate the database
You can use the following repositories for that purpose:

- [https://github.com/Marcos-A/teaching-stats-db-population](https://github.com/Marcos-A/teaching-stats-db-population)
- [https://github.com/Marcos-A/teaching-stats-import-students](https://github.com/Marcos-A/teaching-stats-import-students)

#### 12. Set up your Apache server
    1. Create your VirtualHost configuration file at /etc/apache2/sites-available and save it as enquestes.conf:
    
```
<VirtualHost *:80>
	ServerName your-domain.com
	ServerAlias www.your-domain.com

	ServerAdmin admin@your-domain.com
	DocumentRoot /var/www/enquestes

	ErrorLog /var/www/enquestes/log/error.log
	CustomLog /var/www/enquestes/log/access.log combined

	LoadModule wsgi_module /usr/lib/apache2/modules/mod_wsgi.so

	# WSGI configuration
	WSGIScriptAlias / /var/www/school-form/home/wsgi.py 

	# Adjust the following line to match your Python path 
	WSGIDaemonProcess your-domain.com threads=15 python-path=/var/www/enquestes/enquestes-env python-path=/var/www/enquestes
	WSGIProcessGroup your-domain.com
	WSGIApplicationGroup {%GLOBAL}

        WSGIScriptAlias / /var/www/enquestes/home/wsgi.py

	<Directory /var/www/enquestes/home> 
		Require all granted 
	</Directory> 

	<Directory /var/www/enquestes/home> 
		<Files wsgi.py>
			Require all granted
		</Files>
	</Directory> 
 
	Alias /static/ /var/www/enquestes/static/
 
	<Directory /var/www/enquestes/static> 
 		Require all granted 
	</Directory>

</VirtualHost>
```

   2. To enable your configuration file, run: `sudo a2ensite school-form.conf`.
   3. Make sure you assign the correct permissions:
    
```
sudo chown -R YOUR-USER:www-data /var/www/enquestes
sudo chmod -R 775 /var/www/enquestes
```
    
   4. Restart the server: `sudo systemctl restart apache2`
    
#### 13. Add your Metabase shared dashboards
Make sure to add your shared links to the following files:
- /templates/analytics/adm_analytics.html
- /templates/analytics/counseling_analytics.html
- /templates/analytics/inf_analytics.html
- /templates/analytics/school_analytics.html
- /templates/analytics/subject_analytics.html

In case your site is delivered through HTTPS and your Metabase server operates from a different address, make sure this is a HTTPS address as well, otherwise the iFrames will be blocked.

#### 14. Access

- Access forms from:
http://YOUR-DOMAIN or https://YOUR-DOMAIN if your site has a valid certificate
- Access analytics from:
http://YOUR-DOMAIN/resultats or https://YOUR-DOMAIN/resultats if your site has a valid certificate

#### 15. Open/close surveys
Follow the instructions at /social_app/urls.py to open surveys during surveying season or closing them afterwards.
