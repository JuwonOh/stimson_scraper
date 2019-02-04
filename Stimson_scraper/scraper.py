import time
from .parser import parse_page
from .utils import get_soup
from .utils import news_dateformat
from .utils import user_dateformat
from .utils import strf_to_datetime

pivot_news = 'https://www.stimson.org/programs/grand-strategy-pivotal-places?page={}'

def get_latest_allpivot(begin_date, max_num=10, sleep=1.0):
    """
    Arguments
    ---------
    begin_page : int
        Default is 1
    end_page : int
        Default is 3
    verbose : Boolean
        If True, print current status

    Returns
    -------
    links_all : list of str
        List of urls
    """
    # prepare parameters
    d_begin = strf_to_datetime(begin_date, user_dateformat)
    end_page = 72
    n_news = 0
    outdate = False

    for page in range(0, end_page+1):

        # check number of scraped news
        if n_news >= max_num or outdate:
            break

        # get urls
        links_all = []
        url =  pivot_news.format(page)
        soup = get_soup(url)
        sub_links = soup.find_all('div', class_= 'current-title')
        links = [i.find('a')['href'] for i in sub_links]
        links_all += links
        links_all = ['https://www.stimson.org' + i for i in links_all]

        # scrap
        for url in links_all:

            news_json = parse_page(url)

            # check date
            d_news = strf_to_datetime(news_json['time'], news_dateformat)
            if d_begin > d_news:
                outdate = True
                print('Stop scrapping. {} / {} news was scrapped'.format(n_news, max_num))
                print('The oldest news has been created after {}'.format(begin_date))
                break

            # yield
            yield news_json

             # check number of scraped news
            n_news += 1
            if n_news >= max_num:
                break
            time.sleep(sleep)

def get_pivot_urls(begin_page=0, end_page=3, verbose=True):
    """
    Arguments
    ---------
    begin_page : int
        Default is 1
    end_page : int
        Default is 3
    verbose : Boolean
        If True, print current status

    Returns
    -------
    links_all : list of str
        List of urls
    """

    links_all = []
    for page in range(begin_page, end_page+1):
        url = pivot_news.format(page)
        soup = get_soup(url)
        sub_links = soup.find_all('div', class_= 'current-title')
        links = [i.find('a')['href'] for i in sub_links]
        links_all += links

        if verbose:
            print('get briefing statement urls {} / {}'.format(page, end_page))
    links_all = ['https://www.stimson.org' + i for i in links_all]
    return links_all


url_planet = 'https://www.stimson.org/programs/preserving-planet?page={}/'

def get_latest_allplanet(begin_date, max_num=10, sleep=1.0):
    """
    Arguments
    ---------
    begin_page : int
        Default is 1
    end_page : int
        Default is 3
    verbose : Boolean
        If True, print current status

    Returns
    -------
    links_all : list of str
        List of urls
    """
    # prepare parameters
    d_begin = strf_to_datetime(begin_date, user_dateformat)
    end_page = 72
    n_news = 0
    outdate = False

    for page in range(0, end_page+1):

        # check number of scraped news
        if n_news >= max_num or outdate:
            break

        # get urls
        links_all = []
        url = url_planet.format(page)
        soup = get_soup(url)
        sub_links = soup.find_all('div', class_= 'current-title')
        links = [i.find('a')['href'] for i in sub_links]
        links_all += links
        links_all = ['https://www.stimson.org' + i for i in links_all]

        # scrap
        for url in links_all:

            news_json = parse_page(url)

            # check date
            d_news = strf_to_datetime(news_json['time'], news_dateformat)
            if d_begin > d_news:
                outdate = True
                print('Stop scrapping. {} / {} news was scrapped'.format(n_news, max_num))
                print('The oldest news has been created after {}'.format(begin_date))
                break

            # yield
            yield news_json

             # check number of scraped news
            n_news += 1
            if n_news >= max_num:
                break
            time.sleep(sleep)


def get_planet_urls(begin_page=0, end_page=3, verbose=True):
    """
    Arguments
    ---------
    begin_page : int
        Default is 1
    end_page : int
        Default is 3
    verbose : Boolean
        If True, print current status

    Returns
    -------
    links_all : list of str
        List of urls
    """

    links_all = []
    for page in range(begin_page, end_page+1):
        url = url_planet.format(page)
        soup = get_soup(url)
        sub_links = soup.find_all('div', class_= 'current-title')
        links = [i.find('a')['href'] for i in sub_links]
        links_all += links
        if verbose:
            print('get briefing statement urls {} / {}'.format(page, end_page))
    links_all = ['https://www.stimson.org' + i for i in links_all]
    return links_all


