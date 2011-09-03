$(document).ready(function() {
    // For Login drop down
    $("a.menu").click(function (e) {
      var $li = $(this).parent("li").toggleClass('open');
      return false;
    });
    // For ajax csrf handling - Do not remove
    $.ajaxSetup({ 
         beforeSend: function(xhr, settings) {
             function getCookie(name) {
                 var cookieValue = null;
                 if (document.cookie && document.cookie != '') {
                     var cookies = document.cookie.split(';');
                     for (var i = 0; i < cookies.length; i++) {
                         var cookie = jQuery.trim(cookies[i]);
                         // Does this cookie string begin with the name we want?
                     if (cookie.substring(0, name.length + 1) == (name + '=')) {
                         cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                         break;
                     }
                 }
             }
             return cookieValue;
             }
             if (!(/^http:.*/.test(settings.url) || /^https:.*/.test(settings.url))) {
                 // Only send the token to relative URLs i.e. locally.
                 xhr.setRequestHeader("X-CSRFToken", getCookie('csrftoken'));
             }
         } 
    });
});

function ajax() {
    var form = $("#example_form").serialize();
    $.post("/ajax_example/", form,
        function(response){
            if ( response.success == true ) {
                $("#form").html(response.html);
            }
            else if ( response.success == false ) {
                $("#form").html(response.html);
            }
         }, "json");
}