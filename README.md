# django-calander-app
    - Calander app is an app that retrieves SA holidays from https://holidayapi.com/ and nicely displays all the holidays in a web page.
    
    ## API KEY?
        - The "API KEY" is essentially stored as an environmental variable passed in by the .env file, the app uses dotenv to retrieve the var.
        - For security reseons the .env file is excluded whenever a commit is done, since it may contain sensitive information like passwords, api keys etc..  
    
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
