
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
// $(".indvFilter").click(function() {
//     console.log("filter");
//     $(this).addClass("active");
// });

// Modal validation controllers
$(".loginModalLink").click(function() {
    $('.lemail').remove();
    $('.lpass').remove();
});

$('#login-modal-form').submit(function(e){
    let errors = 0;
    if($("#loginEmail").val() == ""){
        $('.lemail').remove();
        $('#loginEmailmessage').before('<p class="error lemail">Please enter login email</p>');
        errors++;
    } else $('.lemail').remove();

    if($("#loginPassword").val() == ""){
        $('.lpass').remove();
        $('#loginPasswordmessage').before('<p class="error lpass">Please enter login password</p>');
        errors++;
    } else $('.lpass').remove();
    if (errors > 0) e.preventDefault();

})

$('#register-modal-form').submit(function(e){
    let errors = 0;
    print(errors);
    let email_regex = /^[a-zA-Z0-9.+_-]+@[a-zA-z0-9._-]+\.[a-zA-z]+$/;
    if($("#regEmail").val() == ""){
        $('.remail').remove();
        $('#regEmailmessage').before('<p class="error remail">Please enter email</p>');
        errors++;
    }else if (!email_regex.test($("#regEmail").val())){
            $('.remail').remove();
            $('#regEmailmessage').before('<p class="error remail">Email must be valid</p>');
            errors++;
    } else $('.remail').remove();

    if($("#regfirstName").val() == ""){
        $('.rfn').remove();
        $('#regfirstNamemessage').before('<p class="error rfn">Please enter first name</p>');
        errors++;
    }else if ($("#regfirstName").val().length < 3){
            $('.rfn').remove();
            $('#regfirstNamemessage').before('<p class="error rfn">First name must be at least 3 characters</p>');
            errors++;
    } else $('.rfn').remove();

    if($("#reglastName").val() == ""){
        $('.rln').remove();
        $('#reglastNamemessage').before('<p class="error rln">Please enter last name</p>');
        errors++;
    }else if ($("#reglastName").val().length < 3){
            $('.rln').remove();
            $('#reglastNamemessage').before('<p class="error rln">Last name must be at least 3 characters</p>');
            errors++;
    } else $('.rln').remove();

    if($("#regPassword").val() == ""){
        $('.rpass').remove();
        $('#regPasswordmessage').before('<p class="error rpass">Please enter password</p>');
        errors++;
    } else if ($("#regpassword").val().length < 8){
            $('.password').remove();
            $('#password').before('<p class="error password">Password must be at least 8 characters</p>');
            errors++;
    } else $('.rpass').remove();
    
    if (errors > 0) e.preventDefault();

})

// Ajax call to search listings

$('#searchbar_div').submit(function(e){
    e.preventDefault();
    console.log("keyup");
    console.log($(this).serialize());
        $.ajax({
        method: "POST",
        url: '/search/',
        data: $(this).serialize(),
        success: function(response){
            $('#listing_grid').html(response)
        }
    })
});

$('.topcity').click(function(e){
    e.preventDefault();
    let city = this.children[1].firstChild.data;
    var token = $('#topcity-form')[0].children[0].attributes[2].nodeValue;
        $.ajax({
        method: "POST",
        url: '/searchclick/',
        data: {
            'city': city,
            'csrfmiddlewaretoken': token
        },
        success: function(response){
            $('#listing_grid').html(response)
        }
    })
});
 
// Checking screen width

var checkMod = function() {
    if (Modernizr.mq('(min-width: 992px)')) {
        $( "#logo-route" ).attr("href", "/home/");
    } else if (Modernizr.mq('(min-width: 768px)')) {
        $( "#logo-route" ).attr("href", "/menu/");
    } else if (Modernizr.mq('(min-width: 576px)')) {
        $( "#logo-route" ).attr("href", "/menu/");
    } else {
        $( "#logo-route" ).attr("href", "/menu/");
    }
};

$(function() {
    $(window).resize(checkMod);
    checkMod();
})






