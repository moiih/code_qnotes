    // (If-Else) in jQuery.
// if($('.navbar-toggler').data('clicked')) {
//     //clicked element, do-some-stuff
// } else {
//     //run function2
// }


// $("#myNavTitle").click(function() {
//     alert('Good Working !!');
//     console.log('jQ');
// });

// $('#test').click(function() {
//     alert('Good !!');
//     console.log('jq');
// });

// $('#menu-close').hide();

// $('#menu-open').click(function() {
//     $('#menu-open').hide();
//     $('#menu-close').slideDown();
//     $('#menu-open').hide();
// });

// $('#menu-close').click(function() {
//     $('#menu-close').hide();
//     $('#menu-open').slideDown();
//     $('#menu-close').hide();
// });
















// $('#menu-close').hide();
// $("#menu-toggle-icon").hide();

// console.log(document.getElementById("menu-toggle-icon").innerHTML);

// $(".navbar-toggler").click(function() {
//     console.log(document.getElementById("menu-toggle-icon").innerHTML.includes("open"));

//     if ( document.getElementById("menu-toggle-icon").innerHTML.includes("open") ) {
//         console.log("in open");
//         document.getElementById("menu-toggle-icon").innerHTML = "close";
//         $("#menu-open").hide();
//         $("#menu-close").show();
//     }
//     else if ( document.getElementById("menu-toggle-icon").innerHTML.includes("close") ) {
//         console.log("in close");
//         document.getElementById("menu-toggle-icon").innerHTML = "open";
//         $("#menu-close").hide();
//         $("#menu-open").show();
//     }
// });


// $("menu-toggle-icon").hide();



// $("#menu-close").hide();

// $(".navbar-toggler").click(function() {

//     if ( $(".navbar-toggler").css("color") == "rgb(255, 255, 255)" ) {
//         console.log("in open");
//         $(".navbar-toggler").css("color", "rgb(255, 255, 254)");
//         $("#menu-open").hide();
//         $("#menu-close").show();
//         $("#navbarSupportedContent1").collapse('show');

//         // $(".navbar-toggler").css("data-toggle", "collapse");
//         // $(".navbar-toggler").css("data-target", "#navbarSupportedContent1");
//         // $(".navbar-toggler").css("aria-controls", "navbarSupportedContent1");
//         // $(".navbar-toggler").css("aria-label", "Toggle navigation");
//         // $(".navbar-toggler").css("aria-expanded", "true");
//     }
//     else {
//         console.log("in close");
//         $(".navbar-toggler").css("color", "rgb(255, 255, 255)");
//         $("#menu-close").hide();
//         $("#menu-open").show();
//         $("#navbarSupportedContent1").collapse('hide');
//         // $(".navbar-toggler").css("data-toggle", "collapse");
//         // $(".navbar-toggler").css("data-target", "#navbarSupportedContent1");
//         // $(".navbar-toggler").css("aria-controls", "navbarSupportedContent1");
//         // $(".navbar-toggler").css("aria-label", "Toggle navigation");
//         // $(".navbar-toggler").css("aria-expanded", "true");
//     }

// });




    //  ( Super Code Below To Avoid Above JS Mess )
    //  Menu Navigation Toggle

$("#menu-close").hide();

$(".navbar-toggler").click(function() {
    $("#navbarSupportedContent1").collapse('toggle');
});

$('#navbarSupportedContent1').on('show.bs.collapse', function () {
    $("#menu-open").hide();
    $("#menu-close").slideDown(400);

    // $("#menu-close").fadeIn();
    // alert("kite");
});

$('#navbarSupportedContent1').on('hide.bs.collapse', function () {
    $("#menu-close").hide();
    $("#menu-open").slideDown(400);

    // alert("kite");
});






    // For Login To Sign-Up Transition Effects

// console.log("fxfgf");
$('#signup_footer').hide();
$('#image-2a').hide();
$('#image-2b').hide();
$('#signup_box_shadow').hide();

$('#signup_btn').click(function() {

    // console.log("kite");
    // $('#login_box_shadow').animate({paddingTop: "100px"});
    // $('#login_box_shadow').css('background-color', 'white');
    $('#login-signup').css('backgroundImage', 'linear-gradient(to right bottom, red, white)');

    $('#image-1a').fadeOut();
    $('#image-1b').fadeOut();

    // $('#image-1a').hide();
    // $('#image-1b').hide();

    // $('#login_box_shadow').animate({paddingTop: "70px", paddingLeft: "'fast'px", paddingRight: "'fast'px", marginBottom: "50px"}, 'fast');
    // $('#login_box_shadow').animate({paddingTop: "50px"}, 'fast');
    // $('#login_box_shadow').animate({paddingLeft: "50px"}, 'fast');
    // $('#login_box_shadow').animate({paddingRight: "50px"}, 'fast');
    // $('#login_box_shadow').animate({marginBottom: "50px"}, 'fast');
    $('#login_footer').fadeOut();
    $('#signup_footer').fadeIn();

    $('#login_box_shadow').slideUp(1000);
    $('#signup_box_shadow').slideDown(2000);

    $('#image-2a').fadeIn(3000);
    $('#image-2b').fadeIn(3000);


});



    // For Sign-up To Login Transition Effects

