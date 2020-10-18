void main() async {
  print('We are getting data...');
  print(await httpGet('https://api.nasa.com/rockets'));
  print('Last line');
}

Future<String> httpGet(String url) {
  return Future.delayed(Duration(seconds: 4), () {
    return '<Future> Hello World';
  });
}
