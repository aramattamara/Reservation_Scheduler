# Reservation_Scheduler
### https://docs.google.com/document/d/1g5WMLwezVuGCNnZBafREobcDDst8PgxElGPHfk7EgRI/edit


## <a name="installation"></a>Installation Instructions
Reservation_Schedular has not yet been deployed, to run the app locally on your machine follow these instructions:

* Clone the repository:
```sh
git clone https://github.com/aramattamara/Reservation_Scheduler.git
```

* Create and activate a virtual environment inside your project directory:

```sh
$ virtualenv env 
$ echo env >> .gitignore
$ source env/bin/activate
```

* Install dependencies:
```sh
(env)$  pip install -r requirements.txt
```

* Create a new postgreSQL database:
```sh
$ createdb reservation
```

* Seed the database:
```sh
$ python3 seed_database.py
```

* Run the app from tha command line:
```sh
$ python3 server.py
```

* In your web browser navigate to:
```sh
http://localhost:5000/
```
