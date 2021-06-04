## Installing Django
Python and pip should be installed
```
pip install django
django-admin --version
```
![1](https://user-images.githubusercontent.com/64186894/120802798-78412680-c560-11eb-85c2-457b9a235940.jpg)

### Creating Project and migrate to create tables in the database 
```
django-admin startproject myproject
python manage.py migrate
```
![2](https://user-images.githubusercontent.com/64186894/120802802-79725380-c560-11eb-9dca-6dc55ee85c03.jpg)

### Creating administrative user and running server
```
python manage.py createsuperuser
python mange.py runserver 0.0.0.0:8000
```
![3](https://user-images.githubusercontent.com/64186894/120802784-737c7280-c560-11eb-9d82-d95f52c45a5a.jpg)

![4](https://user-images.githubusercontent.com/64186894/120802789-75decc80-c560-11eb-8d37-621317a5d77b.jpg)

### localhost:8000/admin/
![5](https://user-images.githubusercontent.com/64186894/120802794-770ff980-c560-11eb-914b-fa8f1106a7c6.jpg)

