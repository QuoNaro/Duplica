import socket
from pathlib import Path
import json

class DuplicaTFCC:
    def __init__(self, host : str = '127.0.0.1', port: int = 39700) -> None:
        self.socket = socket.socket()
        self._ip : str = host
        self._port : int = port
      
    def make_request(self, sfp: Path , cfp : Path) -> bytes :
        json_bytes = json.dumps(
            {
            'sfp' : sfp,
            'cfp' : cfp
            }
        ).encode('UTF-8')
        return json_bytes

    def send_request(self, request : bytes) -> dict:
    
        self.socket.connect( (self._ip,self._port) )
        self.socket.send(request)

        with open('file.zip', "wb") as file:
            print("Получение данных от сервера...")
            while True:
                data = self.socket.recv(1024)  # Получаем данные от сервера
                if not data:
                    break  # Если данных больше нет, выходим из цикла
                file.write(data)  # Записываем данные в файл
                
        self.socket.close()
    
   
if __name__ == '__main__':
    client = DuplicaTFCC('localhost',39700)
    req = client.make_request('/home/','/path/')
    client.send_request(req)
        