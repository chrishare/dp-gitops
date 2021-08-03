let hm = require('header-metadata');
let sm = require('service-metadata');

sm.setVar('var://service/mpgw/skip-backside', true);
let successResult = {
    "status": "success"
};

if (sm.protocolMethod === 'POST') {
    session.input.readAsJSON(function (error, data) {

        if (error) {
            console.error('Error on readAsJSON: ' + error);
            hm.response.statusCode = 500;
        } else {
            console.log('Request was: ' + JSON.stringify(data));
            session.output.write(successResult);
            hm.response.statusCode = 200;
            hm.response.set('content-type', 'application/json');
        }
    });
} else {
    session.output.write(successResult);
    hm.response.statusCode = 200;
    hm.response.set('content-type', 'application/json');
}