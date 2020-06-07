$(document).ready(function() {
    $('.collapsible').collapsible();
    $('select').material_select();
    $(".button-collapse").sideNav();
    $('.parallax').parallax();
    $('.slider').slider();


    var max_fields = 20;
    var ingredientWrapper = $("#add-ingredient");
    var instructionWrapper = $("#add-instruction");    
    var add_ingredient_button = $("#add-ingredient-button");
    var add_instruction_button = $("#add-instruction-button");

    var x = 1;
    $(add_ingredient_button).click(function(e) {
    e.preventDefault();
    if (x < max_fields) {
        x++;
        $(ingredientWrapper).append('<div><input type="text" name="ingredients"/><a href="#" class="delete">Delete</a></div>'); //add input box
    } else {
        alert('You have reached the limit')
    }
    });
    $(ingredientWrapper).on("click", ".delete", function(e) {
    e.preventDefault();
    $(this).parent('div').remove();
    x--;
    })

    var y = 1;
    $(add_instruction_button).click(function(e) {
    e.preventDefault();
    if (y < max_fields) {
        y++;
        $(instructionWrapper).append('<div><input type="text" name="instructions"/><a href="#" class="delete">Delete</a></div>'); //add input box
    } else {
        alert('You have reached the limit')
    }
    });
    $(instructionWrapper).on("click", ".delete", function(e) {
    e.preventDefault();
    $(this).parent('div').remove();
    y--;
    })
});