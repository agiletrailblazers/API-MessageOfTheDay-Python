# API-MessageOfTheDay-Python
Message of the Day API Written in Python

This project was built using the Django REST Framework (http://www.django-rest-framework.org/)
Django includes security tools that can be utilized in the future.

## Installation
Prerequisites:
* python 2.7.x (can be installed through brew on OSX)
* pip (https://pip.pypa.io/en/stable/installing/)

Run the following commands
```
$> pip install django
$> pip install djangorestframework
```

## Running the API
```
$> python manage.py runserver
```

## Testing the API

### Unit Testing
Run the following command to run the suite of unit tests
```
$> python manage.py test
```

For more information on unit testing in Python and Django, see https://docs.djangoproject.com/en/1.11/topics/testing/

### Using the Postman Client
1. Download and install the Postman client
2. Import the test collection from this file
    * {your-dev-dir}/API-MessageOfTheDay/src/test/postman/API-MessageOfTheDay.postman_collection
3. Import the supported environments from these files
    * {your-dev-dir}/API-MessageOfTheDay/src/test/postman/API-MessageOfTheDay.local.postman_environment
4. Select the appropriate environment and execute the collection of tests

### Using Newman from the command-line.
1. Install Newman using the Node Package Manager (npm)
    * To install newman (for use with Node 4.0+)
`npm install -g newman@beta`
    * To install newman (for use with older versions of Node)
`npm install -g newman`
2. Execute the Postman collection of tests by running the following command
`newman -c apiMOTD/postman/API-MessageOfTheDay.postman_collection  -e apiMOTD/postman/API-MessageOfTheDay.local.postman_environment`
