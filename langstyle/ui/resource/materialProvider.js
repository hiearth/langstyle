
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
            this.addCharacter().then(function (characterId) {
                this.linkImageToCharacter(characterId);
                this.linkSoundToCharacter(characterId);
            } .bind(this));
        },

        addCharacter: function () {
            return ajax.post(this.characterCodeUrl + "/" + this.getCharacterCode());
        },

        linkImageToCharacter: function (characterId) {
            this.imageUploader.send().then(function (imageId) {
                var characterImageParameters = {
                    "character": characterId,
                    "image": imageId
                };
                var characterImageUrl = langstyle.joinUrl(this.characterImageUrl, characterImageParameters);
                ajax.post(characterImageUrl);
            } .bind(this),
            function (error) {
            } .bind(this));
        },

        linkSoundToCharacter: function (characterId) {
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
        }
    };

    langstyle.MeterialProvider = MeterialProvider;

} (langstyle, ajax));
