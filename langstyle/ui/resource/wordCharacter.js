
langstyle.WordCharacter = function (options) {
    if (!(this instanceof langstyle.WordCharacter)) {
        return new langstyle.WordCharacter(options);
    }

    this._characterNode = dom.getById(options.characterId);
    this._restUrl = options.restUrl;
    this._characterUrl = "/character";
};

langstyle.WordCharacter.prototype = {

    getCharacterCode: function (characterId) {
        return ajax.get(this._characterUrl + "/" + characterId);
    },

    next: function () {
        var characterUrl = this._getRequestUrl();
        return ajax.get(characterUrl).then(
            this._setCurrentCharacter.bind(this)
        );
    },

    getCharacter: function () {
        return this._currentCharacter;
    },

    _getRequestUrl: function () {
        return this._restUrl + this._currentCharacter;
    },

    _setCurrentCharacter: function (character) {
        this._currentCharacter = character;
    }
};