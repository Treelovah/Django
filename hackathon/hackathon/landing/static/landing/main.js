window.onscroll = function() {scrolling()};
function scrolling()
{
    if (document.body.scrollTop > 50 || document.documentElement.scrollTop > 50)
    {
        document.getElementById("fancy").classList.remove("bg-light")
    } else
    {
        continue;
    }
}