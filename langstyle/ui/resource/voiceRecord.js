(function (langstyle, dom) {

    navigator.getUserMedia = (navigator.getUserMedia
                            || navigator.webkitGetUserMedia
                            || navigator.mozGetUserMedia
                            || navigator.msGetUserMedia);

    window.AudioContext = window.AudioContext || window.webkitAudioContext;

    var VoiceRecord = function (options) {
        if (!(this instanceof VoiceRecord)) {
            return new VoiceRecord(options);
        }
        this.voiceRecordId = options.voiceRecordId;
        this.voiceRecordElement = dom.getById(options.voiceRecordId);
        this.recordedSign = "recorded";
        this._audioContext = new AudioContext();
        this._audioRecorder = null;
    };

    VoiceRecord.prototype = {

        record: function () {
            navigator.getUserMedia({ audio: true },
                this._getStream.bind(this),
                function (error) {
                    console.log(error);
                } .bind(this)
            );
        },

        _getStream: function (stream) {
            var inputPoint = this._audioContext.createGain();
            var audioInput = this._audioContext.createMediaStreamSource(stream);
            audioInput.connect(inputPoint);
            this._audioRecorder = new langstyle.Recorder(inputPoint);
            this._audioRecorder.record();
            setTimeout(this._stopRecord.bind(this), 3000);
        },

        _stopRecord: function () {
            this._audioRecorder.stop();
            this._audioRecorder.exportWAV(this._exportWav.bind(this));
        },

        _exportWav: function (blob) {
            this.voiceRecordElement.src = URL.createObjectURL(blob);
            this.voiceRecordElement.load();
            this.voiceRecordElement.play();
        },

        reset: function () {
            this.voiceRecordElement.src = null;
            this.voiceRecordElement.classList.remove(this.recordedSign);
        },

        play: function () {
            this.voiceRecordElement.play();
        },

        isFinished: function () {
            return this.voiceRecordElement.classList.contains(this.recordedSign);
        }
    };

    langstyle.VoiceRecord = VoiceRecord;

} (langstyle, dom));