(function (langstyle) {

    var CharacterView = function (options) {
        if (!(this instanceof CharacterView)) {
            return new CharacterView(options);
        }

        this._characterId = options.characterId;
        this._characterViewId = options.characterViewId;
        this._characterElement = dom.getById(options.characterId);
        this._characterViewElement = dom.getById(options.characterViewId);
        this._characterCode = null;
        this._hiddenSign = "hidden";
    };

    CharacterView.prototype = {

        load: function (characterCode) {
            this._characterCode = characterCode;
            this._characterElement.textContent = this._characterCode;
        },

        show: function () {
            this._characterViewElement.classList.remove(this._hiddenSign);
        },

        hide: function () {
            this._characterViewElement.classList.add(this._hiddenSign);
        }
    };

    langstyle.CharacterView = CharacterView;

} (langstyle));