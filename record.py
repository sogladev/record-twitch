#!/usr/bin/env python3
""" record cr """
from pathlib import Path
from contextlib import contextmanager
import datetime as dt
import argparse
import time
import os


def parse_args():
    parser = argparse.ArgumentParser(description='Process arguments')
    parser.add_argument(
        '-u', '--url', dest='url', default='twitch.tv/geekandsundry',
        help='url to twitch channel')
    parser.add_argument(
        '-o', '--out', dest='out_dir',
        default='/home/user/Videos/criticalrole/',
        help='directory where to save video')
    parser.add_argument(
        '-t', '--token', dest='token', help='twitch authentication token')
    parser.add_argument(
        '-w', '--wait', dest='time_wait', type=int, default=0,
        help='wait time (seconds) before start recording')
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
        time.sleep(args.time_wait)
        while(True):
            time_now = dt.datetime.now()
            cmd = (
                f'streamlink {token_arg} {args.url} best -o "{time_now:%Y-%m-%d_%H-%M-%S}.flv" --force '
                '-O --retry-streams 30 --retry-open 9999'
            )
            os.system(cmd)
            time.sleep(30)


if __name__ == '__main__':
    args = parse_args()
    main(args)
    exit(0)
