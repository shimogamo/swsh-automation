#!/usr/bin/env python3
import argparse
from datetime import datetime, timedelta
from utils import get_logger
from pad import GamePad


logger = get_logger(__name__)


def main():
    today = datetime.now()
    parser = argparse.ArgumentParser()
    parser.add_argument('port', type=str)
    parser.add_argument('frame', type=int)
    parser.add_argument('year', type=int, nargs='?', default=today.year)
    parser.add_argument('month', type=int, nargs='?', default=today.month)
    parser.add_argument('day', type=int, nargs='?', default=today.day)
    parser.add_argument('-d', '--delay', type=int, default=5)
    args = parser.parse_args()

    pad = GamePad(args.port)
    current = datetime(args.year, args.month, args.day)
    # 遅延を入れる
    logger.info(f'{args.delay}秒の遅延を入れています…（--delayで指定可能）')
    pad.press('Button X').pause(args.delay)
    try:
        i = args.frame - 3
        last = datetime(args.year, args.month+1, 1) - timedelta(days=1)
        last = last.day
        current = current.day
        while i > 0:
            pad.press('LX MIN', .040, .035)
            pad.press('LX MIN', .040, .035)
            pad.press('LX MIN', .040, .035)
            pad.press('LY MIN', .040, .035)  # 日
            current += 1
            if current <= last:
                i -= 1
            else:
                current = 1
            logger.info(f'日：{current:02d} 消費：{args.frame-3-i} 残り：{i+3}')
            pad.press('LX MAX', .040, .035)
            pad.press('LX MAX', .040, .035)
            pad.press('LX MAX', .040, .035)
            pad.press('Button A', .045, .125)
            pad.press('Button A', .045, .125)
        pad.close()
    except KeyboardInterrupt:
        pad.close()


if __name__ == '__main__':
    main()
