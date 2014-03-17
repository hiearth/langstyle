(function (langstyle, dom) {

    var StageFrame = function (options) {
        if (!(this instanceof StageFrame)) {
            return new StageFrame(options);
        }

        this._imageView = options.imageView;
        this._soundSpeak = options.soundSpeak;
        this._voiceRecord = options.voiceRecord;

        this.init();
    };

    StageFrame.prototype = {

        init: function () {

        },

        isFinished: function () {
            //            if (this._imageView != null && !this._imageView.isFinished()) {
            //                return false;
            //            }
            //            if (this._soundSpeak != null && !this._soundSpeak.isFinished()) {
            //                return false;
            //            }
            //            return true;
            return this._isImageAndSoundFinished() && this._isVoiceFinished();
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

        _isVoiceFinished: function () {
            if (this._voiceRecord != null && !this._voiceRecord.isFinished()) {
                return false;
            }
            return true;
        },

        previous: function () {
            this._imageView.showPrevious();
            this._soundSpeak.playPrevious();
        },

        next: function () {
            if (!this._isImageAndSoundFinished()) {
                this._imageView.showNext();
                this._soundSpeak.playNext();
            }
            else {
                this._voiceRecord.record();
            }
        }

    };

    langstyle.StageFrame = StageFrame;

} (langstyle, dom));