(function (langstyle, dom) {

    // display image one by one
    // can load all images once, and control their visibility
    langstyle.ImageView = function (options) {
        if (!(this instanceof langstyle.ImageView)) {
            return new langstyle.ImageView(options);
        }

        this._imageViewId = options.imageViewId;
        this._imageViewElement = dom.getById(this._imageViewId);
        this._currentSign = "current";
        this._hiddenSign = "hidden";
        this._imageUrls = [];
        this.onshowed = new ObservableEvent();

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
                this._showImage(previousImage);
            }
        },

        showNext: function () {
            var nextImage = this._getNext();
            if (nextImage) {
                this._showImage(nextImage);
            }
        },

        _showImage: function (imageElement) {
            this._hideCurrent();
            imageElement.classList.remove(this._hiddenSign);
            imageElement.classList.add(this._currentSign);
            this.onshowed.notify();
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
        this._currentSign = "current";
        this._soundUrls = [];
        this.onplayed = new ObservableEvent();

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
                soundLink.onended = function (e, args) {
                    this.currentTime = 0;
                    if (this.currentTime > 0) {
                        this.load();
                    }
                };
                this._soundSpeakElement.appendChild(soundLink);
            }
        },

        playFirst: function () {
            var firstSound = this._getFirst();
            if (firstSound) {
                this._playSound(firstSound);
            }
        },

        playLast: function () {
            var lastSound = this._getLast();
            if (lastSound) {
                this._playSound(lastSound);
            }
        },

        playPrevious: function () {
            var previousSound = this._getPrevious();
            if (previousSound) {
                this._playSound(previousSound);
            }
        },

        playNext: function () {
            var nextSound = this._getNext();
            if (nextSound) {
                this._playSound(nextSound);
            }
        },

        hasSound: function () {
            return this._soundSpeakElement.children.length > 0;
        },

        hasNext: function () {
            return this._getNext() != null;
        },

        hasPrevious: function () {
            return this._getPrevious() != null;
        },

        _playSound: function (soundElement) {
            this._unmarkCurrent();
            soundElement.classList.add(this._currentSign);
            soundElement.play();
            this.onplayed.notify();
        },

        _unmarkCurrent: function () {
            var current = this._getCurrent();
            if (current) {
                current.classList.remove(this._currentSign);
            }
        },

        _getCurrent: function () {
            return dom.getFirstChildByClass(this._soundSpeakElement, this._currentSign);
        },

        _getFirst: function () {
            if (this.hasSound()) {
                return this._soundSpeakElement.children[0];
            }
        },

        _getLast: function () {
            if (this.hasSound()) {
                return this._soundSpeakElement.children[this._soundSpeakElement.children.length - 1];
            }
        },

        _getPrevious: function () {
            var currentSound = this._getCurrent();
            if (currentSound) {
                var previousElement = currentSound.previousElementSibling;
                if (previousElement && previousElement.nodeName === "AUDIO") {
                    return previousElement;
                }
            }
            return this._getLast();
        },

        _getNext: function () {
            var currentSound = this._getCurrent();
            if (currentSound) {
                var nextElement = currentSound.nextElementSibling;
                if (nextElement && nextElement.nodeName === "AUDIO") {
                    return nextElement;
                }
            }
            return this._getFirst();
        }
    };

    langstyle.StageFrame = function (options) {
        if (!(this instanceof langstyle.StageFrame)) {
            return new langstyle.StageFrame(options);
        }

        this._nextFrameId = options.nextFrameId;
        this._previousFrameId = options.previousFrameId;
        this._stageFrameId = options.stageFrameId;
        this._nextFrameElement = dom.getById(this._nextFrameId);
        this._previousFrameElement = dom.getById(this._previousFrameId);
        this._stageFrameElement = dom.getById(this._stageFrameId);
        this._hiddenSign = "hidden";
        this._disabledSign = "disabled";
        this._imageView = options.imageView;
        this._soundSpeak = options.soundSpeak;

        this.init();
    };

    langstyle.StageFrame.prototype = {

        init: function () {
            this._previousFrameElement.onclick = function () {
                this._previous();
            } .bind(this);

            this._nextFrameElement.onclick = function () {
                this._next();
            } .bind(this);

            this._imageView.onshowed.unsubscribe(this.refresh.bind(this));
            this._soundSpeak.onplayed.unsubscribe(this.refresh.bind(this));

            this._imageView.onshowed.subscribe(this.refresh.bind(this));
            this._soundSpeak.onplayed.subscribe(this.refresh.bind(this));
        },

        refresh: function () {
            if (this.isEmpty()) {
                this._hide();
                return;
            }
            this._show();

            if (this.hasNext()) {
                this._enableNext();
            }
            else {
                this._disableNext();
            }

            if (this.hasPrevious()) {
                this._enablePrevious();
            }
            else {
                this._disablePrevious();
            }
        },

        isEmpty: function () {
            if (this._imageView != null && this._imageView.hasImage()) {
                return false;
            }
            if (this._soundSpeak != null && this._soundSpeak.hasSound()) {
                return false;
            }
            return true;
        },

        hasNext: function () {
            if (this._imageView != null && this._imageView.hasNext()) {
                return true;
            }
            if (this._soundSpeak != null && this._soundSpeak.hasNext()) {
                return true;
            }
            return false;
        },

        hasPrevious: function () {
            if (this._imageView != null && this._imageView.hasPrevious()) {
                return true;
            }
            if (this._soundSpeak != null && this._soundSpeak.hasPrevious()) {
                return true;
            }
            return false;
        },

        _previous: function () {
            this._imageView.showPrevious();
            this._soundSpeak.playPrevious();
        },

        _next: function () {
            this._imageView.showNext();
            this._soundSpeak.playNext();
        },

        _hide: function () {
            this._disableNext();
            this._disablePrevious();
            this._stageFrameElement.classList.add(this._hiddenSign);
        },

        _show: function () {
            this._stageFrameElement.classList.remove(this._hiddenSign);
        },

        _enablePrevious: function () {
            this._previousFrameElement.classList.remove(this._diabledSign);
        },

        _disablePrevious: function () {
            this._previousFrameElement.classList.add(this._diabledSign);
        },

        _enableNext: function () {
            this._nextFrameElement.classList.remove(this._diabledSign);
        },

        _disableNext: function () {
            this._nextFrameElement.classList.add(this._diabledSign);
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

        this.stageFrame = new langstyle.StageFrame({
            "nextFrameId": options.nextFrameId,
            "previousFrameId": options.previousFrameId,
            "stageFrameId": options.stageFrameId,
            "imageView": this.imageView,
            "soundSpeak": this.soundSpeak
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
            this.wordCharacter.getCharacterCode(characterId)
            .then(function (character) {
                this._character = character;
            } .bind(this),
                function (erorrMessage) {
                    this._character = "";
                } .bind(this)
            ).then(function () {
                this.showCharacter();
            } .bind(this));
        },

        getImages: function (characterId) {
            this.userProgress.getCharacterImages(characterId)
            .then(function (imageIds) {
                this._imageIds = this._getArrayFromString(imageIds);
            } .bind(this),
                function (errorMessage) {
                    this._imageIds = [];
                } .bind(this)
            ).then(function () {
                var imageUrls = this._getImageUrlsByIds(this._imageIds);
                this.imageView.load(imageUrls);
            } .bind(this));
        },

        getSounds: function (characterId) {
            this.userProgress.getCharacterSounds(characterId)
            .then(function (soundIds) {
                this._soundIds = this._getArrayFromString(soundIds);
            } .bind(this),
                function (errorMessage) {
                    this._soundIds = [];
                } .bind(this)
            ).then(function () {
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