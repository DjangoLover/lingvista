KangoAPI.onReady(function() {

    $.ajax({
        "url": URL_LANGUAGES_API,
        "type": "GET",
        "success": function (response) {
            console.log(response);
        }
    });

});
