from bs4 import BeautifulSoup
import requests

class Web:
    def get_soup(self, url):
    # HTTP headers let the server and the client transfer additional information through an HTTP response or request.
        headers = {"***"}
        page = requests.get("http://localhost:8050/render.html", headers = headers, params={'url': url, 'wait': 2})
        soup = BeautifulSoup(page.text, 'html.parser')
        
        return soup

    def get_reviews(self, soup):
        reviews = soup.find_all('div', {'data-hook': 'review'})
        rev_list = []
        
        try:
            for i in reviews:
                review = i.find('a', {'data-hook': 'review-title'}).text.strip().replace('out of 5 stars', '')
                review_dict = {
                'product' : soup.title.text.replace('Amazon.in:Customer reviews: ', ''),
                'rating' : float(review[:3]),
                'title' : review[3:],
                'body' : i.find('span', {'data-hook': 'review-body'}).text.strip()
                }
                rev_list.append(review_dict)
                
            return rev_list
        except:
            pass


    def getnextpage(self, soup):
        page = soup.find('ul', {'class' : 'a-pagination'})
        if not page.find('li', {'class' : 'a-disabled a-last'}):
            url = 'https://www.amazon.in' + str(page.find('li', {'class' : 'a-last'}).find('a')['href'])
            return url
        else:
            return
    