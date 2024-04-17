$(()=>{ 
	function getUrlParameter(name) {
        const urlParams = new URLSearchParams(window.location.search);
        return urlParams.get(name);
    };

    const id = getUrlParameter('id');
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

	$('#submit').click(function(event){
		event.preventDefault()
		const formData = {};
		if ($('#inputName').val() !== "") {
			formData.item_name = $('#inputName').val();
		}
		if ($('#inputImage').val() !== "") {
			formData.item_image = $('#inputImage').val();
		}
		if ($('#inputDesc').val() !== "") {
			formData.item_description = $('#inputDesc').val();
		}
		if ($('#inputFirstPrice').val() !== "") {
			formData.item_first_price = $('#inputFirstPrice').val();
		}
		if ($('#inputSecondPrice').val() !== "") {
			formData.item_second_price = $('#inputSecondPrice').val();
		}
		if ($('#inputIcon').val() !== "") {
			formData.icon_1 = $('#inputIcon').val();
		}
		if ($('#inputCategory').val() !== "") {
			formData.item_category = $('#inputCategory').val();
		}
		const jsonData = JSON.stringify(formData);
		console.log('JSON Data',jsonData);
		$.ajax({
			url: `https://kcodev.tech/restaurantcms/api/food_items/${id}`,
			method: 'PUT',
			contentType: 'application/json',
			data: jsonData,
			success: function(response){
				console.log(response);
				var modal = document.getElementById("myModal");
				var span = document.getElementsByClassName("close")[0];
				var close = document.getElementsByClassName("modal-btn")[0];
				modal.style.display = "block";
				span.onclick = function() {
					modal.style.display = "none";
					location.replace("../../../web_dynamic/templates/dashboard/index.html");
				}
				close.onclick = function() {
					location.replace("../../../web_dynamic/templates/dashboard/index.html");
					modal.style.display = "none";
				}

				// open a new dialog that tells the user that item has beeen successfully updated
				//now redirect the user to the home menu
			},
			error: function(xhr, status, error){
				alert(error);
				console.log(error);
			}
		})
	});

});