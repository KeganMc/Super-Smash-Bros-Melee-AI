function insertBot(botName, auth, stageName, rate, votes, downloads, time, character, description)
{
	var table = document.getElementById("botTable");
	var row = table.insertRow(0);
	row.style.borderTop = "1px solid black";
	var cell = row.insertCell(0);
	var cell2 = row.insertCell(1);
	var imageCell = row.insertCell(2);

// Set up cell 1 components including the bot name, author, download link and description
	var name = document.createElement("h2");
	var nameNode = document.createTextNode(botName);
	name.appendChild(nameNode);
	cell.appendChild(name);

	// Author
	var author = document.createElement("p");
	var authorNode = document.createTextNode("Author: "+auth);
	author.appendChild(authorNode);
	cell.appendChild(author);

	// Stage
	var stage = document.createElement("p");
	var stageNode = document.createTextNode(stageName);
	stage.appendChild(stageNode);
	cell.appendChild(stage);

	// Download Link
	var download = document.createElement("BUTTON");
	var link = document.createElement("a");
	var dExtension = ".zip";
	var dDir = "/dashboard/bots/";
	//var dUrl = dDir.concat(botName, dExtension);
	var dUrl = dDir.concat("exampleBot",dExtension);
	link.href = dUrl;
	link.text = ("Download");
	link.style.color="white";
	link.style.textDecoration="none";
	link.onclick = function(){
		downloadClicked(botName, downloads);
	}
	download.appendChild(link);
	cell.appendChild(download);

// Set up cell 2 components including the ratings and the number of downloads
	var rating = document.createElement("p");
	var ratingNode = document.createTextNode("Rating ("+votes+" votes): ");
	rating.appendChild(ratingNode);
	cell2.appendChild(rating);

//------------------------------------------------------------------------------------------------------------
	// Star pictures
	var star = new Array();
	for(var i = 0; i < 10; i++)
	{
		star[i] = document.createElement("img");
		star[i].style.width="25px";
		star[i].style.height="50px";
		star[i].id=botName+i;
		star[i].addEventListener("mouseenter", function(e){
			var id = e.target.id;
			var botName = id.substring(0,id.length-1);
			var index = id.charAt(id.length-1);
			if(index%2==0){ // Even
				e.target.src = "/dashboard/images/starLeft.png";
			}
			else{
				e.target.src = "/dashboard/images/starRight.png";
			}

			for(var i = 0; i < 10; i++)
			{
				if(i <= index){
					if(i%2==0){ // Even
						document.getElementById(botName+i).src = "/dashboard/images/starLeft.png";
					}
					else{
						document.getElementById(botName+i).src = "/dashboard/images/starRight.png";
					}
				}
				else
				{
					if(i%2==0){ // Even
						document.getElementById(botName+i).src = "/dashboard/images/starEmptyLeft.png";
					}
					else{
						document.getElementById(botName+i).src = "/dashboard/images/starEmptyRight.png";
					}
				}
			}
		});
		star[i].addEventListener("click", function(e){
			var id = e.target.id;
			var botName = id.substring(0,id.length-1);
			var index = id.charAt(id.length-1);

			addRating(botName, (parseInt(index)+1).toString());
		});
		if(i < rate){
			if(i%2==0){ // Even
				star[i].src = "/dashboard/images/starLeft.png";
			}
			else{
				star[i].src = "/dashboard/images/starRight.png";
			}
		}
		else
		{
			if(i%2==0){ // Even
				star[i].src = "/dashboard/images/starEmptyLeft.png";
			}
			else{
				star[i].src = "/dashboard/images/starEmptyRight.png";
			}
		}
		cell2.appendChild(star[i]);
	}

	// Total Downloads
	var totalDownloads = document.createElement("p");
	var totalNode = document.createTextNode("Total Downloads: " + downloads);
	totalDownloads.appendChild(totalNode);
	cell2.appendChild(totalDownloads);

	// Time Created
	var timeCreated = document.createElement("p");
	var timeNode = document.createTextNode("Time created: "+time.toString());
	timeCreated.appendChild(timeNode);
	cell2.appendChild(timeCreated);

// Set up the image cell components
	var image = document.createElement("img");
	var extension = ".jpg";
	var dir = "/dashboard/images/characters/";
	var url = dir.concat(character, extension);
	image.src = url;
	image.style.width="120px";
	image.style.height="150px";
	imageCell.appendChild(image);

	// Set up the description
	var row2 = table.insertRow(1);
	row2.style.borderBottom = "1px solid black";
	var cells = row2.insertCell();
	var desc = document.createElement("p");
	var descNode = document.createTextNode(description);
	desc.appendChild(descNode);
	cells.colSpan="3";
	cells.appendChild(desc);
}

function addRating(botName, rating)
{
  var xhttp = new XMLHttpRequest();
  xhttp.onreadystatechange = function() {
    if (this.readyState == 4 && this.status == 200) {
      location.reload();
    }
  };
  xhttp.open("GET", "/dashboard/PHP/rate.php?name=" + botName + "&rating=" + rating, true);
  xhttp.send();
}