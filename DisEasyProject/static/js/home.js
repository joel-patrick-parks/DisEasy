$(document).ready(function() {
  $('.flip').hover(function(){
        $(this).find('.card').toggleClass('flipped');

    });

  //Submit button click
  $('#flip-diabetes').click(function() {
	  window.location = '/diabetes/form';
  });

  $('#flip-thyroid').click(function() {
    window.location='/thyroid/form';
  });
});
