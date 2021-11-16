# Blog!!!

### 16th Nov. 2021

## Author

[Derrick Macharia](https://github.com/derrickmacharia)

# Description
This is a Python Application where a user(s) can post a blog and also allows other users who have signed up to like and dislike.User is authorised to delete their blog and comments.


## Live Link


## Screenshots

## Screenshot 1
<img src="">

## Screenshot 2
<img src="">

## Screenshot 3
<img src="">

## Screenshot 4
<img src="">

## User Story
  A user can;
* Register to be allowed to log in to the application
* Comment on different blogs posted by other users.
* View the blogs posted by other users.
* Delete created blogs and comments
* View blogs of different categories.
* Submit a blog to a specific category of their choice.


## BDD
| Behaviour | Input | Output |
| :---------------- | :---------------: | ------------------: |
| Load the page | *On page load* | Get all latest blogs, Select between signup and login on the right side|
| Select SignUp| *Email,Username,Password* | Redirect to login|
| Select Login | *Username* and *password* | Redirect to page with app blogs based on categories and commenting section|
| Select comment button | *Comment* | Form that you input your comment|
| Click on submit |  | Redirect to all comments tamplate with your comment and other comments|





## Development Installation
To get the code..

1. Cloning the repository:
  bash
  https://github.com/derrickmacharia/blogs.git
  
2. cd to the folder and install requirements
  bash
  cd Pitches
  pip install -r requirements.txt
  
3. Exporting Configurations
  bash
  export SQLALCHEMY_DATABASE_URI=postgresql+psycopg2://{User Name}:{password}@localhost/{database name}
  
4. Running the application
  bash
  ./start.sh
  
5. Testing the application
  bash
  python3.8 manage.py test
  
Open the application on your browser `127.0.0.1:5000`.


## Technology used

* [Python3.8](https://www.python.org/)
* [Flask==0.12.2](http://flask.pocoo.org/)
* [Heroku](https://heroku.com)


## Known Bugs
* There are no bugs yet.


## Support and contact details
For more information,comments or clarification contact on derrick.macharia@student.moringaschool.com

