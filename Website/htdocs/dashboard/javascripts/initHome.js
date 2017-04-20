function initHome()
{
  var xhttp = new XMLHttpRequest();
  xhttp.onreadystatechange = function() {
    if (this.readyState == 4 && this.status == 200) {
      var count = this.responseText;
      for(var i=1;i<=count;i++)
      {
        xhttp.onreadystatechange = function() {
          if (this.readyState == 4 && this.status == 200) {
            var botString = this.responseText;
            var botArray = botString.split(",");
            insertRow(botArray[0],botArray[1],botArray[2],botArray[3],botArray[4],botArray[5],botArray[6],botArray[7]);
          }
        };
        xhttp.open("GET", "/dashboard/PHP/loadHomepage.php?count=" + i, true);
        xhttp.send();
      }
    }
  };
  xhttp.open("GET", "/dashboard/PHP/saveCount.php", true);
  xhttp.send();
}