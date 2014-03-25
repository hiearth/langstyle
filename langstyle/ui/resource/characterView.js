(function (langstyle) {

    var CharacterView = function (options) {
        if (!(this instanceof CharacterView)) {
            return new CharacterView(options);
        }

        this._characterId = options.characterId;
        this._characterViewId = options.characterViewId;
        this._characterExplainationId = options.characterExplainationId;
        this._characterElement = dom.getById(options.characterId);
        this._characterExplainationElement = dom.getById(options.characterExplainationId);
        this._characterViewElement = dom.getById(options.characterViewId);
        this._characterCode = null;
        this._explaination = null;
        this._hiddenSign = "hidden";
    };

    CharacterView.prototype = {

        load: function (character) {
            this._characterCode = character.characterCode;
            this._explaination = character.explaination;
            this._characterElement.textContent = this._characterCode;
            this._characterExplainationElement.textContent = this._explaination;
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
