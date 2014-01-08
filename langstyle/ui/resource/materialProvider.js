
(function () {
    var MeterialProvider = function (imageFileId, imageRestUrl) {
        if (!(this instanceof MeterialProvider)) {
            return MeterialProvider();
        }
        this.imageUploader = new FileUploader(imageFileId, imageRestUrl);
    };

    MeterialProvider.prototype = {

        addImage: function () {
            this.imageUploader.send();
        },

        linkImageToCharacter: function () {

        }
    };

    if (langstyle) {
        langstyle.MeterialProvider = MeterialProvider;
    }

    window.MeterialProvider = MeterialProvider;

} ());