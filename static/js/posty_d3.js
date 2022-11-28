let upvote_button = d3.select(".upvote-svg").attr("fill", "none").attr("stroke", "black").attr("stroke-width", "0.5");
console.log("hello")
upvote_button.on("click", function () {
    console.log(d3.select(this).attr("fill"))
    if (d3.select(this).attr("fill") == "none") {
        d3.select(this).attr("fill", "black");
    } else {
        d3.select(this).attr("fill", "none");
    }
});