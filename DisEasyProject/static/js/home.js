$(document).ready(function() {
  $('.flip').hover(function(){
        $(this).find('.card').toggleClass('flipped');

    });

  //Submit button click
  $('.flip').click(function() {
	  window.location = '/form';
  });
});