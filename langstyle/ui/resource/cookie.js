
(function () {

    var Cookie = function () {
        if (!(this instanceof Cookie)) {
            return new Cookie();
        }
    };

    Cookie.prototype = {

        get: function (cookieName) {
            if (document.cookie.length > 0) {
                var startIndex = document.cookie.indexOf(cookieName + "=");
                if (startIndex > -1) {
                    startIndex = startIndex + cookieName.length + 1;
                    var endIndex = document.cookie.indexOf(";", startIndex);
                    if (endIndex == -1) {
                        endIndex = document.cookie.length;
                    }
                    return unescape(document.cookie.substring(startIndex, endIndex));
                }
            }
            return null;
        },

        set: function (cookieName, value, expireDays) {
            var cookie = cookieName + "=" + escape(value);
            if (expireDays != null) {
                var expireDate = new Date();
                expireDate.setDate(expireDate.getDate() + expireDays);
                document.cookie = cookie + ";expires=" + expireDate.toGMTString();
            }
        },

        remove: function (cookieName) {
            this.set(cookieName, "", -1);
        }
    };

    langstyle.Cookie = Cookie;

} ());