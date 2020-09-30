import requests, json

url = 'https://www.instagram.com/graphq1/query'
short_code = input('Please enter a short code: ')
varibles = {"shortcode": short_code, "first":50}

params = {
    'query_hash': 'd5d763b1e2acf209d62d22d184488e57',
    'variables': json.dumps(varibles)
}

r = requests.get(url, params=params).json()
users = r['data']['shortcode_media']['edge_liked_by']['edges']

count = 0
for user in users:
    username = user['node']['username']
    full_name = user['node']['full_name']
    profile_pic = user['node']['profile_pic_url']
    print(username, full_name, profile_pic)
    count += 1
    print(count)
    #print(username)
    #print(full_name)
    #print(profile_pic)
