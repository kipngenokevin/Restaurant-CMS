$(()=>{
	const fetchAPIData = () => {
		let loader = `<tr style="border-bottom: none; min-height: 100%;"><td style="text-align: center; vertical-align: middle;"><div class="loader" style="margin: auto;"></div></td></tr>`;
		document.getElementsByClassName('menu-items')[0].innerHTML = loader;
		$.ajax({
			url: 'https://kcodev.tech/restaurantcms/api/food_items',
			method: 'GET',
			success: function(response) {
				console.log(response);
				let coffeeSection = '';
				response.forEach(foodItem => {
					coffeeSection += `
							<tr>
							<td id="item-name">${foodItem.id}</td>
								<td id="item-name">${foodItem.item_name}</td>
								<td id="item-name">${foodItem.item_category}</td>
								<td id="item-name">${foodItem.item_description}</td>
								<td id="item-first-price">${foodItem.item_first_price}</td>
								<td id="item-second-price">${foodItem.item_second_price}</td>
								<td id="item-name"><a href="../../../web_dynamic/templates/dashboard/edit-item.html?id=${foodItem.id}">edit</a></td>
							</tr>
					`;
				});
				$('table.menu-items').append(coffeeSection);
				$('.loader').remove();
			},
			error: function (xhr, status, error) {
				setTimeout(() => {
					fetchAPIData()
				  }, 2000)
			} 
		});
	};

	fetchAPIData();
});