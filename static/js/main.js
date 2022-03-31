// If no patient show the message
$(document).ready(function() {
    var verify = $("#chk_td").length;
    if (verify == 0) {
        $("#no-data").text("No patient found");
    }
});