$('#login_btn').click(function() {

    // console.log("kite");
    // $('#login_box_shadow').animate({paddingTop: "100px"});
    // $('#login_box_shadow').css('background-color', 'white');
    $('#login-signup').css('backgroundImage', 'linear-gradient(to right bottom, orange, white)');

    $('#image-2a').fadeOut();
    $('#image-2b').fadeOut();

    // $('#image-2a').hide();
    // $('#image-2b').hide();

    // $('#login_box_shadow').animate({paddingTop: "70px", paddingLeft: "'fast'px", paddingRight: "'fast'px", marginBottom: "50px"}, 'fast');
    // $('#login_box_shadow').animate({paddingTop: "50px"}, 'fast');
    // $('#login_box_shadow').animate({paddingLeft: "50px"}, 'fast');
    // $('#login_box_shadow').animate({paddingRight: "50px"}, 'fast');
    // $('#login_box_shadow').animate({marginBottom: "50px"}, 'fast');
    $('#signup_footer').fadeOut();
    $('#login_footer').fadeIn();

    $('#signup_box_shadow').slideUp(1000);
    $('#login_box_shadow').slideDown(2000);
    $('#image-1a').fadeIn(3000);
    $('#image-1b').fadeIn(3000);
});





    // For Password and Email Validation in Sign-Up Form

function pass_check() {

        // Password Validation
    console.log("sdknkjb");
    // console.log(document.getElementById('pwd1').value);
    // console.log(document.getElementById('pwd2').value);

    var user_mail = document.getElementById('em2').value;
    const mail_format = /^(([^<>()[\]\\.,;:\s@"]+(\.[^<>()[\]\\.,;:\s@"]+)*)|(".+"))@((\[[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\])|(([a-zA-Z\-0-9]+\.)+[a-zA-Z]{2,}))$/;

    if ( document.getElementById('pwd1').value != document.getElementById('pwd2').value ) {
        alert("Passwords Do Not Match!!");
    }
    else if ( !user_mail.match(mail_format) ) {
        alert('This Email Address is not valid. Please Check Your Email Id.');
    }
    else {
        // alert("Submitting");
        $('#usr').val(" ");
        $('#pwd').val(" ");
        $('#signup_form').submit();
    }

}


$('#fpass_btn').click(function() {

    // console.log('in fpass');
    const mail_format = /^(([^<>()[\]\\.,;:\s@"]+(\.[^<>()[\]\\.,;:\s@"]+)*)|(".+"))@((\[[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\])|(([a-zA-Z\-0-9]+\.)+[a-zA-Z]{2,}))$/;

    if ( $('#oem').val() == '' || $('#code').val() == '' || $('#opass1').val() == '' || $('#opass2').val() == '') {
        alert("Please Fill-up All Fields. All Fields Are Mandatory !!");
    }
    else if ( !$('#fpass').val().match(mail_format) ) {
        alert('Invalid Email Address. Please Check Your Email Id.');
    }
    else {
        // console.log(document.getElementById('fpass').value);
        // alert('Sumitting');
        $('#forgot_password_form').submit();
    }

});





function otp_pass_check() {

    // Password and E-mail Validation
    console.log("otp_password_check");

    var user_mail = document.getElementById('oem').value;
    const mail_format = /^(([^<>()[\]\\.,;:\s@"]+(\.[^<>()[\]\\.,;:\s@"]+)*)|(".+"))@((\[[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\])|(([a-zA-Z\-0-9]+\.)+[a-zA-Z]{2,}))$/;

    if ( document.getElementById('opass1').value != document.getElementById('opass2').value ) {
        alert("New Passwords Do Not Match!!");
    }
    else if ( !user_mail.match(mail_format) ) {
        alert('This Email Address is not valid. Please Check Your Email Id.');
    }
    else {
        // alert("Submitting OTP");
        $('#otp_change_pass_form').submit();
    }

}




function old_pass_check() {

    // Password and E-mail Validation
    console.log("old_new_password_check");

    if ( $('#oldpass').val() == '' || $('#newpass1').val() == '' || $('newpass2').val() == '') {
        alert("Please Do Not Leave Any Field Empty. All Fields Are Mandatory !!");
    }
    else if ( document.getElementById('newpass1').value != document.getElementById('newpass2').value ) {
        alert("New Passwords Do Not Match !!");
    }
    else {
        // alert("Submitting OTP");
        $('#old_new_pass_form').submit();
    }

}



/*     Logged HomePage Active NavBar Tabs     */

// var curr_url = window.location.href;
// //alert('uyvujhyjv');

// // if( curr_url.include('https://qnotes23.pythonanywhere.com/') ) {                    // For Active 'Home' Tab on Logged HomePage
// if( String(curr_url) == 'https://qnotes23.pythonanywhere.com/' ) {
//     alert('Its Home.');
//     $('#qHome').css("background-color", "yellow");
// }
// //else if( curr_url.include('https://qnotes23.pythonanywhere.com/change_user_password/') ) {      // For Active 'Change Password' Tab
// else if( String(curr_url) == 'https://qnotes23.pythonanywhere.com/change_user_password/' ) {
//     alert('Its Change.');
//     $('#qChange_Pwd').css("background-color", "yellow");
// }









