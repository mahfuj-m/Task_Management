### Task_Management
##### This is a simple task management api developed using Python Flask web framework

## Table of Contents
- ###### Installation Process
- ###### Initiation
- ###### About the App
- ###### Methodology
- ###### Data Stoing
- ###### Test
- ###### Technology

##### To set up the project locally, follow these steps
 1. Clone the repository
 2. Navigate the project folder, `cd Task_Management`
 3. Create a vritual environment [Instructions] (https://www.geeksforgeeks.org/create-virtual-environment-using-venv-python/)
 4. Install the requirements from `requirements.txt` file.

##### Initiation of the REST API
  1. Run the main.py file
      `python main.py --file data.json --save True` ...
     `--file` and `--save` arguments are dedicated for storing and retriving the data and they are optional as well.

  <br>
  Now you have successfully intiated the api and ready for calling its services.
  <br>
  ##### About the api
  This api implements a simple task management. By this api you can create, update and delete a task. This api ensures that no XSS has been injected which is a major security threat in api development. <br>
  Currently: Task attributes are Task name and description and a new ID is alloted everytime for each new task. 

  #### Methodology
  After intiating the api, `curl` and `postman` was used to test the api.
  Task properties was inserted using the `postman` and simultaneously 'GET' and 'DELETE' requests was checked using `curl`.
  <br>
  ###### API calls
  1. GET requests: `http://localhost:port/tasks/` this will display all the tasks.
  2. 'POST' requests: `http://localhost:port/addtask/` and data was passed from the POSTMAN app using the `Body option`.
  3. 'PUT', 'DELETE', 'GET' requests: `http://localhost:port/task/<int:id>` this ensure to retrieve single task to delete, update, or view

  ##### Data Storing
  This api uses the local memory to store the data in JSON format. Before closing the server, the api saves the data everytime and after intiating the server it loads the previous data even though its optional.

  ##### Test
  I conducted manual testing and trying different edge scenarios , few examples are listed under the `test_cases.json` file. 

  ###### Technology
  Microservice: Flask
  Language: Python
  API Architecture: REST API
     


