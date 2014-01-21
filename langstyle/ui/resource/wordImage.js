
langstyle.WordImage = function (options) {
    if (!(this instanceof langstyle.WordImage)) {
        return new langstyle.WordImage(options);
    }

    this._imageNode = dom.getById(options.imageId);
    this._currentImage = "";
    this._restUrl = options.restUrl;
    this._imageUrl = "/image";
};

langstyle.WordImage.prototype = {

    getUrlById: function (imageId) {
        return this._imageUrl + "/" + imageId;
    },

    load: function (character) {
        var imageUrl = this._getRequestUrl(character);
        this._imageNode.src = imageUrl;
    },

    _getRequestUrl: function (character) {
        return this._restUrl + character;
    }
};