
(function (dom) {
    var stages = ["stage", "addStage"];
    var wordStage = new langstyle.WordStage({
        "stageId": "stage",
        "characterId": "character",
        "soundId": "sound",
        "imageId": "image",
        "imageViewId": "images"
    });

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

    var startButton = dom.getById("start");
    startButton.onclick = function (e) {
        showStage("stage");
    };

    var addButton = dom.getById("add");
    addButton.onclick = function (e) {
        showStage("addStage");
    };

    window.wordStage = wordStage;

} (dom));
