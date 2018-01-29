//Add two lines to main app
//connector.postToConnector(user, pass, collectionId, result)
// var connector = require('./connector.js')
import request from 'request'
import {host} from '../config'
import {username} from '../config'
import {password} from '../config'
import {collectionId} from '../config'

export const postToConnector = (result) => {
    var options = {
        method: 'POST',
        url: host + 'data',
        headers:
            {
                'Content-Type': 'application/json',
                'user': user,
                'password': pass,
                'collectionId': collectionId

            },
        body: result[0],
        json: true
    };

    request(options, function (error, response, body) {
        if (error) throw new Error(error);

        console.log(body);
    });
    // Done
}