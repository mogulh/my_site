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
		register(email, type);
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
		type = 'noweb';
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
	console.log(type)

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

function submitMessage(){

	email = $('#enqEmail').val();
	name = $('#name').val();
	service = $('#service option:selected').text();
	message = $('#message').val();


	if (name ==""){
		alert("please provide your name")
		return;
	}
	if (message ==""){
		alert("please input a message")
		return;
	}

	if(!IsEmail(email)){
		alert("please provide a valid email address")
		return;
        }

	csrftoken = getCookie('csrftoken')

    $.ajax({
    url: '/inquiry/',
    method: 'POST',
    headers: {'X-CSRFToken': csrftoken},
    data: JSON.stringify({
    	email:email,
    	service:service,
    	message:message,
        name:name}),
    contentType: "application/json",
    dataType: "json",
    success:function(e){
    	if (e.status ==1){
    		alert('Your message has been successfully recieved')
    		window.location='/'

    	}

    }

    })

}


function sendOne(){
	biz = $('#biz').val();
	industry = $('#industry').val();
	channels = $('#channels').val();
	ads = false
	if ($('#ads').is(":checked")){
		ads = true;
	}
	stage = $('#stage option:selected').text();

	csrftoken = getCookie('csrftoken')


	$.ajax({
    url: '/biz/',
    method: 'POST',
    headers: {'X-CSRFToken': csrftoken},
    data: JSON.stringify({biz:biz,
					    	industry:industry,
					    	channels:channels,
					    	ads:ads,
					    	stage:stage}),
    contentType: "application/json",
    dataType: "json",
    success:function(e){
    	if (e.status ==1){
    		console.log('success')

    		$('#step1').css("display", "none")

    		$('#step2').removeAttr("style")

    	}

    }

    })



}

function validURL(str) {
  var pattern = new RegExp('^(https?:\\/\\/)?'+ // protocol
    '((([a-z\\d]([a-z\\d-]*[a-z\\d])*)\\.)+[a-z]{2,}|'+ // domain name
    '((\\d{1,3}\\.){3}\\d{1,3}))'+ // OR ip (v4) address
    '(\\:\\d+)?(\\/[-a-z\\d%_.~+]*)*'+ // port and path
    '(\\?[;&a-z\\d%_.~+=-]*)?'+ // query string
    '(\\#[-a-z\\d_]*)?$','i'); // fragment locator
  if (!pattern.test(str)){
  	return false;

  }
  else 
  	{
  		return true;
  	}

  }


$(document).on("submit", "form", function(e){
    e.preventDefault();
    return  false;
});


function sendTwo(){
	domain = $('#domain').val();

	if (!validURL(domain)){
		alert("input a correct domain")
		return;

	}


	status = $('#status option:selected').text();

	csrftoken = getCookie('csrftoken')


	$.ajax({
    url: '/dom/',
    method: 'POST',
    headers: {'X-CSRFToken': csrftoken},
    data: JSON.stringify({domain:domain,
					    	status:status}),
    contentType: "application/json",
    dataType: "json",
    success:function(e){
    	if (e.status ==1){
    		console.log('success')

    		$('#step2').css("display", "none")

    		$('#step3').removeAttr("style")

    	}

    }

    })
}

function sendThree(){
	target = $('#target').val();
	duration = $('#duration').val();
	start = $('#start').val();


	target_type = $('#type option:selected').text();
	duration_type = $('#duration_type option:selected').text();
	start_type = $('#start_type option:selected').text();

	csrftoken = getCookie('csrftoken')


	$.ajax({
    url: '/vision/',
    method: 'POST',
    headers: {'X-CSRFToken': csrftoken},
    data: JSON.stringify({start:start,
					    	target:target,
					    	duration:duration,
					    	target_type:target_type,
					    	duration_type:duration_type,
					    	start_type:start_type}),
    contentType: "application/json",
    dataType: "json",
    success:function(e){
    	if (e.status ==1){
    		console.log('success')
    		alert('Your application has been successfully recieved')

    		setTimeout(
 				 function() 
  						{
  							window.location = '/'
						   		 //do something special
						  }, 500)

    		

    	}

    }

    })



}