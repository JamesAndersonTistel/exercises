'''
Explore pattern matching.
'''
import os
import pickle

import requests


def fetch_test_data(url):
    'be nice to test api pickle result to reduce calls to api.'
    fname = 'api_data.pickle'
    result = None

    if os.path.exists(fname):
        with open(fname, 'rb') as f:
            result = pickle.load(f)
    else:
        result = requests.get(url).json()
        with open(fname, 'wb') as f:
            pickle.dump(result, f, protocol=pickle.HIGHEST_PROTOCOL)

    return result


def handle_command(msg):
    'handle_command'
    match msg:
        case {'symbol': 'ETHBTC', **rest}:
            print(rest)
        case _:
            pass


def run():
    'main function'
    print('start')
    res = fetch_test_data('https://api4.binance.com/api/v3/ticker/24hr')
    print(len(res))
    # print(f'res: {res[:3]}')

    for r in res:
        handle_command(r)
    print('end')


if __name__ == '__main__':
    run()
