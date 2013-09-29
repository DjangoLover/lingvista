$(function () {
    
    $(".showTranslate").on("click", function () {
        $(this).parent().toggleClass("active");
        $(this).closest('dd').find(".translateText").toggle();
        return false;
    });


    $(".showDefinition").on("click", function () {
        $(this).parent().toggleClass("active");
        $(this).closest('dd').find(".definitionText").toggle();
        return false;
    });

});