KangoAPI.onReady(function() {

    $.ajax({
        "url": "http://localhost:8000/api/v1/languages/",
        "type": "GET",
        "success": function (response) {
            console.log(response);
        }
    });

});
