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

        this.characterView = new langstyle.CharacterView({
            "characterViewId": options.characterViewId,
            "characterId": options.characterId,
            "characterExplainationId":options.characterExplainationId
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

        this.characterTest = new langstyle.CharacterTest({
            "characterTestId": options.characterTestId,
            "userCharacterInputId": options.userCharacterInputId,
            "characterHintId": options.characterHintId,
            "characterView": this.characterView
        });

        this.stageFrame = new langstyle.StageFrame({
            "nextFrameId": options.nextFrameId,
            "previousFrameId": options.previousFrameId,
            "stageFrameId": options.stageFrameId,
            "characterView": this.characterView,
            "imageView": this.imageView,
            "soundSpeak": this.soundSpeak,
            "characterTest": this.characterTest
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
                this._character = {
                    "characterCode": nextWordObj.characterCode, 
                    "explaination": nextWordObj.explaination
                };
                this._imageIds = nextWordObj.images;
                this._soundIds = nextWordObj.sounds;
            } .bind(this),
                function () {
                    this._character = {};
                    this._imageIds = [];
                    this._soundIds = [];
                } .bind(this)
            ).then(function () {
                var imageUrls = this._getImageUrlsByIds(this._imageIds);
                var soundUrls = this._getSoundUrlsByIds(this._soundIds);
                this.stageFrame.load(this._character, imageUrls, soundUrls);
            } .bind(this));
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
