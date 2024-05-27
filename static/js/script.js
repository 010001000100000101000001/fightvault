$(function () {
    $("#rateYo").rateYo({
        rating: 3.6,
        starWidth: "20px",
        fullStar: true,
        normalFill: "#A0A0A0",
        ratedFill: "#E74C3C",
        starSvg: '<i class="fa fa-boxing-glove"></i>'
    }).on("rateyo.set", function (e, data) {
        if (!isAuthenticated) {
            alert("You need to log in or register to rate this post.");
            window.location.href = loginUrl;
            return;
        }

        $.ajax({
            url: ratePostUrl,
            method: "POST",
            data: {
                rating: data.rating,
                csrfmiddlewaretoken: csrfToken
            },
            success: function(response) {
                alert(response.message);
                window.location.href = postUrl;
            },
            error: function(response) {
                if (response.responseJSON && response.responseJSON.message) {
                    alert(response.responseJSON.message);
                } else {
                    alert("There was an error submitting your rating.");
                }
            }
        });
    });
});
