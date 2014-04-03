
(function (langstyle, dom) {

    var Application = function () {
        if (!(this instanceof Application)) {
            return new Application();
        }

        this.hiddenSign = "hidden";
        this.wordStage = new langstyle.WordStage({
            "stageId": "wordStage",
            "characterViewId":"characterView",
            "characterId": "character",
            "characterExplainationId":"characterExplaination",
            "characterTestId": "characterTest",
            "userCharacterInputId":"userCharacterInput",
            "characterHintId":"characterHint",
            "soundId": "sound",
            "imageId": "image",
            "imageViewId": "images",
            "soundSpeakId": "sounds",
            "voiceRecordId": "voice",
            "nextUnavailableId":"nextUnavailable",
            "stageFrameId": "stageFrame",
            "previousFrameId": "previousFrame",
            "nextFrameId": "nextFrame"
        });

        this.materialProvider = new langstyle.MeterialProvider({
            "imageFileId": "imageFile",
            "characterCodeId": "characterCode",
            "soundFileId": "soundFile"
        });

        this.userRegister = new langstyle.UserRegister({
            "userNameId": "registerUserName",
            "passwordId": "registerPassword",
            "confirmPasswordId": "registerConfirmPassword"
        });

        this.userLogin = new langstyle.UserLogin({
            "userNameId": "loginUserName",
            "passwordId": "loginPassword"
        });

        this.stageSwitch = new langstyle.StageSwitch();

        this.homeNavigationButton = dom.getById("homeNavigation");
        this.userNameLink = dom.getById("userName");
        this.startMenu = dom.getById("startMenu");
        this.addMenu = dom.getById("addMenu");
        this.registerUserMenu = dom.getById("registerMenu");
        this.loginMenu = dom.getById("loginMenu");
        this.logoutButton = dom.getById("logout");
        this.loginButton = dom.getById("login");
        this.registerButton = dom.getById("register");
        this.nextWordButton = dom.getById("nextWord");
        this.addForm = dom.getById("addForm");

        this.init();
    };

    Application.prototype = {

        init: function () {
            if (this.userLogin.hasLogin()) {
                this.showUserName();
            }
            else {
                this.hideUserName();
                this.stageSwitch.showLogin();
            }

            this.homeNavigationButton.onclick = function (e) {
                this.stageSwitch.showStart();
            } .bind(this);

            this.startMenu.onclick = function (e) {
                this.stageSwitch.showWord();
            } .bind(this);

            this.addMenu.onclick = function (e) {
                this.stageSwitch.showAdd();
            } .bind(this);

            this.registerUserMenu.onclick = function (e) {
                this.stageSwitch.showRegister();
            } .bind(this);

            this.loginMenu.onclick = function () {
                this.stageSwitch.showLogin();
            } .bind(this);

            this.logoutButton.onclick = function () {
                this.userLogin.logout().then(function () {
                    this.hideMenus();
                    this.hideUserName();
                    this.stageSwitch.showLogin();
                } .bind(this));
            } .bind(this);

            this.loginButton.onclick = function (e) {
                if (this.userLogin.validate()) {
                    this.userLogin.login().then(function () {
                        this.showMenus();
                        this.showUserName();
                        this.stageSwitch.showWord();
                    } .bind(this));
                }
            } .bind(this);

            this.registerButton.onclick = function (e) {
                if (this.userRegister.validate()) {
                    this.userRegister.register().then(function () {
                        this.showMenus();
                        this.showUserName();
                        this.stageSwitch.showWord();
                    } .bind(this));
                }
            } .bind(this);
        },

        showUserName: function () {
            var userName = this.userLogin.getUserName();
            this.userNameLink.textContent = userName;
            this.userNameLink.onclick = function () {
                this.stageSwitch.showUser();
            } .bind(this);
        },

        hideUserName: function () {
            this.userNameLink.textContent = "";
            this.userNameLink.onclick = null;
        },

        hideMenus: function () {
            this.startMenu.classList.add(this.hiddenSign);
            this.addMenu.classList.add(this.hiddenSign);
        },

        showMenus: function () {
            this.startMenu.classList.remove(this.hiddenSign);
            this.addMenu.classList.remove(this.hiddenSign);
        }

    };

    langstyle.Application = Application;

} (langstyle, dom));
