import requests
from bs4 import BeautifulSoup
import pprint

#this is for first page
res1 = requests.get('https://news.ycombinator.com/')

soup1 = BeautifulSoup(res1.text, 'html.parser')
links1=soup1.select('.storylink')
subtext1=soup1.select('.subtext')

#this is for second page
res2 = requests.get('https://news.ycombinator.com/news?p=2')
soup2 = BeautifulSoup(res2.text, 'html.parser')
links2=soup2.select('.storylink')
subtext2=soup2.select('.subtext')

links = links1+links2
subtext =subtext1+subtext2

# for sorting dictoniary 
def sort_dict(hackernews):
    return sorted(hackernews, key=lambda k:k['votes'],reverse=True)


def custom_hackerrank(links,subtext):
    hackernews=[]
    for  index ,item in enumerate(links):
        title= links[index].getText()
        hyperlink = links[index].get('href',None)
        vote =subtext[index].select('.score')
        if len(vote):
            point=int( vote[0].getText().replace(' points',''))
            if point>99:
                hackernews.append({'Name':title,'webaddress':hyperlink,'votes':point})
    return sort_dict( hackernews)

#to print in nice format use pprint
pprint.pprint(custom_hackerrank(links,subtext))
