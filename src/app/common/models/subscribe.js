module.exports = function(Subscribe){

  Subscribe.subscribe = function(email, type, cb){

    var nodemailer = require('nodemailer');
    fs = require('fs')

    templateContent = fs.readFileSync(require('path').resolve(__dirname, 'email.html'), encoding="utf8");

    var transporter = nodemailer.createTransport({
        service: 'gmail',
        auth: {
            user: 'ishipsafe@gmail.com',
            pass: 'goship#123'
        }
    });
    var sub = {
      email: email,
      type: type
    }
    Subscribe.create(sub, function(err, instance){
      if (err){
        response = "Error while subscribing."
        cb(null, response);
      }
      transporter.sendMail({
          from: 'ishipsafe@gmail.com',
          to: email,
          subject: 'Welcome to iShipSafe',
          html: templateContent
      });
      response = "Subscribed successfully.";
      cb(null, response);
    });

  }

  Subscribe.remoteMethod(
    'subscribe', {
      http: {path: '/subscribe', verb: 'get'},
      accepts: [{arg: 'email', type: 'string', http: {source: 'query'}}, {arg: 'type', type: 'string', http: {source: 'query'}}],
      returns: {arg: 'status', type: 'string'}
    }
  )
};
