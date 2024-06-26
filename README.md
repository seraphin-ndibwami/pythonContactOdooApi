# test odoo api

## Description
This Python script connects to an Odoo instance via the RESTful API and sends data along with files to a specific endpoint. The script consists of two main functions: connect_to_odoo_api for authentication and send_data_with_files for sending data and files.

## Prerequisites
- Python 3.x
- requests library installed (pip install requests)
- json library installed

## Script Structure
1. **Function connect_to_odoo_api**
This function authenticates with the Odoo API and obtains a session_id for future requests.
2. **Function send_data_with_files**
This function sends data and files to a specific Odoo API endpoint.

3. **Main Section**
The main section of the script executes the functions defined above. It performs the following actions:

```
- Prompts the user to enter their username and password.
- Authenticates with the Odoo API to obtain a session_id.
- Sends data and a file to a specific API endpoint.
```

## Conclusion
This script provides a simple method for authenticating and sending data, including files, to an Odoo instance via the RESTful API. The two main functions, connect_to_odoo_api and send_data_with_files, encapsulate the necessary steps to accomplish these tasks, offering a reusable and modular solution.