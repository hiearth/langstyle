
langstyle.WordSound = function (options) {
    if (!(this instanceof langstyle.WordSound)) {
        return new langstyle.WordSound(options);
    }

    this._soundNode = dom.getById(options.soundId);
    this._restUrl = options.restUrl;
    this._currentSound = "";
    this._soundUrl = "/sound";
};

langstyle.WordSound.prototype = {

    getUrlById: function (soundId) {
        return this._soundUrl + "/" + soundId;
    },

    load: function (character) {
        var soundUrl = this._getRequestUrl(character);
        this._soundNode.src = soundUrl;
        this._soundNode.play();
    },

    _getRequestUrl: function (character) {
        return this._restUrl + character;
    }
};