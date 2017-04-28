function alterButtonText(buttonIndex, text)
{
	var button = document.getElementById("button2");
	if(buttonIndex == 1)
	{
		button = document.getElementById("button1");
	}
	button.value = text.toString();
	button.style.backgroundColor = "grey";
	return false;
}

function uploadBot()
{
	//alert("The form was submitted");
	var name = document.getElementById("botName").value;
	var character = document.getElementById("button1").value;
	var stage = document.getElementById("button2").value;
	var description = document.getElementById("description").value;

  var xhttp = new XMLHttpRequest();
  xhttp.onreadystatechange = function() {
    if (this.readyState == 4 && this.status == 200) {
      location.reload();
    }
  };
  xhttp.open("GET", "/dashboard/PHP/upload.php?name=" + name + "&character=" + character + "&stage=" + stage + "&description=" + description, true);
  xhttp.send();
}