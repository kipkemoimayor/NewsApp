$(document).ready(function(){
  $("#sources").click(function(){
    $("html,body").animate({scrollTop:$(document).height()},2000);
    return false;

  })
  var typed=new Typed("#type",{
     strings:["This is not the page you were lookig for if you think its a problem please contact us.."],
     backSpeed:70,
     typeSpeed:80,
     smartBackspace:true,
   })

})
