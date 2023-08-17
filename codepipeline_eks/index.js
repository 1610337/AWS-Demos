var http = require('http');
var fs = require('fs');
var uc = require('upper-case')

http.createServer(function (req, res) {
  fs.readFile('./html/index.html', function(err, data) {
    res.writeHead(200, {'Content-Type': 'text/html'});
    res.write(uc.upperCase("Hello World 1!"));
    res.write(data);
    return res.end();
  });
}).listen(3000); 