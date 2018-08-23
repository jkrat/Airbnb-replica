
// hides current modal when switching between the two
$("#signinFromModal").click(function () {
    $("#loginModal").modal("hide");
});

$("#loginFromModal").click(function () {
    $("#registerModal").modal("hide");
});

// toggle show password for both login and register modal
var passwordVisible = false;
$(".getModal").click(function() {
    passwordVisible = false;
});

$(".showpassword").click(function( event ) {
    event.preventDefault();
    if (passwordVisible) {
        $(".passwordInput").attr("type","password");
        $(".showpassword").text("Show password")
        passwordVisible = !passwordVisible;
    } else {
        $(".passwordInput").attr("type","text");
        $(".showpassword").text("Hide password")
        passwordVisible = !passwordVisible;
    }
});

// change heart for like, needs toggle
$("#like").click(function() {
    console.log("like");
    $(this).attr("class", "fas fa-heart fa-3x");
});

//toggle nav pills to active
$(".indvFilter").click(function() {
    console.log("filter");
    $(this).addClass("active");
});





//link cards on dashboard to listing profile. NEED to customize to listing
$("#click").click(function() {
    console.log("clicked card");
    // $.ajax({
    //     type:"GET",
    //     url: "/listing/", 
    //     success: funciton() {
    //         console.log("successful ajax request")
    //     }
    // });
    // return false;
});

// check screen size with Modernizr
var checkMod = function() {
    if (Modernizr.mq('(min-width: 992px)')) {
        console.log("large");
        $("#small-search-button-div").hide();
        $( "#logo-route" ).attr("href", "/home/");
        return "large";
    } else if (Modernizr.mq('(min-width: 768px)')) {
        console.log("medium");
        $("#small-search-button-div").hide();
        $( "#logo-route" ).attr("href", "/menu/");
        return "medium";
    } else if (Modernizr.mq('(min-width: 576px)')) {
        console.log("small");
        $("#small-search-button-div").hide();
        $("#searchbar-div").show();
        return "small";
    } else {
        console.log("extra-small");
        $("#searchbar-div").hide();
        $("#small-search-button-div").show();
        return "extra-small";
    }
};

$(function() {
    $(window).resize(checkMod);
    checkMod();
});


// Example starter JavaScript for disabling form submissions if there are invalid fields
(function() {
  'use strict';
  window.addEventListener('load', function() {
    // Fetch all the forms we want to apply custom Bootstrap validation styles to
    var forms = document.getElementsByClassName('needs-validation');
    // Loop over them and prevent submission
    var validation = Array.prototype.filter.call(forms, function(form) {
      form.addEventListener('submit', function(event) {
        if (form.checkValidity() === false) {
          event.preventDefault();
          event.stopPropagation();
        }
        form.classList.add('was-validated');
      }, false);
    });
  }, false);
})();


