import csv
import requests


# Получение всех постов группы ИМКТ
def take_IMKT():
    token = '53ce25b453ce25b453ce25b4f853b3370b553ce53ce25b431631f2080d210ce13cc286a'
    version = 5.92
    domain = 'imct_fefu'
    count = 100
    offset = 0
    all_posts = []
    while offset < 500:  # т. к. постов всего 484, решаем, что не нужно перегружать ОЗУ и устрановим local_max = 500
        response = requests.get('https://api.vk.com/method/wall.get',
                                params={
                                    'access_token': token,
                                    'v': version,
                                    'domain': domain,
                                    'count': 100
                                }
                                )
        data = response.json()['response']['items']
        offset += 100
        all_posts.extend(data)

    return all_posts


def file_writer(all_posts):
    with open('imkt.csv', 'w') as file:
        a_pen = csv.writer(file)
        a_pen.writerow(('Likes', 'Comments', 'Views'))
        i = 0
        for post in all_posts:
            i += 1
            a_pen.writerow((post['likes']['count'], post['comments']['count'], post['views']['count']))


all_posts = take_IMKT()
file_writer(all_posts)

print("Parsing done")
