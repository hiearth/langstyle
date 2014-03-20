(function (langstyle) {

    var CharacterTest = function (options) {
        if (!(this instanceof CharacterTest)) {
            return new CharacterTest(options);
        }

        this.characterTestId = options.characterTestId;
        this.characterInputId = options.userCharacterInputId;
        this.characterHintId = options.characterHintId;
        this.characterTestElement = dom.getById(options.characterTestId);
        this.characterInputElement = dom.getById(options.userCharacterInputId);
        this.characterHintElement = dom.getById(options.characterHintId);
        this.characterView = options.characterView;
        this._characterCode = null;
        this._passSign = "pass";
        this._wrongSign = "wrong";
        this._correctSign = "correct";
        this._hiddenSign = "hidden";
        this._hintTimer = null;

        this.init()
    };

    CharacterTest.prototype = {

        init: function () {
            this.characterInputElement.oninput = function (e) {
                this._testRealTime(e.target);
            } .bind(this);

            this.characterInputElement.onkeypress = function (e) {
                this._clearTimer();
                if (!this._isHintShown()) {
                    this._hintTimer = setTimeout(this._showHint.bind(this), 4000);
                }
            } .bind(this);

            this.characterHintElement.onclick = function () {
                this.characterView.show();
            } .bind(this);
        },

        load: function (characterCode) {
            this._reset();
            this._characterCode = characterCode;
        },

        _testRealTime: function (inputElement) {
            var userInput = inputElement.value.trim();
            if (userInput.length > this._characterCode.length) {
                this._showWrongSign();
                return;
            }
            if (userInput.length < this._characterCode.length) {
                var leftPartCharacter = this._characterCode.slice(0, userInput.length);
                if (userInput !== leftPartCharacter) {
                    this._showWrongSign();
                }
                else {
                    this._resetSign();
                }
                return;
            }
            if (userInput !== this._characterCode) {
                this._showWrongSign();
            }
            else {
                this._showCorrectSign();
            }
        },

        isWaitingTest: function () {
            return !this.characterTestElement.classList.contains(this._hiddenSign);
        },

        test: function () {
            if (this._isCorrect()) {
                this._showCorrectSign();
            }
            else {
                this._showWrongSign();
                this._showHelp();
            }
        },

        _showHelp: function () {
            if (!this.characterInputElement.value) {
                this.characterInputElement.placeholder = "type word character";
            }
        },

        _hideHelp: function () {
            this.characterInputElement.placeholder = "";
        },

        _showCorrectSign: function () {
            this.characterInputElement.classList.remove(this._wrongSign);
            this.characterInputElement.classList.add(this._correctSign);
            this.characterTestElement.classList.add(this._passSign);
        },

        _showWrongSign: function () {
            this.characterInputElement.classList.remove(this._correctSign);
            this.characterInputElement.classList.add(this._wrongSign);
            this.characterTestElement.classList.remove(this._passSign);
        },

        _showHint: function () {
            this.characterHintElement.classList.remove(this._hiddenSign);
        },

        _hideHint: function () {
            this.characterHintElement.classList.add(this._hiddenSign);
        },

        _isHintShown: function () {
            return !this.characterHintElement.classList.contains(this._hiddenSign);
        },

        _isCorrect: function () {
            var userInput = this._getUserInput();
            return userInput === this._characterCode;
        },

        _getUserInput: function () {
            return this.characterInputElement.value.trim();
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
            this.characterInputElement.value = "";
            this._resetSign();
            this._clearTimer();
            this._hideHint();
            this._hideHelp();
        },

        _resetSign: function () {
            this.characterInputElement.classList.remove(this._correctSign);
            this.characterInputElement.classList.remove(this._wrongSign);
            this.characterTestElement.classList.remove(this._passSign);
        },

        _clearTimer: function () {
            if (this._hintTimer) {
                clearTimeout(this._hintTimer);
            }
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