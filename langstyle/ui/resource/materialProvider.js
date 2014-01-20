
(function () {
    var MeterialProvider = function (imageFileId, characterCodeId) {
        if (!(this instanceof MeterialProvider)) {
            return MeterialProvider(imageFileId, characterCodeId);
        }

        this.imageUploader = new FileUploader(imageFileId, langstyle.imageUrl);
        this.characterCodeId = characterCodeId;
        this.characterImageUrl = langstyle.characterImageUrl;
        this.characterUrl = langstyle.characterUrl;
        this.characterCodeUrl = langstyle.characterCodeUrl;
    };

    MeterialProvider.prototype = {

        linkImageToCharacter: function () {
            var self = this;
            this.imageUploader.send().then(function (imageId) {
                ajax.post(self.characterCodeUrl + "/" + self.getCharacterCode()).then(function (characterId) {
                    var characterImageParameters = {
                        "character": characterId,
                        "image": imageId
                    };
                    var characterImageUrl = langstyle.joinUrl(self.characterImageUrl, characterImageParameters);
                    ajax.post(characterImageUrl);
                });
            },
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

    if (langstyle) {
        langstyle.MeterialProvider = MeterialProvider;
    }

    window.MeterialProvider = MeterialProvider;

} ());
