
(function (langstyle, ajax) {

    var MeterialProvider = function (options) {
        if (!(this instanceof MeterialProvider)) {
            return MeterialProvider(options);
        }

        this.imageUrl = "/image";
        this.soundUrl = "/sound";
        this.characterUrl = "/character";
        this.characterCodeUrl = "/charactercode";
        this.characterImageUrl = "/characterimage";
        this.characterSoundUrl = "/charactersound";
        this.characterCodeId = options.characterCodeId;
        this.imageUploader = new FileUploader(options.imageFileId, this.imageUrl);
        this.soundUploader = new FileUploader(options.soundFileId, this.soundUrl);
    };

    MeterialProvider.prototype = {

        upload: function () {
            this.linkImageToCharacter();
            this.linkSoundToCharacter();
        },

        linkImageToCharacter: function () {
            var self = this;
            this.imageUploader.send().then(function (imageId) {
                this.addCharacter().then(function (characterId) {
                    var characterImageParameters = {
                        "character": characterId,
                        "image": imageId
                    };
                    var characterImageUrl = langstyle.joinUrl(self.characterImageUrl, characterImageParameters);
                    ajax.post(characterImageUrl);
                });
            } .bind(this),
            function (error) {
            });
        },

        linkSoundToCharacter: function () {
            this.soundUploader.send().then(function (soundId) {
                this.addCharacter().then(function (characterId) {
                    var characterSoundParameters = {
                        "character": characterId,
                        "sound": soundId
                    };
                    var characterSoundUrl = langstyle.joinUrl(this.characterSoundUrl, characterSoundParameters);
                    ajax.post(characterSoundUrl)
                } .bind(this));
            } .bind(this),
            function (error) {
            });
        },

        getCharacterCode: function () {
            var characterCodeElement = dom.getById(this.characterCodeId);
            if (characterCodeElement) {
                return characterCodeElement.value;
            }
        },

        addCharacter: function () {
            return ajax.post(this.characterCodeUrl + "/" + this.getCharacterCode());
        }
    };

    langstyle.MeterialProvider = MeterialProvider;

} (langstyle, ajax));
