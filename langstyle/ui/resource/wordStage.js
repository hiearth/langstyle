(function (langstyle, dom) {

    var WordStage = function (options) {
        if (!(this instanceof WordStage)) {
            return new WordStage(options);
        }

        this._options = options;
        this._stageNode = dom.getById(options.stageId);

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

        this.characterUnavailable = new langstyle.CharacterUnavailable({
            "nextUnavailableId":options.nextUnavailableId
        });

        this.stageFrame = new langstyle.StageFrame({
            "nextFrameId": options.nextFrameId,
            "previousFrameId": options.previousFrameId,
            "stageFrameId": options.stageFrameId,
            "characterView": this.characterView,
            "imageView": this.imageView,
            "soundSpeak": this.soundSpeak,
            "characterTest": this.characterTest,
            "characterUnavailable":this.characterUnavailable
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
                var wordMeaning = {
                    "wordMeaningId": nextWordObj.wordMeaningId,
                    "characterCode": nextWordObj.characterCode, 
                    "explaination": nextWordObj.explaination
                };
                var imageUrls = this._getImageUrlsByIds(nextWordObj.images);
                var soundUrls = this._getSoundUrlsByIds(nextWordObj.sounds);
                this.stageFrame.load(wordMeaning, imageUrls, soundUrls);
            } .bind(this),
                function (errorResponse) {
                    this.stageFrame.nextUnavailable(errorResponse.status);
                } .bind(this)
            );
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
