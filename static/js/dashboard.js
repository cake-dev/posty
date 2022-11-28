// for hiding the create Post error tag
function hideError() {
  document.getElementsByClassName("errorlist")[0].style.display = "none";
}
// hideError();

// move post form area with scroll keeping in same alignment using jquery
// $(document).ready(function () {
//   var nav = $('#post_block');
//   var navHomeY = nav.offset().top;
//   var isFixed = false;
//   var $w = $(window);
//   $w.scroll(function () {
//     var scrollTop = $w.scrollTop();
//     var shouldBeFixed = scrollTop > navHomeY;
//     if (shouldBeFixed && !isFixed) {
//       nav.css({
//         position: 'fixed',
//         top: 0,
//         left: nav.offset().left,
//         width: nav.width()
//       });
//       isFixed = true;
//     }
//     else if (!shouldBeFixed && isFixed) {
//       nav.css({
//         position: 'static'
//       });
//       isFixed = false;
//     }
//   });
// });

function upvoteSVG(this) {
  this.style.fill = "red";
}