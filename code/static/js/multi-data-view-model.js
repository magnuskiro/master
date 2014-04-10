/**
 * Created by kiro on 20/01/14.
 */

var D3KD = this.D3KD || {};

(function (namespace) {
    "use strict";
    namespace.multiDataViewModel = function() {
        var self = this;


        // initialize the data array for the graph
        self.multiChartData = ko.observableArray([
            {date: "1-May-12", price: 582.13, volume: 1, pos: 402.13, neg: 500, sentiment: 1062.13, trend: 692.13},
            {date: "30-Apr-12", price: 583.98, volume: 500, pos: 402.13, neg: 500, sentiment: 1092.13, trend: 692.13},
            {date: "27-Apr-12", price: 603.00, volume: 500, pos: 402.13, neg: 500, sentiment: 1062.13, trend: 692.13},
            {date: "26-Apr-12", price: 607.70, volume: 500, pos: 402.13, neg: 500, sentiment: 1062.13, trend: 692.13},
            {date: "25-Apr-12", price: 610.00, volume: 500, pos: 402.13, neg: 500, sentiment: 1022.13, trend: 692.13},
            {date: "24-Apr-12", price: 560.28, volume: 500, pos: 402.13, neg: 500, sentiment: 1062.13, trend: 692.13},
            {date: "23-Apr-12", price: 571.70, volume: 500, pos: 402.13, neg: 500, sentiment: 1132.13, trend: 692.13},
            {date: "20-Apr-12", price: 572.98, volume: 500, pos: 402.13, neg: 500, sentiment: 1262.13, trend: 692.13},
            {date: "19-Apr-12", price: 587.44, volume: 500, pos: 402.13, neg: 500, sentiment: 1162.13, trend: 692.13},
            {date: "18-Apr-12", price: 608.34, volume: 500, pos: 402.13, neg: 500, sentiment: 1062.13, trend: 692.13},
            {date: "17-Apr-12", price: 609.70, volume: 500, pos: 402.13, neg: 500, sentiment: 1092.13, trend: 692.13},
            {date: "16-Apr-12", price: 580.13, volume: 500, pos: 402.13, neg: 500, sentiment: 1062.13, trend: 692.13},
            {date: "13-Apr-12", price: 605.23, volume: 1500, pos: 402.13, neg: 500, sentiment: 1072.13, trend: 692.13}
        ]
        );

        self.test = ko.observableArray([
            {date: "13-Apr-12", price: 605.23, volume: 1500, pos: 402.13, neg: 500, sentiment: 472.13, trend: 492.13}
        ]
        );

        // create new datapoint for the graph
        var addMultiDataPoint = function(){
            $.get(
                "/trend_data",
                function(data) {
                    //return self.multiChartData.push(data);
                    //alert(data);
                    //return {date: "13-Apr-12", price: 605.23, volume: 1500, pos: 402.13, neg: 500, sentiment: 472.13, trend: 492.13}
                    console.log(data.date);
                    //var json = JSON.stringify(eval("(" + data + ")"));
                    //console.log(json);
                    self.test.push(data);
                }
            );
            console.log(self.test.length);
            //return self.test.push({date: "13-Apr-12", price: 605.23, volume: 1500, pos: 402.13, neg: 500, sentiment: 472.13, trend: 492.13});
            return;
        };

        // update the graph at intervals
        setInterval(addMultiDataPoint, 2000);
        //addMultiDataPoint()
    };
}(D3KD));
