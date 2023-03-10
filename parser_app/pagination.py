from configuration.parser import Parser


class Paginator(Parser):
    def find_button_next(self) -> bool:
        pagination = self.get_soup().find('div', class_='pagination')
        return 'Next' in pagination.text
