/**
 * Created by kiro on 20/01/14.
 */

var D3KD = this.D3KD || {};

(function (namespace) {
    "use strict";
    namespace.dataViewModel = function() {
        var self = this;

        // create new datapoint for the graph
        var addLineDataPoint = function(){
            // todo get new data points from api
            return self.lineChartData.push({date: new Date(), close: Math.random()*1000+500})
        };

        // initialize the data array for the graph
        self.lineChartData = ko.observableArray([
            {date: new Date(), close: Math.random()*100}
            ]
        );

        // update the graph at intervals
        setInterval(addLineDataPoint, 2000);
    };
}(D3KD));