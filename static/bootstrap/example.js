$(document).ready(function(){

    $("a.menu").click(function (e) {
      var $li = $(this).parent("li").toggleClass('open');
      return false;
    });

});