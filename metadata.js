	var artistvar = "No Artist";
	var albumvar = "No Album";
	var titlevar = "No Title";
	var artistmetadata;
	var albummetadata;
	var titlemetadata;

	function doesFileExist(urlToFile){
    var xhr = new XMLHttpRequest();
    xhr.open('HEAD', urlToFile, false);
    xhr.send();
     
    if (xhr.status == "404") {
        return false;
    } else {
        return true;
    }
}

	if (doesFileExist("artist") == false) {
		artistmetadata = "No Artist";
	}
	else {
		artistmetadata = $.ajax({type: "GET", url: "artist", async: false}).responseText;
	}

	if (doesFileExist("album") == false) {
		albummetadata = "No Album";
	}
	else {
		albummetadata = $.ajax({type: "GET", url: "album", async: false}).responseText;
	}

	if (doesFileExist("title") == false) {
		titlemetadata = "No Title";
	}
	else {
		titlemetadata = $.ajax({type: "GET", url: "title", async: false}).responseText;
	}



	console.log(artistmetadata);
	console.log(albummetadata);
	console.log(titlemetadata);