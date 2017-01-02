document.addEventListener("DOMContentLoaded", function(event) {
	document.querySelector('.body').onchange = function(evt) {
		console.log(evt.target);
		console.log(evt.target.name);
		console.log(evt.target.value);
		
		// range elements have not the property checked and must not be 
		// deleted from cookie but instead set to 0 if deactivated
		// radio buttons must have some value and are not deleted either
		if (evt.target.type == 'range' || evt.target.type == 'radio') {
			setCookie(evt.target.name, evt.target.value);
			console.log('yes');
		}
		// all other elements are checkboxes and
		// are deleted from cookie if deactivated
		else {
			var checkbox_name = evt.target.name;
			deleteCookie(checkbox_name);

			var list_of_checkbox_nodes = document.getElementsByName(evt.target.name);
			var i;
			var list_of_values = [];
			var combined_string = '';
			for (i = 0; i < list_of_checkbox_nodes.length; i++) {
				if (list_of_checkbox_nodes[i].checked) {
					list_of_values.push(list_of_checkbox_nodes[i].value);
				}
			}
			setCookie(checkbox_name, list_of_values.join());
		}
	};
	
	// Toggle visibility of all UI elements like buttons, checkboxes etc.
    if (document.getElementById("hide_form_button") !== null) {
		document.getElementById('hide_form_button').onclick=function(){
			document.getElementById('configure').style.display = (document.getElementById('configure').style.display == 'none') ? 'block' : 'none';
			document.getElementById('hide_form_button').innerHTML = (document.getElementById('hide_form_button').innerHTML == "Show controls") ? "Hide controls" : "Show controls";
		};
	}
    if (document.getElementById("enable_cookies") !== null) {
		document.getElementById("enable_cookies").click(function() {
			// if checked
			setCookie('allowCookies', 'True');
			// else
			// deleteCookie('allowCookies');
		});
	}
});

function deleteCookie(cname) {
    document.cookie = cname + "=;expires=Thu, 01 Jan 1970 00:00:00 UTC;path=/";
}

function setCookie(cname, cvalue) {
    var d = new Date();
    d.setTime(d.getTime() + (1000 * 24 * 60 * 60 * 1000)); // 3 years or so
    var expires = "expires="+d.toUTCString();
    document.cookie = cname + "=" + cvalue + ";" + expires + ";path=/";
}

function getCookie(cname) {
    var name = cname + "=";
    var ca = document.cookie.split(';');
    for(var i = 0; i < ca.length; i++) {
        var c = ca[i];
        while (c.charAt(0) == ' ') {
            c = c.substring(1);
        }
        if (c.indexOf(name) == 0) {
            return c.substring(name.length, c.length);
        }
    }
    return "";
}
