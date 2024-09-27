import socket
from loguru import logger
from pathlib import Path
import sys
import json


        

class DuplicaTFS:
    
    def __init_logger(self):
        """Инициализирование логгеров"""
        # Logging
        logger.remove()
        __log_format = '{time:DD/MM/YY (HH:mm:ss)} | {message}'
        logger.add(Path(__file__).parent / 'dtfs.log', 
                   format=__log_format)
        logger.add(sys.stdout, format='{message}')
    
    @property
    def port(self):
        return self.__port
    
    @port.setter
    def port(self, value):
        self.__port = value    
    
    def __init__(self, port : int = 39700) -> None:
        self.__port = port
        self.socket = socket.socket()
        self.socket.bind( ('', self.__port) )
        self.__init_logger() # Логирование
         
    def is_request(data: bytes) -> bool:
        data_str = data.decode('utf-8')
        request = json.loads(data_str)
        
        return True
    
    
    def start(self):
        """Запуск сервера"""
        logger.info(f"The server is running on port {self.__port}.")
        self.socket.listen(1)
        try:
            while True: 
                connection,addr = self.socket.accept()
                data = connection.recv(1024)
                
                if not data:
                    break
                else :
                    data = json.loads(data.decode('UTF-8'))
                    logger.info(f'Data received from {addr[0]}:\n{data}')
                    connection.send(b'Accepted')
                    
                connection.close()
        except KeyboardInterrupt:
            connection.close()
            self.socket.close()
            

if __name__ == '__main__':
    server = DuplicaTFS()
    server.start()
    
        