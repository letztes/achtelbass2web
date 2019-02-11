document.addEventListener("DOMContentLoaded", function(event) {
	

	// only relevant for start page
	var submit_music_parameters = function() {
		if (document.getElementById("music_parameters") !== null) {
			var music_parameters = document.getElementById('music_parameters');
			music_parameters.submit();
		}

		return;
	} 
	
	// music_parameters section exists only on start page 
    if (document.getElementById("music_parameters") !== null) {
		document.querySelector('#music_parameters').onchange = function(evt) {

			// do not set cookies if user has not enabled cookies
			if (getCookie("enable_cookies") == "") {
				submit_music_parameters();
			}

			toggleCookie(evt);
			submit_music_parameters();
		};
	}
	
	// Toggle visibility of all UI elements like buttons, checkboxes etc.
	// only if the main page is displayed
    if (document.getElementById("hide_form_button") !== null) {
			
		document.getElementById('hide_form_button').onclick=function(){
			document.getElementById('music_parameters').style.display = (document.getElementById('music_parameters').style.display == 'none') ? 'block' : 'none';
			document.getElementById('hide_form_button').innerHTML = (document.getElementById('hide_form_button').innerHTML == "Show controls") ? "Hide controls" : "Show controls";
		};
	}
	
	// this is handled separately because all other ui elements set
	// cookie only if this one was enabled
	// enable_cookies switch exists only on configuration page
	if (document.getElementById("enable_cookies") !== null) {
		document.querySelector('#enable_cookies').onchange = function(evt) {
			
			var configuration_elements = document.getElementsByClassName('configuration');
			if (evt.target.checked) {
				setCookie('enable_cookies', 'on');
				
				//Enable the other configuration setting elements
				for (var i = 0; i < configuration_elements.length; i++) {
					configuration_elements[i].disabled = false;
				}
			}
			else {
				deleteAllCookies();
				
				// Uncheck and disable all other configuration settings
				for (var i = 0; i < configuration_elements.length; i++) {
					
					// Don't want to disable the switch for enabling...
					if (configuration_elements[i].name == 'enable_cookies') {
						continue;
					}
						
					configuration_elements[i].disabled = "disabled";
					if (configuration_elements[i].type == 'checkbox') {
						configuration_elements[i].checked = false;
					}
				}
			}
		}
		document.querySelector('#site_configuration').onchange = function(evt) {
			toggleCookie(evt);
		}
	}
	
	// Prefill the UI elements in the configuration site onload from cookie
	if (document.getElementById("enable_cookies") !== null) {
		var configuration_elements = document.getElementsByClassName('configuration');
		if (getCookie("enable_cookies") == "on") {
			
			for (var i = 0; i < configuration_elements.length; i++) {
				
				// prefill checkbox values
				if (configuration_elements[i].type == 'checkbox') {
					if (getCookie(configuration_elements[i].name) == "on") {
						configuration_elements[i].checked = true;
					}
				}
				
				else {
					if (typeof getCookie(configuration_elements[i].name) !== "undefined") {
						configuration_elements[i].value = getCookie(configuration_elements[i].name);
					}
				}
			}
		}
		else {
			// Disable onload all configuration settings but for enabling
			for (var i = 0; i < configuration_elements.length; i++) {
				
				// Don't want to disable the switch for enabling.
				// Must stay clickable.
				if (configuration_elements[i].name == 'enable_cookies') {
					continue;
				}
					
				configuration_elements[i].disabled = "disabled";
			}
		}
	}
	
});

function toggleCookie(evt) {
	
	// Store parameters onchange to cookie
	
	// range elements have not the property checked and must not be 
	// deleted from cookie but instead set to 0 if deactivated
	// radio buttons must have some value and are not deleted either
	if (evt.target.type == 'range' || evt.target.type == 'radio' || evt.target.type == 'number') {
		setCookie(evt.target.name, evt.target.value);
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
		if (list_of_values.length > 0) {
			setCookie(checkbox_name, list_of_values.join('###'));
		}
	}
	
    return;
}

function deleteCookie(cname) {
    document.cookie = cname + "=;expires=Thu, 01 Jan 1970 00:00:00 UTC;path=/";
    return;
}

function setCookie(cname, cvalue) {
    var d = new Date();
    d.setTime(d.getTime() + (1000 * 24 * 60 * 60 * 1000)); // 3 years or so
    var expires = "expires="+d.toUTCString();
    document.cookie = cname + "=" + cvalue + ";" + expires + ";path=/";
    return;
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



function deleteAllCookies() {
    var cookies = document.cookie.split(";");

    for (var i = 0; i < cookies.length; i++) {
        var cookie = cookies[i];
        var eqPos = cookie.indexOf("=");
        var name = eqPos > -1 ? cookie.substr(0, eqPos) : cookie;
        document.cookie = name + "=;expires=Thu, 01 Jan 1970 00:00:00 GMT;path=/";
    }
    return;
}


