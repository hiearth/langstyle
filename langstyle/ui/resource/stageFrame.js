(function (langstyle, dom) {

    var StageFrame = function (options) {
        if (!(this instanceof StageFrame)) {
            return new StageFrame(options);
        }

        this._imageView = options.imageView;
        this._soundSpeak = options.soundSpeak;

        this.init();
    };

    StageFrame.prototype = {

        init: function () {

        },

        isFinished: function () {
            if (this._imageView != null && !this._imageView.isFinished()) {
                return false;
            }
            if (this._soundSpeak != null && !this._soundSpeak.isFinished()) {
                return false;
            }
            return true;
        },

        previous: function () {
            this._imageView.showPrevious();
            this._soundSpeak.playPrevious();
        },

        next: function () {
            this._imageView.showNext();
            this._soundSpeak.playNext();
        }

    };

    langstyle.StageFrame = StageFrame;

} (langstyle, dom));