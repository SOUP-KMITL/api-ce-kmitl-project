import mongojs from 'mongojs'

let databaseUrl = 'mongo/SocialData'
let collections = ['tweetQuery', 'tweet', 'tweetSpecific']

export const db = mongojs(databaseUrl, collections)


export const host = 'https://api.smartcity.kmitl.io/api/v1/'
export const user = 'twitter-connector'
export const pass =  'TwitterConnector#123'
export const collectionId = ''
// import Sequelize from 'sequelize'
//
// export const sequelize = new Sequelize('SocialRest', 'rest', 'restapi', {
//   host: '13.76.94.234',
//   dialect: 'mariadb',
//   pool: {
//     max: 5,
//     min: 0,
//     idle: 10000
//   },
// })
