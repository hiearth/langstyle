(function (langstyle, dom) {

    var SoundSpeak = function (options) {
        if (!(this instanceof SoundSpeak)) {
            return SoundSpeak(options);
        }

        this._soundSpeakId = options.soundSpeakId;
        this._soundSpeakElement = dom.getById(this._soundSpeakId);
        this._playedSign = "played"
        this._currentSign = "current";
        this._soundUrls = [];
        this.onplayed = new ObservableEvent();
    };

    SoundSpeak.prototype = {

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

        isFinished: function () {
            if (this.hasSound()) {
                for (var i = this._soundSpeakElement.children.length - 1; i >= 0; i--) {
                    if (!this._soundSpeakElement.children[i].classList.contains(this._playedSign)) {
                        return false;
                    }
                }
            }
            return true;
        },

        _playSound: function (soundElement) {
            this._unmarkCurrent();
            soundElement.classList.add(this._currentSign);
            soundElement.play();
            soundElement.classList.add(this._playedSign);
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

    langstyle.SoundSpeak = SoundSpeak;

} (langstyle, dom));