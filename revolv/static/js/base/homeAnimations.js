var js_urls = {};

//count for 1st Number of "OUR IMPACTS" section in Home page
function increaseCount1(currentValue1,step1,value1){
  if((currentValue1+step1)<=value1)
  {
    currentValue1 = currentValue1+step1;
    $(".our-impacts-module .module-box .titles").eq(0).html(format(currentValue1)+"");
  }
  else
  {
    $(".our-impacts-module .module-box .titles").eq(0).html(format(value1)+"");
    return;
  }
  setTimeout(function () {
    increaseCount1(currentValue1, step1, value1);
  }, 100);
}

//count for 2nd Number of "OUR IMPACTS" section in Home page
function increaseCount2(currentValue2,step2,value2){
  if((currentValue2+step2)<=value2)
  {
    currentValue2 = currentValue2+step2;
    $(".our-impacts-module .module-box .titles").eq(1).html(format(currentValue2)+"");
  }
  else
  {
    return;
  }
  setTimeout(function () {
    increaseCount2(currentValue2, step2, value2);
  }, 100);
}

//count for 3rd Number of "OUR IMPACTS" section in Home page
function increaseCount3(currentValue3,step3,value3){
  if((currentValue3+step3)<=value3)
  {
    currentValue3 = currentValue3+step3;
    $(".our-impacts-module .module-box .titles").eq(2).html(format(currentValue3)+'<span class="font20">lbs</span>');
  }
  else
  {
    return;
  }
  setTimeout(function () {
    increaseCount3(currentValue3, step3, value3);
  }, 100);
}

//count for 4th Number of "OUR IMPACTS" section in Home page
function increaseCount4(currentValue4,step4,value4){
  if((currentValue4+step4)<=value4)
  {
    currentValue4 = currentValue4+step4;
    $(".our-impacts-module .module-box .titles").eq(3).html(format(currentValue4)+"");
  }
  else
  {
    return;
  }
  setTimeout(function () {
    increaseCount4(currentValue4, step4, value4);
  }, 100);
}

//format the Number text
function format(number){
  number = number +"";
  number = number.replace(/,/g, "");
  var digit = number.indexOf(".");
  var int = number.substr(0, digit);
  var i;
  var mag = new Array();
  var word;
  if (number.indexOf(".") === -1) {
    i = number.length;
    while (i > 0) {
        word = number.substring(i, i - 3);
        i -= 3;
        mag.unshift(word);
    }
    number = mag;
  } else {
    i = int.length;
    while (i > 0) {
        word = int.substring(i, i - 3);
        i -= 3;
        mag.unshift(word);
    }
    number = mag + number.substring(digit);
  }
  return number;
}

