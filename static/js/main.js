// If no patient show the message
$(document).ready(function () {
  var verify = $("#chk_td").length;
  if (verify == 0) {
    $("#no-data").text("No patient found");
  }
});

// Time running at realtime
setInterval(function () {
  var date = new Date();
  $("#clock").html(
    (date.getHours() < 10 ? "0" : "") +
      date.getHours() +
      ":" +
      (date.getMinutes() < 10 ? "0" : "") +
      date.getMinutes() +
      ":" +
      (date.getSeconds() < 10 ? "0" : "") +
      date.getSeconds()
  );
}, 500);

// Validate all <inputs>
function validateEmail(email) {
  var regex = /^([a-zA-Z0-9_.+-])+\@(([a-zA-Z0-9-])+\.)+([a-zA-Z0-9]{2,4})+$/;
  return regex.test(email);
}
function validateAll() {
  var name = $("#name").val();
  var phone = $("#phone").val();
  var email = $("#email").val();
  var age = $("#age").val();
  var gender = $("#gender").val();

  // Validate name input
  if (name == "") {
    swal("Opsss !", "Name field cannot be empty.", "error");
    return false;
  } else if (name == name.toUpperCase()) {
    swal("Opsss !", "Name cannot be uppercase.", "info");
    $("#name").val("");
    return false;
  } else if (name.split(" ").length < 2) {
    swal("Opsss !", "Put at least the last name.", "info");
    return false;
  }
  // Validate phone number input
  else if (phone == "") {
    swal("Opsss !", "Phone field cannot be empty.", "error");
    return false;
  }
  // Validate email input
  else if (email == "") {
    swal("Opsss !", "Email field cannot be empty.", "error");
    return false;
  }
  else if (!validateEmail(email)) {
    swal("Opsss !", "Put a valid address.", "error");
    $("#email").val("");
    return false;
  }
  // Validate age input
  else if (age == "") {
    swal("Opsss !", "Age field cannot be empty.", "error");
    return false;
  }
  else if (age > 100) {
    swal("Denied !", "The maximum value is 100 years old.", "error");
    $("#age").val("");
    return false;
  }
  // Validate gender option
  else if (gender == "") {
    swal("Opsss !", "Gender field cannot be empty.", "error");
    return false;
  } else {
    return true;
  }
}
$(".btn-add").bind("click", validateAll);

// Scripts - Only letter is allowed
$(document).ready(function () {
  jQuery('input[name="name"]').keyup(function () {
    var letter = jQuery(this).val();
    var allow = letter.replace(/[^a-zA-Z _]/g, "");
    jQuery(this).val(allow);
  });
  // Prevent starting with space
  $("input").on("keypress", function (e) {
    if (e.which === 32 && !this.value.length) e.preventDefault();
  });
});

// Only the first and last name (prevent full name)
$(document).ready(function () {
  $("#name").keyup(function () {
    var name = $("#name").val();
    if (name.split(" ").length == 3) {
      swal("Opsss !", "Only Name and Last name.", "info");
      $("#name").val("");
      return false;
    }
  });
});

// First letter capitalized (first name and last name)
$("#name").keyup(function () {
  var txt = $(this).val();
  $(this).val(
    txt.replace(/^(.)|\s(.)/g, function ($1) {
      return $1.toUpperCase();
    })
  );
});

// Phone mask (inputmask)
$(document).ready(function () {
  $("#phone").inputmask("(99) 99999-9999", {
    onincomplete: function () {
      swal("Opsss !", "incomplete phone. Please review !", "info");
      $("#phone").val
      return false;
    }
  });
});

// Script to LOWERCASE <input> email
$(document).ready(function () {
  $("#name").keyup(function () {
    this.value = this.value.toLowerCase();
  });
});

// If AGE has number greater than 100, auto clear (second method)
$(document).ready(function () {
  $("#age").keyup(function () {
    var age = $("#age").val();
    if (age > 100) {
      // swal("Denied !", "The maximum value is 100 years old.", "error");
      $("#age").val("");
      return false;
    }
  });
});

// Scripts to allow only numbers in AGE
$("#age").keyup(function () {
  if (!/^[0-9]*$/.test(this.value)) {
    this.value = this.value.split(/[^0-9]/).join('');
  }
});

// Prevent starting by zero in AGE field
$("#age").on("input", function() {
  if (/^0/.test(this.value)) {
    this.value = this.value.replace(/^0/, "")
  }
});

// Close offcanvas when a button is clicked
$(document).ready(function () {
  jQuery("#offcanvasRight, .offcanvas-body a").click(function() {
    console.log($(this).attr('href'));
    jQuery('.offcanvas').offcanvas('hide');
  });
});
