module.exports = function(Subscriber){

  Subscriber.subscribe = function(email, type, cb){

    var nodemailer = require('nodemailer');
    fs = require('fs')
    console.log(type);
    templateContent = fs.readFileSync(require('path').resolve(__dirname, 'email.html'), encoding="utf8");

    var transporter = nodemailer.createTransport({
        service: 'gmail',
        auth: {
            user: 'ishipsafe@gmail.com',
            pass: 'goship#123'
        }
    });
    if (!type){
      type = 'flyer';
    }
    var sub = {
      email: email,
      type: type
    }
    Subscriber.create(sub, function(err, instance){
      console.log(err);
      if (err && err.code == 23505){
        console.log(err);
        response = "User already subscribed."
        cb(null, response);
      }else if(err){
        console.log(err);
        response = "Oops something went wrong. Please try again after sometime."
        cb(null, response);
      }else{
        transporter.sendMail({
            from: 'ishipsafe@gmail.com',
            to: email,
            subject: 'Welcome to iShipSafe',
            html: templateContent
        });
        response = "Subscribed successfully.";
        cb(null, response);
      }
    });

  }

  Subscriber.remoteMethod(
    'subscribe', {
      http: {path: '/subscribe', verb: 'get'},
      accepts: [{arg: 'email', type: 'string', http: {source: 'query'}}, {arg: 'type', type: 'string', http: {source: 'query'}}],
      returns: {arg: 'status', type: 'string'}
    }
  )
};
