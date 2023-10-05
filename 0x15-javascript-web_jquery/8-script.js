$.get('https://swapi-api.alx-tools.com/api/people/5/?format=json', function (data, status){
	$(data.result).each(function (){
		$(result).append('<li>' + this.title + '</li>');
	});
});
