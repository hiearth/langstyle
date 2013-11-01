
// call then method to bind on-done and on-fail handler
// the asynchronize method should invoke the done or fail method when some operation finish
// call on-done handler if promise transform to done state
// call on-fail handler if promise transform to fail state

(function (window, undefined) {

    // Promise must be in one of three states: pending, fulfilled and rejected.
    // pending --> fulfilled or rejected
    // fulfilled must have a value, and cannot transform to other state
    // rejected must have a reason, and cannot transform to other state
    // if fulfilled state, onfulfilled will be called
    // if rejected state, onrejected will be called
    // then method will return a promise to support chainable then

    // Now, only support 
    // (fn(){ some code; return a promise}).then(onFulfilled, onRejected) // only first then has onRejected
    //                                     .then(onFulfilled)
    //                                     .then(onFulfilled)
    //                                     .then(onFulfilled);
    var StateEnum = {
        Pending: 1,
        Fulfilled: 2,
        Rejected: 4
    };

    var State = function (stateValue) {
        if (!(this instanceof State)) {
            return new State(stateValue);
        }

        this._stateValue = stateValue;
        this._transits = {};
        this._mapTransit(StateEnum.Pending, this._pend);
        this._mapTransit(StateEnum.Fulfilled, this._fulfill);
        this._mapTransit(StateEnum.Rejected, this._reject);
    };

    State.prototype = {

        get: function () {
            return this._stateValue;
        },

        transit: function (destState) {
            var transitMethod = this._transits[destState];
            if (transitMethod) {
                return transitMethod.apply(this);
            }
            else {
                throw new Error("can not transit to state: " + destState);
            }
        },

        _mapTransit: function (state, transitMethod) {
            this._transits[state] = transitMethod;
        },

        _pend: function () {
            if (this._stateValue !== StateEnum.Pending) {
                throw new Error("can not transit to pending");
            }
            return this;
        },

        _fulfill: function () {
            if (this._stateValue === StateEnum.Pending) {
                return new State(StateEnum.Fulfilled);
            }
            if (this._stateValue === StateEnum.Fulfilled) {
                return this;
            }
            else {
                throw new Error("can not transit to fulfilled");
            }
        },

        _reject: function () {
            if (this._stateValue === StateEnum.Pending) {
                return new State(StateEnum.Rejected);
            }
            if (this._stateValue === StateEnum.Rejected) {
                return this;
            }
            else {
                throw new Error("can not transit to rejected");
            }
        }
    };

    var PromiseHandler = function (onFulfilled, onRejected) {
        if (!(this instanceof PromiseHandler)) {
            return new PromiseHandler(onFulfilled, onRejected);
        }

        this._stateHandlers = {};
        this.nextPromise = new Promise();
        this._setStateHandler(StateEnum.Fulfilled, onFulfilled);
        this._setStateHandler(StateEnum.Rejected, onRejected);
    };

    PromiseHandler.prototype = {

        _setStateHandler: function (state, handler) {
            this._stateHandlers[state] = handler;
        },

        call: function (state, result) {
            var handlerResult;
            var handler = this._stateHandlers[state];
            if (handler) {
                handlerResult = handler(result);
                this.nextPromise.fulfill(handlerResult);
            }
        }
    };

    var Promise = function () {
        if (!(this instanceof Promise)) {
            return new Promise();
        }

        this._state = new State(StateEnum.Pending);
        this._handlers = [];
    };

    Promise.prototype = {

        _callHandlers: function (result) {
            var state = this._state.get();
            for (var i = 0; i < this._handlers.length; i++) {
                this._handlers[i].call(state, result);
            }
        },

        fulfill: function (value) {
            this._state = this._state.transit(StateEnum.Fulfilled);
            this._state.value = value;

            this._callHandlers(value);
        },

        reject: function (reason) {
            this._state = this._state.transit(StateEnum.Rejected);
            this._state.reason = reason;

            this._callHandlers(reason);
        },

        then: function (onFulfilled, onRejected) {
            var handler = new PromiseHandler(onFulfilled, onRejected);
            this._handlers.push(handler);
            return handler.nextPromise;
        }
    };

    window.Promise = Promise;

} (window));


var promiseTest = function () {

    var equal4 = function () {
        var promise = Promise();

        setTimeout(function () {
            if (2 + 1 === 4) {
                promise.fulfill(4);
            }
            else {
                promise.reject("it is 3 not 4");
            }
        }, 100)

        return promise;
    };

    equal4().then(function (result) {
        console.log(result);
        return "sucess";
    },
    function (reason) {
        console.log(reason);
        return "fail";
    }).then(function (result) {
        console.log(result);
        return "from second then"
    }).then(function (result) {
        console.log(result);
        return "from third then"
    });
};