import urllib2
from bs4 import BeautifulSoup


def crawlRollsHistory(htmlPath):
    htmlfile = open(htmlPath, 'r').read()
    soup = BeautifulSoup(htmlfile, 'html.parser')

    tdlist = soup.findAll('td')
    thlist = soup.findAll('th')
    currentID = tdlist[1].get_text()
    currentID = currentID[:-1]
    for i in xrange(2, 12):
        if (tdlist[i].get_text() != ""):
            currentID = (int)(currentID + thlist[i].get_text())
            break
    results = soup.findAll('td', class_='td-val')
    if (results is not None):
        for result in results:
            result_file.write("%d %s\n" % (currentID, result.get_text()))
            currentID += 1

result_file = open('result.txt', 'w')
max_index = 143
for index in xrange(0, max_index):
    path = "(%d).htm" % (index)
    print path
    crawlRollsHistory(path)
result_file.close()
