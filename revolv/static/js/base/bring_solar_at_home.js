
$(document).ready(function() {
    $.ajaxSetup({
      data: {csrfmiddlewaretoken: '{{ csrf_token }}' },
      });
   $(".navbar-toggle").click(function (event) {
        var clickover = $(event.target);
        var _opened = $(".navbar-collapse").hasClass("collapse in");
        if (_opened === true ) {
              $('.navbar-collapse').removeClass('in');
            event.stopPropagation();
          }
        });
      $(document).click(function (event) {
        var clickover = $(event.target);
        var _opened = $(".navbar-collapse").hasClass("collapse in");
        if (_opened === true ) {
              $('.navbar-collapse').removeClass('in');
            event.stopPropagation();
          }
        });

      $('.dropdown-title').on('click', function() {
      $('.dropdown-menu').toggle();
      });
   $(".grid-data").click(function(){
    window.location.href = $(this).data('chapter-url');
   });
    $(".grid-data").mouseenter(function(){
      $(this).find(".data-text").css("color","#fff");
    });
  $(".grid-data").mouseleave(function(){
     $(this).find(".data-text").css("color","#666");
  });

  $(".get-start-btn").click(function(e){
      window.location.href = $(this).data('form-url');
  });
   $(".form-checkbox").click(function(e){
       e.stopPropagation();
       var findParent = $(this);
       if(findParent.parents('.know-interest-cntnr').length) {
          var $this = $(this).find("div:first-child");
          var checkboxSatus = $this.data('checkbox-status');
          if(checkboxSatus == "unchecked") {
              findParent.closest('.know-interest-cntnr').find('.form-checkbox div:first-child').addClass('unmarked-checkbox').removeClass('mark-checkbox');
              findParent.closest('.know-interest-cntnr').find('.form-checkbox div:first-child').data('checkbox-status', "unchecked");
              $this.removeClass('unmarked-checkbox').addClass('mark-checkbox');
              $this.data('checkbox-status', "checked");
           }
       }  else if (findParent.parents('.colstudent-block').length){
          var $this = $(this).find("div:first-child");
          var checkboxSatus = $this.data('checkbox-status');
          if(checkboxSatus == "unchecked") {
              findParent.closest('.colstudent-block').find('.form-checkbox div:first-child').addClass('unmarked-checkbox').removeClass('mark-checkbox');
              findParent.closest('.colstudent-block').find('.form-checkbox div:first-child').data('checkbox-status', "unchecked");
              $this.removeClass('unmarked-checkbox').addClass('mark-checkbox');
              $this.data('checkbox-status', "checked");
          }
       }  else if (findParent.parents('.colteam-block').length){
        var $this = $(this).find("div:first-child");
        var checkboxSatus = $this.data('checkbox-status');
        if(checkboxSatus == "unchecked") {
            findParent.closest('.colteam-block').find('.form-checkbox div:first-child').addClass('unmarked-checkbox').removeClass('mark-checkbox');
            findParent.closest('.colteam-block').find('.form-checkbox div:first-child').data('checkbox-status', "unchecked");
            $this.removeClass('unmarked-checkbox').addClass('mark-checkbox');
            $this.data('checkbox-status', "checked");
          }
       }  else if (findParent.parents('.get-to-know-revolv-block').length){
          var $this = $(this).find("div:first-child");
          var checkboxSatus = $this.data('checkbox-status');
          if(checkboxSatus == "unchecked") {
              findParent.closest('.get-to-know-revolv-block').find('.form-checkbox div:first-child').addClass('unmarked-checkbox').removeClass('mark-checkbox');
              findParent.closest('.get-to-know-revolv-block').find('.form-checkbox div:first-child').data('checkbox-status', "unchecked");
              $this.removeClass('unmarked-checkbox').addClass('mark-checkbox');
              $this.data('checkbox-status', "checked");
          }
       } else if (findParent.parents('.affiliation-org-block').length){
          var $this = $(this).find("div:first-child");
          var checkboxSatus = $this.data('checkbox-status');
          if(checkboxSatus == "unchecked") {
              findParent.closest('.affiliation-org-block').find('.form-checkbox div:first-child').addClass('unmarked-checkbox').removeClass('mark-checkbox');
              findParent.closest('.affiliation-org-block').find('.form-checkbox div:first-child').data('checkbox-status', "unchecked");
              $this.removeClass('unmarked-checkbox').addClass('mark-checkbox');
              $this.data('checkbox-status', "checked");
          }
       } else if (findParent.parents('.schoolLoc-org-block').length){
          var $this = $(this).find("div:first-child");
          var checkboxSatus = $this.data('checkbox-status');
          if(checkboxSatus == "unchecked") {
              findParent.closest('.schoolLoc-org-block').find('.form-checkbox div:first-child').addClass('unmarked-checkbox').removeClass('mark-checkbox');
              findParent.closest('.schoolLoc-org-block').find('.form-checkbox div:first-child').data('checkbox-status', "unchecked");
              $this.removeClass('unmarked-checkbox').addClass('mark-checkbox');
              $this.data('checkbox-status', "checked");
          }
       } else if (findParent.parents('.schoolTeam-org-block').length){
        var $this = $(this).find("div:first-child");
        var checkboxSatus = $this.data('checkbox-status');
        if(checkboxSatus == "unchecked") {
            findParent.closest('.schoolTeam-org-block').find('.form-checkbox div:first-child').addClass('unmarked-checkbox').removeClass('mark-checkbox');
            findParent.closest('.schoolTeam-org-block').find('.form-checkbox div:first-child').data('checkbox-status', "unchecked");
            $this.removeClass('unmarked-checkbox').addClass('mark-checkbox');
            $this.data('checkbox-status', "checked");
          }
       } else if (findParent.parents('.solar-proj-need-block').length){
          var $this = $(this).find("div:first-child");
          var checkboxSatus = $this.data('checkbox-status');
          if(checkboxSatus == "unchecked") {
              findParent.closest('.solar-proj-need-block').find('.form-checkbox div:first-child').addClass('unmarked-checkbox').removeClass('mark-checkbox');
              findParent.closest('.solar-proj-need-block').find('.form-checkbox div:first-child').data('checkbox-status', "unchecked");
              $this.removeClass('unmarked-checkbox').addClass('mark-checkbox');
              $this.data('checkbox-status', "checked");
          }
       } else if (findParent.parents('.annual-budget-cntnr').length){
          var $this = $(this).find("div:first-child");
          var checkboxSatus = $this.data('checkbox-status');
          if(checkboxSatus == "unchecked") {
              findParent.closest('.annual-budget-cntnr').find('.form-checkbox div:first-child').addClass('unmarked-checkbox').removeClass('mark-checkbox');
              findParent.closest('.annual-budget-cntnr').find('.form-checkbox div:first-child').data('checkbox-status', "unchecked");
              $this.removeClass('unmarked-checkbox').addClass('mark-checkbox');
              $this.data('checkbox-status', "checked");
          }
       } else if (findParent.parents('.own-building-block').length){
          var $this = $(this).find("div:first-child");
          var checkboxSatus = $this.data('checkbox-status');
          if(checkboxSatus == "unchecked") {
              findParent.closest('.own-building-block').find('.form-checkbox div:first-child').addClass('unmarked-checkbox').removeClass('mark-checkbox');
              findParent.closest('.own-building-block').find('.form-checkbox div:first-child').data('checkbox-status', "unchecked");
              $this.removeClass('unmarked-checkbox').addClass('mark-checkbox');
              $this.data('checkbox-status', "checked");
          }
       } else if (findParent.parents('.org-building-years').length){
          var $this = $(this).find("div:first-child");
          var checkboxSatus = $this.data('checkbox-status');
          if(checkboxSatus == "unchecked") {
              findParent.closest('.org-building-years').find('.form-checkbox div:first-child').addClass('unmarked-checkbox').removeClass('mark-checkbox');
              findParent.closest('.org-building-years').find('.form-checkbox div:first-child').data('checkbox-status', "unchecked");
              $this.removeClass('unmarked-checkbox').addClass('mark-checkbox');
              $this.data('checkbox-status', "checked");
          }
       } else if (findParent.parents('.get-building-roof-year').length){
          var $this = $(this).find("div:first-child");
          var checkboxSatus = $this.data('checkbox-status');
          if(checkboxSatus == "unchecked") {
              findParent.closest('.get-building-roof-year').find('.form-checkbox div:first-child').addClass('unmarked-checkbox').removeClass('mark-checkbox');
              findParent.closest('.get-building-roof-year').find('.form-checkbox div:first-child').data('checkbox-status', "unchecked");
              $this.removeClass('unmarked-checkbox').addClass('mark-checkbox');
              $this.data('checkbox-status', "checked");
          }
       } else if (findParent.parents('.roof-replace-plan').length){
          var $this = $(this).find("div:first-child");
          var checkboxSatus = $this.data('checkbox-status');
          if(checkboxSatus == "unchecked") {
              findParent.closest('.roof-replace-plan').find('.form-checkbox div:first-child').addClass('unmarked-checkbox').removeClass('mark-checkbox');
              findParent.closest('.roof-replace-plan').find('.form-checkbox div:first-child').data('checkbox-status', "unchecked");
              $this.removeClass('unmarked-checkbox').addClass('mark-checkbox');
              $this.data('checkbox-status', "checked");
          }
       }
           /*var $this = $(this).find("div:first-child");
           var checkboxSatus = $this.data('checkbox-status');
           if(checkboxSatus == "checked") {
               $this.removeClass('mark-checkbox').addClass('unmarked-checkbox');
               $this.data('checkbox-status', "unchecked");
           } else {
                  $this.removeClass('unmarked-checkbox').addClass('mark-checkbox');
                  $this.data('checkbox-status', "checked");
           }*/
  });
   function step1Validation() {
          var firstName = $('.input-full-name .firstname input[type=text]').val().trim();
          var lastName = $('.input-full-name .lastname input[type=text]').val().trim();
          var email = $('.input-email-code > div:first-child input[type=text]').val().trim();

          var firstZip = $('.input-full-zip  > div:first-child input[type=text]').val().trim();
          var zipCode = $('.input-email-code > div:last-child input[type=text]').val().trim();
          var regExp = /^([A-Za-z0-9_\-\.])+\@([A-Za-z0-9_\-\.])+\.([A-Za-z]{2,4})$/;
          var status = "success";
          $(".field-error").remove();
          if(firstName.length <= 0) {
              var errorMsg = '<div class="field-error">Please enter your first name.</div>';
              $(".input-full-name > div:first-child").append(errorMsg);
              status = "error";
          }     
          if(lastName.length <= 0) {
              var errorMsg = '<div class="field-error">Please enter your last name.</div>';
              $(".input-full-name > div:last-child").append(errorMsg);
              status = "error";
          }
 
          if(email.length <= 0 || regExp.test(email) == false) {
              var errorMsg = '<div class="field-error">Please enter valid email.</div>';
              $(".input-email-code > div:first-child").append(errorMsg);
              status = "error";
          } 
          return status;
   }
   function step2Validation() {
          var personalDesc = $(".proj-intrest-desc-block .text-area").val().trim();
          var leadDesc = $(".lead-exp-desc-block .text-area").val().trim();
          var status = "success";
          $(".field-error").remove();
          if(personalDesc.length <= 0) {
              var errorMsg = '<div class="field-error">Please tell us why are you personally interested in spearheading a solar project in your community?</div>';
              $(".proj-intrest-desc-block").after(errorMsg);
              status = "error";
          } if(leadDesc.length <= 0) {
              var errorMsg = '<div class="field-error">Please tell us what experience do you have leading community-based projects?</div>';
              $(".lead-exp-desc-main-block").append(errorMsg);
              status = "error";
          }
          return status;
   }
   function step3Validation() {
          var organisationName = $('.org-name-taxid > div:first-child input[type=text]').val().trim();
          var organisationTaxId = $('.org-name-taxid > div:last-child input[type=text]').val().trim();
          var organisationAddress = $('.org-address input[type=text]').val().trim();

          var websiteName = $('.org-name-taxid > div:last-child input[type=text]').val().trim();



          var urlRegEx = /^(http[s]?:\/\/){0,1}(www\.){0,1}[a-zA-Z0-9\.\-]+\.[a-zA-Z]{2,5}[\.]{0,1}/;
          var status = "success";
          $(".field-error").remove();
          if(organisationName.length <= 0) {
              var errorMsg = '<div class="field-error">Please enter organization name.</div>';
              $(".org-name-taxid > div:first-child").append(errorMsg);
              status = "error";
          } if(organisationTaxId.length <= 0) {
              var errorMsg = '<div class="field-error">Please enter tax id.</div>';
              $(".org-name-taxid > div:last-child").append(errorMsg);
              status = "error";
          } if(organisationAddress.length <= 0) {
              var errorMsg = '<div class="field-error">Please enter organization address.</div>';
              $(".org-address").append(errorMsg);
              status = "error";
          }
           if(websiteName.length <= 0 || urlRegEx.test(websiteName) == false) {
              var errorMsg = '<div class="field-error">Please enter your website name.</div>';
              $(".webite-and-phone > div:first-child").append(errorMsg);
              status = "error";
          } 
          if(missionStatement.length <= 0) {
              var errorMsg = '<div class="field-error">Please enter mission statement.</div>';
              $(".mission-stmnt").append(errorMsg);
              status = "error";
          } if(orgStartYear.length <= 0 || orgStartYear > 2017) {
              var errorMsg = '<div class="field-error">Please enter valid organization start year.</div>';
              $(".org-strt-year").append(errorMsg);
              status = "error";
          }
          return status;
   }
   function step4Validation() {
          var folkCounts = $('.folk-count input[type=text]').val().trim();
          var electricityProvider = $('.electricity-provider input[type=text]').val().trim();
          var orgInterestBlock = $(".org-intrest-solar-block .text-area").val().trim();
          var status = "success";
          $(".field-error").remove();
          if(folkCounts.length <= 0) {
              var errorMsg = '<div class="field-error">Please enter people count.</div>';
              $(".folk-count").append(errorMsg);
              status = "error";
          } if(electricityProvider.length <= 0) {
              var errorMsg = '<div class="field-error">Please enter electric utility provider. </div>';
              $(".electricity-provider").append(errorMsg);
              status = "error";
          }
          if(orgInterestBlock.length <= 0) {
              var errorMsg = '<div class="field-error">Please tell us why is the organization interested in going solar?</div>';
              $(".org-intrest-solar-block").after(errorMsg);
              status = "error";
          }
          return status;
   }
  $(".from-nxt-btn").click(function(e){
      var $this = $(this);
      var status;
      if ($this.parents('.form-step-1').length) {
          status = step1Validation();
          if (status == "success") {
              var checkFilter = $this.closest('.form-step-1').find(".know-interest-cntnr .mark-checkbox").data('form-filter');
              if (checkFilter == "addFilter") {
                  $(".form-step-1 .from-nxt-btn").hide();
                  $(".form-step-1 .form-submit-btn").hide();
              }
          }
      }
      if ($this.parents('.form-step-2').length) {
          status = step3Validation();
      }
      if ($this.parents('.form-step-3').length) {
          status = step3Validation();
      }
      if (status == "success") {
              var formNumber = parseInt($this.parent().prop('className').substr($this.parent().prop('className').length - 1));
              (++formNumber).toString();
              $this.parent().hide();
              $(".form-step-"+formNumber).show();
      }

  });
  $(".form-submit-btn").click(function(e){
       var $this = $(this);
       var status, data= {};
      var firstName = $('.input-full-name .firstname input[type=text]').val().trim();
      var lastName = $('.input-full-name .lastname input[type=text]').val().trim();
      var email = $('.input-email-code > div:first-child input[type=text]').val().trim();

      var firstZip = $('.input-full-zip  > div:first-child input[type=text]').val().trim();

      var phonenumber = $('.input-email-code > div:last-child input[type=text]').val().trim();
      var orgState = $('.org-statezip > div:last-child input[type=text]').val().trim();
      var zipCode = '';
      
      var signUp = $(".sign-up-revolve-update div:last-child").text().trim();
      var interest = $(".know-interest-cntnr .mark-checkbox").parent().next().text().trim();
      var colstudent = $(".colstudent-cntnr .mark-checkbox").parent().next().text().trim();
      var colteam = $(".colteam-cntnr .mark-checkbox").parent().next().text().trim();
      var heardSource = $(".get-to-know-revolv-block .mark-checkbox").parent().next().text().trim();


      if ($this.parents('.form-step-1').length) {
          status = step1Validation();
          if(status == "error")
           return;
      }
       if ($this.parents('.form-step-4').length) {
          status = step4Validation();
          if(status == "error")
           return;
      }

      var organisationName = $('.org-name-taxid > div:first-child input[type=text]').val().trim();
      var organisationTaxId = $('.org-name-taxid > div:last-child input[type=text]').val().trim();
      var organisationAddress = $('.org-statezip > div:first-child input[type=text]').val().trim();

      var websiteName = $('.org-name-taxid > div:last-child input[type=text]').val().trim();

      var otherForm = $(".get-to-know-revolv-cntnr .get-to-know-revolv-block #otherCheckbox .get-to-know-text .text-area").val().trim();
      
      var schoolLoc = $(".schoolLoc-org-cntnr .schoolLoc-org-block .text-area").val().trim();
      var schoolTeam = $(".schoolTeam-org-cntnr .schoolTeam-org-block .text-area").val().trim();

      var affiliation = $(".affiliation-org-cntnr .affiliation-org-block .text-area").val().trim();
      var solarProjNeed = $(".solar-proj-need-cntnr .mark-checkbox").parent().next().text().trim();

      var intakeForm = '<div class="intake-form-msg-cntnr">'
                              +'<div class="intake-form-msg">'
                                  +'<span>Thank you for your interest in becoming a Solar Ambassador!<br> We will be in touch soon!</span>'
                                  +'<div class="form-submit-msg-btn-cntnr">'
                                      +'<div class="form-submit-msg-btn">OK</div>'
                                  +'</div>'
                              +'</div>'
                          +'</div>';
      $("body").prepend(intakeForm);
      $('body').css('overflow', 'hidden');
      formMessage();

      var urlData = [location.protocol, '//', location.host, '/bring_solar_to_your_community/intake_form/submit/'].join('');
      $.ajax({
              type: 'GET',
              url: urlData,
              data: {
                  firstName: firstName,
                  lastName: lastName,
                  email: email,
                  zipCode: zipCode,
                  colstudent: colstudent,
                  signUp: signUp,
                  interest: interest,
                  colteam: colteam,
                  heardSource: heardSource,
                  otherForm: otherForm,  
                  orgState : orgState,
                  phonenumber: phonenumber,
                  
                  firstZip: firstZip,

                  organisationName: organisationName,
                  organisationTaxId: organisationTaxId,
                  organisationAddress: organisationAddress,

                  websiteName: websiteName,
           

                  schoolLoc: schoolLoc,
                  schoolTeam: schoolTeam,
                  affiliation: affiliation,
                  solarProjNeed: solarProjNeed,

              }

          })
          .done(function (response) {
              console.log(response)
          })
          .fail(function (msg) {

          });
   });
   $(".webite-and-phone > div:last-child input[type=text]").mask("(999) 999-9999",{placeholder:"x"});
   $.mask.definitions['h'] = "[0-9]";
   /* $('.org-name-taxid > div:last-child input[type=text]').mask("hh-hhhhhhh",{placeholder:"x"}); */
   $('.org-strt-year input[type=text]').mask("hhhh",{placeholder:""});
   /*$('.input-email-code > div:last-child input[type=text]').mask("hhhhh-hhhh?-hh",{placeholder:"x"});*/
  function formMessage() {
      $(".form-submit-msg-btn").click(function(e){
          window.location.href = "/get-involved/solar-ambassador/";
      });

  }
});
var streamVideo = 0, element, instance, playersrc;
function play(vidId) {
      instance = document.getElementById(vidId);
      playersrc=$(instance).attr('src');
      console.log(playersrc);
      $(instance).attr('src',playersrc+'&autoplay=1');

}

