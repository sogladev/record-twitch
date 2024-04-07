""" Record stream """
from contextlib import contextmanager
from pathlib import Path
import argparse
import datetime as dt
import logging
import os
import time

logger = logging.getLogger(__name__)
logging.basicConfig(format="%(levelname)s:%(message)s", level=logging.INFO)


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
def get_seconds_until_criticalrole() -> int | None:
    """ Calculate seconds until critical role
    if anything goes wrong, default to 0 seconds """
    logger.info("Using selenium to get seconds until CR airs")
    from selenium import webdriver
    from selenium.webdriver.common.by import By
    from selenium.webdriver.firefox.options import Options
    my_url = "http://wheniscriticalrole.com"
    options = Options()
    options.headless = True
    with webdriver.Firefox(options=options) as driver:
        driver.get(my_url)
        try:
            days = int(driver.find_element(By.ID, "days").text)
            hours = int(driver.find_element(By.ID, "hours").text)
            minutes = int(driver.find_element(By.ID, "minutes").text)
            seconds = int(driver.find_element(By.ID, "seconds").text)
            logger.info(
                f"CR Airs in: {days} days, {hours} hours, {minutes} minutes, {seconds} seconds")
            seconds_until_criticalrole = days * 24 * \
                3600 + hours * 3600 + minutes * 60 + seconds
            return seconds_until_criticalrole
        except ValueError:
            logger.error("Failed to parse website")
            return None


def parse_args():
    """ Parse args """
    parser = argparse.ArgumentParser(description="Process arguments")
    parser.add_argument(
        "-u", "--url", dest="url", default="twitch.tv/criticalrole",
        help="url to twitch channel"
    )
    parser.add_argument(
        "-o", "--out", dest="out_dir",
        default=Path.home(),
        help="directory where to save video"
    )
    parser.add_argument(
        "-s", "--sleep", dest="sleep_time", type=int,
        help="time to sleep in seconds before recording starts"
    )
    parser.add_argument(
        "-n", "--now", dest="now", action="store_true",
        help="start recording right now"
    )
    parser.add_argument(
        "--offset", type=int, default=5,
        help="amount of minutes to start recording before stream is online. Default is 5"
    )
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


def record_worker(url):
    """ Call streamlink to record """
    failure_count = 0
    while True:
        time_now = dt.datetime.now()
        cmd = (
            f"streamlink {url} best -o \"{time_now: %Y-%m-%d_ %H-%M-%S}.flv\" "
            + "--force -O --retry-streams 30 --retry-open 9999"
        )
        os.system(cmd)
        failure_count += 1
        if failure_count >= 10: # Assume stream is offline if it fails 10 times in a row
            logger.info("Stream offline or failing to record")
            break
        time.sleep(30)


def main(args):
    """ Set up worker to record CR """
    # Change to the output directory
    with working_directory(Path(args.out_dir)):
        # If not starting immediately, calculate the sleep time
        if not args.now:
            if args.sleep_time is not None:
                sleep_duration = args.sleep_time
            else:
                # Calculate seconds until CR starts, subtract offset
                sleep_duration = max(
                    0, get_seconds_until_criticalrole()-(args.offset*60))
                if sleep_duration is None:
                    # Log warning if sleep time can't be calculated
                    logger.warning(
                        "Failed to parse website! Input time with -w instead")
            # Log the sleep time
            logger.info(f"Sleep for {sleep_duration:,} seconds")
            time.sleep(sleep_duration)
        # Log a message to indicate recording is starting
        logger.info("Start recording")
        # Call the record worker function
        record_worker(args.url)


if __name__ == "__main__":
    ARGS = parse_args()
    main(ARGS)
