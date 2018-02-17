import mongojs from 'mongojs'

let databaseUrl = 'mongo:27017/SocialData'
let collections = ['tweetQuery', 'tweet', 'tweetSpecific']

export const db = mongojs(databaseUrl, collections)


export const host = 'https://api.smartcity.kmitl.io/api/v1/'
export const user = 'twitter-connector'
export const pass =  'TwitterConnector#123'
export const collectionId = '9330e9183d8fadae5aee0854cd4114f0a300c168b36f2dc9904e9b5b239d7dce'
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
