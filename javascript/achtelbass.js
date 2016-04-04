$(document).ready(function() {
    $("#hide_form_button").toggle(function() {
        $(this).text('Show Content');
    }, function() {
        $(this).text('Hide Content');
    }).click(function(){
        $("#configure").animate({width: 'toggle'}, "slow");
    });
});
