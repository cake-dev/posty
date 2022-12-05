

// for hiding the create Post error tag
function hideError() {
  document.getElementsByClassName("errorlist")[0].style.display = "none";
}
// hideError();

function upvoteSVG(p_id, u_id) {
  console.log("upvote " + p_id);

  u_tri = document.getElementById("upvote_tri_" + p_id);
  d3.select(u_tri).attr("fill", "green");

  var catid;
  var userid;
  catid = $(this).attr("data-catid");
  userid = $(this).attr("data-userid");
  $.ajax(
    {
      type: "GET",
      url: "/post_detail/upvotepost",
      data: {
        post_id: p_id,
        user_id: u_id
      },
      success: function (data) {
        $('#post' + catid).remove();
        $('#post' + userid).remove();
        $('#message').text(data);
        alert(data);
        location.reload();
      }
    })
}

function downvoteSVG(p_id, u_id) {
  console.log("downvote " + p_id);

  d_tri = document.getElementById("downvote_tri_" + p_id);
  d3.select(d_tri).attr("fill", "red");

  var catid;
  var userid;
  catid = $(this).attr("data-catid");
  userid = $(this).attr("data-userid");
  $.ajax(
    {
      type: "GET",
      url: "/post_detail/downvotepost",
      data: {
        post_id: p_id,
        user_id: u_id
      },
      success: function (data) {
        $('#post' + catid).remove();
        $('#post' + userid).remove();
        $('#message').text(data);
        alert(data);
        location.reload();
      }
    })

}

function fillUpvoted(p_id) {
  u_tri = document.getElementById("upvote_tri_" + p_id);
  d3.select(u_tri).attr("fill", "green");
}

function fillDownvoted(p_id) {
  d_tri = document.getElementById("downvote_tri_" + p_id);
  d3.select(d_tri).attr("fill", "red");
}