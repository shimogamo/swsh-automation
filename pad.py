from time import sleep
from serial import Serial
from utils import get_logger


logger = get_logger(__name__)


class GamePad(object):

    def __init__(self, port):
        self._port = port
        logger.info(f'ポート使用：{port}')
        self._ser = Serial(port)

    def press(self, cmd, duration1=.045, duration2=.035, show_log=False):
        self._ser.write(f'{cmd}\r\n'.encode('utf-8'))
        sleep(duration1)
        self._ser.write('RELEASE\r\n'.encode('utf-8'))
        sleep(duration2)
        if show_log:
            logger.info(f'{cmd}')
        return self

    def repeat(self, cmd, n, duration1=.045, duration2=.035):
        for i in range(n):
            self.press(cmd, duration1, duration2)
        return self

    @staticmethod
    def pause(duration):
        sleep(duration)

    def close(self):
        self._ser.write('RELEASE\r\n'.encode('utf-8'))
        logger.info(f'ポート閉鎖：{self._port}')
        self._ser.close()
