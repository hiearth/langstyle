
(function (window, undefined) {

    var _sendRequest = function (url, requestMethod, data) {
        var httpRequest = new XMLHttpRequest();
        var promise = new Promise();

        httpRequest.onreadystatechange = function () {
            if (httpRequest.readyState === 4) {
                if (httpRequest.status === 200) {
                    promise.fulfill(httpRequest.responseText);
                }
                else {
                    promise.reject(httpRequest.statusText);
                }
            }
        };

        httpRequest.open(requestMethod, url, true);
        httpRequest.send(data);

        return promise;
    };

    var ajax = {

        get: function (url) {
            return _sendRequest(url, "GET");
        },

        put: function (url, data) {
            return _sendRequest(url, "PUT", data);
        },

        post: function (url, data) {
            return _sendRequest(url, "POST", data);
        },

        delete_: function (url) {
            return _sendRequest(url, "DELETE");
        }
    };

    window.ajax = ajax;

} (window));