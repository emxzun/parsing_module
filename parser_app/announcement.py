from datetime import datetime
from parser_app.table import Announcement

from parser_app.pagination import Paginator


class AnnouncementParser(Paginator):

    def get_data(self):
        data = self.get_soup().find_all('div', class_='search-item')
        res = []
        for announcement in data:
            try:
                image = announcement.find('div', class_='image').img.get('data-src')
            except AttributeError:
                image = ''
            try:
                added_at = announcement.find('span', class_='date-posted').text.split('/')
                added_at = '-'.join(added_at)
            except AttributeError:
                added_at = ''
            try:
                price = announcement.find('div', class_='price').text.strip()
            except AttributeError:
                price = ''
            date = datetime.now().strftime('%m-%d-%Y')
            res.append(Announcement(
                image=image,
                price=price,
                added_at=added_at,
                date=date
            ))
            Announcement.bulk_create(res)
