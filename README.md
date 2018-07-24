# slack-THD-Linker
##### version 1.0.2
This is a slack app built for the Luther Technology Help Desk in order to increase productivity and ease of use when discussing internal matters.

## Getting Started

Offline development of features is possible, though using the Slack API is limited to an online deployment.

The exception to the rule is the use of a Slack Legacy Token, which can be generated for specific users in specific workspaces. This replaces the Application token generated, and has elevated permissions (not requiring the use of scopes). With little effort and a reference to the Slack API, you can build many one-time use tools for a slack channel; many of which will be easier to write, implement, and discard of safely. The only reason to not use a legacy token is if the process you wish to implement needs to run without supervision. 

### Prerequisites

This project is written in Python 3.x. 

### Installing

This project has a few packages installed. To follow best practices, the first step should be to install a virtual environment in python. Navigate to the working directory where you have these project files, and run the following commands:

```
python3 -m venv .
. bin/activate
```

If you're using Windows, you might not have to specify using Python 3.x. In that case, run the following commands:
```
python -m venv .
Scripts\activate.bat
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

* Invoking the /ticket command in any slack chat window will automatically link the ticket number in the message to help.luther.edu. In the examples below, the ticket should be formatted as just the ticket number without the \# symbol, like so:
```
/ticket 12345
/ticket text 12345 more text
```
This will return a link that looks like this: *help.luther.edu/adminui?ticket=12345*

Currently, the ticket number must be enclosed in spaces, otherwise the link will be formatted incorrectly. As an example,
```
/ticket here are some words12345more words
```
will spit out the following url: *help.luther.edu/adminui?ticket=words12345more*

This issue is planned to be fixed at a later time.

## Deployment
Deploying a slack app requires the use of external hosting. While the specific functions can often be tested outside of the Slack API, actual interactions require a live version to be running.

In order to create your own slack app, you do need to provide your own hosting, such as on [Heroku](www.heroku.com) or [Python Anywhere](www.pythonanywhere.com). This requires a free account to route the commands. The code provided here should work with little adjustment or setup, but the setup will vary depending on where you deploy the code.

With slack in particular, it is important to maintain a separate authentication url to redirect to the specific oauth page for the slack app from the callback url. The callback url should be the first time in the program the slack API should be used, and requires the CLIENT_SECRET and CLIENT_ID keys generated for your app as confirmation.

It bears stressing that maintaining as high a level of obfuscation with the tokens and keys used is extremely important. If you do upload a version of this code to a public repository, take care to remove any reference to the keys that might have been accidentally hardcoded in while developing.

## Built With

* [Flask](http://flask.pocoo.org/) - The microframework used
* [dotenv](https://github.com/theskumar/python-dotenv) - Obfuscation 
* [slackclient](https://github.com/slackapi/python-slackclient) - HTTP Python Wrapper for Slack API

## Versioning

I use [SemVer](http://semver.org/) for versioning. 

## Authors

* **Gavin Lochtefeld** - *Initial work* - [lochga01](https://www.github.com/lochga01)

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details.

## Acknowledgments

* Special thanks to my managers for letting me work on this FOSS project instead of paying attention to tickets.
