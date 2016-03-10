/**
 * Created by ORusak on 09.03.2016.
 */
'use strict';

const staticServer = require('node-static');

//
// Create a node-static server instance to serve the './public' folder
//
let file = new staticServer.Server('./public');

require('http').createServer(function (request, response) {
    request.addListener('end', function () {
        //
        // Serve files!
        //
        file.serve(request, response);
    }).resume();
}).listen(3000);