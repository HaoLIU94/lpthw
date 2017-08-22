import builtwith
import whois
import urllib2
import re
# get a web site informations
#print builtwith.parse('http://app.scoledge.com')
#print whois.whois('http://app.scoledge.com')

#url = 'http://www.meetup.com/'
import urllib2
def download(url,user_agent='wswp',num_retries=2):
    print 'Downloading:', url
    headers = {'User-agent': user_agent}
    request = urllib2.Request(url, headers=headers)
    try:
        html = urllib2.urlopen(url).read()
    except urllib2.URLError as e:
        print 'Download error:', e.reason
        html = None
        if num_retries > 0:
            if hasattr(e, 'code') and 500 <= e.code < 600:
                # recursively retry 5xx HTTP errors
                return download(url,user_agent ,num_retries-1)
    return html
#print download(url,'wswp',2)

def crawl_sitemap(url):
    # download the sitemap file
    sitemap = download(url)
    print sitemap
    # extract the sitemap links
    links = re.findall('<a> href="(.*?)"</a>', sitemap)
    # download each link
    for link in links:
        html = download(link)
    # scrape html here
    # ...
#if __name__ == '__main__':
    #crawl_sitemap('http://example.webscraping.com/sitemap.xml')

import itertools
for page in itertools.count(1):
    url = 'http://example.webscraping.com/view/-%d' % page
    html = download(url)
    if html is None:
        break
    '''
    else:
        # success - can scrape the result
    pass
    '''