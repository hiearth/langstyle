(function (langstyle, ajax, dom) {

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
        this._wordMeaningId = null;
        this._passSign = "pass";
        this._wrongSign = "wrong";
        this._correctSign = "correct";
        this._hiddenSign = "hidden";
        this._hintTimer = null;
        this._feedbackUrl = "/charactertest";
        this._feedbackSent = false;
        this._correctSignChanged = new ObservableEvent();

        this.init()
    };

    CharacterTest.prototype = {

        init: function () {
            this.characterInputElement.oninput = function (e) {
                this._testRealTime(e.target);
            } .bind(this);

            this.characterHintElement.onclick = function () {
                this.characterView.show();
            } .bind(this);

            this._correctSignChanged.subscribe(this._manageTimer.bind(this));
        },

        load: function (wordMeaning) {
            this._reset();
            this._wordMeaningId = wordMeaning.wordMeaningId;
            this._characterCode = wordMeaning.characterCode || "";
        },

        _testRealTime: function () {
            var userInput = this._getUserInput();
            var correct = false;
            if (userInput.length < this._characterCode.length) {
                correct = this._partialCorrect();
                if (correct) {
                    this._resetSign();
                }
                else {
                    this._showWrongSign();
                }
            }
            else {
                correct = this._totalCorrect(userInput);
                if (correct) {
                    this._showCorrectSign();
                }
                else {
                    this._showWrongSign();
                }
            }
        },

        _manageTimer: function () {
            var startTimer = this.characterInputElement.classList.contains(this._wrongSign);
            if (startTimer) {
                if (!this._isHintShown()) {
                    this._hintTimer = setTimeout(this._showHint.bind(this), 4000);
                }
            }
            else{
                this._clearTimer();
            }
        },

        _partialCorrect: function () {
            var userInput = this._getUserInput();
            var leftPartCharacter = this._characterCode.slice(0, userInput.length);
            return userInput === leftPartCharacter
        },

        _totalCorrect: function () {
            var userInput = this._getUserInput();
            return userInput === this._characterCode;
        },

        isWaitingTest: function () {
            return !this.characterTestElement.classList.contains(this._hiddenSign);
        },

        test: function () {
            if (this._totalCorrect()) {
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
            var inputClassList=this.characterInputElement.classList;
            var isChanged = inputClassList.contains(this._wrongSign);
            this.characterInputElement.classList.remove(this._wrongSign);

            isChanged = isChanged || !inputClassList.contains(this._correctSign);
            this.characterInputElement.classList.add(this._correctSign);

            isChanged = isChanged || !inputClassList.contains(this._passSign);
            this.characterTestElement.classList.add(this._passSign);
            if(isChanged){
                this._correctSignChanged.notify();
            }

            this._sendFeedback();
        },

        _showWrongSign: function () {
            var inputClassList=this.characterInputElement.classList;
            var isChanged = inputClassList.contains(this._correctSign);
            this.characterInputElement.classList.remove(this._correctSign);

            isChanged = isChanged || !inputClassList.contains(this._wrongSign);
            this.characterInputElement.classList.add(this._wrongSign);

            isChanged = isChanged || inputClassList.contains(this._passSign);
            this.characterTestElement.classList.remove(this._passSign);

            if(isChanged){
                this._correctSignChanged.notify();
            }
        },
        
        _sendFeedback:function(){
            if(!this._feedbackSent){
                var feedback = {
                    "wordMeaningId": this._wordMeaningId,
                    "isPass": !this._isHintShown()
                };
                ajax.post(this._feedbackUrl, null, JSON.stringify(feedback));
                this._feedbackSent = true;
            }
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
            this._feedbackSent = false;
            this._resetSign();
            this._clearTimer();
            this._hideHint();
            this._hideHelp();
        },

        _resetSign: function () {
            var inputClassList=this.characterInputElement.classList;
            var isChanged = inputClassList.contains(this._correctSign);
            this.characterInputElement.classList.remove(this._correctSign);

            isChanged = isChanged || inputClassList.contains(this._wrongSign);
            this.characterInputElement.classList.remove(this._wrongSign);

            isChanged = isChanged || inputClassList.contains(this._passSign);
            this.characterTestElement.classList.remove(this._passSign);
            if(isChanged){
                this._correctSignChanged.notify();
            }
        },

        _clearTimer: function () {
            if (this._hintTimer) {
                clearTimeout(this._hintTimer);
            }
        },

        show: function () {
            this.characterTestElement.classList.remove(this._hiddenSign);
            this.characterInputElement.focus();
        },

        hide: function () {
            this.characterTestElement.classList.add(this._hiddenSign);
        }
    };

    langstyle.CharacterTest = CharacterTest;

} (langstyle, ajax, dom));
