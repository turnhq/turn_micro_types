# Turn´s Alerts Microservice

Client library to create alerts for turn's alerts microservice
github: https://github.com/turnhq/alerts_micro/
heroku: https://dashboard.heroku.com/pipelines/19e4ce68-cec8-48d2-9bc7-be84588e7bd5

## Installing

This package can be installed into other projects using pip with the following command:

`pip install git+https://github.com/turnhq/turn-alerts-client`

Sometimes it may be necessary to specify the exact commit which you wish to install. This can be achieved by adding the commit hash to the end of the url like so:

`pip install git+https://github.com/turnhq/turn-alerts-client@c94755da3c6d56b639d02a5aab03ccb2476c88e4`

## Instructions

When making updates to this library, be sure to update the version number in _settings.py_.

## Initiating client

All this client needs in order to be initiate is the API token and the host for the Alerts Micro app that you wish to connect to.

A

```
token = os.environ.get("TOKEN")
host = os.environ.get("HOST")
alert = AlertAPI(token=token, host=host)
```
