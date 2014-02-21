
(function () {

    var ObservableEvent = function (eventName) {
        var handlers = [];
        var eventName = eventName || "CustomEvent";

        /*
        * Adds an event handler to be called when the event is fired.
        * <p>Event handler will receive two arguments - an <code>EventData</code> and the <code>data</code>
        * object the event was fired with.<p>
        */
        this.subscribe = function (fn) {
            handlers.push(fn);
        };

        /*
        * Removes an event handler added with <code>subscribe(fn)</code>.
        */
        this.unsubscribe = function (fn) {
            for (var i = handlers.length - 1; i >= 0; i--) {
                if (handlers[i] === fn) {
                    handlers.splice(i, 1);
                }
            }
        };

        this.unsubscribeAll = function () {
            handlers = [];
        };

        this.getHandlers = function () {
            return handlers;
        };

        /*
        * Fires an event notifying all subscribers.
        */
        this.notify = function (args, e, scope) {
            var returnValue, i;

            e = e || new CustomEvent(eventName);
            scope = scope || this;

            for (i = 0; i < handlers.length; i++) {
                returnValue = handlers[i].call(scope, e, args);
            }

            return returnValue;
        };
    };

    window.ObservableEvent  = ObservableEvent;

} ());