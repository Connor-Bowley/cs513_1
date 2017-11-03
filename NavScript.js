function setNav( id ){
	var out = "<ul id='menu'>";

	if(id > 0){ // customer
		out += "<li><a href='view_customer.html?id="+id+"&cid="+id+"'>Home</a></li>";
		out += "<li><a href='list_data.html?id="+id+"'>List All</a></li>";
	}
	else //admin
	{
		out += "<li><a href='list_data.html?id="+id+"'>Home</a></li>";
	}
	out += "<li><a href='search_games.html?id="+id+"'>Search/Purchase Games</a></li>";
	out += "<li><a href='index.html'>Logout</a></li>";
	out += "<li><a href='https://github.com/Connor-Bowley/cs513_1'>Display Source</a></li>";
	out += "</ul>";
	document.getElementById("nav01").innerHTML = out;
}
