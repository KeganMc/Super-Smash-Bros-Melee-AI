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
	}
	else if(!re.test(emailText))
	{
	  emailLabel.style.color = "red";
	  emailLabel.innerHTML = "Invalid Email Address";
	}
	
	if(passText == ""){
	  var passLabel = document.getElementById("passwordLabel");
	  passLabel.style.color = "red";
	  passLabel.innerHTML = "Password: (Required Field)";
	}
	if(passCheckText == ""){
	  var passCheckLabel = document.getElementById("passwordCheckLabel");
	  passCheckLabel.style.color = "red";
	  passCheckLabel.innerHTML = "Password Confirmation: (Required Field)";
	}
	
	if(passText != passCheckText)
	{
		warning.innerHTML = "Warning: Passwords must be identical"
	}
	
	return false;
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