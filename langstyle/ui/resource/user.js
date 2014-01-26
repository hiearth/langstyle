
langstyle.User = function (options) {
    if (!(this instanceof langstyle.User)) {
        return new langstyle.User(options);
    }

    this.userNameId = options.userNameId;
    this.passwordId = options.passwordId;
    this.confirmPasswordId = options.confirmPasswordId;
    this.emailId = options.emailId;
    this.userUrl = "/user";
};

langstyle.User.prototype = {

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
        ajax.post(this.userUrl, null, userInfo).then(
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
        dom.getFirstByClass("js-user-validation").textContent = msg;
    }

};