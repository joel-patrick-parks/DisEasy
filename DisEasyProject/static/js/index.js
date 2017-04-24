$(document).ready(function() {
  //Updates the value of the dropdown menus
  $('.dropdown-menu > li').click(function() {
    var $toggle = $(this).parent().siblings('.dropdown-toggle');
    $toggle.html("<i class=\"icon icon-envelope icon-white\"></i> " + $(this).text() + "  <span class=\"caret\"></span>")
  });

  //Submit button click
  $('#submitButton').click(function() {
	var isValid = true;  
	  
	var genderVal = $('#genderDropdown').text();
    var ageVal = $('#ageInput').val();
    var heightVal = $('#heightInput').val();
    var weightVal = $('#weightInput').val();
	var labVal = $('#labDropdown').text();
    var testOneVal = $('#testOneInput').val();
    var testTwoVal = $('#testTwoInput').val();
	var familyHistoryVal = $('#familyHistoryDropdown').text();
	var diagnosedDiabeticVal = $('#diabeticDropdown').text();
	var diagnosedPreDiabeticVal = $('#prediabeticDropdown').text();
	
	var ageNum = parseInt(ageVal);
	var weightNum = parseInt(weightVal);
	var heightNum = parseInt(heightVal);
	var testOneNum = parseInt(testOneVal);
	var testTwoNum = parseInt(testTwoVal);
	
	var jString = {};
	jString["gender"] = genderVal
	jString["age"] = ageVal;
	jString["height"] = heightVal;
	jString["weight"] = weightVal;
	jString["lab"] = labVal;
	jString["testOne"] = testOneVal;
	jString["testTwo"] = testTwoVal;
	jString["familyHistory"] = familyHistoryVal;
	jString["diagnosedDiabetic"] = diagnosedDiabeticVal;
	jString["diagnosedPreDiabetic"] = diagnosedPreDiabeticVal;
	
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
	if(jString.familyHistory !== " Yes  " && jString.familyHistory !== " No  "){
		$('#familyHistoryWarning').show();
		isValid = false;
	}
	if(jString.familyHistory == " Yes  " || jString.familyHistory == " No  "){
		$('#familyHistoryWarning').hide();
	}
	if(jString.diagnosedDiabetic !== " Yes  " && jString.diagnosedDiabetic !== " No  "){
		$('#diabeticWarning').show();
		isValid = false;
	}
	if(jString.diagnosedDiabetic == " Yes  " || jString.diagnosedDiabetic == " No  "){
		$('#diabeticWarning').hide();
	}
	if(jString.diagnosedPreDiabetic !== " Yes  " && jString.diagnosedPreDiabetic !== " No  "){
		$('#prediabteticWarning').show();
		isValid = false;
	}
	if(jString.diagnosedPreDiabetic == " Yes  " || jString.diagnosedPreDiabetic == " No  "){
		$('#prediabteticWarning').hide();
	}
	if(isNaN(ageNum)) {
		$('#ageWarning').show();
		isValid = false;
	}else{
		$('#ageWarning').hide();
	}
	if(isNaN(weightNum)) {
		$('#weightWarning').show();
		isValid = false;
	}else{
		$('#weightWarning').hide();
	}
	if(isNaN(heightNum)) {
		$('#heightWarning').show();
		isValid = false;
	}else{
		$('#heightWarning').hide();
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
	
	if(isValid){
    console.log(jString);
		$.post("/submit", jString,
		function(data, status){
			window.location = data;
		});
	}
  });
});
