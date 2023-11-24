import { createRequire } from 'module';
const require = createRequire(import.meta.url);

const CognitoExpress = require('cognito-express');
const cognitoExpress = new CognitoExpress({
  region: 'AWS_REGION',
  cognitoUserPoolId: 'AWS_REGION_POOLID',
  tokenUse: 'access', // Possible Values: access | id
  tokenExpiration: 3600000, // Up to default expiration of 1 hour (3600000 ms)
});

const express = require('express');
const port = process.env.PORT || 3000;
const app = express();
const authenticatedRoute = express.Router();

app.use('/api', authenticatedRoute);

// middleware  authenticates all APIs under 'authenticatedRoute' router
authenticatedRoute.use((req, res, next) => {
  const accessTokenFromClient = req.headers.cookie.match(/accesstoken=([^&]*)/)[1];
  // fail if token not present in header.
  if (!accessTokenFromClient) return res.status(401).send(':/ seems like you dont have a token');
  // fail if token not valid
  cognitoExpress.validate(accessTokenFromClient, (err, response) => {
    if (err){
      // console.log(err);
      return res.status(401).send(':/ seems like your token is not valid');
    }
    res.locals.user = response;
    next(); // basically proceed otherwise
  });
});

// unauthenticated routes
app.get('/', (req, res) => {
 res.sendFile('index.html', {root: 'src'});
 })

// authenticated routes
authenticatedRoute.get('/myfirstapi', (req, res, next) => {
  res.send(`Hi ${res.locals.user.username}, your API call is authenticated!`);
});

// when starting the server
app.listen(port, () => {
  console.log(`Example app listening on port ${port}`);
});
