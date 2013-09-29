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
    var text = $.trim(getSelected());

    if (!!text) {
        $.ajax({
            "url": "http://localhost:8000/api/v1/translate/",
            "type": "GET",
            "data": {"text": text},
            "success": function (response) {
                var translation = response["translation"];
                showPopup(e.pageX, e.pageY, translation);
            }
        });
    }

});

kango.addMessageListener('LV.ContextMenuItemClick', function(event) {
    // showPopup(e.pageX, e.pageY, getSelected());
});

kango.addMessageListener('LV.Start', function(event) {
    var style = $("<style />").text(event.data.content).attr("id", "LVStyle");
    $("html head").append(style);
});
