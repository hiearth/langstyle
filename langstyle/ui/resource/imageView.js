
(function (langstyle, dom) {

    // display image one by one
    // can load all images once, and control their visibility
    var ImageView = function (options) {
        if (!(this instanceof ImageView)) {
            return new ImageView(options);
        }

        this._imageViewId = options.imageViewId;
        this._imageViewElement = dom.getById(this._imageViewId);
        this._currentSign = "current";
        this._hiddenSign = "hidden";
        this._imageUrls = [];
        this.onshowed = new ObservableEvent();

        this.init();
    };

    ImageView.prototype = {

        init: function () {
            this._imageViewElement.addEventListener("touchMove", this.showNext.bind(this));
        },

        load: function (imageUrls) {
            this._imageUrls = imageUrls;
            this._reset();
            this._loadImages();
            this.showFirst();
        },

        _reset: function () {
            dom.emptyElement(this._imageViewElement);
        },

        _loadImages: function () {
            var length = this._imageUrls.length;
            for (var i = 0; i < length; i++) {
                var imageLink = dom.createElement("img");
                imageLink.alt = this._imageUrls[i];
                imageLink.src = this._imageUrls[i];
                imageLink.classList.add(this._hiddenSign);
                this._imageViewElement.appendChild(imageLink);
            }
        },

        hasImage: function () {
            return this._imageViewElement.children.length > 0;
        },

        hasNext: function () {
            return this._getNext() != null;
        },

        hasPrevious: function () {
            return this._getPrevious() != null;
        },

        showFirst: function () {
            var firstImage = this._getFirst();
            if (firstImage) {
                this._showImage(firstImage);
            }
        },

        showPrevious: function () {
            var previousImage = this._getPrevious();
            if (previousImage) {
                this._showImage(previousImage);
            }
        },

        showNext: function () {
            var nextImage = this._getNext();
            if (nextImage) {
                this._showImage(nextImage);
            }
        },

        _showImage: function (imageElement) {
            this._hideCurrent();
            imageElement.classList.remove(this._hiddenSign);
            imageElement.classList.add(this._currentSign);
            this.onshowed.notify();
        },

        _hideCurrent: function () {
            var currentImage = this._getCurrent();
            if (currentImage) {
                currentImage.classList.remove(this._currentSign);
                currentImage.classList.add(this._hiddenSign);
            }
        },

        _getFirst: function () {
            if (this.hasImage()) {
                return this._imageViewElement.children[0];
            }
        },

        _getLast: function () {
            if (this.hasImage()) {
                var lastImageIndex = this._imageViewElement.children.length - 1;
                return this._imageViewElement.children[lastImageIndex];
            }
        },

        _getCurrent: function () {
            return dom.getFirstChildByClass(this._imageViewElement, this._currentSign);
        },

        _getNext: function () {
            var currentImage = this._getCurrent();
            if (currentImage) {
                var nextElement = currentImage.nextElementSibling;
                if (nextElement && nextElement.nodeName === "IMG") {
                    return nextElement;
                }
            }
            return this._getFirst();
        },

        _getPrevious: function () {
            var currentImage = this._getCurrent();
            if (currentImage) {
                var previousElement = currentImage.previousElementSibling;
                if (previousElement && previousElement.nodeName === "IMG") {
                    return previousElement;
                }
            }
            return this._getLast();
        }
    };

    langstyle.ImageView = ImageView;

} (langstyle, dom));