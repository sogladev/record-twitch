""" Record stream """
# !/usr/bin/env python3
import argparse
import datetime as dt
import os
import time
from contextlib import contextmanager
from pathlib import Path


def try_except_default(func):
    """ Ignore exceptions """
    def try_except_function(default_return_value, *args, **kwargs):
        try:
            result = func(*args, **kwargs)
        except Exception:  # pylint: disable=W0703
            result = default_return_value
        return result
    return try_except_function


@try_except_default(0)
def seconds_until_criticalrole():
    """ Calculate seconds until critical role
    if anything goes wrong, default to 0 seconds """
    from selenium import webdriver
    from selenium.webdriver.firefox.options import Options
    my_url = 'http://wheniscriticalrole.com'
    options = Options()
    options.headless = True
    driver = webdriver.Firefox(options=options)
    driver.get(my_url)
    days = int(driver.find_element_by_id(id_='days').text)
    hours = int(driver.find_element_by_id(id_='hours').text)
    minutes = int(driver.find_element_by_id(id_='minutes').text)
    seconds = int(driver.find_element_by_id(id_='seconds').text)
    print(
        f'CR Airs in: {days} days, {hours} hours,'
        '{minutes} minutes, {seconds} seconds')
    return days * 24 * 3600 + hours * 3600 + minutes * 60 + seconds


def parse_args():
    """ Parse args """
    parser = argparse.ArgumentParser(description='Process arguments')
    parser.add_argument(
        '-u', '--url', dest='url', default='twitch.tv/criticalrole',
        help='url to twitch channel')
    parser.add_argument(
        '-o', '--out', dest='out_dir',
        default=f'/home/{os.getlogin()}/Videos/criticalrole/',
        help='directory where to save video')
    parser.add_argument(
        '-t', '--token', dest='token', help='twitch authentication token')
    parser.add_argument(
        '-w', '--wait', dest='time_wait', type=int,
        help='wait time (seconds) before start recording')
    parser.add_argument(
        '-n', '--now', dest='now', action="store_true",
        help='start recording right now')
    return parser.parse_args()


@contextmanager
def working_directory(path):
    """ Use path as working directory then switch back to prev dir after """
    prev_cwd = Path.cwd()
    os.chdir(path)
    try:
        yield
    finally:
        os.chdir(prev_cwd)


def record_worker(token, url):
    """ Call streamlink to record """
    while True:
        time_now = dt.datetime.now()
        cmd = (
            f'streamlink {token} {url} best -o '
            f'"{time_now:%Y-%m-%d_%H-%M-%S}.flv" '
            '--force -O --retry-streams 30 --retry-open 9999'
        )
        os.system(cmd)
        time.sleep(30)


def main(args):
    """ Set up worker to record CR """
    token = f'--twitch-oauth-token {args.token}' if\
            args.token is not None else ''
    if not args.now:
        if args.time_wait is not None:
            sleep_duration = args.time_wait
        else:
            sleep_duration = seconds_until_criticalrole()-10*60
            if sleep_duration == 0:
                print('WARNING: Failed to parse website! Input time with -w')
        print(f'Sleep for {sleep_duration} seconds!')
        time.sleep(sleep_duration)
    with working_directory(Path(args.out_dir)):
        print('Start recording')
        record_worker(token, args.url)


if __name__ == '__main__':
    ARGS = parse_args()
    main(ARGS)
