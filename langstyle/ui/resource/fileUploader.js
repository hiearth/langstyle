
(function () {

    var FileUploader = function (fileElementId, uploadUrl) {
        this.fileElementId = fileElementId;
        this.uploadUrl = uploadUrl;
    };

    FileUploader.prototype = {

        send: function () {
            var self = this;

            var fileElement = dom.getById(this.fileElementId);
            if (fileElement.files && fileElement.files.length > 0) {
                var file = fileElement.files[0];
                var fileReader = new FileReader();
                fileReader.addEventListener("loadend", function () {
                    if (fileReader.error) {
                        console.log(fileReader.error);
                        return;
                    }
                    var xhr = new XMLHttpRequest();
                    xhr.open("post", self.uploadUrl);
                    if (file.type) {
                        xhr.overrideMimeType(file.type);
                    }
                    xhr.send(fileReader.result);
                });
                fileReader.readAsArrayBuffer(file);
            }
        }
    };

    if (langstyle) {
        langstyle.FileUploader = FileUploader;
    }

    window.FileUploader = FileUploader;

} ());