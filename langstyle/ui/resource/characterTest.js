(function (langstyle) {

    var CharacterTest = function (options) {
        if (!(this instanceof CharacterTest)) {
            return new CharacterTest(options);
        }

        this.characterTestId = options.characterTestId;
        this.characterInputId = options.userCharacterInputId;
        this.characterTestElement = dom.getById(options.characterTestId);
        this.characterInputElement = dom.getById(options.userCharacterInputId);
        this._characterCode = null;
        this._passSign = "sign";
        this._hiddenSign = "hidden";
    };

    CharacterTest.prototype = {

        load: function (characterCode) {
            this._reset();
            this._characterCode = characterCode;
        },

        test: function (characterCode) {
            // display image and play sound
            // user type character
            // compare user's input with the correct character
            this.characterTestElement.classList.add(this._passSign);
        },

        hasCharacter: function () {
            if (this._characterCode) {
                return this._characterCode.length > 0;
            }
            return false;
        },

        isFinished: function () {
            if (this.hasCharacter()) {
                return this.characterTestElement.classList.contains(this._passSign);
            }
            return true;
        },

        _reset: function () {
            this.characterTestElement.classList.remove(this._passSign);
        },

        show: function () {
            this.characterTestElement.classList.remove(this._hiddenSign);
        },

        hide: function () {
            this.characterTestElement.classList.add(this._hiddenSign);
        }
    };

    langstyle.CharacterTest = CharacterTest;

} (langstyle));