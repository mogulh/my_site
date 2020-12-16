function getCookie(name) {
    let cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        const cookies = document.cookie.split(';');
        for (let i = 0; i < cookies.length; i++) {
            const cookie = cookies[i].trim();
            // Does this cookie string begin with the name we want?
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}


function haveweb(){
	email = $('#myEmail').val();

	if(IsEmail(email)==false){
		alert("please provide a valid email address")
		return;
        }

	if (email ==""){
		alert("please provide an email address")

	}
	else{
		console.log("I have a website");
		type = 'hasweb';
		register(email);
	}
	
	

}

function noweb(){
	email = $('#myEmail').val();

	if(IsEmail(email)==false){
		alert("please provide a valid email address")
		return;
        }

	if (email ==""){
		alert("please provide an email address")
	}
	else{
		console.log("I dont have a website");
		type = 'noweb'
		register(email, type)

	}
	

}



function IsEmail(email) {
  var regex = /^([a-zA-Z0-9_\.\-\+])+\@(([a-zA-Z0-9\-])+\.)+([a-zA-Z0-9]{2,4})+$/;
  if(!regex.test(email)) {
    return false;
  }else{
    return true;
  }
}


function register(email, type){
	console.log(email)

	csrftoken = getCookie('csrftoken')

    $.ajax({
    url: '/register/',
    method: 'POST',
    headers: {'X-CSRFToken': csrftoken},
    data: JSON.stringify({email:email, type:type}),
    contentType: "application/json",
    dataType: "json",
    success:function(e){
    	if (e.status ==1){
    		window.location= '/start/'

    	}

    }

    })
    
   



}
