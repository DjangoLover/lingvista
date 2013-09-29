var LINGVO_VISTA_API_URL = "http://lingvista/api/v1/translate/";

function getSelected () {
  if (window.getSelection) {
    return window.getSelection().toString();
  } else if (document.getSelection) {
    return document.getSelection().toString();
  } else if (document.selection) {
    return document.selection.createRange().text;
  }
  return "";
}

function getLanguage () {
    if ( window.navigator.language ) {
        return window.navigator.language;
    }
    else if (navigator.browserLanguage ) {
        return navigator.browserLanguage;
    }

    return "";
}

$(document).on("dblclick", function (e) {
    var text = getSelected();

    $("#LVPanel").remove();

    alert(text);

    // if (text) {
    //     var requestData = {
    //         "method": "GET",
    //         "url": LINGVO_VISTA_API_URL,
    //         "async": true,
    //         "params": {
    //             "text": getSelected(),
    //             "lang_to": getLanguage()
    //         },
    //         "contentType": "json"
    //     };
    //     kango.xhr.send(requestData, function (response) {
    //         var el = $("<div />");
    //         el.css({
    //             "position": "absolute",
    //             "display": "inline-block",
    //             "max-width": "300",
    //             "background": "#000",
    //             "color": "#fff",
    //             "text-align": "center",
    //             "opacity": 0.7,
    //             "padding": "10px 20px",
    //             "left": e.pageX,
    //             "top": e.pageY
    //         });
    //         el.attr("id", "LVPanel");
    //         el.text(text);
    //         $("body").append(el);
    //     });
    // }

});

kango.addMessageListener('LV.ContextMenuItemClick', function(event) {
    alert(getSelected());
});

kango.addMessageListener('LV.Start', function(event) {
    var style = $("<style />").text(event.data.content).attr("id", "LVStyle");
    $("html head").append(style);
});
