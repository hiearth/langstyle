
langstyle.User = function () {
    if (!(this instanceof langstyle.User)) {
        return new langstyle.User();
    }

    this._characterImagesUrl = "/characterimages";
    this._currentCharacterUrl = "/usercharacter/current";
};

langstyle.User.prototype = {

    getCurrentCharacter:function(){
        return ajax.get(this._currentCharacterUrl);
    },

    getCharacterImages: function (characterId) {
        return ajax.get(this._getCharacterImagesUrl(characterId));
    },

    _getCharacterImagesUrl: function (characterId) {
        return this._characterImagesUrl + "/" + characterId;
    },
};