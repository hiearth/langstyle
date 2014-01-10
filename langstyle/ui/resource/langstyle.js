
(function (window, undefined) {

    var langstyle = {
        imageUrl: "/image",
        characterUrl: "/character",
        characterCodeUrl: "/charactercode",
        characterImageUrl: "/characterimage",

        joinUrl: function (rootUrl, parameters) {
            return rootUrl + this._joinParameters(parameters);
        },

        _joinParameters: function (parameters) {
            var result = "";
            for (var paraName in parameters) {
                if (parameters.hasOwnProperty(paraName)) {
                    result += "/" + paraName + "/" + parameters[paraName];
                }
            }
            return result;
        }
    };

    window.langstyle = langstyle;
} (window));