## Flask Server

This flask server will serve a socket via socket.io on `localhost:5000` to notify it's clients about incoming alarms.

### Starting the server

In this directory, simply run `env FLASK_APP=server.py flask run` to start a development server

### Sending test data

Making a GET-Request to `localhost:5000/test` will send some example data to the socket

### Viewing the data

`localhost:5000` itself will log all data sent to the socket into the browser console
