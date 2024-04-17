$(()=>{ 
	function getUrlParameter(name) {
        const urlParams = new URLSearchParams(window.location.search);
        return urlParams.get(name);
    };

    let id = getUrlParameter('id');
	console.log(id);

	const fetchAPIData = () => {
		$.ajax({
			url: `https://kcodev.tech/restaurantcms/api/food_items/${id}`,
			method: 'GET',
			success: function(response) {
				console.log("API Response:", response);
				
				$('#inputName').attr('placeholder', response.item_name);
				$('#inputImage').attr('placeholder', response.item_image);
                $('#inputDesc').attr('placeholder', response.item_description);
                $('#inputFirstPrice').attr('placeholder', response.item_first_price);
                $('#inputSecondPrice').attr('placeholder', response.item_second_price);
                $('#inputIcon').attr('placeholder', response.icon_1); // Change to appropriate icon field
                $('#inputCategory').attr('placeholder', response.item_category);
			},
			error: function(xhr, status, error){
				setTimeout(() => {
					fetchAPIData()
				  }, 2000)
			},
		});
	};

	fetchAPIData();

});