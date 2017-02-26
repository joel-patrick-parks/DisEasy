$(document).ready(function() {
  //Updates the value of the dropdown menus
  $('.dropdown-menu > li').click(function() {
    var $toggle = $(this).parent().siblings('.dropdown-toggle');
    $toggle.html("<i class=\"icon icon-envelope icon-white\"></i> " + $(this).text() + "  <span class=\"caret\"></span>")
  });

  //Submit button click
  $('#submitButton').click(function() {
	var isValid = true;  
	  
	var conditionVal = "Type II Diabetes";
	var genderVal = $('#genderDropdown').text();
    var ageVal = $('#ageInput').val();
    var heightVal = $('#heightInput').val();
    var weightVal = $('#weightInput').val();
	var labVal = $('#labDropdown').text();
    var testOneVal = $('#testOneInput').val();
    var testOneUnitVal = $('#testOneDropdown').text();
    var testTwoVal = $('#testTwoInput').val();
    var testTwoUnitVal = $('#testTwoDropdown').text();
	var familyHistoryVal = $('#familyHistoryDropdown').text();
	var diagnosedDiabeticVal = $('#diabeticDropdown').text();
	var diagnosedPreDiabeticVal = $('#prediabeticDropdown').text();
	
	var ageNum = parseInt(ageVal);
	var weightNum = parseInt(weightVal);
	var heightNum = parseInt(heightVal);
	
	var jString = {};
	jString["diseaseState"] = conditionVal;
	jString["gender"] = genderVal.trim();
	jString["age"] = ageVal.trim();
	jString["height"] = heightVal.trim();
	jString["weight"] = weightVal.trim();
	jString["lab"] = labVal.trim();
	jString["testOne"] = testOneVal.trim();
	jString["testOneUnit"] = testOneUnitVal.trim();
	jString["testTwo"] = testTwoVal.trim();
	jString["testTwoUnit"] = testTwoUnitVal.trim();
	jString["familyHistory"] = familyHistoryVal.trim();
	jString["diagnosedDiabetic"] = diagnosedDiabeticVal.trim();
	jString["diagnosedPreDiabetic"] = diagnosedPreDiabeticVal.trim();
	
	/*if(jString.diseaseState !== " Type II Diabetes  "){
		$('#conditionWarning').show();
		isValid = false;
	}
	if(jString.gender !== " Male  " || jString.gender !== " Female  "){
		$('#genderWarning').show();
		isValid = false;
	}
	if(ageNum == NaN && jString.age == null){
		$('#ageWarning').show();
		isValid = false;
	}
	if(weightNum == NaN && jString.weight == ""){
		$('#weightWarning').show();
		isValid = false;
	}
	if(heightNum == NaN && jString.height == ""){
		$('#heightWarning').show();
		isValid = false;
	}
	if(testOneVal == NaN && jString.testOne == ""){
		$('#testOneWarning').show();
		isValid = false;
	}
	if(jString.testOneUnit !== " mM/L  " || jString.testOneUnit !== " mg/dL  "){
		$('#testOneUnitWarning').show();
		isValid = false;
	}
	if(testTwoVal == NaN && jString.testTwo == ""){
		$('#testTwoWarning').show();
		isValid = false;
	}
	if(jString.testTwoUnit !== " mM/L  " || jString.testTwoUnit !== " mg/dL  "){
		$('#testTwoUnitWarning').show();
		isValid = false;
	}*/
  
  // DELETE ME LATER
  isValid = true;
	
	if(isValid){
    console.log(jString);
		$.post("/submit",
		{
			data: jString
		},
		function(data, status){
			window.location = data;
		});
	}
  });
});
