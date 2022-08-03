from article_crawler import NaverArticleCrawler, NaverPressArticleListCrawler
from time import sleep

def crawl_a_day(oid, date):
    naver_press_article_list_crawler = NaverPressArticleListCrawler()
    a_list = naver_press_article_list_crawler.crawl(oid, date)
    data = []
    for a in a_list:
        print(a.get('title'))
        naver_article_crawler = NaverArticleCrawler()
        data.append(naver_article_crawler.crawl(a.get('href')))
        sleep(3)

if __name__ == "__main__":
    crawl_a_day('032', '20220803')
