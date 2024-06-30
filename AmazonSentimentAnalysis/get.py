import pandas as pd
from scrape import Web

class GetData:
    def __init__(self, url):
        self.url = url
        
    def get_info(self):
        web = Web()
        
        # url = "https://www.amazon.in/Oneplus-Nord-Chrome-256GB-Storage/product-reviews/B0CX5BZXLF/ref=cm_cr_dp_d_show_all_btm?ie=UTF8&reviewerType=all_reviews"

        new_url = self.url
        review = []
        while True:
            soup = web.get_soup(new_url)
            reviews_on_page = web.get_reviews(soup)
            if reviews_on_page:
                review.append(reviews_on_page)
            new_url = web.getnextpage(soup)
            if not new_url:
                break

        reviews = []
        for i in review:
            for j in i:
                reviews.append(j)
            
        data = pd.DataFrame(reviews)
        return data

