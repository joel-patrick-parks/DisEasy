$(document).ready(function() {
  //Updates the value of the dropdown menus
  $('.dropdown-menu > li').click(function() {
    var $toggle = $(this).parent().siblings('.dropdown-toggle');
    $toggle.html("<i class=\"icon icon-envelope icon-white\"></i> " + $(this).text() + "  <span class=\"caret\"></span>")
  });
  
  $('.flip').hover(function(){
        $(this).find('.card').toggleClass('flipped');

    });
	
	$('.flip').click(function() {
	  window.location = 'index.html';
  });

  //Submit button click
  $('#submitButton').click(function() {
	var isValid = true;  
	  
	var genderVal = $('#genderDropdown').text();
    var ageVal = $('#ageInput').val();
	var labVal = $('#labDropdown').text();
    var testOneVal = $('#testOneInput').val();
    var testTwoVal = $('#testTwoInput').val();
	var testThreeVal = $('#testThreeInput').val();
	
	var ageNum = parseInt(ageVal);
	var testOneNum = parseInt(testOneVal);
	var testTwoNum = parseInt(testTwoVal);
	var testThreeNum = parseInt(testThreeVal);
	
	var jString = {};
	jString["gender"] = genderVal
	jString["age"] = ageVal;
	jString["lab"] = labVal;
	jString["testOne"] = testOneVal;
	jString["testTwo"] = testTwoVal;
	jString["testTwo"] = testThreeVal;
	
	//alert(isValid);
	
	if(jString.gender !== " Male  " && jString.gender !== " Female  "){
		$('#genderWarning').show();
		isValid = false;
	}
	if(jString.gender == " Male  " || jString.gender == " Female  "){
		$('#genderWarning').hide();
	}
	if(jString.lab !== " Quest Diagnostics  " && jString.lab !== " LabCorp  "){
		$('#labWarning').show();
		isValid = false;
	}
	if(jString.lab == " Quest Diagnostics  " || jString.lab == " LabCorp  "){
		$('#labWarning').hide();
	}
	if(isNaN(ageNum)) {
		$('#ageWarning').show();
		isValid = false;
	}else{
		$('#ageWarning').hide();
	}
	if(isNaN(testOneNum)) {
		$('#testOneWarning').show();
		isValid = false;
	}else{
		$('#testOneWarning').hide();
	}
	if(isNaN(testTwoNum)) {
		$('#testTwoWarning').show();
		isValid = false;
	}else{
		$('#testTwoWarning').hide();
	}
	if(isNaN(testThreeNum)) {
		$('#testThreeWarning').show();
		isValid = false;
	}else{
		$('#testThreeWarning').hide();
	}
	
	/*if(isValid){
		$.post("/submit",
		{
			PatiantResults: jString
		},
		function(data, status){
			alert("Sent the object.");
		});
	}*/
  });
});