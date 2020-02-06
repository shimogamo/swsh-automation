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
    parser.add_argument('frame', type=int, nargs='?', default=4)
    parser.add_argument('year', type=int, nargs='?', default=today.year)
    parser.add_argument('month', type=int, nargs='?', default=today.month)
    parser.add_argument('day', type=int, nargs='?', default=today.day)
    parser.add_argument('-d', '--delay', type=int, default=5)
    args = parser.parse_args()

    pad = GamePad(args.port)
    current = datetime(args.year, args.month, args.day)
    # 遅延を入れる
    logger.info(f'{args.delay}秒の遅延を入れています…（--delayで指定可能）')
    pad.press('Button X', .05, args.delay)
    try:
        while True:
            for i in range(args.frame-1):
                pad.press('Button A').pause(5.0)
                pad.press('Button HOME', .1).pause(1.0)
                pad.press('LY MAX')
                pad.repeat('LX MAX', 4)
                pad.press('Button A').pause(1.0)
                pad.repeat('LY MAX', 14)
                pad.press('Button A').pause(1.0)
                pad.repeat('LY MAX', 4)
                pad.press('Button A').pause(1.0)
                pad.repeat('LY MAX', 4)
                pad.press('Button A').pause(1.0)
                tomorrow = current + timedelta(days=1)
                if tomorrow.year != current.year:
                    pad.press('LX MAX')
                    pad.press('LX MAX')
                    pad.press('LY MIN')  # 日
                    pad.press('LX MIN')
                    pad.press('LY MIN')  # 月
                    pad.press('LX MIN')
                    pad.press('LY MIN')  # 年
                    pad.press('LX MAX')
                    pad.press('LX MAX')
                elif tomorrow.month != current.month:
                    pad.press('LX MAX')
                    pad.press('LX MAX')
                    pad.press('LY MIN')  # 日
                    pad.press('LX MIN')
                    pad.press('LY MIN')  # 月
                    pad.press('LX MAX')
                else:
                    pad.press('LX MAX')
                    pad.press('LX MAX')
                    pad.press('LY MIN')  # 日
                pad.press('LX MAX')
                pad.press('LX MAX')
                pad.press('LX MAX')
                pad.press('Button A').pause(1.0)
                current = tomorrow
                logger.info(f'{i+2}日目 現在日時：{current}')
                pad.press('Button B').pause(1.0)
                pad.press('Button B')
                pad.press('Button B').pause(1.0)
                pad.repeat('LX MIN', 4)
                pad.press('LY MIN')
                pad.press('Button A').pause(1.0)
                pad.press('Button B').pause(1.0)
                pad.press('Button A').pause(5.0)
                pad.press('Button A').pause(1.0)
                pad.press('Button A').pause(1.0)
                pad.press('Button A').pause(1.0)
            flag = input('厳選を終えますか？：')
            if flag.lower() == 'y':
                break
            else:
                pad.press('Button HOME', .1).pause(1.0)
                pad.press('Button X').pause(1.0)
                pad.press('Button A').pause(5.0)
                pad.press('Button A').pause(20.0)
                pad.press('Button A').pause(10.0)
                pad.press('Button A').pause(1.0)
        pad.close()
    except KeyboardInterrupt:
        pad.close()


if __name__ == '__main__':
    main()
