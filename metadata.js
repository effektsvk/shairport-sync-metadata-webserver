// function set_cover(jsonObj) {
//     if(jsonObj.checksum == null) {
//         return
//     }
//     if (!lol.cover) {
//         console.log(jsonObj);
//         lol.cover = true;
//     }
//     if(jsonObj.checksum != infobuffer.coverHash) {
//         //var temp_cover_url = cover_url + jsonObj.extension + "#" + new Date().getTime();
//         var temp_cover_url = "data:image/png;base64," + jsonObj.base64;


//         $("#coverimage").src = temp_cover_url;
//         infobuffer.coverHash = jsonObj.checksum;
//         loadJSON(color_json_url, set_color);
//     }

// }


///

// var HTML_FILE_URL = 'http://localhost:8080/image';

// $(document).ready(function() {
//     $.get(HTML_FILE_URL, function(data) {
//         var fileDom = $(data);
//         fileDom.find('h2').each(function() {
//             alert($(this).text());
//         });
//     });
// });


///

// $(document).ready(function() {
//     $.get(HTML_FILE_URL, function(data) {
//         $("#coverimage").src = "data:image/png;base64," + data});
// });

$(document).ready(function() {
    $.get('http://localhost:8080/image.b64', function(data) {
        $('#coverimage').src = "data:image/png;base64," + data;});
    });