$('.upvotebutton').click(function () {
    var catid;
    var userid;
    catid = $(this).attr("data-catid");
    userid = $(this).attr("data-userid");
    $.ajax(
        {
            type: "GET",
            url: "/post_detail/upvotepost",
            data: {
                post_id: catid,
                user_id: userid
            },
            success: function (data) {
                $('#post' + catid).remove();
                $('#post' + userid).remove();
                $('#message').text(data);
                alert(data);
                location.reload();
            }
        })
});

$('.downvotebutton').click(function () {
    var catid;
    var userid;
    catid = $(this).attr("data-catid");
    userid = $(this).attr("data-userid");
    $.ajax(
        {
            type: "GET",
            url: "/post_detail/downvotepost",
            data: {
                post_id: catid,
                user_id: userid
            },
            success: function (data) {
                $('#post' + catid).remove();
                $('#post' + userid).remove();
                $('#message').text(data);
                alert(data);
                location.reload();
            }
        })
});

$('.clearbutton').click(function () {
    var catid;
    var userid;
    catid = $(this).attr("data-catid");
    userid = $(this).attr("data-userid");
    $.ajax(
        {
            type: "GET",
            url: "/post_detail/clearpost",
            data: {
                post_id: catid,
                user_id: userid
            },
            success: function (data) {
                $('#post' + catid).remove();
                $('#post' + userid).remove();
                $('#message').text(data);
                location.reload();
            }
        })
});

$('.commentbutton').click(function () {
    var catid;
    var userid;
    var comment;
    catid = $(this).attr("data-catid");
    userid = $(this).attr("data-userid");
    comment = $('#comment' + catid).val();
    $.ajax(
        {
            type: "GET",
            url: "/post_detail/commentpost",
            data: {
                post_id: catid,
                user_id: userid,
                comment: comment
            },
            success: function (data) {
                $('#post' + catid).remove();
                $('#post' + userid).remove();
                $('#post' + comment).remove();
                $('#message').text(data);
                location.reload();
            }
        })
});

$('.deletebutton').click(function () {
    var catid;
    var userid;
    catid = $(this).attr("data-catid");
    userid = $(this).attr("data-userid");
    $.ajax(
        {
            type: "GET",
            url: "/post_detail/deletepost",
            data: {
                post_id: catid,
                user_id: userid
            },
            success: function (data) {
                $('#post' + catid).remove();
                $('#post' + userid).remove();
                $('#message').text(data);
                if (data == "True") {
                    alert("Post deleted");
                    $(location).prop('href', '/')
                }
                else {
                    alert("You can only delete your own posts!")
                    location.reload();
                }

            }
        })
});

$('.updatebutton').click(function () {
    var body = $('#post-body');
    var updatebutton = $('.updatebutton')[0];
    var deletebutton = $('.deletebutton')[0];
    var updatebuttonconfirm = $(".updatebuttonconfirm")[0];
    var updatebuttoncancel = $(".updatebuttoncancel")[0];
    body.replaceWith('<textarea id="body" class="textarea is-info" rows="4" spellcheck="true">' + body.text() + '</textarea>');
    updatebuttonconfirm.style.display = "inline";
    updatebuttoncancel.style.display = "inline";
    updatebutton.style.display = "none";
    deletebutton.style.display = "none";
});

$('.updatebuttonconfirm').click(function () {
    var catid;
    var userid;
    var body;
    var updatebutton = $('.updatebutton')[0];
    var deletebutton = $('.deletebutton')[0];
    var updatebuttonconfirm = $(".updatebuttonconfirm")[0];
    catid = $(this).attr("data-catid");
    userid = $(this).attr("data-userid");
    body = $('#body').val();
    $.ajax(
        {
            type: "GET",
            url: "/post_detail/updatepost",
            data: {
                post_id: catid,
                user_id: userid,
                body: body
            },
            success: function (data) {
                $('#post' + catid).remove();
                $('#post' + userid).remove();
                $('#post' + body).remove();
                $('#message').text(data);
                if (data == "True") {
                    alert("Post updated!");
                }
                else {
                    alert("An error occured! Make sure the post is not empty.");
                }
                location.reload();
            }
        })
});
$('.updatebuttoncancel').click(function () {
    var body = $('#body');
    var updatebutton = $('.updatebutton')[0];
    var deletebutton = $('.deletebutton')[0];
    var updatebuttonconfirm = $(".updatebuttonconfirm")[0];
    var updatebuttoncancel = $(".updatebuttoncancel")[0];
    body.replaceWith('<p id="post-body" class="subtitle is-6">' + body.text() + '</p>');
    updatebuttonconfirm.style.display = "none";
    updatebutton.style.display = "inline";
    deletebutton.style.display = "inline";
    updatebuttoncancel.style.display = "none";
});

$('.deletecomment').click(function () {
    var catid;
    var userid;
    catid = $(this).attr("data-catid");
    userid = $(this).attr("data-userid");
    postid = $(this).attr("data-postid");
    $.ajax(
        {
            type: "GET",
            url: "/post_detail/deletecomment",
            data: {
                comment_id: catid,
                user_id: userid,
                post_id: postid
            },
            success: function (data) {
                $('#post' + catid).remove();
                $('#post' + userid).remove();
                $('#message').text(data);
                if (data == "True") {
                    alert("Comment deleted");
                }
                else {
                    alert("An error occured!");
                }
                location.reload();
            }
        })
});
$('.updatecomment').click(function () {
    var body = $('#comment-body');
    var updatebutton = $('.updatecomment')[0];
    var deletebutton = $('.deletecomment')[0];
    var updatebuttonconfirm = $(".updatecommentconfirm")[0];
    var updatebuttoncancel = $(".updatecommentcancel")[0];
    body.replaceWith('<textarea id="body" class="textarea is-info" rows="1" spellcheck="true">' + body.text() + '</textarea>');
    updatebuttonconfirm.style.display = "inline";
    updatebuttoncancel.style.display = "inline";
    updatebutton.style.display = "none";
    deletebutton.style.display = "none";
});
$('.updatecommentcancel').click(function () {
    var body = $('#body');
    var updatebutton = $('.updatecomment')[0];
    var deletebutton = $('.deletecomment')[0];
    var updatebuttonconfirm = $(".updatecommentconfirm")[0];
    var updatebuttoncancel = $(".updatecommentcancel")[0];
    body.replaceWith('<p style="display:inline" id="comment-body" class="subtitle is-6">' + body.text() + '</p>');
    updatebuttonconfirm.style.display = "none";
    updatebutton.style.display = "inline";
    deletebutton.style.display = "inline";
    updatebuttoncancel.style.display = "none";
});
$('.updatecommentconfirm').click(function () {
    var catid;
    var userid;
    var body;
    var updatebutton = $('.updatecomment')[0];
    var deletebutton = $('.deletecomment')[0];
    var updatebuttonconfirm = $(".updatecommentconfirm")[0];
    catid = $(this).attr("data-catid");
    userid = $(this).attr("data-userid");
    body = $('#body').val();
    $.ajax(
        {
            type: "GET",
            url: "/post_detail/updatecomment",
            data: {
                comment_id: catid,
                user_id: userid,
                body: body
            },
            success: function (data) {
                $('#post' + catid).remove();
                $('#post' + userid).remove();
                $('#post' + body).remove();
                $('#message').text(data);
                if (data == "True") {
                    alert("Comment updated!");
                }
                else {
                    alert("An error occured! Make sure the comment is not empty.");
                }
                location.reload();
            }
        })
});