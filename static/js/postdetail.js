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
                window.location.href = '/';
            }
        })
});