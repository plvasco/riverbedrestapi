import grequests
urls = ['http://google.com', 'http://yahoo.com', 'http://bing.com']

unsent_request=(grequests.get(url) for url in urls)


results = grequests.map(unsent_request)

print results