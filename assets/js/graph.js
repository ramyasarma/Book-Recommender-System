
var data = [{"letter":"q","presses":1},{"letter":"w","presses":5},{"letter":"e","presses":2}];

var width = 300,
	height = 300,
	// Think back to 5th grade. Radius is 1/2 of the diameter. What is the limiting factor on the diameter? Width or height, whichever is smaller
	radius = Math.min(width, height) / 2;

var color = d3.scaleOrdinal()
	.range(["#2C93E8","#838690","#F56C4E"]);

var pie = d3.pie()
	.value(function(d) { return d.presses; })(data);

var arc = d3.arc()
	.outerRadius(radius - 10)
	.innerRadius(0);

var labelArc = d3.arc()
	.outerRadius(radius - 40)
	.innerRadius(radius - 40);

var svg = d3.select("#pie")
	.append("svg")
	.attr("width", width)
	.attr("height", height)
		.append("g")
		.attr("transform", "translate(" + width/2 + "," + height/2 +")"); 
		// Moving the center point. 1/2 the width and 1/2 the height

var g = svg.selectAll("arc")
	.data(pie)
	.enter().append("g")
	.attr("class", "arc");

g.append("path")
	.attr("d", arc)
	.style("fill", function(d) { return color(d.data.letter);});

g.append("text")
	.attr("transform", function(d) { return "translate(" + labelArc.centroid(d) + ")"; })
	.text(function(d) { return d.data.letter;})
	.style("fill", "#fff");