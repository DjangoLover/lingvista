$(function () {

    $.ajax({
        "url": "http://lingvista.org/api/v1/lang/",
        "type": "GET",
        "success": function (response) {

            $.each(response["languages"], function (index, item) {
                $("<option />").val(item).text(item).appendTo('#id_lang');
            });

            $("#id_lang").val(response["currentLanguage"]);
        }
    });

});