function pause(vidId) {
      instance = document.getElementById(vidId);
      console.log(playersrc)
      $(instance).attr('src',playersrc);
}
function showDesktopFullscreen(vidId) {
    element = document.getElementById(vidId);
   $(element).attr('src',playersrc);
  $("#video-popup").show();
  $( ".pop-up-vid-cntnr" ).remove();
  var popUpVideoId = document.getElementById("pop-up-video");
  console.log(element, $(element).attr('src'))

  var $iframe = $("<iframe id='pop-up-iframe-vid-id' frameborder='0'>").attr("src", $(element).attr('src')+'&autoplay=1');
  $("#video-popup .play-main-video").append($iframe);
  $iframe.wrap("<div class='pop-up-vid-cntnr'>");

  $(".video-popup-body, #video-popup").click(function(e){
       e.stopPropagation();
       if (e.target !== this)
          return;

      $("#pop-up-iframe-vid-id").attr("src", playersrc);
      $("#video-popup").hide();
  });
   $(document).keydown(function(e) {
      if (e.keyCode == 27) {
      $("#pop-up-iframe-vid-id").attr("src", playersrc);
           $("#video-popup").hide();
      }
  });
   $(".close-video").click(function(e){
       e.stopPropagation();

      $("#pop-up-iframe-vid-id").attr("src", playersrc);
      $("#video-popup").hide();
  });
  /* $('#video-popup').bind('keydown', function(event) {
       console.log("key down")
      if (event.keyCode == 27){
          $("#pop-up-iframe-vid-id").attr("src", playersrc);
           $("#video-popup").hide();
      }
   });*/
}
function goFullscreen(id) {
  console.log(id)
    element = document.getElementById(id);
  $("#video-popup").show();
  $( ".pop-up-vid-cntnr" ).remove();
  var popUpVideoId = document.getElementById("pop-up-video");

  var $iframe = $("<iframe id='pop-up-iframe-vid-id' frameborder='0' allowfullscreen>").attr("src", $(element).attr('src')+'&autoplay=1');
  $("#video-popup .play-main-video").append($iframe);
  $iframe.wrap("<div class='pop-up-vid-cntnr'>");


$(".video-popup-body, #video-popup").click(function(e){
       e.stopPropagation();
        if (e.target !== this)
          return;
          $("#pop-up-iframe-vid-id").attr("src", $(element).attr('src'));
        $("#video-popup").hide();
  });
$(document).keydown(function(e) {
      if (e.keyCode == 27) {
      $("#pop-up-iframe-vid-id").attr("src", $(element).attr('src'));
           $("#video-popup").hide();
      }
  });
}



