$(()=>{ 
	function getUrlParameter(name) {
        const urlParams = new URLSearchParams(window.location.search);
        return urlParams.get(name);
    };

    // Get the value of 'id' from the URL
    var id = getUrlParameter('id');

    // Set the value of the HTML field
    $('#field').val(id);
});