function loginCheck(){
    var emailText = document.forms["login"]["email"].value;
	var passText = document.forms["login"]["password"].value;
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