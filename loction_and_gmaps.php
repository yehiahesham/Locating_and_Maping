<!DOCTYPE html>
<html>
<body>

<!--
This HTML code pinpoint the user location using the HTML5 Geolocation API and maps it in a google map

EVERYTHING WORKS FOR OTHER PLATFORMS LIKE IPHONE,MAC,WIND,& LUNIX, BUT  FOR THE Android PHONES: YOU MUST OPEN YOU LOCATOR AND HTTPS THE REQUEST.
for reference check: https://developer.mozilla.org/en-US/docs/Web/API/Geolocation/Using_geolocation or  http://www.w3schools.com/html/html5_geolocation.asp

Also THE JAVA SCRIPT WOULDN'T WORK ON Android PHONES, because they don't support it. thus Android phones will fail to get the google map, unlike other platforms mentioned above
-->


<p id="demo">Click the button to get your position.</p>

<button onclick="getLocation()">Try It</button>

<div id="mapholder"></div>

<script src="http://maps.google.com/maps/api/js?sensor=false&key=PUT_YOUR_KEY_HERE"></script>

<script>
var x = document.getElementById("demo");
function getLocation() {
    if (navigator.geolocation) {
        navigator.geolocation.getCurrentPosition(showPosition, showError);
    } else {
        x.innerHTML = "Geolocation is not supported by this browser.";
    }
}

function showPosition(position) {
    lat = position.coords.latitude;
    lon = position.coords.longitude;
    latlon = new google.maps.LatLng(lat, lon)
    mapholder = document.getElementById('mapholder')
    mapholder.style.height = '250px';
    mapholder.style.width = '500px';

    var myOptions = {
    center:latlon,zoom:14,
    mapTypeId:google.maps.MapTypeId.ROADMAP,
    mapTypeControl:false,
    navigationControlOptions:{style:google.maps.NavigationControlStyle.SMALL}
    }

    var map = new google.maps.Map(document.getElementById("mapholder"), myOptions);
    var marker = new google.maps.Marker({position:latlon,map:map,title:"You are here!"});
}

function showError(error) {
    switch(error.code) {
        case error.PERMISSION_DENIED:
            x.innerHTML = "User denied the request for Geolocation."
            break;
        case error.POSITION_UNAVAILABLE:
            x.innerHTML = "Location information is unavailable."
            break;
        case error.TIMEOUT:
            x.innerHTML = "The request to get user location timed out."
            break;
        case error.UNKNOWN_ERROR:
            x.innerHTML = "An unknown error occurred."
            break;
    }
}
</script>

</body>
</html>
