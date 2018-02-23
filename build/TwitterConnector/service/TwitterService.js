import Twit from 'twit'
import {db} from '../config'
import cron from 'cron'
import axios from 'axios'
//import {postToConnector} from './connector'

let cronJob = cron.CronJob

let T = new Twit({
    consumer_key: 'eFroY0pfuCmbSf4OrwFckHDUY',
    consumer_secret: 'xCJRkrUHuPGAGs7ZCAdKOjqDfIcghzMGjfrS6xLXHZUKwJ430x',
    access_token: '3854752459-6KWXoTPeBbxUdydKsAUNohUru2DBioZ9jmeaIFn',
    access_token_secret: '9qow1TnZqKaWVgZ6V22qcNeqEz5IoFroVOTGs846H6yfQ',
    timeout_ms: 60 * 1000
})

export function tweet(status) {
    return new Promise((resolve, reject) => {
        T.post('statuses/update', {
            status: status
        }, (err, data, response) => {
            if (err) {
                reject(err)
            } else {
                resolve(data)
            }
        })
    })
}

export function searchAndSaveTweet(q) {
    return new Promise((resolve, reject) => {
        searchTweet(q).then(data => {
            saveTweet(data)
            resolve(data)
        }).catch(err => {
            reject(err)
        })
    })
}

export function searchTweet(q) {
    return new Promise((resolve, reject) => {
        T.get('search/tweets', {
            q: q,
            count: 10
        }, (err, data, response) => {
            if (err) {
                reject(err)
            } else {
                resolve(data)
            }
        })
    })
}

export function searchTweetNearby(lat, lng, since) {
    return new Promise((resolve, reject) => {
        T.get('search/tweets', {
            q: "since:" + since,
            geocode: "\"" + lat + "," + lng + "," + "0.2km\"",
            result_type: 'mixed'
        }, (err, data, response) => {
            if (err) {
                reject(err)
            } else {
                resolve(data)
            }
        })
    })
}

function saveTweet(data, place_id) {
data.statuses.forEach(item => {
    db.tweet.findOne({
        id: item.id
    }, (err, document) => {
        if (!document) {
            let tweet = item
            tweet.created_at = new Date(item.created_at)
            tweet.user.created_at = new Date(item.user.created_at)
            if (typeof tweet.retweeted_status != 'undefined') {
                tweet.retweeted_status.created_at = new Date(item.retweeted_status.created_at)
                tweet.retweeted_status.user.created_at = new Date(item.retweeted_status.user.created_at)
            }
            if (item.retweeted_status != null) {
                tweet.text = item.retweeted_status.text
            }
            tweet.place_id = place_id
            let count = 0
            getLatestTweet(place_id).then((res) => { count = res })
            console.log('count: ', count)
            if (count != 0){
                db.latestTweet2.update({'place_id':place_id},{'id':tweet.id, 'text': tweet.text, 'created_at':tweet.created_at, 'place_id':place_id})
            }
            else{
                db.latestTweet2.insert({'id':tweet.id, 'text': tweet.text, 'created_at':tweet.created_at, 'place_id':place_id})
            }
            //postToConnector(tweet)
            db.tweet.insert(tweet, err => {
                if (err) {
                    console.log(err)
                }
            })
        }
    })
})
}

function getLatestTweet(place_id){
    return new Promise((resolve, reject) => {
        db.latestTweet2.find({'place_id':place_id}).count((err, res) =>{
            resolve(res)
        })
    })
}

// save tweets every 30 second
let saveTweetJob = new cronJob('*/5 * * * *', () => {
  let all_tweets = []
  axios.get('http://socialdata-service:5005/query').then((response) => {
    response.data.queries.forEach((item, idx) => {
        T.get('search/tweets', {
            q: item.keyword,
            count: 100,
            lang: 'th'
        }, (err, data) => {
            if (err) {
                console.log(err.stack)
            } else {
                tweet = {}
                tweet.tweets = data.statuses
                tweet.query = item
                all_tweets.push(tweet)
                saveTweet(data, item.place_id)
                // if(idx == response.data.queries.length - 1) {
                //     sendToHadoop(all_tweets)
                // }
            }
        })
    })
  }).catch((err) => {
      console.log(err)
  })
}, () => {
console.log('saveTweetJob has stopped')
}, true)

