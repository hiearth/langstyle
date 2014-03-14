(function (langstyle, dom) {

    var WordStage = function (options) {
        if (!(this instanceof WordStage)) {
            return new WordStage(options);
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

    WordStage.prototype = {

        play: function () {
            if (this.stageFrame.isFinished()) {
                this._getNextWord();
            }
            else {
                this.stageFrame.next();
            }
        },

        _getNextWord: function () {
            this.userProgress.getNext().then(function (nextWord) {
                var nextWordObj = JSON.parse(nextWord);
                this._character = nextWordObj.characterCode;
                this._imageIds = nextWordObj.images;
                this._soundIds = nextWordObj.sounds;
            } .bind(this),
                function () {
                    this._character = "";
                    this._imageIds = [];
                    this._soundIds = [];
                } .bind(this)
            ).then(function () {
                this.showCharacter();
                var imageUrls = this._getImageUrlsByIds(this._imageIds);
                this.imageView.load(imageUrls);
                var soundUrls = this._getSoundUrlsByIds(this._soundIds);
                this.soundSpeak.load(soundUrls);
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

    langstyle.WordStage = WordStage;

} (langstyle, dom));