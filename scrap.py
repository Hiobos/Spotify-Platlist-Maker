import requests
from bs4 import BeautifulSoup


class Music:
    def __init__(self):
        self.playlist = []

    def get_music(self):
        print("Enter Date in format YYYY-MM-DD")
        date = input("What date would you like to see?: ")

        billboard_endpoint = f'https://www.billboard.com/charts/hot-100/{date}/'
        header = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:131.0) Gecko/20100101 Firefox/131.0"}
        try:
            response = requests.get(url=billboard_endpoint, headers=header)
            if response.status_code == 200:
                response = requests.get(url=billboard_endpoint, headers=header).text
            else:
                print("Something went wrong, check spelling")
                return
        except IndexError:
            print("An error occured, check if date is correct.")
            return

        soup = BeautifulSoup(response, 'html.parser')

        # title list
        title = soup.select('ul ul li h3',
                            class_='o-chart-results-list-row // lrv-a-unstyle-list lrv-u-flex u-height-200 u-height-100@mobile-max u-height-100@tablet-only lrv-u-background-color-white a-chart-has-chart-detail, lrv-a-unstyle-list lrv-u-flex lrv-u-height-100p lrv-u-flex-direction-column@mobile-max, o-chart-results-list__item // lrv-u-flex-grow-1 lrv-u-flex lrv-u-flex-direction-column lrv-u-justify-content-center lrv-u-border-b-1 u-border-b-0@mobile-max lrv-u-border-color-grey-light  lrv-u-padding-l-1@mobile-max, c-title  a-no-trucate a-font-primary-bold-s u-letter-spacing-0021 u-font-size-23@tablet lrv-u-font-size-16 u-line-height-125 u-line-height-normal@mobile-max a-truncate-ellipsis u-max-width-245 u-max-width-230@tablet-only u-letter-spacing-0028@tablet')
        title_list = [title_item.string.strip() for title_item in title]

        # author list
        author = soup.select('ul ul li span',
                             class_='o-chart-results-list-row // lrv-a-unstyle-list lrv-u-flex u-height-200 u-height-100@mobile-max u-height-100@tablet-only lrv-u-background-color-white a-chart-has-chart-detail, lrv-a-unstyle-list lrv-u-flex lrv-u-height-100p lrv-u-flex-direction-column@mobile-max, o-chart-results-list__item // lrv-u-flex-grow-1 lrv-u-flex lrv-u-flex-direction-column lrv-u-justify-content-center lrv-u-border-b-1 u-border-b-0@mobile-max lrv-u-border-color-grey-light  lrv-u-padding-l-1@mobile-max, c-label  a-no-trucate a-font-primary-s lrv-u-font-size-14@mobile-max u-line-height-normal@mobile-max u-letter-spacing-0021 lrv-u-display-block a-truncate-ellipsis-2line u-max-width-330 u-max-width-230@tablet-only u-font-size-20@tablet')
        author_list = [author_item.string.strip() for author_item in author if len(author_item.string.strip()) > 2]

        #adding each track to the list
        for i in range(0, 100):
            try:
                self.playlist.append(f"{title_list[i]} {author_list[i]}")
            except IndexError:
                "Something went wrong, check spellin."
                return
        #returning list of tracks and date so that later playlist can be named after it
        return self.playlist, date