$(document).ready(function() {
  //Updates the value of the dropdown menus
  $('.dropdown-menu > li').click(function() {
    var $toggle = $(this).parent().siblings('.dropdown-toggle');
    $toggle.html("<i class=\"icon icon-envelope icon-white\"></i> " + $(this).text() + "  <span class=\"caret\"></span>")
  });

  //Submit button click
  $('#submitButton').click(function() {
	var conditionVal = $('#conditionDropdown').text();
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
	var jString = {};
	jString["diseaseState"] = conditionVal;
	jString["gender"] = genderVal
	jString["age"] = ageVal;
	jString["height"] = heightVal;
	jString["weight"] = weightVal;
	jString["testOne"] = testOneVal;
	jString["testOneUnit"] = testOneUnitVal;
	jString["testTwo"] = testTwoVal;
	jString["testTwoUnit"] = testTwoUnitVal;
	jString["familyHistory"] = familyHistoryVal;
	jString["diagnosedDiabetic"] = diagnosedDiabeticVal;
	jString["diagnosedPreDiabetic"] = diagnosedPreDiabeticVal;
	alert(JSON.stringify(jString, null, ' '));
  });
});