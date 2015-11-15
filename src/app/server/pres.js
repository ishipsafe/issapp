var express = require('express')
var stylus = require('stylus')
var nib = require('nib')

var app = express()
var bodyParser = require("body-parser");
var json = require('json');
var request = require('request');

function compile(str, path) {
  return stylus(str)
    .set('filename', path)
    .use(nib())
}

app.set('views',  '../client/views')
app.set('view engine', 'jade')
app.use(stylus.middleware(
	{
	src:  '../client'
  	, compile: compile
  	}
 ));

app.use(express.static('../client'))

app.get('/', function (req, res) {
  res.render('index',
  { title : 'Home' }
  )
})

app.get('/subscribe', function (req, res){

    console.log(req.query.email);
    console.log(req.query.type);
    request.get({
        headers: {'content-type' : 'application/json'},
        url:     'http://0.0.0.0:3000/api/Subscribers/subscribe/?email='+req.query.email+'&type='+req.query.type
    }, function(error, response, body){
        console.log(body);
        if(body){
            var ndata = JSON.parse(body);
            console.log(ndata);
            res.render('index',{
              title : 'Home',
              message: ndata.status
            }
            )
        }else{
            console.log("Dude error")
        }

    });
});

//app.listen(3030)
app.listen(80)
