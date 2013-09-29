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

function showPopup(x, y, text) {
    var popup = $('<div class="popover fade top in" style="display: block;"><div class="arrow"></div><div class="popover-content"></div></div>');

    $("#LVPanel").remove();
    popup.find(".popover-content").text(text);

    popup.css({
        "position": "absolute",
        "left": -10000,
        "top": -10000
    });
    popup.attr("id", "LVPanel");
    $("body").append(popup);

    popup.css({
       "left": x - popup.width() / 2,
       "top": y - popup.height() - 10
    });
}

$(document).on("dblclick", function (e) {

    showPopup(e.pageX, e.pageY, getSelected());



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
    // showPopup(e.pageX, e.pageY, getSelected());
});

kango.addMessageListener('LV.Start', function(event) {
    var style = $("<style />").text(event.data.content).attr("id", "LVStyle");
    $("html head").append(style);
});
