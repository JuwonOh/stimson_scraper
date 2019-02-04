import re
from .utils import get_soup
from .utils import now

def parse_page(url):
    """
    Argument
    --------
    url : str
        Web page url

    Returns
    -------
    json_object : dict
        JSON format web page contents
        It consists with
            title : article title
            time : article written time
            content : text with line separator \\n
            url : web page url
            scrap_time : scrapped time
    """

    try:
        soup = get_soup(url)
        title = soup.find('h1', class_= 'product-title').text
        time = soup.find('div', class_ ='author-date-block').find('span', class_='date-product').text
        # for writting Co-worker
        sub_author = soup.find_all('div', class_ ='expert-name')
        author = [i.text for i in sub_author]
        contents = soup.find('div', class_= 'field__item even').text

        json_object = {
            'title' : title,
            'time' : time,
            'content' : contents,
            'author' :author,
            'url' : url,
            'scrap_time' : now()
        }
        return json_object
    except Exception as e:
        print(e)
        print('Parsing error from {}'.format(url))
        return None
