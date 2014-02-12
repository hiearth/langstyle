
(function (dom) {
    var wordStage = new langstyle.WordStage({
        "stageId": "stage",
        "characterId": "character",
        "soundId": "sound",
        "imageId": "image",
        "imageViewId": "images",
        "imageNavId": "imageNav",
        "previousImageId": "previousImage",
        "nextImageId": "nextImage"
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

    var showUserName = function () {
        var userName = userLogin.getUserName();
        dom.getById("userName").textContent = userName;
    };

    var hideUserName = function () {
        dom.getById("userName").textContent = "";
    };

    var startButton = dom.getFirstByClass("js-start-menu");
    startButton.onclick = function (e) {
        showStage("stage");
    };

    var addButton = dom.getFirstByClass("js-add-menu");
    addButton.onclick = function (e) {
        showStage("addStage");
    };

    var registerUserMenu = dom.getFirstByClass("js-register-menu");
    registerUserMenu.onclick = function (e) {
        showStage("registerPage");
    };

    var loginMenu = dom.getFirstByClass("js-login-menu");
    loginMenu.onclick = function () {
        showStage("loginPage");
    };

    var logoutMenu = dom.getFirstByClass("js-logout-menu");
    logoutMenu.onclick = function () {
        userLogin.logout();
        disableMenus();
        hideUserName();
        hideLogout();
        showStage("loginPage");
    };

    var loginButton = dom.getById("login");
    loginButton.onclick = function (e) {
        if (userLogin.validate()) {
            userLogin.login().then(function () {
                enableMenus();
                showUserName();
                showLogout();
                showStage("stage");
            });
        }
    };

    var registerButton = dom.getById("register");
    registerButton.onclick = function (e) {
        if (userRegister.validate()) {
            userRegister.register().then(function () {
                enableMenus();
                showUserName();
                showLogout();
                showStage("stage");
            });
        }
    };
    var showLogout = function () {
        logoutMenu.classList.remove("hidden");
        loginMenu.classList.add("hidden");
        registerUserMenu.classList.add("hidden");
    };

    var hideLogout = function () {
        logoutMenu.classList.add("hidden");
        loginMenu.classList.remove("hidden");
        registerUserMenu.classList.remove("hidden");
    };

    var disableMenus = function () {
        startButton.disabled = true;
        addButton.disabled = true;
    };

    var enableMenus = function () {
        startButton.disabled = false;
        addButton.disabled = false;
    };

    if (userLogin.hasLogin()) {
        enableMenus();
        showUserName();
        showLogout();
    }
    else {
        disableMenus();
        hideUserName();
        hideLogout();
    }

} (dom));
