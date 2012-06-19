/* Author:

*/

function check_sentiment(text){
	var client = new XMLHttpRequest();
	client.open("GET", "http://happy.elevenbasetwo.com?text=" + text, true);
	client.onreadystatechange = function() {
		if(client.readyState == 4) {
			if(client.responseText == "happy") {
			document.getElementById("smiley").setAttribute("class", "smile");	
		} else {
			document.getElementById("smiley").setAttribute("class", "frown");	
		}
			
		};
	};

	client.send();
}