$(document).ready(function() {
    var fullScreenMode = "OFF";
    $(document).on('webkitfullscreenchange mozfullscreenchange fullscreenchange', function(e) {
            if(fullScreenMode == "OFF"){
                fullScreenMode = "ON";
                $(".Ellipse_543").hide();
            } else {
                fullScreenMode = "OFF";
                $(".Ellipse_543").show();
            }

    });

    //style the form elements
  if($(".form-container").length>0){
    $('.form-container').jqTransform({imgPath:'/static/images/'});
  }

  //swipe on carousel
  $(".carousel-inner").hammer().on('swipeleft', function(){
    $(this).parent().find(".right.carousel-control").click();
  });

  $(".carousel-inner").hammer().on('swiperight', function(){
    $(this).parent().find(".left.carousel-control").click();
  });

  $(".active-projects-module").css("opacity", 0);
  $(".our-impacts-module").css("opacity", 0);
  $(".how-it-works-module").css("opacity", 0);
  $(".testimonial-module").css("opacity", 0);
  $(".featured-on-module").css("opacity", 0);
  $(".newsletter-module .container").css("opacity", 0);

  //show reveal animation effect when Scrolling down the Home page
  $(".active-projects-module").waypoint(function() {
      $(".active-projects-module").addClass("fadeInUp");
  }, { offset: "70%"});

  if($(".our-impacts-module").length>0)
  {
    var Counting = false;
    var value1 = parseInt($(".our-impacts-module .module-box .titles").eq(0).html().replace('.',''));
    var value2 = parseInt($(".our-impacts-module .module-box .titles").eq(1).html().replace('.',''));
    var value3 = parseInt($(".our-impacts-module .module-box .titles").eq(2).html().replace('<span class="font20">lbs</span>','').replace('.','').replace('.',''));
    var value4 = parseInt($(".our-impacts-module .module-box .titles").eq(3).html().replace('.',''));

    var step1 = parseInt(value1/(5*10));
    step1 = (step1<1)?1:step1;

    var step2 = parseInt(value2/(5*10));
    step2 = (step2<1)?1:step2;

    var step3 = parseInt(value3/(5*10));
    step3 = (step3<1)?1:step3;

    var step4 = parseInt(value4/(5*10));
    step4 = (step4<1)?1:step4;

    var currentValue1 = 0;
    var currentValue2 = 0;
    var currentValue3 = 0;
    var currentValue4 = 0;

    $(".our-impacts-module .module-box .titles").eq(0).html(0);
    $(".our-impacts-module .module-box .titles").eq(1).html(0);
    $(".our-impacts-module .module-box .titles").eq(2).html(0+'<span class="font20">lbs</span>');
    $(".our-impacts-module .module-box .titles").eq(3).html(0);
  }

  $(".our-impacts-module").waypoint(function() {
    $(".our-impacts-module").addClass("fadeInUp");

    if(!Counting)
    {
      Counting = true;
      increaseCount1(currentValue1,step1,value1);
      increaseCount2(currentValue2,step2,value2);
      increaseCount3(currentValue3,step3,value3);
      increaseCount4(currentValue4,step4,value4);
    }
  }, { offset: "70%"});
  $(".how-it-works-module").waypoint(function() {
      $(".how-it-works-module").addClass("fadeInUp");
  }, { offset: "70%"});
  $(".testimonial-module").waypoint(function() {
      $(".testimonial-module").addClass("fadeInUp");
  }, { offset: "70%"});
  $(".featured-on-module").waypoint(function() {
      $(".featured-on-module").addClass("fadeInUp");
  }, { offset: "70%"});
  $(".newsletter-module").waypoint(function() {
      $(".newsletter-module .container").addClass("fadeInUp");
  }, { offset: "70%"});

  //set parallax images for NewLetter section in Home page

  if(($(window).width()+17)>= 1200 && js_urls['newsletter-bg.jpg'])
  {
    $('#parallax-anchor').parallax({imageSrc: js_urls['newsletter-bg.jpg']});
  }
  else if(js_urls['small-newsletter-bg.jpg'])
  {
    $('#parallax-anchor').parallax({imageSrc: js_urls['small-newsletter-bg.jpg']});
  }

  //show animation for progress bar
  $(".status-indicator input").each(function(){$(this).attr("data-oldvalue", $(this).val());});
  $(".status-indicator input").each(function(){$(this).val(0).trigger('change').delay(2000);});
  $(".status-indicator input").knob({
    'draw' : function () {
      if (typeof this._max === 'undefined') {
        this._max = parseInt($(this.i).data('oldvalue'));
      }
       $(this.i).val(this.cv + '%');
       if(this.cv === 85 && (this._max === 100 || this._max === 0)) {
          // Three digits, not one or two, so we make it a bit smaller
         $(this.i).css({"font-family" : "Source Sans Pro", "font-size" : "22px", "color" : "#003399", "font-weight" : "700"});
         $(this.i).addClass('smaller');
       }
       else {
         $(this.i).css({"font-family" : "Source Sans Pro", "font-size" : "30px", "color" : "#003399", "font-weight" : "700"});
       }
       $(this.i).on("focus", function(){
        $(this.i).parent().click();
       });
    }
  });
  $(".status-indicator input").each(function(){
    animateKnob($(this));
  });

  //show pecentage value animate
  function animateKnob ($elem) {
    var endval = parseInt($elem.attr("data-oldvalue"));
    var m1 = 0;
    var tmr1;

    function delayProgress(){
      m1 += 1;
      $elem.val(m1).trigger('change');
      if(m1 === endval || m1 === 100) {
        clearInterval(tmr1);
      }
    }

    if (m1 < endval) {
      tmr1 = self.setInterval(delayProgress,10);
    }
  }
  $("#form1 .btn-sign-up, #form2 .btn-sign-up").click(function(e){
            $(".newsletter-error-email-msg").remove();
            $('.newsletter-module .group-main .group').css('padding-bottom', '3vmin');
            var signupEmail = $('#form1 .inputs input[type="email"]').val();
            var signupMobileEmail = $('#form2 .inputs input[type="email"]').val();
            var regExp = /^(([^<>()\[\]\\.,;:\s@"]+(\.[^<>()\[\]\\.,;:\s@"]+)*)|(".+"))@((\[[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}])|(([a-zA-Z\-0-9]+\.)+[a-zA-Z]{2,}))$/;

        if(signupEmail.length > 0 && regExp.test(signupEmail) == true || signupMobileEmail.length > 0 && regExp.test(signupMobileEmail) == true) {
              var $form = $(this).closest('form');
              $('#donation-spinner').css('display', 'flex');
              $.ajax({
                 type: "POST",
                 url: '/subscribe/',
                 data: $form.serializeArray(), // serializes the form's elements.
                 success: function(data)
                 {
                    $('#donation-spinner').css('display', 'none');
                    if (data.status == 'subscription_success') {
                                        $('#newslettermodal').modal('show');
                                        $('.donation-text').text("Thank you for signing up for our newsletter, we look forward to keeping in touch!");
                    }
                    else if (data.status == 'already_exist') {
                                        $('#newslettermodal').modal('show');
                                        $('.donation-text').text("Thank you for showing the interest, this email is already registered.");
                    }
                    else if (data.status =='subscription_fail'){
                                        $('#newslettermodal').modal('show');
                                        $('.donation-text').text("Newsletter subsciption fail, due to some reason, please try again.");

                    }
                    closeNewsletterPopUp();
                 },
                 error: function(data) {
                    $('#donation-spinner').css('display', 'none');
                    $('#newslettermodal').modal('show');
                    $('.modal-title').text('Error!');
                    $('.donation-text').text("Newsletter subsciption fail due to some reason, please try again.");
                }
               });


               e.preventDefault(); // avoid to execute the actual submit of the form.


        } else {
                var errorText = '<span class="newsletter-error-email-msg">Please enter a valid email.</span>';
                $("#form1").append(errorText);
                $("#form2 .inputs").append(errorText);
                $('.newsletter-module .group-main .group').css('padding-bottom', '5vmin');
        }
    });


});

function closeNewsletterPopUp() {
    $(".close-newsletter").click(function(e){
         e.stopPropagation();
         $('#newslettermodal').modal('hide');
         $('#form1 .inputs input[type="email"]').val("");
         $('#form2 .inputs input[type="email"]').val("");
    });
    $(".newsletter-ok-btn").click(function(e){
         e.stopPropagation();
         $('#newslettermodal').modal('hide');
         $('#form1 .inputs input[type="email"]').val("");
         $('#form2 .inputs input[type="email"]').val("");
    });
    $(document).keydown(function(e) {
        if (e.keyCode == 27) {
            $('#newslettermodal').modal('hide');
           $('#form1 .inputs input[type="email"]').val("");
           $('#form2 .inputs input[type="email"]').val("");
       }
    });
}




