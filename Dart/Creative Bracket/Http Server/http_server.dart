import "dart:io";

void main() {
  HttpServer.bind("localhost", 8080).then((HttpServer server) {
    server.listen((HttpRequest request) {
      request.response.write(write());
      request.response.close();
    });
  });
}

String write() => "This is my first line on the Dart HTTP Server";