// // save tweets every 30 second
// let saveTweetJob = new cronJob('*/5 * * * *', () => {
//   getAllQuery().then(docs => {
//     docs.forEach(item => {
//       // let item = {}
//       // item.query = "สนามหลวง"
//       T.get('search/tweets', { q: item.query, count: 100, lang: 'th'}, (err, data) => {
//         if(err) {
//           console.log(err.stack)
//         }
//         else {
//           saveTweet(data, item.query)
//           // sendToHadoop(data)
//         }
//       })
//     })
//   })
//   .catch((err) => {
//     console.log(err)
//   })
// },
// () => {
//   console.log('saveTweetJob has stopped')
// },
// true
// )

export function addQuery(query) {
db.tweetQuery.insert({
    query: query
}, err => {
    if (err) {
        console.log(err)
    }
})
testTweetQuery()
}

function getAllQuery() {
return new Promise((resolve, reject) => {
    db.tweetQuery.find((err, docs) => {
        if (err) {
            reject(reject)
        } else {
            resolve(docs)
        }
    })
})
}

function testTwitterQuery() {
db.tweet.find((err, docs) => {
    if (err) {
        console.log(err)
    } else {
        console.log(docs)
    }
})
}

function testTweetQuery() {
db.tweetQuery.find((err, docs) => {
    if (err) {
        console.log(err)
    } else {
        console.log(docs)
    }
})
}

export function getAllTweet() {
return new Promise((resolve, reject) => {
    db.tweet.find((err, docs) => {
        if (err) {
            reject(err)
        } else {
            resolve(docs)
        }
    })
})
}

let T_ant = new Twit({
consumer_key: 'CpCVGROxFCQDcV5Jy0eYFWW7K',
consumer_secret: '2pWbgAa6tWs3X7HG8NXU7Vx5jogHjp4FstsQX0bAOI0kOAmfKO',
access_token: '3854752459-9m8JOA8p3ZqT6PONwuIkDovFDuIEpIg817isjs6',
access_token_secret: 'AaRo30SSKLN8buG2J9JfgsmGRBfjw4AR1XjdovfimfL5V',
timeout_ms: 60 * 1000
})

// let saveTweetSpecificJob = new cronJob('0 */30 * * * *', () => {
// // getAllQuery().then(docs => {
// // docs.forEach(item => {
// let item = []
// item.forEach(i => {
//     console.log(i);
//     T_ant.get('search/tweets', {
//         q: i,
//         count: 100
//     }, (err, data) => {
//         if (err) {
//             console.log(err.stack)
//         } else {
//             saveTweetSpecific(data, i)
//         }
//     }).catch((err) => {
//         console.log(err)
//     })
// })
//
// // })
// // })
// }, () => {
// console.log('saveTweetJob has stopped')
// }, true)

function saveTweetSpecific(data, query) {
data.statuses.forEach(item => {
    db.tweet.findOne({
        id: item.id
    }, (err, document) => {
        if (!document) {
            let tweet = item
            tweet.created_at = new Date(item.created_at)
            tweet.user.created_at = new Date(item.user.created_at)
            if (typeof tweet.retweeted_status != 'undefined') {
                tweet.retweeted_status.created_at = new Date(item.retweeted_status.created_at)
                tweet.retweeted_status.user.created_at = new Date(item.retweeted_status.user.created_at)
            }
            if (item.retweeted_status != null) {
                tweet.text = item.retweeted_status.text
            }
            tweet.query = query
            db.tweetSpecific.insert(tweet, err => {
                if (err) {
                    console.log(err)
                }
            })
        }
    })
})
}
