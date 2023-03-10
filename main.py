from parser_app.announcement import AnnouncementParser


def main():
    page = 1
    while True:
        url = f'https://www.kijiji.ca/b-apartments-condos/city-of-toronto/page-{page}/c37l1700273'
        parser = AnnouncementParser(url)
        parser.get_html()
        parser.get_data()
        if not parser.find_button_next():
            break
        page += 1


if __name__ == '__main__':
    main()
