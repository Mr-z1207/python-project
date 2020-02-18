import requests

searchName = '毛不易'

headers = {'Referer': 'http://www.kuwo.cn/search/list?key=',
           'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.130 Safari/537.36',
           'csrf': 'NZNCXJFZLFF',
           'Host': 'www.kuwo.cn',
           'Cookie': '_ga=GA1.2.172942019.1580702894; _gid=GA1.2.771718281.1580890479; uname3=%u3081%u3044%u305F%u3093%u3066%u3044%u3053%u306A%u3093; t3kwid=235511292; userid=235511292; websid=2033651825; pic3="http://q.qlogo.cn/qqapp/100243533/BEB10B9B72AB7C5E6700E08B820BA1C5/100"; t3=qq; Hm_lvt_cdb524f42f0ce19b169a8071123a4797=1580702894,1580890479,1580891122; _gat=1; Hm_lpvt_cdb524f42f0ce19b169a8071123a4797=1580892336; kw_token=NZNCXJFZLFF'
           }

url_params = {'key': searchName}

url = 'http://www.kuwo.cn/search/list'

requson = requests.get(url, params=url_params, headers=headers)

print(requson.json)
