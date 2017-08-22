
import urllib
import urllib2
 
values={}
values['email'] = "liuhaoxdu@outlook.com"
values['password']="liuhao1234"
data = urllib.urlencode(values) 
url = "https://app.scoledge.com/signin"
geturl = url + "?"+data
request = urllib2.Request(geturl)
response = urllib2.urlopen(request)
print response.read()

print geturl