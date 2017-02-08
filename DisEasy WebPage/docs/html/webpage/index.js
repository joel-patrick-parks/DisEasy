$(document).ready(function() {
  //Updates the value of the dropdown menus
  $('.dropdown-menu > li').click(function() {
    var $toggle = $(this).parent().siblings('.dropdown-toggle');
    $toggle.html("<i class=\"icon icon-envelope icon-white\"></i> " + $(this).text() + "  <span class=\"caret\"></span>")
  });

  //Submit button click
  $('#submitButton').click(function() {
    var ageVal = $('#ageInput').val();
    var heightVal = $('#heightInput').val();
    var weightVal = $('#weightInput').val();
    var testOneVal = $('#testOneInput').val();
    var testOneUnitVal = $('#testOneDropdown').text();
    var testTwoVal = $('#testTwoInput').val();
    var testTwoUnitVal = $('#testTwoDropdown').text();
    var conditionVal = $('#conditionDropdown').text();
    $("p").text(ageVal + " " + heightVal + " " + weightVal + " " + testOneVal + " " + testOneUnitVal + " " + testTwoVal + " " + testTwoUnitVal);
  });
});