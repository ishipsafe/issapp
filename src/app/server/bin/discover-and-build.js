var path = require('path');
var app = require(path.resolve(__dirname, '../server'));

var dataSource = app.dataSources.pg;

dataSource.discoverAndBuildModels('account', {schema: 'public'},
    function(err, models) {
  if (err) throw err;

  models.Account.find(function(err, accounts) {
    if (err) return console.log(err);

    console.log(accounts);

    dataSource.disconnect();
  });
});
