(function (langstyle, dom) {

    langstyle.ImageNavigation = function (options) {
        if (!(this instanceof langstyle.ImageNavigation)) {
            return new langstyle.ImageNavigation(options);
        }
        this._imageNavId = options.imageNavId;
        this._previousImageId = options.previousImageId;
        this._nextImageId = options.nextImageId;
        this._imageView = options.imageView;
        this._diabledSign = "disabled";
        this._hiddenSign = "hidden";
        this._imageNavElement = dom.getById(this._imageNavId);
        this._previousImageElement = dom.getById(this._previousImageId);
        this._nextImageElement = dom.getById(this._nextImageId);

        this.init();
    };

    langstyle.ImageNavigation.prototype = {

        init: function () {
            this._previousImageElement.onclick = function () {
                this._imageView.showPrevious();
            } .bind(this);

            this._nextImageElement.onclick = function () {
                this._imageView.showNext();
            } .bind(this);
        },

        refresh: function () {
            if (this._imageView == null || !this._imageView.hasImage()) {
                this._hide();
                return;
            }
            this._show();
            if (this._imageView.hasNext()) {
                this._enableNext();
            }
            else {
                this._disableNext();
            }
            if (this._imageView.hasPrevious()) {
                this._enablePrevious();
            }
            else {
                this._disablePrevious();
            }
        },

        _hide: function () {
            this._disableNext();
            this._disablePrevious();
            this._imageNavElement.classList.add(this._hiddenSign);
        },

        _show: function () {
            this._imageNavElement.classList.remove(this._hiddenSign);
        },

        _enablePrevious: function () {
            this._previousImageElement.classList.remove(this._diabledSign);
        },

        _disablePrevious: function () {
            this._previousImageElement.classList.add(this._diabledSign);
        },

        _enableNext: function () {
            this._nextImageElement.classList.remove(this._diabledSign);
        },

        _disableNext: function () {
            this._nextImageElement.classList.add(this._diabledSign);
        }
    };

    // display image one by one
    // can load all images once, and control their visibility
    langstyle.ImageView = function (options) {
        if (!(this instanceof langstyle.ImageView)) {
            return new langstyle.ImageView(options);
        }

        this._imageViewId = options.imageViewId;
        this._imageNav = new langstyle.ImageNavigation({
            "imageNavId": options.imageNavId,
            "previousImageId": options.previousImageId,
            "nextImageId": options.nextImageId,
            "imageView": this
        });
        this._imageViewElement = dom.getById(this._imageViewId);
        this._currentSign = "current";
        this._hiddenSign = "hidden";
        this._imageUrls = [];

        this.init();
    };

    langstyle.ImageView.prototype = {

        init: function () {
            this._imageViewElement.addEventListener("touchMove", this.showNext.bind(this));
        },

        load: function (imageUrls) {
            this._imageUrls = imageUrls;
            this._reset();
            this._loadImages();
            this.showFirst();
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

        hasImage: function () {
            return this._imageViewElement.children.length > 0;
        },

        hasNext: function () {
            return this._getNext() != null;
        },

        hasPrevious: function () {
            return this._getPrevious() != null;
        },

        showFirst: function () {
            var firstImage = this._getFirst();
            if (firstImage) {
                this._showImage(firstImage);
            }
        },

        showPrevious: function () {
            var previousImage = this._getPrevious();
            if (previousImage) {
                this._hideCurrent();
                this._showImage(previousImage);
            }
        },

        showNext: function () {
            var nextImage = this._getNext();
            if (nextImage) {
                this._hideCurrent();
                this._showImage(nextImage);
            }
        },

        _showImage: function (imageElement) {
            imageElement.classList.remove(this._hiddenSign);
            imageElement.classList.add(this._currentSign);
            this._imageNav.refresh();
        },

        _hideCurrent: function () {
            var currentImage = this._getCurrent();
            if (currentImage) {
                currentImage.classList.remove(this._currentSign);
                currentImage.classList.add(this._hiddenSign);
            }
        },

        _getFirst: function () {
            if (this.hasImage()) {
                return this._imageViewElement.children[0];
            }
        },

        _getLast: function () {
            if (this.hasImage()) {
                var lastImageIndex = this._imageViewElement.children.length - 1;
                return this._imageViewElement.children[lastImageIndex];
            }
        },

        _getCurrent: function () {
            return dom.getFirstChildByClass(this._imageViewElement, this._currentSign);
        },

        _getNext: function () {
            var currentImage = this._getCurrent();
            if (currentImage) {
                var nextElement = currentImage.nextElementSibling;
                if (nextElement && nextElement.nodeName === "IMG") {
                    return nextElement;
                }
            }
            return this._getFirst();
        },

        _getPrevious: function () {
            var currentImage = this._getCurrent();
            if (currentImage) {
                var previousElement = currentImage.previousElementSibling;
                if (previousElement && previousElement.nodeName === "IMG") {
                    return previousElement;
                }
            }
            return this._getLast();
        }
    };

    langstyle.SoundSpeak = function (options) {
        if (!(this instanceof langstyle.SoundSpeak)) {
            return langstyle.SoundSpeak(options);
        }

        this._soundSpeakId = options.soundSpeakId;
        this._soundSpeakElement = dom.getById(this._soundSpeakId);
        this._soundUrls = [];

        this.init();
    };

    langstyle.SoundSpeak.prototype = {

        init: function () {
        },

        load: function (soundUrls) {
            this._soundUrls = soundUrls;
            this._reset();
            this._loadSounds();
            this.playFirst();
        },

        _reset: function () {
            dom.emptyElement(this._soundSpeakElement);
        },

        _loadSounds: function () {
            var length = this._soundUrls.length;
            for (var i = 0; i < length; i++) {
                var soundLink = document.createElement("audio");
                soundLink.src = this._soundUrls[i];
                this._soundSpeakElement.appendChild(soundLink);
            }
        },

        playFirst: function () {
            var firstSound = this._getFirst();
            if (firstSound) {
                this._playSound(firstSound);
            }
        },

        hasSound: function () {
            return this._soundSpeakElement.children.length > 0;
        },

        _playSound: function (soundElement) {
            soundElement.play();
        },

        _getFirst: function () {
            if (this.hasSound()) {
                return this._soundSpeakElement.children[0];
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

        this.imageView = new langstyle.ImageView({
            "imageViewId": options.imageViewId,
            "imageNavId": options.imageNavId,
            "previousImageId": options.previousImageId,
            "nextImageId": options.nextImageId
        });

        this.soundSpeak = new langstyle.SoundSpeak({
            "soundSpeakId": options.soundSpeakId
        });

    };

    langstyle.WordStage.prototype = {

        play: function () {
            this.userProgress.getNextCharacter().then(function (characterId) {
                this.getCharacter(characterId);
                this.getImages(characterId);
                this.getSounds(characterId);
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
                this.imageView.load(imageUrls);
            } .bind(this));
        },

        getSounds: function (characterId) {
            // add a sign to mark sound ready
            this.userProgress.getCharacterSounds(characterId).then(function (soundIds) {
                this._soundIds = this._getArrayFromString(soundIds);
                var soundUrls = this._getSoundUrlsByIds(this._soundIds);
                this.soundSpeak.load(soundUrls);
            } .bind(this));
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
        },

        _getSoundUrlsByIds: function (soundIds) {
            soundIds = soundIds || [];
            var soundUrls = [];
            for (var i = soundIds.length - 1; i >= 0; i--) {
                soundUrls.push(this.wordSound.getUrlById(soundIds[i]));
            }
            return soundUrls.reverse();
        }
    };

} (langstyle, dom));