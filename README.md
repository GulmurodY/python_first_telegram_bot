# GMK bot
This Bot is created in order to provide information about some of Mortal Kombat characters.
This bot give some basic info about the caracter we want and also gives us a link to its page where we can find a lot more.

## Installing
In order to use this bot we need to instlall some modules.

*Telegram bot module* - in order to install it you should run following command in your terminal
```
$ pip install python-telegram-bot
```
## Running
1.Download the source code from the repository.

2.Find the bot @g_MK_bot

3.Run the code using command 
```
python3 main.py
```
## Imports
1.*Updater*: This will contain the API key we got from BotFather to specify in which bot we are adding functionalities to using our python code.

2.*Update*: This will invoke every time a bot receives an update i.e. message or command and will send the user a message.

3.*CallbackContext*: We will not use its functionality directly in our code but when we will be adding the dispatcher it is required (and it will work internally)

4.*CommandHandler*: This Handler class is used to handle any command sent by the user to the bot, a command always starts with “/” i.e “/start”,”/help” etc.

5.*MessageHandler*: This Handler class is used to handle any normal message sent by the user to the bot,

6.*FIlters*: This will filter normal text, commands, images, etc from a sent message.

## Description
This bot was created using python-telgram-bot module. We have to .py file in one we define output functions for each character, 
and in the other file we have defined start output, help output, and error output functions. In adddtion we implemented command 
handlers in main file.
