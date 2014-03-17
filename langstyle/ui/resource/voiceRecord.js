(function (langstyle, dom) {

    navigator.getUserMedia = (navigator.getUserMedia
                            || navigator.webkitGetUserMedia
                            || navigator.mozGetUserMedia
                            || navigator.msGetUserMedia);

    var VoiceRecord = function (options) {
        if (!(this instanceof VoiceRecord)) {
            return new VoiceRecord(options);
        }
        this.voiceRecordId = options.voiceRecordId;
        this.voiceRecordElement = dom.getById(options.voiceRecordId);
        this.recordedSign = "recorded";
        this._voiceStream = null;
    };

    VoiceRecord.prototype = {

        record: function () {
            navigator.getUserMedia({ audio: true },
                function (stream) {
                    this._voiceStream = stream;
                    this.voiceRecordElement.src = URL.createObjectURL(stream);
                    this.voiceRecordElement.classList.add(this.recordedSign);
                    setTimeout(this.stop.bind(this), 2000);
                } .bind(this),
                function (error) {
                } .bind(this)
            );
        },

        reset: function () {
            this.voiceRecordElement.src = null;
            this.voiceRecordElement.classList.remove(this.recordedSign);
        },

        play: function () {
            this.voiceRecordElement.play();
        },

        stop: function () {
            if (this._voiceStream) {
                this._voiceStream.stop();
            }
        },

        isFinished: function () {
            return this.voiceRecordElement.classList.contains(this.recordedSign);
        }
    };

    langstyle.VoiceRecord = VoiceRecord;

} (langstyle, dom));