void main() {
  print('We are getting data...');
  httpGet('https://api.nasa.com/rockets').then((data) {
    print(data);
  });
  print('Last line');
}

Future<String> httpGet(String url) {
  return Future.delayed(Duration(seconds: 4), () {
    return '<Future> Hello World';
  });
}
