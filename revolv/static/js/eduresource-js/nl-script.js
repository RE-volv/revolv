$(function(){
  var overlay = $('<div id="overlay"></div>');

  overlay.appendTo(document.body);
  $("#overlay").delay(7000).show(0);
  $(".popup").delay(7000).show(0);

  $('.close').click(function(){
    $('.popup').hide();
    document.getElementById("overlay").style.display = "none";
    overlay.appendTo(document.body).remove();
    return false;
  });
});

function setCookie(cname,cvalue,exdays) {
  var d = new Date();
  d.setTime(d.getTime() + (exdays*2*60*60*1000));
  var expires = "expires=" + d.toGMTString();
  document.cookie = cname + "=" + cvalue + ";" + expires + ";path=/";
}
function getCookie(cname) {
    var name = cname + "=";
    var decodedCookie = decodeURIComponent(document.cookie);
    var ca = decodedCookie.split(';');
    for(var i = 0; i < ca.length; i++) {
        var c = ca[i];
        while (c.charAt(0) == ' ') {
            c = c.substring(1);
        }
        if (c.indexOf(name) == 0) {
            return c.substring(name.length, c.length);
        }
    }
    return "";
}
function areCookiesEnabled() {
  document.cookie = "__verify=1";
  var supportsCookies = document.cookie.length >= 1 &&
                        document.cookie.indexOf("__verify=1") !== -1;
  var thePast = new Date(1976, 8, 16);
  document.cookie = "__verify=1;expires=" + thePast.toUTCString();
  return supportsCookies;
}

function welcomeBannerCookie() {
    var welcomeCookie=getCookie("noShowWelcome");
    if (welcomeCookie == "true") {
        $('.popup').hide(0);
        $('#overlay').hide(0);
        //console.log('Cookies are stored');
    }
    else {
        //console.log('no cookie found')
        $('.popup').addClass('visible-banner');
        $("#close-welcome").click(function() {
            $(".popup").removeClass('visible-banner');
            $("#overlay").removeClass('visible-banner');
            
            setCookie("noShowWelcome", "true", 30);
        });
    }
};
$(document).ready(function() {
  if ( areCookiesEnabled() ) {
    //console.log('Cookies are enabled.');
    welcomeBannerCookie();
  } else {
    //console.log('Cookies are disabled');
  $("#close-welcome").click(function() {
      $(".popup").removeClass('visible-banner');
      
  });
  }
});