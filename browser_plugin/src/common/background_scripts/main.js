function LingvistaExtension() {
    var self = this;

    self.notify = function () {
        kango.browser.tabs.getCurrent(function(tab) {
            tab.dispatchMessage('LV.Start', {content: self.content});
        });
    };

    self.content = null;

    kango.ui.browserButton.addEventListener(kango.ui.browserButton.event.COMMAND, function () {
        kango.browser.tabs.create({url: 'http://kangoextensions.com/'});
    });

    kango.browser.addEventListener(kango.browser.event.DOCUMENT_COMPLETE, function (e) {
        self.notify();
    });

    kango.browser.addEventListener(kango.browser.event.WINDOW_CHANGED, function (e) {
        self.notify();
    });

    // kango.browser.addEventListener(kango.browser.event.TAB_CHANGED, function (e) {
    //     self.notify();
    // });

    kango.ui.contextMenuItem.addEventListener(kango.ui.contextMenuItem.event.CLICK, function() {
        kango.browser.tabs.getCurrent(function(tab) {
            tab.dispatchMessage('LV.ContextMenuItemClick');
        });
    });

    kango.invokeAsync('kango.io.getExtensionFileContents', 'content_scripts/bootstrap/css/bootstrap.min.css', function(content) {
        self.content = content;
    });

}

var extension = new LingvistaExtension();
kango.ui.browserButton.setPopup({url:'popup.html', width: 710, height:510});
