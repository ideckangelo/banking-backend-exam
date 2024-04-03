# Banking Backend Exam

This is a rough banking application development for a backend exam, using Django REST API.

**Development details:**

1. This uses Django (Python) as the backend framework for this project.
2. OS used for development: WSL2

# Local Setup

1. Setup your local environment
   - clone this repository
   - setup your virtual environment
     - prerequisite: Python installation
     - setup your virtual env (e.g. `python3 -m venv <name>`)
     - run your virtual env `source <name>/bin/activate`
   - install the dependencies
     - dependencies are listed on `requirements.txt`
     - use `pip install requirements.txt`
2. Initialize the application
   - preferred prerequisite: `make` command installation
   - refer to the `Makefile` for the commands
   - initialize using the `make initialize-app` command
   - you may follow on the other make commands, if needed
   - follow the logs for the development server (e.g. `http://127.0.0.1:8000/`)

# Discussion

1. Account Creation
   - follow the development server with URL `accounts/`
   - API UI requires inputs: `customer id`, `name`, `email`, and `phone number`
2. Account List & Query
   - follow the development server with URL `accounts/`
     - this will return a list of accounts and their details
     - this will also display a UI for account creation
   - follow the development server with URL `accounts/{pk}`
     - where `{pk}` is the account_id of the account you are querying
     - this will return the details of the account
     - this will also display a UI for account updating
   - follow the development server with URL `find-account-by-customer/{id}`
     - where `{id}` is the customer_id of the account you are querying
     - this will return the details of the account
3. Transaction Creation
   - follow the development server with URL `transactions/`
   - API UI requires inputs: `account id`, `amount`, and `transaction type`
4. Transaction List & Query
   - follow the development server with URL `transactions/`
     - this will return a list of transactions and their details
     - this will also display a UI for account creation
   - follow the development server with URL `transactions/{pk}`
     - where `{pk}` is the transaction_id of the transaction you are querying
     - this will return the details of the transaction
     - this will also display a UI for transaction updating, however this method is not allowed
5. Account Statement Query
   - follow the development server with URL `statements/{pk}`
     - where `{pk}` is the account_id of the account you are querying a statement for
     - this will return the details of the account, as well as all the transactions under it

# For Improvement

1. Implement typing and lint in the `.py` or django files
2. Use `postgreSQL` as the database instead of `SQLite`
3. Implement `TODO:` comments
