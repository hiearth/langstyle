
// id selector

// css selector

(function (window, undefined) {

    var dom = {

        isBrowserEligible: function () {
            if (!document.getElementsByClassName) {
                return false;
            }
            return true;
        },

        createElement:function(elementName){
            return document.createElement(elementName);
        },

        appendAsChild:function(parentElement, targetElement){
            parentElement.appendChild(targetElement);
        },

        emptyElement:function(targetElement){
            while(targetElement.lastChild){
                targetElement.removeChild(targetElement.lastChild);
            }
        },

        getById: function (elementId) {
            return document.getElementById(elementId);
        },

        getByClass: function (className) {
            return document.getElementsByClassName(className);
        },

        getFirstByClass: function (className) {
            var elements = document.getElementsByClassName(className);
            if (elements && elements.length > 0) {
                return elements[0];
            }
            return null;
        },

        addClass: function (elementNode, className) {
            try {
                elementNode.classList.add(className);
                return elementNode;
            }
            catch (e) {

            }
        },

        removeClass: function (elementNode, className) {
            try {
                elementNode.classList.remove(className);
                return elementNode;
            }
            catch (e) {

            }
        },

        toggleClass: function (elementNode, className) {
            try {
                elementNode.classList.toggle(className);
                return elementNode;
            }
            catch (e) {

            }
        },

        hasClass: function (elementNode, className) {
            try {
                return elementNode.classList.contains(className);
            }
            catch (e) {

            }
            return false;
        }
    };

    window.dom = dom;
} (window));
