from urllib.parse import urlencode
import requests
import json
import re
import random
import time

base_url = 'https://www.zhihu.com//api/v4/questions/27364360/answers?'

headers = {
    'Host': 'www.zhihu.com',
    'Referer': 'https://www.zhihu.com/question/27364360',
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36',
    'X-Requested-With': 'XMLHttpRequest',
}

def get_page(offset):
    params = {
        'include': 'data[*].is_normal,admin_closed_comment,reward_info,is_collapsed,annotation_action,annotation_detail,collapse_reason,is_sticky,collapsed_by,suggest_edit,comment_count,can_comment,content,editable_content,voteup_count,reshipment_settings,comment_permission,created_time,updated_time,review_info,relevant_info,question,excerpt,relationship.is_authorized,is_author,voting,is_thanked,is_nothelp,is_labeled,is_recognized,paid_info,paid_info_content;data[*].mark_infos[*].url;data[*].author.follower_count,badge[*].topics',
        'limit': '5',
        'offset': offset,
        'platform': 'desktop',
        'sort_by': 'default'
    }
    url = base_url + urlencode(params)
    
    try:
        response = requests.get(url, headers=headers)
        if response.status_code == 200:
            return response.text
    except requests.ConnectionError as e:
        print('Error', e.args)
        
for offset in range(0,75,5):
    time.sleep(random.randint(1,2))
    html = get_page(offset)
    site = re.findall(r'img src=\\"([a-z]+://[^\s]*)\\"',html)
    print(site)
    for i in site:
        k = i.split('/')
        with open('download\\'+k[-1],'wb') as g:
            g.write(requests.get(i).content)
    