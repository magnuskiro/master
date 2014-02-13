/**
 * Created by kiro on 20/01/14.
 */

ko.bindingHandlers.multiChart = {
    init: function(element) {
        "use strict";

        var margin = {top: 20, right: 20, bottom: 30, left: 50},
            elementWidth = parseInt(d3.select(element).style("width"), 10),
            elementHeight = parseInt(d3.select(element).style("height"), 10),
            width = elementWidth - margin.left - margin.right,
            height = elementHeight - margin.top - margin.bottom;

    },
    update: function(element, valueAccessor) {
        "use strict";

        var margin = {top: 20, right: 20, bottom: 30, left: 50},
            elementWidth = parseInt(d3.select(element).style("width"), 10),
            elementHeight = parseInt(d3.select(element).style("height"), 10),
            width = elementWidth - margin.left - margin.right,
            height = elementHeight - margin.top - margin.bottom;

        var x = d3.time.scale()
            .range([0, width]);

        var xVar = d3.scale.ordinal()
            .rangeRoundBands([width, 0], .1);

        var y = d3.scale.linear()
            .range([height, 0]);

        var xAxis = d3.svg.axis()
            .scale(x)
            .orient("bottom");

        var yAxis = d3.svg.axis()
            .scale(y)
            .orient("left");

        // Add the graph to the html. aka make the graph visible on the page.
        var svg = d3.select(element).append("svg")
            .attr("width", width + margin.left + margin.right)
            .attr("height", height + margin.top + margin.bottom)
            .append("g")
            .attr("transform", "translate(" + margin.left + "," + margin.top + ")");

        // map data from datahandler multi-data-vie-model.js
        var data = ko.unwrap(valueAccessor());

        // parsing of date objects.
        var parseDate = d3.time.format("%d-%b-%y").parse;

        // parse all the data and set it to usable objects.
        data.forEach(function(d) {
            d.date = parseDate(d.date);
            d.price = +d.price;
            d.volme = +d.volume;
            d.sentiment = +d.sentiment;
            d.trend = +d.trend;
            d.pos = +d.pos;
            d.neg = +d.neg;
        });

        // data mapping for the price graph.
        var priceLine = d3.svg.price()
            .x(function(d) { return x(d.date); })
            // define what data to map to the y axis.
            .y(function(d) { return y(d.price); });

        // data mapping for the price graph.
        var volumeLine = d3.svg.price()
            .x(function(d) { return x(d.date); })
            // define what data to map to the y axis.
            .y(function(d) { return y(d.volume); });

        // data mapping for the price graph.
        var sentimentLine = d3.svg.price()
            .interpolate("basis")
            .x(function(d) { return x(d.date); })
            // define what data to map to the y axis.
            .y(function(d) { return y(d.sentiment); });

        // data mapping for the price graph.
        var trendLine = d3.svg.price()
            .interpolate("basis")
            .x(function(d) { return x(d.date); })
            // define what data to map to the y axis.
            .y(function(d) { return y(d.trend); });

        // data mapping for the bar elements in the graph.
        var pos = d3.svg.price()
            .x(function(d) { return x(d.date); })
            // define what data to map to the y axis.
            .y(function(d) { return y(d.pos); });

        // data mapping for the bar elements in the graph.
        var neg = d3.svg.price()
            .x(function(d) { return x(d.date); })
            // define what data to map to the y axis.
            .y(function(d) { return y(d.neg); });

        // gather data arrays for use in max-min calculations. (range of the graph)
        var priceMaxMin = d3.extent(data, function(d) { return d.price; });
        var volumeMaxMin = d3.extent(data, function(d) { return d.volume; });
        var posMaxMin = d3.extent(data, function(d) { return d.pos; });
        var negMaxMin = d3.extent(data, function(d) { return d.neg; });
        var sentimentMaxMin = d3.extent(data, function(d) { return d.sentiment; });
        var trendMaxMin = d3.extent(data, function(d) { return d.trend; });

        // set the boundaries of the y dimension of the graph.
        var allData = d3.merge([ priceMaxMin, volumeMaxMin, posMaxMin, negMaxMin, sentimentMaxMin, trendMaxMin ]);

        // setting max and min values to know the range of the graph.
        x.domain(d3.extent(data, function(d) { return d.date; }));
        xVar.domain(data.map(function(d) { return d.date; }));
        y.domain(d3.extent(allData));

        // draw the x axis to the canvas.
        svg.append("g")
            .attr("class", "x axis")
            .attr("transform", "translate(0," + height + ")")
            .call(xAxis);

        // draw the y axis to the canvas.
        svg.append("g")
            .attr("class", "y axis")
            .call(yAxis)
            .append("text")
            .attr("transform", "rotate(-90)")
            .attr("y", 6)
            .attr("dy", ".71em")
            .style("text-anchor", "end")
            .text("Price ($)");

        // to get equal spacing between the bars of the chart.
        var widthOffset = 5;
        // draw the bar chart bars to the canvas
        svg.selectAll(".pos")
            .data(data)
            .enter().append("rect")
            .attr("class", "pos")
            .attr("x", function(d) { return xVar(d.date); })
            // offset reduces the width of the bar on the graph
            .attr("width", xVar.rangeBand()/widthOffset)
            // d.xxx selects the data value of the bar.
            .attr("y", function(d) { return y(d.pos); })
            .attr("height", function(d) { return height - y(d.pos); });

        // draw the bar chart bars to the canvas
        svg.selectAll(".neg")
            .data(data)
            .enter().append("rect")
            .attr("class", "neg")
            // '+(xVar.rangeBand()/offset)' sets the position of the bar. its right besides the pos bar.
            .attr("x", function(d) { return xVar(d.date)+(xVar.rangeBand()/widthOffset); })
            // the offset moves the neg bar to the right of the pos bar.
            .attr("width", xVar.rangeBand()/widthOffset)
            // y(d.neg) selects the part of data(d.neg) to use as y values in the graph.
            .attr("y", function(d) { return y(d.neg); })
            .attr("height", function(d) { return height - y(d.neg); });

        // add the price data svg to the graph.
        svg.append("path")
            .datum(data)
            // defines the css class this price should use.
            .attr("class", "priceLine")
            // select the drawing method to use.
            .attr("d", priceLine);

        // add the volume data svg to the graph.
        svg.append("path")
            .datum(data)
            // defines the css class this price should use.
            .attr("class", "volumeLine")
            // select the drawing method to use.
            .attr("d", volumeLine);

        // add the volume data svg to the graph.
        svg.append("path")
            .datum(data)
            // defines the css class this price should use.
            .attr("class", "sentimentLine")
            // select the drawing method to use.
            .attr("d", sentimentLine);

        // add the volume data svg to the graph.
        svg.append("path")
            .datum(data)
            // defines the css class this price should use.
            .attr("class", "trendLine")
            // select the drawing method to use.
            .attr("d", trendLine);

    }
};
