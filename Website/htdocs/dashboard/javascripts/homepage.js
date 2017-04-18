function insertRow(rate)
{
	var table = document.getElementById("botTable");
	var row = table.insertRow(0);
	row.style.border = "1px solid black";
	var cell = row.insertCell(0);
	var cell2 = row.insertCell(1);
	var imageCell = row.insertCell(2);

// Set up cell 1 components including the bot name, author, download link and description
	var name = document.createElement("h3");
	var nameNode = document.createTextNode("Default Bot");
	name.appendChild(nameNode);
	cell.appendChild(name);

	// Author
	var author = document.createElement("p");
	var authorNode = document.createTextNode("Author");
	author.appendChild(authorNode);
	cell.appendChild(author);

	// Download Link
	var download = document.createElement("a");
	var downloadNode = document.createTextNode("Download");
	download.appendChild(downloadNode);
	download.href="/dashboard/bots/exampleBot.zip";
	cell.appendChild(download);

// Set up cell 2 components including the ratings and the number of downloads
	var rating = document.createElement("p");
	var ratingNode = document.createTextNode("Rating (0 votes): ");
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

// Set up the image cell components
	var image = document.createElement("img");
	image.src = "/dashboard/images/mario.png";
	image.style.width="100px";
	image.style.height="100px";
	imageCell.appendChild(image);
}