# telegram

## Setup
* ##### Dependencies
    * [Python 2.7](https://www.python.org/download/releases/2.7/)
    * [MongoDB] port and host will need to configured in config.json
    * *virtualenv* - `pip install virtualenv`
    
* ##### Setup
    * `git clone https://github.com/dabba-app/telegram`
    * `add a config.json file in root of project, or ping me to get it`
    * `cd telegram`
    * `virtualenv venv`
    * `source venv/bin/activate`
    * `sudo pip install -r requirements.txt`
    * `run mongo however u want, on the host and port as per the config.json` 
    * `exit`
* ##### One time setup
    * `cd ./api/init`
    * `python -c "from telegram_api import telegram as t; p=t(); p.poll()"`
    * `now give command /start to the bot from ur telegram messenger, ask all other users who would want to receive message from this bot to use the /start command while this script is running. This basically populates the telegram db with releveant chat ids which help in sending messages.`
    * `once all users are done with the /start, terminate the script`
 
 * ##### Finally to run the app:
    * `python app.py`

## API Documentation

##### **Note that trailing slash in every endpoint is mandatory**

#### 1. /sendasync/ [POST]

* `POST /sendasync/` allows to send msg:
    ```
    { 
        "USER": "piyush9620",
        "MSG":"1234"
    }
    
* ##### config.json:

{

  "TELEGRAM_KEY": "xyz",
  
  "DB_HOST": "0.0.0.0",
  
  "DB_PORT": "27017",
  
  "HOST": "0.0.0.0",
  
  "PORT": "8000"
  
}


