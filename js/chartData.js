function formatDate(d){
  var hours = d.getHours();
  var minutes = d.getMinutes();
  minutes = minutes < 10 ? '0'+minutes : minutes;
  var strTime = hours + ':' + minutes;
  return d.getMonth()+1 + "/" + d.getDate() + "/" + d.getFullYear() + "  " + strTime;
}

var arr = JSON.parse(data);
var arrDates = []
var arrDownloads = []
var arrUploads = []


for (var key in arr) {
  if (arr.hasOwnProperty(key)) {
    //alert(key + " -> " + arr[key]['ping']);
    var d = new Date(0);
    d.setUTCSeconds(key);
    arrDates.push(formatDate(d));
    arrDownloads.push(arr[key]['download']);
    arrUploads.push(arr[key]['upload'])
  }
}

var lineChartData = {
  labels : arrDates,//["January","February","March","April","May","June","July","January","February","March","April","May","June"],
  datasets : [
    {
      label: "Mbps Down",
      fillColor : "rgba(220,220,220,0.2)",
      strokeColor : "rgba(220,220,220,1)",
      pointColor : "rgba(220,220,220,1)",
      pointStrokeColor : "#fff",
      pointHighlightFill : "#fff",
      pointHighlightStroke : "rgba(220,220,220,1)",
      data : arrDownloads//[randomScalingFactor(),randomScalingFactor(),randomScalingFactor(),randomScalingFactor(),randomScalingFactor(),randomScalingFactor(),randomScalingFactor(),randomScalingFactor(),randomScalingFactor(),randomScalingFactor(),randomScalingFactor(),randomScalingFactor(),randomScalingFactor(),randomScalingFactor()]
    },
    {
      label: "Mbps Up",
      fillColor : "rgba(151,187,205,0.2)",
      strokeColor : "rgba(151,187,205,1)",
      pointColor : "rgba(151,187,205,1)",
      pointStrokeColor : "#fff",
      pointHighlightFill : "#fff",
      pointHighlightStroke : "rgba(151,187,205,1)",
      data : arrUploads//[randomScalingFactor(),randomScalingFactor(),randomScalingFactor(),randomScalingFactor(),randomScalingFactor(),randomScalingFactor(),randomScalingFactor(),randomScalingFactor(),randomScalingFactor(),randomScalingFactor(),randomScalingFactor(),randomScalingFactor(),randomScalingFactor(),randomScalingFactor()]
    }
  ]

}
