if (Meteor.isServer) {
    // create routes for all the app.get's and app.all's in bibbase.js
    // (server)
    console.log("setting routes:", routes);
    _.each(routes, function(foo, route) {
        Router.map(function () {
            this.route(route, {
                path: route,
                where: 'server',
                action: function() {
                    this.request.params = this.params;
                    var html = waiter(foo, this.request, this.response);
                    if (!this.response.statusCode) {
                        this.response.statusCode = 200;
                    }
                    if (!this.response.getHeader('Content-Type')) {
                        this.response
                            .setHeader('Content-Type', 'text/html');
                    }
                    this.response.end(html);
                }
            });
        });
    });

}
