
(function (dom) {
    var stages = ["stage", "addStage", "loginPage", "registerPage"];

    var hideStages = function () {
        for (var i = stages.length - 1; i >= 0; i--) {
            var stage = dom.getById(stages[i]);
            dom.addClass(stage, "hidden");
        }
    };

    var showStage = function (stageId) {
        hideStages();
        var stage = dom.getById(stageId);
        dom.removeClass(stage, "hidden");
    };

    var startButton = dom.getFirstByClass("js-start-menu");
    startButton.onclick = function (e) {
        showStage("stage");
    };

    var addButton = dom.getFirstByClass("js-add-menu");
    addButton.onclick = function (e) {
        showStage("addStage");
    };

    var registerUserButton = dom.getFirstByClass("js-register-menu");
    registerUserButton.onclick = function (e) {
        showStage("registerPage");
    };

    var wordStage = new langstyle.WordStage({
        "stageId": "stage",
        "characterId": "character",
        "soundId": "sound",
        "imageId": "image",
        "imageViewId": "images"
    });
    window.wordStage = wordStage;

    var materialProvider = new langstyle.MeterialProvider({
        "imageFileId": "imageFile",
        "characterCodeId": "characterCode"
    });

    window.materialProvider = materialProvider;

    var userRegister = new langstyle.UserRegister({
        "userNameId": "registerUserName",
        "passwordId": "registerPassword",
        "confirmPasswordId": "registerConfirmPassword"
    });

    window.userRegister = userRegister;

    var userLogin = new langstyle.UserLogin({
        "userNameId": "loginUserName",
        "passwordId": "loginPassword"
    });

    var loginButton = dom.getById("login");
    loginButton.onclick = function (e) {
        if (userLogin.validate()) {
            userLogin.login();
        }
    };

    var registerButton = dom.getById("register");
    registerButton.onclick = function (e) {
        if (userRegister.validate()) {
            userRegister.register();
        }
    };
} (dom));
