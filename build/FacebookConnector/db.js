import mongojs from 'mongojs'

let databaseUrl = '127.0.0.1/SocialData'
let collections = ['FB_PAGE', 'FB_POST', 'FB_COMMENT']

export const db = mongojs(databaseUrl, collections)
