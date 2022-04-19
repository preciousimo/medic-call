// If no patient show the message
$(document).ready(function() {
    var verify = $("#chk_td").length;
    if (verify == 0) {
        $("#no-data").text("No patient found");
    }
});

// Time running at realtime
setInterval(function() {
    var date = new Date();
    $("#clock").html(
        (date.getHours() < 10 ? '0' : '') + date.getHours() + ":" + (date.getMinutes() < 10 ? '0' : '') + date.getMinutes() + ":" + (date.getSeconds() < 10 ? '0' : '') + date.getSeconds()
    );
}, 500);