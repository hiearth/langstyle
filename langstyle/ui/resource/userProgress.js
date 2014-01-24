
langstyle.UserProgress = function () {
    if (!(this instanceof langstyle.UserProgress)) {
        return new langstyle.UserProgress();
    }

    this._characterImagesUrl = "/characterimages";
    this._currentCharacterUrl = "/usercharacter/current";
    this._nextCharacterUrl = "/usercharacter/next";
};

langstyle.UserProgress.prototype = {

    getCurrentCharacter:function(){
        return ajax.get(this._currentCharacterUrl);
    },

    getNextCharacter:function(){
        return ajax.get(this._nextCharacterUrl);
    },

    getCharacterImages: function (characterId) {
        return ajax.get(this._getCharacterImagesUrl(characterId));
    },

    _getCharacterImagesUrl: function (characterId) {
        return this._characterImagesUrl + "/" + characterId;
    }
};