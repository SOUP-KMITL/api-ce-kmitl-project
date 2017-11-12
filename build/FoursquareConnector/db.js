import mongojs from 'mongojs'

let databaseUrl = '127.0.0.1/SocialData'
let collections = ['FQ_VENUE', 'FQ_POPULARHOUR', 'FQ_CHECKIN','FQ_TIP','FQ_USER','FQ_PHOTO','place2']

export const db = mongojs(databaseUrl, collections)
