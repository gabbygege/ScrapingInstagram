import requests, json, time, csv

url = 'https://www.instagram.com/graphq1/query'
short_code = input('Please enter a short code: ')
end_cursor = ''
count = 0
counter_file = 1
jumlah_per_file = 1000

writer = csv.writer(open('hasil_like/{} {}.csv'.format(short_code,counter_file), 'w', newline=''))
headers = ['User Name', 'Full Name', 'Profile Pic']
writer.writerow(headers)
while 1:
    varibles = {"shortcode": short_code, "first": 50, "after": end_cursor}

    params = {
        'query_hash': 'd5d763b1e2acf209d62d22d184488e57',
        'variables': json.dumps(varibles)
    }

    r = requests.get(url, params=params).json()
    try:
        users = r['data']['shortcode_media']['edge_liked_by']['edges']
    except:
        print('please wait')
        time.sleep(20)
        continue

    for user in users:
        if count % jumlah_per_file == 0 and count != 0:
            counter_file += 1
            writer = csv.writer(open('hasil_like/{} {}.csv'.format(short_code, counter_file), 'w', newline=''))
            headers = ['User Name', 'Full Name', 'Profile Pic']
            writer.writerow(headers)
        username = user['node']['username']
        full_name = user['node']['full_name']
        profile_pic = user['node']['profile_pic_url']
        count += 1
        print(count, username, full_name, profile_pic)
        writer = csv.writer(open('hasil_like/{} {}.csv'.format(short_code, counter_file), 'a', newline='', encoding='utf-8'))
        data = [username, full_name, profile_pic]
        writer.writerow(data)

    end_cursor = r['data']['shortcode_media']['edge_liked_by']['page_info']['end_cursor']
    has_next_page = r['data']['shortcode_media']['edge_liked_by']['page_info']['has_next_page']
    if has_next_page == False: break
    time.sleep(3)
