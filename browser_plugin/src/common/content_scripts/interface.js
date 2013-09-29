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

function translateText(text, x, y) {
    if (!!text) {

        showPopup(x, y, "<img src='" + Settings.URL_STATIC + "img/ajax-loader.gif' />");

        var data = {
            "lang_to": "ru",
            "source": text
        };
        $.ajax({
            "url": Settings.URL_TRANSDEF_API,
            "type": "GET",
            "data": data,
            "success": function (response) {
                var result = "<b>Translation:</b> " + response.translation;
                if (response.definition !== null) {
                    result += "<br/><b>Definition:</b> " + response.definition;
                    result += "<br/><a href=" + response.definition_url + '">More on Wikipedia</a>';
                }
                showPopup(x, y, result);
            }
        });
    }
}

function showPopup(x, y, text) {
    var popup = $('<div class="popover fade top in" style="display: block;"><div class="arrow"></div><div class="popover-content"></div></div>');
    $("#LVPanel").remove();

    popup.find(".popover-content").html(text);

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

$(document).on("click", function (e) {
    $("#LVPanel").remove();
});


$(document).on("dblclick", function (e) {
    var text = $.trim(getSelected());
    translateText(text, e.pageX, e.pageY);
});

kango.addMessageListener('LV.ContextMenuItemClick', function(event) {
    var text = $.trim(getSelected());
    // translateText(text, e.pageX, e.pageY);
});

kango.addMessageListener('LV.Start', function(event) {
    var style = $("<style />").text(event.data.content).attr("id", "LVStyle");
    $("html head").append(style);
});
