
langstyle.WordImage = function (options) {
    if (!(this instanceof langstyle.WordImage)) {
        return new langstyle.WordImage(options);
    }

    this._imageNode = dom.getById(options.imageId);
    this._currentImage = "";
    this._restUrl = options.restUrl;
};

langstyle.WordImage.prototype = {

    load: function (character) {
        var imageUrl= this._getRequestUrl(character);
        this._imageNode.src = imageUrl;
    },

    _getRequestUrl: function (character) {
        return this._restUrl + character;
    }
};