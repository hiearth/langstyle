
langstyle.WordStage = function (options) {
    if (!(this instanceof langstyle.WordStage)) {
        return new langstyle.WordStage(options);
    }

    this._stageNode = dom.getById(options.stageId);

    this.wordCharacter = new langstyle.WordCharacter({
        "restUrl": "/characterbait/",
        "characterId": options.characterId
    });
    this.wordImage = new langstyle.WordImage({
        "restUrl": "/image/",
        "imageId": options.imageId
    });
    this.wordSound = new langstyle.WordSound({
        "restUrl": "/sound/",
        "soundId": options.soundId
    });

};

langstyle.WordStage.prototype = {

    start: function () {
        dom.removeClass(this._stageNode, "hidden");
        dom.addClass(this._stageNode, "start");
    },

    nextWord: function () {
        // first get character
        // then show image of this character
        // and then play the sound of this character
        // at last display character
        this.wordCharacter.next().then(function () {
            var currentCharacter = this.wordCharacter.getCharacter();
            this.wordImage.load(currentCharacter);
            this.wordSound.load(currentCharacter);
        }.bind(this));
    }
};