$(()=>{
	const fetchAPIData = () => {
		$.ajax({
			url: 'https://kcodev.tech/restaurantcms/api/food_items',
			method: 'GET',
			success: function(response) {
				console.log(response);
				let coffeeSection = '';
				response.forEach(foodItem => {
					coffeeSection += `
							<tr>
								<td id="item-name">${foodItem.item_name}</td>
								<td id="item-first-price">${foodItem.item_first_price}</td>
								<td id="item-second-price">${foodItem.item_second_price}</td>
							</tr>
					`;
				});
				$('table#coffee-table').append(coffeeSection);
			},
			error: function (xhr, status, error) {
				console.error('Error:', status, error);
			} 
		});
	};

	fetchAPIData();
});