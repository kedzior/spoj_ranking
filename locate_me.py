import argparse
import requests
import sys

URL_RANKING = 'http://pl.spoj.com/ranks2/'

def main(args):
    session = requests.Session()
    start_pos = 0
    while True:
        resp = session.post(URL_RANKING + '?start=' + str(start_pos))
        sys.stdout.write('\rSearching ' + str(start_pos) + '...')
        if resp.status_code != 200:
            raise Exception('Strona nie dziala')
        if args.login in resp.text:
            print('\r' + args.login + ' found!')
            print(URL_RANKING + '?start=' + str(start_pos))
            break
        start_pos += 25


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Locate me in pl.spoj.com ranking.')
    parser.add_argument('login', type=str)
    args = parser.parse_args()
    main(args)

