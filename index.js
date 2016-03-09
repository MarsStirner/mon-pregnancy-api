/**
 * Created by ORusak on 09.03.2016.
 */

const static = require('node-static');

//
// Create a node-static server instance to serve the './public' folder
//
let file = new static.Server('./public');

require('http').createServer(function (request, response) {
    request.addListener('end', function () {
        //
        // Serve files!
        //
        file.serve(request, response);
    }).resume();
}).listen(8080);