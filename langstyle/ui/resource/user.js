
(function () {

    var User = function (options) {
        if (!(this instanceof User)) {
            return new User(options);
        }

    };

    User.prototype = {

        validate: function () {

        },

        getFieldValue: function () {

        },

        showMessage: function () {

        }
    };

    var UserRegister = function (options) {
        if (!(this instanceof UserRegister)) {
            return new UserRegister(options);
        }

        this.userNameId = options.userNameId;
        this.passwordId = options.passwordId;
        this.confirmPasswordId = options.confirmPasswordId;
        this.emailId = options.emailId;
        this.userUrl = "/user";
    };

    UserRegister.prototype = {

        validate: function () {
            var userInfo = this._gather();
            var validationMessage = "";
            if (!userInfo.userName || userInfo.userName.trim() === "") {
                validationMessage = "user name is required";
            }
            else if (!userInfo.password || userInfo.password.trim() === "") {
                validationMessage = "password is required";
            }
            else if (userInfo.password !== userInfo.confirmPassword) {
                validationMessage = "password and confirm password are not identical";
            }
            this._showMessage(validationMessage)
            return validationMessage === "";
        },

        register: function () {
            var userInfo = this._gather();
            return ajax.post(this.userUrl, null, userInfo).then(
                function (userId) {
                    this._showMessage("register success");
                } .bind(this),
                function (errorMessage) {
                    this._showMessage(errorMessage);
                } .bind(this)
            );
        },

        _gather: function () {
            return {
                "userName": this._getFieldValue(this.userNameId),
                "password": this._getFieldValue(this.passwordId),
                "confirmPassword": this._getFieldValue(this.confirmPasswordId)
            };
        },

        _getFieldValue: function (fieldId) {
            var fieldElement = dom.getById(fieldId);
            if (fieldElement) {
                return fieldElement.value;
            }
            return null;
        },

        _showMessage: function (msg) {
            dom.getFirstByClass("js-register-validation").textContent = msg;
        }

    };

    langstyle.UserRegister = UserRegister;


    var UserLogin = function (options) {
        if (!(this instanceof UserLogin)) {
            return new UserLogin(options);
        }
        this.userNameId = options.userNameId;
        this.passwordId = options.passwordId;
        this.userUrl = "/authentication";
    };

    UserLogin.prototype = {

        validate: function () {
            var userInfo = this._gather();
            var validationMessage = "";
            if (!userInfo.userName || userInfo.userName.trim() === "") {
                validationMessage = "user name is required";
            }
            else if (!userInfo.password || userInfo.password.trim() === "") {
                validationMessage = "password is required";
            }
            this._showMessage(validationMessage)
            return validationMessage === "";
        },

        login: function () {
            var userInfo = this._gather();
            return ajax.post(this.userUrl, null, userInfo).then(
                function (userId) {
                    this._showMessage("login success");
                } .bind(this),
                function (errorMessage) {
                    this._showMessage(errorMessage);
                } .bind(this)
            );
        },

        logout: function () {
            var cookie = langstyle.Cookie();
            cookie.remove("userName");
        },

        hasLogin: function () {
            var cookie = langstyle.Cookie();
            var userName = cookie.get("userName");
            if (userName != null && userName.trim() !== "") {
                return true;
            }
            return false;
        },

        _gather: function () {
            return {
                "userName": this._getFieldValue(this.userNameId),
                "password": this._getFieldValue(this.passwordId)
            };
        },

        _getFieldValue: function (fieldId) {
            var fieldElement = dom.getById(fieldId);
            if (fieldElement) {
                return fieldElement.value;
            }
            return null;
        },

        _showMessage: function (msg) {
            dom.getFirstByClass("js-login-validation").textContent = msg;
        }
    };

    langstyle.UserLogin = UserLogin;

} ());