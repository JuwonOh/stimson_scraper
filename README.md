# Stimson_scraper

미국의 씽크탱크인(https://www.stimson.org)의 자료들을 받아오기 위한 크롤러입니다. 전체 4가지 category(Protecting people, Greand stretegy of pivotal place, Preserving the planer, Promoting security and prosperity)의 프로그램에 대한 자료들을 저장해줍니다.

## User guide

크롤러의 파이썬 파일은 util.py, scraper.py 그리고 parser.py 총 세가지로 구성되어 있습니다. 
util.py는 크롤링 한 파이썬의 beautifulsoup 패키지를 받아서 url내의 html정보를 정리합니다.
scraper는 util.py내의 사이트내의 url 링크들을 get_soup함수를 통해 모아줍니다.
parser는 이렇게 만들어진 url리스트를 통해서 각 분석들의 제목/일자/내용을 모아줍니다.


Using Python script with arguments

| Argument name | Default Value | Note |
| --- | --- | --- |
| begin_date | 2019-01-10 | datetime YYYY-mm-dd |
| directory | ./output/ | Output directory |
| max_num | 100 | Maximum number of news to be scraped |
| sleep | 1.0 | Sleep time for each news |
| verbose | False, store_true | If True use verbose mode |

```
python scraping_latest_news.py을 사용하면, 특정기간까지 모든 카테고리의 자료를 ouput폴더에 받아올 수 있습니다.
```
특정한 카테고리와 기간동안의 글을 받아오기 위해서는 다음과 같이 사용할 수 있습니다.

```
from Stimson_scraper import get_latest_allsecurity

begin_date = '2018-07-01'
max_num = 5
sleep = 1.0

for i, json_obj in enumerate(get_latest_allsecurity(begin_date, max_num, sleep)):
    title = json_obj['title']
    time = json_obj['time']
    print('[{} / {}] ({}) {}'.format(i+1, max_num, time, title))
    
```
```
[1 / 5] (Jan 3, 2019) Field Notes - Deep Geological Repository at Olkiluoto, Finlan
[2 / 5] (Dec 14, 2018) ATT Reaches Milestone 100 States Parties
[3 / 5] (Dec 7, 2018) Amazon in Crystal City: Threat and Opportunity for the Defense Department
[4 / 5] (Nov 16, 2018) Shaping Strong Security Norms
[5 / 5] (Nov 13, 2018) Nukes, the New Congress, and the Lost Art of Political Compromise
```

## 참고 코드

본 코드는 https://github.com/lovit/whitehouse_scraper를 참조하여 만들어졌습니다.
