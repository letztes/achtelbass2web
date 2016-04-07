$(document).ready(function() {
    $("#hide_form_button").click(function() {
        $('#configure').toggle('slow');
		$(this).text(function(i, text){
			return text === "Show controls" ? "Hide controls" : "Show controls";
		})
    });
});

