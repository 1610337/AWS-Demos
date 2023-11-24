## About this repository:
This repository contains a basic node.js webserver with routes for authenticated and unauthenticated users. Users can authenticate using AWS Cognito.
The idea of this repository is to demonstrate how JWT tokens issued by an IdP can be used with node.js and express. This demo is meant only for demonstation purposes for local deployments.

## Setup:
### Cognito
This code required an AWS Cognito User Pool to be set up. No client secret will be needed and its cruical to use a UI hosted by Cognito for everything regarding user signin and login.
Cognito specific parameters need to be set in the ```server.js``` file.

The Callback after the signin needs to be set to: http://localhost:3000/
### Node.js server
The node server simply runs by ```node server.js```. Note: In order to actually login to the application and obersve the JWT tokens (stored as a cookie in the front-end). You need to open
the Signin UI hosted by Cognito - through a link that looks like the following:

https://YOUR_COGNITO_SIGNIN_DOMAINNAME.auth.YOUR_REGION.amazoncognito.com/login?client_id=CLIENT_ID_OF_YOUR_CLIENT&response_type=token&redirect_uri=http://localhost:3000/

## To Do
This is WIP. It'd be good to explain the different tokens a bit more and how they are being used in here (using graphics). For the codebase it'd be worth to implemnt a token refresh functionality.