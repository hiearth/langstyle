
(function () {

    var StageSwitch = function () {
        if (!(this instanceof StageSwitch)) {
            return new StageSwitch();
        }
        this.stages = [
            "startStage",
            "wordStage",
            "addStage",
            "loginStage",
            "registerStage",
            "userStage"
        ];
        this.stagesWithHeader = ["startStage", "loginStage", "registerStage"];
        this.headerElement = dom.getById("header");
        this.navigationBar = dom.getById("navigation");
        this.hiddenSign = "hidden";
    };

    StageSwitch.prototype = {

        showStart: function () {
            this._showStage("startStage");
        },

        showWord: function () {
            this._showStage("wordStage");
        },

        showAdd: function () {
            this._showStage("addStage");
        },

        showLogin: function () {
            this._showStage("loginStage");
        },

        showRegister: function () {
            this._showStage("registerStage");
        },

        showUser: function () {
            this._showStage("userStage");
        },

        _showStage: function (stageId) {
            this._hideStages();
            var stage = dom.getById(stageId);
            dom.removeClass(stage, this.hiddenSign)
            if (this._isStageWithHeader(stageId)) {
                this._showHeader();
                this._hideNavigation();
            }
            else {
                this._hideHeader();
                this._showNavigation();
            }
        },

        _isStageWithHeader: function (stageId) {
            for (var i = this.stagesWithHeader.length - 1; i >= 0; i--) {
                if (this.stagesWithHeader[i] === stageId) {
                    return true;
                }
            }
            return false;
        },

        _hideHeader: function () {
            dom.addClass(this.headerElement, this.hiddenSign);
        },

        _showHeader: function () {
            dom.removeClass(this.headerElement, this.hiddenSign);
        },

        _showNavigation: function () {
            dom.removeClass(this.navigationBar, this.hiddenSign);
        },

        _hideNavigation: function () {
            dom.addClass(this.navigationBar, this.hiddenSign);
        },

        _hideStages: function () {
            for (var i = this.stages.length - 1; i >= 0; i--) {
                var stage = dom.getById(this.stages[i]);
                dom.addClass(stage, this.hiddenSign);
            }
        }
    };

    langstyle.StageSwitch = StageSwitch;

} (langstyle, dom));