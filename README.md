#Trafikboxen

###What?
Trafikboxen is a realtime display for your public transportation departures.

###Development Workflow
####Cloning and setup
1. Clone the repository `git clone https://github.com/ReyMichaelFichter/trafikboxen.git`
2. Install python 3.8
3. Create a virtual environment with `python3.8 -m venv .venv`
4. Install development requirements by running `make install`. You need to have make installed for this to work.
5. Get an API key for [ResRobot Stolptidtabeller 2 - Avgående Trafik](https://www.trafiklab.se/api/resrobot-stolptidtabeller-2) and set as an environment variable with `export RESROBOT_API_KEY=<YOUR_API_KEY>`
6. Get an API key for [SL Platsuppslag](https://www.trafiklab.se/api/sl-platsuppslag) and set as an environment variable with `export PLATSUPPSLAG_API_KEY=<YOUR_API_KEY>`

####Running the tests
The test suite is executed by running `make test`.

####Running the app
The app is started with `make run-app`
