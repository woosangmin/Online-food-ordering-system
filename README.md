
# Online Food Ordering System 

A web-based application for restaurant owners to receive orders from customers.

    
## Run Locally

Clone the project

```bash
  git clone https://github.com/harshit-wadhwani/Online-food-ordering-system.git
```

Go to the project directory

```bash
  cd Online-food-ordering-system
```

create a mysql database named 'the_lounge', 'the_order_lounge' and grant your user read/write permission.
Give your password to your user and hosting address in the control_db.py file 
```
db = mysql.connector.connect(
    host='localhost',
    user='root',
    password='',
    database="onlinerest"
)

```
Install dependencies by using the following code 

```
pip install -r requirements.txt
```
[python version 3.8 Recommended / use conda venv]

Start the server

```bash
  streamlit run main.py
```

Additional details need to be added to this README.md file.
    - how to install conda venv and create DB user, etc

The login feature also needs to be added to this repository.
