(function (langstyle, dom) {

    var StageFrame = function (options) {
        if (!(this instanceof StageFrame)) {
            return new StageFrame(options);
        }

        this._characterView = options.characterView;
        this._imageView = options.imageView;
        this._soundSpeak = options.soundSpeak;
        this._characterTest = options.characterTest;
    };

    StageFrame.prototype = {

        load: function (characterCode, imageUrls, soundUrls) {
            this._showCharacterView();
            this._characterView.load(characterCode);
            this._imageView.load(imageUrls);
            this._soundSpeak.load(soundUrls);
            this._characterTest.load(characterCode);
        },

        next: function () {
            if (this._isImageAndSoundFinished()) {
                if (this._characterTest.isWaitingTest()) {
                    this._characterTest.test();
                }
                else {
                    this._showCharacterTest();
                }
            }
            this._imageView.showNext();
            this._soundSpeak.playNext();
        },

        previous: function () {
            this._imageView.showPrevious();
            this._soundSpeak.playPrevious();
        },

        isFinished: function () {
            return this._isImageAndSoundFinished() && this._isTestFinished();
        },

        _isImageAndSoundFinished: function () {
            if (this._imageView != null && !this._imageView.isFinished()) {
                return false;
            }
            if (this._soundSpeak != null && !this._soundSpeak.isFinished()) {
                return false;
            }
            return true;
        },

        _isTestFinished: function () {
            if (this._characterTest != null && !this._characterTest.isFinished()) {
                return false;
            }
            return true;
        },

        _showCharacterView: function () {
            this._characterTest.hide();
            this._characterView.show();
        },

        _showCharacterTest: function () {
            this._characterView.hide();
            this._characterTest.show();
        }
    };

    langstyle.StageFrame = StageFrame;

} (langstyle, dom));