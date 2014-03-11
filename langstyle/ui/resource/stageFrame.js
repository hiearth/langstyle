(function (langstyle, dom) {

    var StageFrame = function (options) {
        if (!(this instanceof StageFrame)) {
            return new StageFrame(options);
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

    StageFrame.prototype = {

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

    langstyle.StageFrame = StageFrame;

} (langstyle, dom));