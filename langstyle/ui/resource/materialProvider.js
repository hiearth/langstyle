
(function () {
    var MeterialProvider = function (options) {
        if (!(this instanceof MeterialProvider)) {
            return MeterialProvider(options);
        }

        this.imageUrl = "/image";
        this.characterUrl = "/character";
        this.characterCodeUrl = "/charactercode";
        this.characterImageUrl = "/characterimage";
        this.characterCodeId = options.characterCodeId;
        this.imageUploader = new FileUploader(options.imageFileId, this.imageUrl);
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
