from http.server import SimpleHTTPRequestHandler, HTTPServer

# Создаем класс-обработчик запросов, унаследованный от SimpleHTTPRequestHandler
class CORSRequestHandler(SimpleHTTPRequestHandler):
    def end_headers(self):
        self.send_header('Access-Control-Allow-Origin', '*') # Разрешаем доступ со всех доменов
        super().end_headers()

# Запускаем HTTP-сервер
def run(server_class=HTTPServer, handler_class=CORSRequestHandler, port=8000):
    server_address = ('', port)
    httpd = server_class(server_address, handler_class)
    print(f'Сервер запущен на порту {port}')
    httpd.serve_forever()

if __name__ == '__main__':
    run()