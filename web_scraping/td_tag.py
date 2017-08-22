import re
from download_iteration import download
url = 'http://example.webscraping.com/view/UnitedKingdom-239'
html = download(url)
print re.findall('<td classe="w2p_fw">(.*?)</td>',html)