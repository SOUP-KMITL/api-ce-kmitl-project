"use strict"
import express from 'express'
//const express = require("express")
import bodyParser from 'body-parser'
//const bodyParser = require("body-parser")
import twitterRouter from './controller/TwitterController'
//const twitterRouter = require('./controller/TwitterController')
import cors from 'cors'
//const cors = require("cors")
import swagger from 'swagger-node-express'
//const swagger = require("swagger-node-express")
import { applicationUrl, swaggerPath } from './swagger'
//const { applicationUrl, swaggerPath } =  require('./swagger')

//Port
const port = process.env.port || 7777
let app = express()

//enable cors
app.use(cors())

// parse application/json
app.use(bodyParser.json())
app.use(bodyParser.urlencoded({
  extended: true
}))

//parent url
app.route('/').get((req, res) => {
  res.send('<h1>Social REST Api</h1><ul><li>/twitter</li><li>/facebook</li></ul>')
})

app.use('/twitter', twitterRouter)

//Swagger
app.use('/swagger', swaggerPath)
swagger.setAppHandler(swaggerPath)
app.use(express.static(__dirname + '/dist'))
swagger.setApiInfo({
  title: "Twitter Conector API",
  description: "API which can connect to Twitter",
  termsOfServiceUrl: "",
  contact: "yourname@something.com",
  license: "",
  licenseUrl: ""
})
swagger.configureSwaggerPaths('', 'api-docs', '')
swagger.configure(applicationUrl, '1.0.0')

//service start
app.listen(port, () => {
  console.log('Starting node.js on port ' + port)
});
