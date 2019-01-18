#!/usr/bin/env python3
""" record cr """
from contextlib import contextmanager
from pathlib import Path
import datetime as dt
import argparse
import time
import os


def try_except_default(func):
    def try_except_function(default_return_value, *args, **kwargs):
        try:
            result = func(*args, **kwargs)
        except:
            result = default_return_value
        return result
    return try_except_function


@try_except_default(0)
def seconds_until_criticalrole():
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
    print(f'CR Airs in: {days} days, {hours} hours, {minutes} minutes, {seconds} seconds')
    return days * 24 * 3600 + hours * 3600 + minutes * 60 + seconds


def parse_args():
    parser = argparse.ArgumentParser(description='Process arguments')
    parser.add_argument(
        '-u', '--url', dest='url', default='twitch.tv/geekandsundry',
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
    parser.add_argument(
        '-d', '--duration', dest='record_duration',
        help='duration of recording (in seconds)')
    return parser.parse_args()


@contextmanager
def working_directory(path):
    """Changes working directory and returns to previous on exit."""
    prev_cwd = Path.cwd()
    os.chdir(path)
    try:
        yield
    finally:
        os.chdir(prev_cwd)


def main(args):
    token_arg = f'--twitch-oauth-token {args.token}' if\
            args.token is not None else ''
    with working_directory(Path(args.out_dir)):
        if not args.now:
            if args.time_wait is not None:
                sleep_duration = args.time_wait
            else:
                sleep_duration = seconds_until_criticalrole()-10*60
                if sleep_duration == 0:
                    print('WARNING: Failed to load data! Input time manually')
            print(f'Going to sleep for {sleep_duration} seconds!')
            time.sleep(sleep_duration)
        while(True):
            time_now = dt.datetime.now()
            cmd = (
            f'streamlink {token_arg} {args.url} best -o '
                f'"{time_now:%Y-%m-%d_%H-%M-%S}.flv" '
                '--force -O --retry-streams 30 --retry-open 9999'
            )
            print('Starting recording')
            os.system(cmd)
            time.sleep(30)


if __name__ == '__main__':
    args = parse_args()
    main(args)
    exit(0)
