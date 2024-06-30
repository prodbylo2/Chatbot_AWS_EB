from bs4 import BeautifulSoup
import requests
# import pandas as pd

class Web:

    # url = "https://www.amazon.in/Oneplus-Nord-Chrome-256GB-Storage/product-reviews/B0CX5BZXLF/ref=cm_cr_dp_d_show_all_btm?ie=UTF8&reviewerType=all_reviews"

    def get_soup(self, url):
    # HTTP headers let the server and the client transfer additional information through an HTTP response or request.
        headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36"}
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

    # new_url = url
    # review = []
    # while True:
    #     soup = get_soup(new_url)
    #     review.append(get_reviews(soup))
    #     new_url = getnextpage(soup)
    #     if not new_url:
    #         break

    # reviews = []
    # for i in review:
    #     for j in i:
    #         reviews.append(j)
        
    # data = pd.DataFrame(reviews)
    # print(data)
    
    