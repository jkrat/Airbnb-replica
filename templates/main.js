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
    
    // check screen size with Modernizr
    var checkMod = function() {
        if (Modernizr.mq('(min-width: 992px)')) {
            console.log("large");
            return "large";
        } else if (Modernizr.mq('(min-width: 768px)')) {
            console.log("medium");
            return "medium";
        } else if (Modernizr.mq('(min-width: 576px)')) {
            console.log("small");
            return "small";
        } else {
            console.log("extra-small");
            return "extra-small";
        }
    };
   
    $(function() {
        $(window).resize(checkMod);
        checkMod();
    });
