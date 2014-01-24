
(function (dom) {
    var stages = ["stage", "addStage", "registerUser"];

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
        showStage("registerUser");
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

    var user = new langstyle.User({
        "userNameId": "userName",
        "passwordId": "password",
        "confirmPasswordId": "confirmPassword"
    });

    window.user = user;

    var registerButton = dom.getById("register");
    registerButton.onclick = function (e) {
        if (user.validate()) {
            user.register();
        }
    };
} (dom));
