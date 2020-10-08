#######################
##   AifedayoScrumy  ##
#######################

AifedayoScrumy is a simple django chat application using aws api and websockets

Detailed documentation is in the "doc" directory

Quick Start
-----------

1. Add "Aifedayoscrumy" to your INSTALLED_APPS settings like this::
	
	INSTALLED_APPS = [
		...
		'aifedayoscrumy',
	]

2. Include the scrumy URLconf in your project urls.py like this:
	path('aifedayoscrumy/', include('aifedayoscrumy.urls')),

3. Run 'python manage.py migrate to create the scrumy models

4. Start the dev server and visit http://127.0.0.1:8000/admin to create a scrumy 