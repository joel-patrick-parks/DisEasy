/*var data =[{
	"probability": ".0",
	"value": "0"
},	{
	"probability": ".10",
	"value": "10"
},	{
	"probability": ".15",
	"value": "20"
},	{
	"probability": ".25",
	"value": "30"
},	{
	"probability": ".40",
	"value": "40"
},	{
	"probability": ".60",
	"value": "50"
},	{
	"probability": ".40",
	"value": "60"
},	{
	"probability": ".25",
	"value": "70"
},	{
	"probability": ".15",
	"value": "80"
},	{
	"probability": ".10",
	"value": "90"
},	{
	"probability": ".0",
	"value": "100"
}];

//chart size/placement
var vis = d3.select("#testvis"),
	WIDTH = 1000,
	HEIGHT = 500,
	MARGINS = {
		top: 20,
		right: 20,
		bottom: 20,
		left: 50
	};

//setting scales
	var xScale = d3.scaleLinear().range([MARGINS.left, WIDTH - MARGINS.right]).domain([0, 100]);
	var yScale = d3.scaleLinear().range([HEIGHT - MARGINS.top, MARGINS.bottom]).domain([0,1]);

//drawing axis
  var xAxis = d3.axisBottom(xScale).ticks(20);
	var yAxis = d3.axisLeft(yScale);

  vis.append('svg:g')
    .attr('class', 'x axis')
    .attr('transform', 'translate(0,' + (HEIGHT - MARGINS.bottom) + ')')
    .call(xAxis);

  vis.append('svg:g')
    .attr('class', 'y axis')
    .attr('transform', 'translate(' + (MARGINS.left) + ',0)')
    .call(yAxis);


	console.log(" We got Here");*/

  