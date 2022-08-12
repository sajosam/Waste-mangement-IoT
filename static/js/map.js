 
 const labels = "ABCDEFGHIJKLMNOPQRSTUVWXYZ";
 let labelIndex = 0;
 
 function initMap() {
    var a =[{lat: 10.97, lng: 77.59},{lat: 11.97, lng: 77.59},{lat: 12.97, lng: 77.59}]
   const bangalore = { lat: 12.97, lng: 77.59 };
   const map = new google.maps.Map(document.getElementById("map"), {
     zoom: 12,
     center: bangalore,
   });
 
   // This event listener calls addMarker() when the map is clicked.
   // Add a marker at the center of the map.
   for(var i=0;i<a.length;i++){
    addMarker({lat:a[i].lat,lng:a[i].lng}, map)
   }
   

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
 