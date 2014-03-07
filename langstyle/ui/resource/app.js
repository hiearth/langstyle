
(function (dom) {

    var hiddenSign = "hidden";
    var wordStage = new langstyle.WordStage({
        "stageId": "wordStage",
        "characterId": "character",
        "soundId": "sound",
        "imageId": "image",
        "imageViewId": "images",
        "soundSpeakId": "sounds",
        "stageFrameId": "stageFrame",
        "previousFrameId": "previousFrame",
        "nextFrameId": "nextFrame"
    });
    window.wordStage = wordStage;

    var materialProvider = new langstyle.MeterialProvider({
        "imageFileId": "imageFile",
        "characterCodeId": "characterCode",
        "soundFileId": "soundFile"
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

    var stageSwitch = new langstyle.StageSwitch();

    var userNameLink = dom.getById("userName");
    userNameLink.onclick = null;

    var showUserName = function () {
        var userName = userLogin.getUserName();
        userNameLink.textContent = userName;
        userNameLink.onclick = function () {
            stageSwitch.showUser();
        };
    };

    var hideUserName = function () {
        userNameLink.textContent = "";
    };

    var startMenu = dom.getById("startMenu");
    startMenu.onclick = function (e) {
        stageSwitch.showWord();
    };

    var addMenu = dom.getById("addMenu");
    addMenu.onclick = function (e) {
        stageSwitch.showAdd();
    };

    var registerUserMenu = dom.getById("registerMenu");
    registerUserMenu.onclick = function (e) {
        stageSwitch.showRegister();
    };

    var loginMenu = dom.getById("loginMenu");
    loginMenu.onclick = function () {
        stageSwitch.showLogin();
    };

    var logoutButton = dom.getById("logout");
    logoutButton.onclick = function () {
        userLogin.logout().then(function () {
            hideMenus();
            hideUserName();
            stageSwitch.showLogin();
        });
    };

    var loginButton = dom.getById("login");
    loginButton.onclick = function (e) {
        if (userLogin.validate()) {
            userLogin.login().then(function () {
                showMenus();
                showUserName();
                stageSwitch.showWord();
            });
        }
    };

    var registerButton = dom.getById("register");
    registerButton.onclick = function (e) {
        if (userRegister.validate()) {
            userRegister.register().then(function () {
                showMenus();
                showUserName();
                stageSwitch.showWord();
            });
        }
    };

    var hideMenus = function () {
        startMenu.classList.add(hiddenSign);
        addMenu.classList.add(hiddenSign);
    };

    var showMenus = function () {
        startMenu.classList.remove(hiddenSign);
        addMenu.classList.remove(hiddenSign);
    };

    if (userLogin.hasLogin()) {
        showUserName();
    }
    else {
        hideUserName();
        stageSwitch.showLogin();
    }

} (dom));
