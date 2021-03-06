
(function (langstyle, ajax) {

    langstyle.UserProgress = function () {
        if (!(this instanceof langstyle.UserProgress)) {
            return new langstyle.UserProgress();
        }

        this._characterImagesUrl = "/characterimages";
        this._characterSoundsUrl = "/charactersounds";
        this._currentCharacterUrl = "/usercharacter/current";
        this._nextCharacterUrl = "/usercharacter/next";
        this._nextWordUrl = "/userprogress/next";
    };

    langstyle.UserProgress.prototype = {

        getNext: function () {
            return ajax.get(this._nextWordUrl);
        },

        getCurrentCharacter: function () {
            return ajax.get(this._currentCharacterUrl);
        },

        getNextCharacter: function () {
            return ajax.get(this._nextCharacterUrl);
        },

        getCharacterImages: function (characterId) {
            return ajax.get(this._getCharacterImagesUrl(characterId));
        },

        _getCharacterImagesUrl: function (characterId) {
            return this._characterImagesUrl + "/" + characterId;
        },

        getCharacterSounds: function (characterId) {
            return ajax.get(this._getCharacterSoundsUrl(characterId));
        },

        _getCharacterSoundsUrl: function (characterId) {
            return this._characterSoundsUrl + "/" + characterId;
        }
    };

} (langstyle, ajax));