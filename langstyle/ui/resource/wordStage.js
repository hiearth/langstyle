
// display image one by one
// can load all images once, and control their visibility
langstyle.ImageView = function (imageViewId) {
    if (!(this instanceof langstyle.ImageView)) {
        return new langstyle.ImageView(imageViewId);
    }

    this._imageViewId = imageViewId;
    this._imageViewElement = dom.getById(this._imageViewId);
    this._currentSign = "current";
    this._hiddenSign = "hidden";
    this._imageUrls = [];

    this.init();
};

langstyle.ImageView.prototype = {

    init: function () {
        dom.getById("nextImage").onclick = this._showNext.bind(this);
        this._imageViewElement.addEventListener("touchMove", this._showNext.bind(this));
    },

    show: function (imageUrls) {
        this._imageUrls = imageUrls;
        this._reset();
        this._loadImages();
        this._showFirst();
    },

    _reset: function () {
        dom.emptyElement(this._imageViewElement);
    },

    _loadImages: function () {
        var length = this._imageUrls.length;
        for (var i = 0; i < length; i++) {
            var imageLink = dom.createElement("img");
            imageLink.alt = this._imageUrls[i];
            imageLink.src = this._imageUrls[i];
            imageLink.classList.add(this._hiddenSign);
            this._imageViewElement.appendChild(imageLink);
        }
    },

    _hasImage: function () {
        return this._imageViewElement.children.length > 0;
    },

    _showFirst: function () {
        var firstImage = this._getFirst();
        if (firstImage) {
            this._showImage(firstImage);
        }
    },

    _showImage: function (imageElement) {
        imageElement.classList.remove(this._hiddenSign);
        imageElement.classList.add(this._currentSign);
    },

    _showNext: function () {
        var nextImage = this._getNext();
        if (nextImage) {
            this._hideCurrent();
            this._showImage(nextImage);
        }
    },

    _hideCurrent: function () {
        var currentImage = this._getCurrent();
        if (currentImage) {
            currentImage.classList.remove(this._currentSign);
            currentImage.classList.add(this._hiddenSign);
        }
    },

    _getFirst: function () {
        if (this._hasImage()) {
            return this._imageViewElement.children[0];
        }
    },

    _getCurrent: function () {
        return dom.getFirstChildByClass(this._imageViewElement, this._currentSign);
    },

    _getNext: function () {
        var currentImage = this._getCurrent();
        if (currentImage) {
            var nextNode = currentImage.nextSibling;
            if (nextNode && nextNode.nodeType === Node.ELEMENT_NODE && nextNode.nodeName === "IMG") {
                return nextNode;
            }
        }
        return this._getFirst();
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

    this.userProgress = new langstyle.UserProgress();

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

        this.userProgress.getNextCharacter().then(function (characterId) {
            this.getCharacter(characterId);
            this.getImages(characterId);
            this.getSound(characterId);
        } .bind(this));
    },

    getCharacter: function (characterId) {
        this.wordCharacter.getCharacterCode(characterId).then(function (character) {
            this._character = character;
            this.showCharacter();
        } .bind(this));
    },

    getImages: function (characterId) {
        this.userProgress.getCharacterImages(characterId).then(function (imageIds) {
            this._imageIds = this._getArrayFromString(imageIds);
            var imageUrls = this._getImageUrlsByIds(this._imageIds);
            this.imageView.show(imageUrls);
        } .bind(this));
    },

    getSound: function (characterId) {
        // add a sign to mark sound ready
    },

    showCharacter: function () {
        var characterElement = dom.getById("character");
        characterElement.textContent = this._character;
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
    }
};