url_people = 'https://www.stimson.org/programs/protecting-people?page={}'

def get_latest_allpeople(begin_date, max_num=10, sleep=1.0):
    """
    Arguments
    ---------
    begin_page : int
        Default is 1
    end_page : int
        Default is 3
    verbose : Boolean
        If True, print current status

    Returns
    -------
    links_all : list of str
        List of urls
    """

    # prepare parameters
    d_begin = strf_to_datetime(begin_date, user_dateformat)
    end_page = 72
    n_news = 0
    outdate = False

    for page in range(0, end_page+1):

        # check number of scraped news
        if n_news >= max_num or outdate:
            break

        # get urls
        links_all = []
        url = url_people.format(page)
        soup = get_soup(url)
        sub_links = soup.find_all('div', class_= 'current-title')
        links = [i.find('a')['href'] for i in sub_links]
        links_all += links
        links_all = ['https://www.stimson.org' + i for i in links_all]

        # scrap
        for url in links_all:

            news_json = parse_page(url)

            # check date
            d_news = strf_to_datetime(news_json['time'], news_dateformat)
            if d_begin > d_news:
                outdate = True
                print('Stop scrapping. {} / {} news was scrapped'.format(n_news, max_num))
                print('The oldest news has been created after {}'.format(begin_date))
                break

            # yield
            yield news_json

             # check number of scraped news
            n_news += 1
            if n_news >= max_num:
                break
            time.sleep(sleep)


def get_people_urls(begin_page=0, end_page=3, verbose=True):
    """
    Arguments
    ---------
    begin_page : int
        Default is 1
    end_page : int
        Default is 3
    verbose : Boolean
        If True, print current status

    Returns
    -------
    links_all : list of str
        List of urls
    """

    links_all = []
    for page in range(begin_page, end_page+1):
        url = url_people.format(page)
        soup = get_soup(url)
        sub_links = soup.find_all('div', class_= 'current-title')
        links = [i.find('a')['href'] for i in sub_links]
        links_all += links
        if verbose:
            print('get briefing statement urls {} / {}'.format(page, end_page))
    links_all = ['https://www.stimson.org' + i for i in links_all]
    return links_all

url_security = 'https://www.stimson.org/programs/promoting-security-and-prosperity?page={}'

def get_latest_allsecurity(begin_date, max_num=10, sleep=1.0):
    """
    Arguments
    ---------
    begin_page : int
        Default is 1
    end_page : int
        Default is 3
    verbose : Boolean
        If True, print current status

    Returns
    -------
    links_all : list of str
        List of urls
    """
    # prepare parameters
    d_begin = strf_to_datetime(begin_date, user_dateformat)
    end_page = 72
    n_news = 0
    outdate = False

    for page in range(0, end_page+1):

        # check number of scraped news
        if n_news >= max_num or outdate:
            break

        # get urls
        links_all = []
        url = url_security.format(page)
        soup = get_soup(url)
        sub_links = soup.find_all('div', class_= 'current-title')
        links = [i.find('a')['href'] for i in sub_links]
        links_all += links
        links_all = ['https://www.stimson.org/' + i for i in links_all]

        # scrap
        for url in links_all:

            news_json = parse_page(url)

            # check date
            d_news = strf_to_datetime(news_json['time'], news_dateformat)
            if d_begin > d_news:
                outdate = True
                print('Stop scrapping. {} / {} news was scrapped'.format(n_news, max_num))
                print('The oldest news has been created after {}'.format(begin_date))
                break

            # yield
            yield news_json

             # check number of scraped news
            n_news += 1
            if n_news >= max_num:
                break
            time.sleep(sleep)

def get_security_urls(begin_page=1, end_page=3, verbose=True):
    """
    Arguments
    ---------
    begin_page : int
        Default is 1
    end_page : int
        Default is 3
    verbose : Boolean
        If True, print current status

    Returns
    -------
    links_all : list of str
        List of urls
    """

    links_all = []
    for page in range(begin_page, end_page+1):
        url = url_security.format(page)
        soup = get_soup(url)
        sub_links = soup.find_all('div', class_= 'current-title')
        links = [i.find('a')['href'] for i in sub_links]
        links_all += links
        if verbose:
            print('get briefing statement urls {} / {}'.format(page, end_page))
    links_all = ['https://www.stimson.org' + i for i in links_all]
    return links_all
