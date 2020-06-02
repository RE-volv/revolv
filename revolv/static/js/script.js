$(document).ready(function(){
    $('#dropdown-select-text').on('click', function() {
        $('.dropdown-menu').toggle();
    });
    $('#firstnamelabel').click(function() {
        $('#id_first_name').prop('readonly', false);
        $('#id_first_name').focus();
    });
    $('#lastnamelabel').click(function() {
        $('#id_last_name').prop('readonly', false);
        $('#id_last_name').focus();
    });
    $('#emaillabel').click(function() {
        $('#id_email').prop('readonly', false);
        $('#id_email').focus();
    });
     $('#usernamelabel').click(function() {
        $('#id_username').prop('readonly', false);
        $('#id_username').focus();
    });
    $('.operation-donation').click(function() {
        $('#operation-amt').prop('readonly', false);
        $('#operation-amt').focus();
    });
    $('.solar-donation').click(function() {
        $('#donation-amt').prop('readonly', false);
        $('#donation-amt').focus();
    });
    $('#passwordlabel').click(function() {
        window.location.href='/password_change/';
    });
    $('.option').on('click', function() {
        $(this).closest('.dropdown-menu').hide();
        $(this).parents('.dropdown').find('.dropdown-title span:first-child').text($(this).html());
        $(this).parents('.dropdown').find('.dropdown-select').val($(this).html());
        selectedValue=$(this).data("selected-state");
        changeFunc(selectedValue);
    });
    $(document).click(function (event) {
        var clickover = $("event.target");
        var _opened = $(".navbar-collapse-settings").hasClass("collapse in");
        if (_opened === true && !clickover.hasClass("container1")) {
            $(".container1").click();
        }
    });
    $('#email-preference-info').hide();
    $('#account-link').click(function (event) {
        $('#account-info').show();
        $('#account-information-block').show();
        $('#donation-info').hide();
        $('#email-preference-info').hide();
        $('#account-link').addClass('account-tab-text-active');
        $('#donation-link').removeClass('account-tab-text-active');
        $('#email-preference-link').removeClass('account-tab-text-active');
    });
    $('#donation-link').click(function (event) {
        $('#donation-info').show();
        $('#account-info').hide();
        $('#account-link').removeClass('account-tab-text-active');
        $('#email-preference-link').removeClass('account-tab-text-active');
        $('#donation-link').addClass('account-tab-text-active');
    });
    $('#email-preference-link').click (function () {
        $('#account-info').show();
        $('#account-information-block').hide();
        $('#donation-info').hide();
        $('#email-preference-info').show();
        $('#account-link').removeClass('account-tab-text-active');
        $('#donation-link').removeClass('account-tab-text-active');
        $('#email-preference-link').addClass('account-tab-text-active');
    });

    // Common myths box drop down.
    $('.collapse').on('shown.bs.collapse', function(){
        $(this).parent().find(".glyphicon-chevron-down").removeClass("glyphicon-chevron-down").addClass("glyphicon-chevron-up");
        }).on('hidden.bs.collapse', function(){
        $(this).parent().find(".glyphicon-chevron-up").removeClass("glyphicon-chevron-up").addClass("glyphicon-chevron-down");
    });
    // Show fact card info on Exciting facts page.
    $('.fact-card').on('click', function(){
        $('.card-logo').removeClass('hide-card');
        $('.card-info').removeClass('show-card');
        $(this).find('.card-logo').addClass('hide-card');
        $(this).find('.card-info').addClass('show-card');
    });

    $(".container1").click(function (event) {
           $(".navbar-collapse-settings").toggle();
    });

     function changeFunc(selectedValue) {


       var states1 = ["AZ","CO","CT","DC","DE","FL", "GA","IN","LA","ME", "MI","MO","NC","NH","NM","NV","OH","PA","TX", "UT","VA","VT","WI"];
       var states2 = ["AK","AL", "AR","CA", "HI","IA", "ID", "KS","KY", "MA","MS", "MT","ND", "NE", "NJ","NY","RI","MD","IL","MN",
                      "OK", "OR", "SC","TN", "WA", "WV","WY"];

        for (i=0;i<50;i++)
        {
            if (selectedValue == states1[i])
            {
                $(".investors_logo_text").text("Instantly compare quotes from solar companies in your area with Energy Sage:");
                $("#img").attr("src",'/static/images/EnergySage_updated.jpg');
                $("#invstr-logo-link").attr("href",'http://www.energysage.com/p/re-volv/');
                $("#invstr-logo-link").attr("target",'_blank');
                $(".investor-remaining-img").hide();
                $(".hide-state-text-div span").hide();
                $(".selected-logo").css('border','0');
                $("#img").closest(".invstr-logo-images").removeClass("col-sm-4");
                $("#img").closest(".invstr-logo-images").addClass("col-sm-6");
            }
            else if (selectedValue == states2[i])
            {
                $(".investors_logo_text").text("Instantly compare quotes from solar companies in your area with Pick My Solar:");
                $("#img").attr("src","/static/images/PickMySolar_updated.png");
                $("#invstr-logo-link").attr("href",'https://pickmysolar.com/re-volv/');
                $("#invstr-logo-link").attr("target",'_blank');
                $(".investor-remaining-img").hide();
                $(".hide-state-text-div span").hide();
                $(".selected-logo").css('border','0');
                $("#img").closest(".invstr-logo-images").removeClass("col-sm-4");
                $("#img").closest(".invstr-logo-images").addClass("col-sm-6");
            }

        }
   }
    $(document).click(function (event) {
        var clickover = $(event.target);
        var _opened = $(".navbar-collapse").hasClass("collapse in");
        if (_opened === true ) {
            $("button.navbar-toggle").click();
        }
    });
    $(document).mouseup(function (e) {
         var popup = $(".dropdown-menu");
         if (!$('#dropdown-select-text').is(e.target) && !$('#dropdown-title').is(e.target) && !$('#dropdown-title span').is(e.target) &&
             !popup.is(e.target) && popup.has(e.target).length == 0) {
             popup.hide();
             $('.dropdown-triangle').html('▾');
         }
     });
    $('#dropdown-select-text, .option').on('click', function() {
    if ($('.dropdown-triangle').html() == '▾') {
        $('.dropdown-triangle').html('▴');
    }
    else if ($('.dropdown-triangle').html() == '▴'){
        $('.dropdown-triangle').html('▾');
    }
    });

    $(document).on('click', '#stOverlay', function(e) {
        window.location.href='/my-portfolio/';
    });
     $(document).on('click', '#share-modal', function(e) {
        if(e.target!== this)
        return;
        window.location.href='/my-portfolio/';
    });
      $(document).on('click', '#share-signup-modal', function(e) {
        if(e.target!== this)
        return;
        window.location.href='/my-portfolio/';
    });

     $(".stripe-button-el").click(function(){
         if($(this).find("span:last-child").text() != "Next") {
            $(".input-custom-amount input[type=number]").val($(this).find("span:last-child").text());
         }
     });

     $(".stripe-button-el").click(function(){

    });

    $('#twenty-amount').click(function(){
        $('#donation-inputz').val('25');

    });

    $('#fifty-amount').click(function(){
        $('#donation-inputz').val('50');

    });

    $('#seventyfive-amount').click(function(){
      $('#donation-inputz').val('75');

    });

    $('#hundred-amount').click(function(){
        $('#donation-inputz').val('100');

    });

    $(".other-amount-button").click(function(){
      $(".donate-form-body .donation-values .amount-buttons-wrapper .other-amount-button").addClass("hidden");
      $(".donate-form-body .donation-values .amount-buttons-wrapper .other-input-button").removeClass("hidden");
    });

    $(".amount-button").click(function(){
      $(".donate-form-body .donation-values .amount-buttons-wrapper .other-amount-button").removeClass("hidden");
      $(".donate-form-body .donation-values .amount-buttons-wrapper .other-input-button").addClass("hidden");
    });

    $(".amount-button").on("click", function(e) {
      $(this).addClass("selected").siblings().removeClass("selected");
    });

    // $(".u-background--grey div:first-child").off();
     $(".u-background--grey label").click(function() {
       console.log("clicked")
          $(".monthly-plan-msg").toggle();
     });

      // Donation form 
      $(".donate-form-body .donation-values .amount-buttons-wrapper .input-wrapper .input-field-container input[type=number]").change(function(){
      if($(this).val().trim() > 0) {
          $(".donate-form-body .donation-values .amount-buttons-wrapper .next-button").addClass("stripe-button-el");
          $(".donate-form-body .donation-values .amount-buttons-wrapper .next-button").css("background-color", "#FF8A00"); 
          $(".donate-form-body .donation-values .amount-buttons-wrapper .next-button").removeClass("disable-donation-btn");
      } else {
          $(".donate-form-body .donation-values .amount-buttons-wrapper .next-button").css("background-color", "#9a9a9a");
          $(".donate-form-body .donation-values .amount-buttons-wrapper .next-button").removeClass("stripe-button-el");
          $(".donate-form-body .donation-values .amount-buttons-wrapper .next-button").addClass("disable-donation-btn");
      }
     });

     $(".input-custom-amount input[type=number]").change(function(){
       if($(this).val().trim() > 0) {
           $(".donate-popup .next-button").addClass("stripe-button-el");
           $(".donate-popup .next-button").css("background-color", "#4EB181");
           $(".donate-popup .next-button").removeClass("disable-donation-btn");
       } else {
          $(".donate-popup .next-button").css("background-color", "#9a9a9a");
           $(".donate-popup .next-button").removeClass("stripe-button-el");
           $(".donate-popup .next-button").addClass("disable-donation-btn");
       }
     });
     $(document).on('click','.stripe-button-el',function (e) {
          $(this).closest(".modal").hide();
     });
      $(document).click(function (event) {
          var clickover = $(event.target);
          var _opened = $(".navbar-collapse").hasClass("collapse in");
          if (_opened === true ) {
              $('.navbar-collapse').collapse('hide');
            }
          });
            $(".navbar-toggle").click(function (event) {
          var clickover = $(event.target);
          var _opened = $(".navbar-collapse").hasClass("collapse in");
          if (_opened === true ) {
          	  $('.navbar-collapse').removeClass('in');
			  event.stopPropagation();
            }
          });
          $(".right-list").click(function() {
              window.location.href = $(this).data('chapter-url');

          });


  //click Down arrow in Home page
  $(".down-arrow-button").click(function(){
    var scroll_offset = $(".active-projects-module").offset();
    $("body,html").animate({
      scrollTop:scroll_offset.top
    },1000);
    setTimeout(function(){
      if(!$("header").hasClass("after-scroll-header"))
      {
        $("header").removeClass("top-section-header").addClass("after-scroll-header");
        $("header").hide();
        $("header").slideDown();
      }
    },1500)

  });

  //click option in Dropdown list
  $(".dropdown-menu li a").click(function(){
    $(this).parents(".dropdown").find("li a").removeClass("active");
    $(this).addClass("active");

    $(this).parents(".dropdown").find(".selected-option").html($(this).html());
    $(this).parents(".dropdown").find(".selected-option").attr("title",$(this).html());
  });

  //hover on User photos in Testimonial section in Home page
  $(".testimonial-module .head-row ul li .head-img").hover(function(){
    var index = $(this).parents(".testimonial-module .head-row ul").find(".head-img").index($(this));

    $(this).parents(".testimonial-module .head-row ul").find(".head-img.active").removeClass("active");
    $(this).addClass("active");

    $(this).parents(".testimonial-module").find(".info-area").addClass("hide");
    $(this).parents(".testimonial-module").find(".info-area").eq(index).removeClass("hide");
  });

  //loading Home page
 /** / if($(".home-page-content").length>0)
  {
    $("#video-player").mediaelementplayer({
      flashScriptAccess: 'always',
      loop: true
  });
  }**/



    //click tabs
  $(".mains-tabs .tab-index .row a").click(function(){
    var index = $(this).parents(".mains-tabs .tab-index").find(".row a").index($(this));

    $(this).parents(".mains-tabs .tab-index").find(".row a").removeClass("active");
    $(this).addClass("active");

    $(this).parents(".mains-tabs").find(".tab-content .tab-content-section").removeClass("active");
    $(this).parents(".mains-tabs").find(".tab-content .tab-content-section").eq(index).addClass("active");
  })

  //click on Login button in Sign In page
  $(".btn-login").click(function(){
    var pass = true;
    for(var i=0;i<$("input.required-input").length;i++)
    {
      if($("input.required-input").eq(i).val() === "")
      {
        $("input.required-input").eq(i).parent().addClass("input-error-style");
        pass = false;
      }
      else
      {
        $("input.required-input").eq(i).parent().removeClass("input-error-style");
      }
    }

    if(pass)
    {
      location.href = "home.html";
    }
  })

  //click on Sign Up button in Sign Up page
  $(".btn-signup").click(function(){
    var pass = true;
    for(var i=0;i<$("input.required-input").length;i++)
    {
      if($("input.required-input").eq(i).val() === "")
      {
        $("input.required-input").eq(i).parent().addClass("input-error-style");
        pass = false;
      }
      else if($("input.required-input").eq(i).hasClass("email-format"))
      {
        if(!checkMail($("input.required-input").eq(i).val()))
        {
          $("input.required-input").eq(i).parent().addClass("input-error-style");
          pass = false;
        }
        else
        {
          $("input.required-input").eq(i).parent().removeClass("input-error-style");
        }
      }
      else if($("input.required-input").eq(i).hasClass("password-match"))
      {
        if($("input.required-input").eq(i).val() !== $("input.required-input").eq(i-1).val())
        {
          $("input.required-input").eq(i).parent().addClass("input-error-style");
          pass = false;
        }
        else
        {
          $("input.required-input").eq(i).parent().removeClass("input-error-style");
        }
      }
      else
      {
        $("input.required-input").eq(i).parent().removeClass("input-error-style");
      }
    }

    if(!$(".required-checkbox").prev().hasClass("jqTransformChecked"))
    {
      pass = false;
    }

    if(pass)
    {
      location.href = "home.html";
    }
  })

  //check Email format
  function checkMail(mail){
    var filter  = /^([a-zA-Z0-9_\.\-])+\@(([a-zA-Z0-9\-])+\.)+([a-zA-Z0-9]{2,4})+$/;
    if (filter.test(mail))
      return true;
    else
    {
      return false;
    }
  }

  //focus on input box in Sign In/Sign Up pages
  $("input.required-input").focus(function(){
    $(this).parent().removeClass("input-error-style");
  })

  //click Enter key
  $(document).keydown(function(event){
    if(event.keyCode===13){
      if($(".btn-login").length>0)
      {
        $(".btn-login").click();
      }

      if($(".btn-signup").length>0)
      {
        $(".btn-signup").click();
      }
    }
  });

  //load google map
  if($("#map-canvas").length>0)
  {
    loadMap();
  }

  //load the google map
  function loadMap(){
    function initialize() {
      /*
      var mapOptions = {
        zoom: 4,
        mapTypeControl: false
      };
      var map = new google.maps.Map(document.getElementById('map-canvas'), mapOptions);

      var marker = new google.maps.Marker({
        position: myLatlng,
        map: map
      });
      */
    }

    initialize();
  }
})
