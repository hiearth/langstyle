
(function(langstyle, dom){
    
    var CharacterUnavailable = function(options){
        if (!(this instanceof CharacterUnavailable)){
            return new CharacterUnavailable(options);
        }

        this._nextUnavailableId = options.nextUnavailableId;
        this._nextUnavailableElement = dom.getById(options.nextUnavailableId);
        this._hiddenSign = "hidden";
    };

    CharacterUnavailable.prototype={

        load:function(responseStatusCode){
            var errorText = this._getText(responseStatusCode);
            this._nextUnavailableElement.textContent = errorText;
        },

        _getText:function(responseStatusCode){
            if (responseStatusCode === 500){
                return "Error happen when request (请求发生错误)";
            }
            return "Next is unavailable (下面没有了)";
        },

        show:function(){
            this._nextUnavailableElement.classList.remove(this._hiddenSign);
        },

        hide:function(){
            this._nextUnavailableElement.textContent = "";
            this._nextUnavailableElement.classList.add(this._hiddenSign);
        }
    };

    langstyle.CharacterUnavailable = CharacterUnavailable;

}(langstyle, dom));
