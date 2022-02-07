# django-calander-app
    - Calander app is an app that retrieves SA holidays from https://holidayapi.com/.
    - The app uses the views module to pull data from holidaysapi, the data gets processed and only relevant data gets stored on sqlite db and rendered.
    - The modules module is responsible for creating a schema and specifications of the table fields, It is used by the views module to store data into the relevant table. - - The urls module is the entry point and it utilizes the views module for serving the webpage with data rendered by the views module
    
## To run the app you need:
    1. Docker and docker-composed installed in you machine
    2. Internet Access
    
## How to run the app :
    0. Clone the app (git clone https://github.com/thumavu/django-calander-app.git | gh repo clone thumavu/django-calander-app)
    1. docker-compose build
    2. docker-compose up
    3. docker ps -a (Confirm the container that contains the application is started and running)
    ![image](https://user-images.githubusercontent.com/16895199/149706571-a27dece5-8427-4ba8-b664-a82e89514ef6.png)
    4. Follow the link : http://localhost:8000/ 
    ![image](https://user-images.githubusercontent.com/16895199/149706727-b5ce0bd9-5bd8-4768-bc8e-8799edebface.png)
