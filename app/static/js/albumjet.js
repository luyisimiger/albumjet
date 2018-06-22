
var selector_laminas = "span.lamina";

function mark_lamina (evt) {
    
    var $target = $(evt.target);
    
    $target.toggleClass("is-info");
    $target.data("mark", $target.hasClass("is-info"));

    var mark = $target.data("mark");
    var iduserlamina = $target.data("id");

    $.ajax({
        url: "/ajax/lamina/mark",
        method: "GET",
        data: {
            iduserlamina: iduserlamina,
            mark: mark,
        }
    });

};

$(document).ready(function (){
    $(selector_laminas).on("click", mark_lamina);
});