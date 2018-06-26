# slack-THD-Linker
##### version 1.0.0
This is a slack app built for the Luther Technology Help Desk in order to increase productivity and ease of use when discussing internal matters.

## Getting Started

Offline development of features is possible, though using the Slack API is limited to an online deployment. 

### Prerequisites

This project is written in Python 3.x. 

### Installing

This project has a few packages installed. To follow best practices, the first step should be to install a virtual environment in python. Navigate to the working directory where you have these project files, and run the following commands:

```
$python3 -m venv .
$. bin/activate
```

If you're using Windows, you might not have to specify using Python 3.x. In that case, run the following commands:
```
>python -m venv .
>Scripts\activate.bin
```

You can read the official documentation for Venv in [the official Python Docs](https://docs.python.org/3/library/venv.html).

At this point, the virtual environment should be activated. Here, you can install the packages located in requirements.txt:
```
pip install -r requirements.txt
```
From here, all of the packages should be installed and development can continue. Depending where you deploy the package, you may find that more commands may need to be ran. For example, on Python Anywhere, packages must be installed with
```
pip install --user -r requirements.txt
```

## Features 
```
/[COMMAND] help
```
Will return a small explanation of what the command does.

* Invoking the /ticket command in any slack chat window will automatically link the ticket number in the message to help.luther.edu. In the examples below, the \[TICKET NUMBER\] should be formatted as just :
```
/ticket [TICKET NUMBER]
/ticket text [TICKET NUMBER] more text
```
Currently, not enclosing the ticket number in spaces 
## Deployment
Deploying a slack app requires the use of a 

In order to create your own slack app, you do need to provide your own hosting, such as on [Heroku](www.heroku.com) or [Python Anywhere](www.pythonanywhere.com). This requires a free account to route the commands. The code provided here should work with little adjustment or setup, but the setup will vary depending on where you deploy the code.

## Built With

* [Flask](http://flask.pocoo.org/) - The microframework used
* [dotenv](https://github.com/theskumar/python-dotenv) - Obfuscation 
* [slackclient](https://github.com/slackapi/python-slackclient) - HTTP Python Wrapper for Slack API

## Versioning

I use [SemVer](http://semver.org/) for versioning. For the versions available, see the [tags on this repository](https://github.com/your/project/tags). 

## Authors

* **Gavin Lochtefeld** - *Initial work* - dsfsdfsdf[lochga01](https://www.github.com/lochga01)

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details.

## Acknowledgments

* Special thanks to my managers for letting me work on this FOSS project instead of paying attention to tickets.
