
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
        this.userValidationUrl = "/uservalidation";

        this.init();
    };

    UserRegister.prototype = {

        init: function () {
            var self = this;
            var userNameField = dom.getById(this.userNameId);
            userNameField.onblur = function (e) {
                var userName = e.target.value;
                if (userName && userName.trim() !== "") {
                    var userNameValidationUrl = self.userValidationUrl + "?userName=" + userNameField.value;
                    ajax.get(userNameValidationUrl).then(
                        function () {
                            self._showMessage("");
                        },
                        function (errorMessage) {
                            self._showMessage(errorMessage);
                        } .bind(this)
                    );
                }
            };
        },

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
            var promise = new Promise();
            var userInfo = this._gather();
            ajax.post(this.userUrl, null, JSON.stringify(userInfo)).then(
                function (userId) {
                    this._showMessage("register success");
                    promise.fulfill(userId);
                } .bind(this),
                function (errorMessage) {
                    this._showMessage(errorMessage);
                    promise.reject(errorMessage);
                } .bind(this)
            );
            return promise;
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
        this._cookieName = "userName";
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
            var promise = new Promise();
            var userInfo = this._gather();
            ajax.post(this.userUrl, null, JSON.stringify(userInfo)).then(
                function (userId) {
                    this._showMessage("login success");
                    promise.fulfill(userId);
                } .bind(this),
                function (errorMessage) {
                    this._showMessage(errorMessage);
                    promise.reject(errorMessage);
                } .bind(this)
            );
            return promise;
        },

        logout: function () {
            var cookie = new langstyle.Cookie();
            cookie.remove(this._cookieName);
        },

        hasLogin: function () {
            var userName = this.getUserName();
            if (userName != null && userName !== "") {
                return true;
            }
            return false;
        },

        getUserName: function () {
            var cookie = new langstyle.Cookie();
            var userName = cookie.get(this._cookieName);
            if (userName != null) {
                return userName.trim();
            }
            return userName;
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