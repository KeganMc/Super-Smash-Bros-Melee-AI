function registrationCheck(){
    var emailText = document.forms["registration"]["email"].value;
	var passText = document.forms["registration"]["password"].value;
	var passCheckText = document.forms["registration"]["passwordCheck"].value;
	var warning = document.getElementById("warning");
	var emailLabel = document.getElementById("emailLabel");
	warning.style.color = "red";
	
	var re = /^(([^<>()\[\]\\.,;:\s@"]+(\.[^<>()\[\]\\.,;:\s@"]+)*)|(".+"))@((\[[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}])|(([a-zA-Z\-0-9]+\.)+[a-zA-Z]{2,}))$/;
	
	if(emailText == ""){
	  emailLabel.style.color = "red";
	  emailLabel.innerHTML = "Email: (Required Field)";
	  return false;
	}
	else if(!re.test(emailText))
	{
	  emailLabel.style.color = "red";
	  emailLabel.innerHTML = "Invalid Email Address";
	  return false;
	}
	
	if(passText == ""){
	  var passLabel = document.getElementById("passwordLabel");
	  passLabel.style.color = "red";
	  passLabel.innerHTML = "Password: (Required Field)";
	  return false;
	}
	if(passCheckText == ""){
	  var passCheckLabel = document.getElementById("passwordCheckLabel");
	  passCheckLabel.style.color = "red";
	  passCheckLabel.innerHTML = "Password Confirmation: (Required Field)";
	  return false;
	}
	if(passText != passCheckText)
	{
	  warning.innerHTML = "Warning: Passwords must be identical"
      return false;
	}
	return true;
}

function emailChange()
{
	var emailLabel = document.getElementById("emailLabel");
	
	emailLabel.style.color = "black";
	emailLabel.innerHTML = "Email:";
}

function passChange()
{
	var passLabel = document.getElementById("passwordLabel");
	var warning = document.getElementById("warning");
	
	passLabel.style.color = "black";
	passLabel.innerHTML = "Password:";
	warning.innerHTML = "";
}

function passCheckChange()
{
	var passCheckLabel = document.getElementById("passwordCheckLabel");
	var warning = document.getElementById("warning");
	
	passCheckLabel.style.color = "black";
	passCheckLabel.innerHTML = "Password Confirmation:";
	warning.innerHTML = "";
}

/**
* Warns user that the email already esits in database
*/
function userAlreadyExists()
{
	var warning = document.getElementById("warning");
	warning.style.color = "red"; 

	warning.innerHTML = "Warning: Email already exists";
}

function userRegistered()
{
	var warning = document.getElementById("warning");
	warning.style.color = "#660066"; 

	warning.innerHTML = "User Registered!";
}

function userRegistrationError()
{
	var warning = document.getElementById("warning");
	warning.style.color = "red"; 

	warning.innerHTML = "Warning: Error adding user to the database";
}