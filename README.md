# Environment Setup

## Clone the Project
`git clone git@github.com:hussain-alhassan/insurance.git && cd insurance`
## Create a Virtual Environment
* Run `virtualenv venv -p python3` (to create a virtual environment with python3 virsion)
* Activate the virtual environment `source venv/bin/activate`
* Install the project's requirements `pip install -r src/requirements.txt`


# Running the project
* Move to the src directory `cd src`
* Migrate the database `python manage.py migrate`
* Create an admin user`python manage.py createsuperuser`
* Run the server `python manage.py runserver`
