// var API_URL = "http://lingvista.org/api/v1/lang/";
var API_URL = "http://localhost:8000/api/v1/langs/";

$(function () {

    $.ajax({
        "url": API_URL,
        "type": "GET",
        "success": function (response) {

            $.each(response["languages"], function (index, item) {
                $("<option />").val(item).text(item).appendTo('#id_lang');
            });

            $("#id_lang").val(response["currentLanguage"]);
        }
    });

});
