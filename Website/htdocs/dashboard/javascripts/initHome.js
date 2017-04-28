function initHome()
{
  var count = 0;
  var xhttp = new XMLHttpRequest();
  xhttp.onreadystatechange = function() {
    if (this.readyState == 4 && this.status == 200) {
      var count = this.responseText;
      for(var i=1;i<=count;i++)
      {
        var xhttp2 = new XMLHttpRequest();  
        xhttp2.onreadystatechange = function() {
          if (this.readyState == 4 && this.status == 200) {
            var botString = this.responseText;
            var botArray = botString.split(",");
            insertBot(botArray[0],botArray[1],botArray[2],botArray[3],botArray[4],botArray[5],botArray[6],botArray[7],botArray[8]);
          }
        };
        xhttp2.open("GET", "/dashboard/PHP/loadHomepage.php?count=" + i, true);
        xhttp2.send();
      }
    }
  };
  xhttp.open("GET", "/dashboard/PHP/saveCount.php", true);
  xhttp.send();
}

function downloadClicked(botName, downloads)
{
  var xhttp = new XMLHttpRequest();
  xhttp.onreadystatechange = function() {
    if (this.readyState == 4 && this.status == 200) {
      location.reload();
    }
  };
  xhttp.open("GET", "/dashboard/PHP/download.php?botName=" + botName, true);
  xhttp.send();
}