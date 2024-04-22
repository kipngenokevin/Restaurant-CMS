$(()=>{ 
	// validate form data 
	$("#add-item").validate({
        rules: {
            item_name: "required",
			item_first_price: "required",
        },
        messages: {
            item_name: "Please enter the name of the food item",
			item_first_price: "Please enter the item price",
        }
    });

	$('#add-item').submit(function(event){
		event.preventDefault();
		console.log('Checking is Form Data is Valid');
		if ($(this).valid()) {
			const formData = {};
			const jsonData = JSON.stringify(formData);
			console.log('JSON Data',jsonData);
		} else {
			console.log("Form is invalid");
		}
	});

});