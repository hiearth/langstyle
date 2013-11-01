
langstyle.WordSound = function (options) {
    if (!(this instanceof langstyle.WordSound)) {
        return new langstyle.WordSound(options);
    }

    this._soundNode = dom.getById(options.soundId);
    this._restUrl = options.restUrl;
    this._currentSound = "";
};

langstyle.WordSound.prototype = {

    load: function (character) {
        var soundUrl = this._getRequestUrl(character);
        this._soundNode.src = soundUrl;
        this._soundNode.play();
    },

    _getRequestUrl: function (character) {
        return this._restUrl + character;
    }
};