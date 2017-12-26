import mongojs from 'mongojs'

let databaseUrl = 'mongo/SocialData'
let collections = ['FB_PAGE', 'FB_POST', 'FB_COMMENT']

export const db = mongojs(databaseUrl, collections)
