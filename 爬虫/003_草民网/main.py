import module.get_urlList as get_urlList
import threading

caomin = get_urlList.Reques('https://www.cmdy5.com/')
urlList = caomin.get_content(".nav-down-1[id^='topnav'] a::attr('href')")
urlListName = caomin.get_content(".nav-down-1[id^='topnav'] a::text")
threads = []


def nextPage(doc):
    a_button_text = doc.get_content(".page.mb a::text")
    try:
        next_page_index = a_button_text.index('下一页')
    except Exception:
        return False

    next_button_url = 'https://www.cmdy5.com/' + \
        doc.get_content(".page.mb a::attr('href')")[next_page_index]
    return next_button_url


def saveMovie(movie_urlList, movie_nameList, filename):
    for i in range(len(movie_urlList)):
        name = movie_nameList[i]
        url = movie_urlList[i]
        print(name, '-->', url)

        with open('{}.txt'.format(filename), 'a') as f:
            try:
                f.write('{} --> {}\n'.format(movie_urlList, movie_nameList))
            except Exception:
                continue


def target_fn(url, filename):
    while url:
        movie_classify = get_urlList.Reques(url)
        movie_urlList = movie_classify.get_content(".link-hover::attr('href')")
        movie_nameList = movie_classify.get_content(".link-hover .name::text")
        url = nextPage(movie_classify)

        saveMovie(movie_urlList, movie_nameList, filename)


for i in range(len(urlList)):
    filename = urlListName[i]
    url = urlList[i]
    T = threading.Thread(target=target_fn, args=(url, filename))
    T.start()
    threads.append(T)
    print(threads)

for t in threads:
    t.join()
