# Trade App
setup required for django Trade app

asgiref==3.5.2
beautifulsoup4==4.11.1
certifi==2022.9.14
charset-normalizer==2.1.1
configparser==5.3.0
Django==4.1.1
django-bootstrap4==22.2
django-cors-headers==3.13.0
django-crispy-forms==1.14.0
django-filter==22.1
djangorestframework==3.13.1
djangorestframework-simplejwt==5.2.0
djongo==1.3.6
dnspython==2.2.1
ez-setup==0.9
idna==3.4
PyJWT==2.4.0
pymongo==3.12.3
PyMySQL==1.0.2
pytz==2022.2.1
requests==2.28.1
soupsieve==2.3.2.post1
sqlparse==0.2.4
urllib3==1.26.12


#Trade app

Brief:
*Django MVT
It is a Trade app in django framework,Django template,crispy forms,bootstrap,javascript

 View Order:
1. View all the records of Trade's order 
2. filter order of record using select and global search input form record
3. Used DRF GET api to fetch data from database.

Add order:
1.user can add new order
2.Used DRF post API to push data.

Add signup :
1.Used auth user model for User signup .

SignIn:
1.Used auth user model for User signup .







●Technology used:
*Backend:
1. Django framework
2. Mongodb:-djongo framework for connect Django ORM with MONGODB localhost
3. Django library: messages,mixins,decorators,forms,generic,auth,User_model, Usercreation
*Frontend
1. Django Template
2. Bootstrap 5.2 CDN
3. Crispy Forms

●API
*Django REST framework
1. View all the records of order 
3. Update an entry of a order
4. Delete a order
5. Get all order
6. Get detail of a order
7. Django REST library:- serializers,Response,generics,status.ModelSerializer,User





