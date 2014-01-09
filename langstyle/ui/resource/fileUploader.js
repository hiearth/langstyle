
(function () {

    var _FileReader = function (fileElementId) {
        if (!(this instanceof _FileReader)) {
            return _FileReader();
        }
        this.fileElementId = fileElementId;
    };

    _FileReader.prototype = {

        _getFileElement: function () {
            return dom.getById(this.fileElementId);
        },

        _getFile: function () {
            if (this.hasFile()) {
                var fileElement = this._getFileElement();
                return fileElement.files[0];
            }
        },

        hasFile: function () {
            var fileElement = this._getFileElement();
            return fileElement.files && fileElement.files.length > 0;
        },

        read: function () {
            var file = this._getFile();
            var promise = new Promise();
            if (file) {
                var fileReader = new FileReader();
                fileReader.addEventListener("loadend", function () {
                    if (fileReader.error) {
                        promise.reject(fileReader.error);
                    }
                    else {
                        promise.fulfill({ "type": file.type, "content": fileReader.result });
                    }
                });
                fileReader.readAsArrayBuffer(file);
            }
            else {
                promise.reject("no file");
            }
            return promise;
        }
    };

    var FileUploader = function (fileElementId, uploadUrl) {
        this._fileReader = new _FileReader(fileElementId);
        this.uploadUrl = uploadUrl;
    };

    FileUploader.prototype = {

        send: function () {
            var self = this;
            this._fileReader.read().then(function (file) {
                var requestHeaders = null;
                if (file.type) {
                    requestHeaders = { "content-type": file.type };
                }
                ajax.post(self.uploadUrl, requestHeaders, file.content);
            },
            function (error) {
            });
        }
    };

    if (langstyle) {
        langstyle.FileUploader = FileUploader;
    }

    window.FileUploader = FileUploader;

} ());