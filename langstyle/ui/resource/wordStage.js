
// display image one by one
// can load all images once, and control their visibility
langstyle.ImageView = function (imageViewId) {
    if (!(this instanceof langstyle.ImageView)) {
        return new langstyle.ImageView(imageViewId);
    }

    this._imageViewId = imageViewId;
    this._imageUrls = [];
};

langstyle.ImageView.prototype = {

    show: function (imageUrls) {
        this._imageUrls = imageUrls;
        this._reset();
        this._loadImages();
    },

    _reset: function () {
        var viewElement = dom.getById(this._imageViewId);
        dom.emptyElement(viewElement);
    },

    _loadImages: function () {
        var viewElement = dom.getById(this._imageViewId);
        var length = this._imageUrls.length;
        for (var i = 0; i < length; i++) {
            var imageLink = dom.createElement("img");
            imageLink.alt = this._imageUrls[i];
            imageLink.src = this._imageUrls[i];
            viewElement.appendChild(imageLink);
        }
    }
};

langstyle.WordStage = function (options) {
    if (!(this instanceof langstyle.WordStage)) {
        return new langstyle.WordStage(options);
    }

    this._stageNode = dom.getById(options.stageId);
    this._character = null;
    this._images = [];
    this._sound = null;

    this.user = new langstyle.User();

    this.wordCharacter = new langstyle.WordCharacter({
        "restUrl": "/character/",
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

    this.imageView = new langstyle.ImageView(options.imageViewId);

};

langstyle.WordStage.prototype = {

    play: function () {

        this.user.getCurrentCharacter().then(function (characterId) {
            this.getImages(characterId);
            this.getSound(characterId);
        } .bind(this));
    },

    getCharacter: function () {
        return this.wordCharacter.getCurrent().then(function (character) {
            this._character = character;
            return character.id;
        } .bind(this));
    },

    getImages: function (characterId) {
        this.user.getCharacterImages(characterId).then(function (imageIds) {
            this._imageIds = this._getArrayFromString(imageIds);
            var imageUrls = this._getImageUrlsByIds(this._imageIds);
            this.imageView.show(imageUrls);
        } .bind(this));
    },

    _getArrayFromString: function (idsString) {
        if (idsString.indexOf(",") >= 0) {
            return idsString.split(",");
        }
        return [idsString];
    },

    _getImageUrlsByIds: function (imageIds) {
        imageIds = imageIds || [];
        var imageUrls = [];
        for (var i = imageIds.length - 1; i >= 0; i--) {
            imageUrls.push(this.wordImage.getUrlById(imageIds[i]));
        }
        return imageUrls.reverse();
    },

    _getUrlById: function (imageId) {

    },

    getSound: function (characterId) {
        // add a sign to mark sound ready
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
        } .bind(this));
    }

};