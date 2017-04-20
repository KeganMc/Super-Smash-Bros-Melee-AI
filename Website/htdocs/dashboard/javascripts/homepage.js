function insertRow(botName, auth, stageName, rate, votes, downloads, time, character)
{
	var table = document.getElementById("botTable");
	var row = table.insertRow(0);
	row.style.border = "1px solid black";
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
	var downloadNode = document.createTextNode("Download");
	download.appendChild(downloadNode);
	download.href="/dashboard/bots/exampleBot.zip";
	cell.appendChild(download);

// Set up cell 2 components including the ratings and the number of downloads
	var rating = document.createElement("p");
	var ratingNode = document.createTextNode("Rating ("+votes+" votes): ");
	rating.appendChild(ratingNode);
	cell2.appendChild(rating);

	// Star pictures
	for(var i = 0; i < rate; i++){
		var star = document.createElement("img");
		star.src = "/dashboard/images/star.png";
		star.style.width="50px";
		star.style.height="50px";
		cell2.appendChild(star);
	}

	// Total Downloads
	var totalDownloads = document.createElement("p");
	var totalNode = document.createTextNode("Total Downloads: 0");
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
}