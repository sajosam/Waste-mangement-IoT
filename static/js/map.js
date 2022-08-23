const labels = "ABCDEFGHIJKLMNOPQRSTUVWXYZ";
let labelIndex = 0;

function initMap() {
  var a = [
    { lat: 10.97, lng: 77.59 },
    { lat: 11.97, lng: 77.59 },
    { lat: 12.97, lng: 77.59 },
  ];
  const bangalore = { lat: 10.053498231231606, lng: 76.31555169898813 };
  const map = new google.maps.Map(document.getElementById("map"), {
    zoom: 12,
    center: bangalore,
  });

  // This event listener calls addMarker() when the map is clicked.
  // Add a marker at the center of the map.
  addMarker(bangalore, map);
}

// Adds a marker to the map.
function addMarker(location, map) {
  // Add the marker at the clicked location, and add the next-available label
  // from the array of alphabetical characters.
  new google.maps.Marker({
    position: location,
    label: labels[labelIndex++ % labels.length],
    map: map,
  });
}

window.initMap = initMap;
