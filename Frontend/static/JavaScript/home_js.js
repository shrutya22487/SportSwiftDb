$(".go_up_1").on("mouseover", function () {
    $(".go_up_1").stop().animate({
        height: "220px"});
});
$(".go_up_1").on("mouseout", function() {
    $(".go_up_1").stop().animate({
        height: "150px"
    });
});
$(".go_up_2").on("mouseover", function () {
    $(".go_up_2").stop().animate({
        height: "220px"});
});
$(".go_up_2").on("mouseout", function() {
    $(".go_up_2").stop().animate({
        height: "150px"
    });
});

$(document).ready(function() {
    const $linkHoverAnimation = $('.link-hover-animation');

    $linkHoverAnimation.on('mouseover', function() {
        $(this).addClass('bounce-animation');
    });

    $linkHoverAnimation.on('animationend', function() {
        $(this).removeClass('bounce-animation');
    });
});

$(document).ready(function() {
    const $shakeAnimation = $('.grow');

    $shakeAnimation.on('mouseover', function() {
        $(this).addClass('grow-animation');
    });

    $shakeAnimation.on('mouseout', function() {
        $(this).removeClass('grow-animation');
    });
});
$(document).ready(function() {
    $('body').addClass('visible');
});

