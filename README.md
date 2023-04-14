## <a href="https://github.com/tmsnn/Journey_Journal"><img src="https://readme-typing-svg.demolab.com?font=Josefin+Sans&size=40&duration=3000&pause=500&color=360672&background=263F6800&center=true&vCenter=true&repeat=true&width=550&lines=Web+Project+-+Journey+Journal;" alt="..." /></a>


## Frontend:
TypeScript, HTML, CSS, Framework Angular 

## Backend: 
Python, Framework Django 

##Getting Started
To run this application locally, you'll need to have Python 3 and Node.js installed on your machine. You can download Python 3 from the official website (https://www.python.org/downloads/) and Node.js from the official website (https://nodejs.org/en/download/).

## Backend: 
To get the backend up and running, follow these steps:

    Clone the repository and navigate to the backend directory.
    Create a new Python virtual environment using the command python3 -m venv env.
    Activate the virtual environment using the command source env/bin/activate.
    Install the required Python packages using the command pip install -r requirements.txt.
    Create a new PostgreSQL database and add the database details to the DATABASES setting in the settings.py file.
    Run the Django migrations using the command python manage.py migrate.
    Create a new superuser account using the command python manage.py createsuperuser.
    Start the Django development server using the command python manage.py runserver.
    
## Frontend:
   To get the frontend up and running, follow these steps:
   
    Clone the repository and navigate to the frontend directory.
    Install the required Node.js packages using the command npm install.
    Start the Angular development server using the command ng serve.
    
## Usage:
Once both the backend and frontend are up and running, you can access the web application by navigating to http://localhost:4200 in your web browser.

The application provides the following functionality:

    Browse vouchers by category.
    View details of a specific voucher.
    Add vouchers to the shopping cart.
    Checkout and purchase vouchers.
    View purchase history.
    Add comments to vouchers.
    
## API Endpoints:
The application provides the following API endpoints:

    /vouchers/ - List all vouchers or create a new voucher.
    /vouchers/:id/ - Retrieve, update or delete a specific voucher.
    categories/ - List all categories or create a new category.
    /categories/:id/ - Retrieve, update or delete a specific category.
    /comments/ - List all comments or create a new comment.
    /comments/:id/ - Retrieve, update or delete a specific comment.
    /api/auth/token/ - Obtain an authentication token.
    /api/auth/token/refresh/ - Refresh an authentication token.
    
## Contributing:
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.


## Group members:
| Surname       | Name          | Github                                            |
| :-----------: |:-------------:| :-------------:                                   |
| Akhtanov      | Amir          | [Click Here](https://github.com/AdonisVernaliss)  |
| Ten           | Olga          | [Click Here](https://github.com/21BTen)           |
| Nyshanbek     | Tomiris       | [Click Here](https://github.com//tmsnn)           |
