// for name change
$('.changename').click(function () {
    var name = $('#name-body');
    var changebutton = $('.changename')[0];
    var changebuttonconfirm = $(".changenameconfirm")[0];
    var changebuttoncancel = $(".changenamecancel")[0];
    name.replaceWith('<p id="name-body" class="p is-info" rows="1" spellcheck="false" contentEditable="true">' + name.text() + '</p>');
    changebuttonconfirm.style.display = "inline";
    changebuttoncancel.style.display = "inline";
    changebutton.style.display = "none";
});
$('.changenamecancel').click(function () {
    var name = $('#name-body');
    var changebutton = $('.changename')[0];
    var changebuttonconfirm = $(".changenameconfirm")[0];
    var changebuttoncancel = $(".changenamecancel")[0];
    name.replaceWith('<p style="display:inline" id="name-body" class="subtitle is-6" contentEditable="false">' + name.text() + '</p>');
    changebuttonconfirm.style.display = "none";
    changebutton.style.display = "inline";
    changebuttoncancel.style.display = "none";
});
$('.changenameconfirm').click(function () {
    var userid;
    var name;
    var changebutton = $('.changename')[0];
    var changebuttonconfirm = $(".changenameconfirm")[0];
    userid = $(this).attr("data-userid");
    name = $('#name-body').text();
    $.ajax(
        {
            type: "GET",
            url: "/profile_settings/changename",
            data: {
                user_id: userid,
                name: name
            },
            success: function (data) {
                console.log(data);
                if (data == "True") {
                    alert("Name Changed!");
                }
                else {
                    alert("An error occured! Make sure the name is not empty.");
                }
                location.reload();
            }
        })
});
// for email change
$('.changeemail').click(function () {
    var email = $('#email-body');
    var changebutton = $('.changeemail')[0];
    var changebuttonconfirm = $(".changeemailconfirm")[0];
    var changebuttoncancel = $(".changeemailcancel")[0];
    email.replaceWith('<p id="email-body" class="p is-info" rows="1" spellcheck="false" contentEditable="true">' + email.text() + '</p>');
    changebuttonconfirm.style.display = "inline";
    changebuttoncancel.style.display = "inline";
    changebutton.style.display = "none";
});
$('.changeemailcancel').click(function () {
    var email = $('#email-body');
    var changebutton = $('.changeemail')[0];
    var changebuttonconfirm = $(".changeemailconfirm")[0];
    var changebuttoncancel = $(".changeemailcancel")[0];
    email.replaceWith('<p style="display:inline" id="email-body" class="subtitle is-6" contentEditable="false">' + email.text() + '</p>');
    changebuttonconfirm.style.display = "none";
    changebutton.style.display = "inline";
    changebuttoncancel.style.display = "none";
});
$('.changeemailconfirm').click(function () {
    var userid;
    var email;
    var changebutton = $('.changeemail')[0];
    var changebuttonconfirm = $(".changeemailconfirm")[0];
    userid = $(this).attr("data-userid");
    email = $('#email-body').text();
    $.ajax(
        {
            type: "GET",
            url: "/profile_settings/changeemail",
            data: {
                user_id: userid,
                email: email
            },
            success: function (data) {
                console.log(data);
                if (data == "True") {
                    alert("email Changed!");
                }
                else {
                    alert("An error occured! Make sure the email is not empty or that the email is valid.");
                }
                location.reload();
            }
        })
});
