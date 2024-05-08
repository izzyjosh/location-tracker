var map = L.map("map").setView([51.505, -0.09], 9);
L.tileLayer("https://tile.openstreetmap.org/{z}/{x}/{y}.png", {
  maxZoom: 16,
  attribution:
    '&copy; <a href="http://www.openstreetmap.org/copyright">OpenStreetMap</a>'
}).addTo(map);

navigator.geolocation.watchPosition(success, error);

let marker, circle, zoomed;
function success(pos) {
  const lat = pos.coords.latitude;
  const lng = pos.coords.longitude;
  const accuracy = pos.coords.accuracy;
  if (marker) {
    map.removeLayer(marker);
    map.removeLayer(circle);
  }
  marker = L.marker([lat, lng]).addTo(map);
  circle = L.circle([lat, lng], { radius: accuracy }).addTo(map);

  if (!zoomed) {
    zoomed = map.fitBounds(circle.getBounds());
  }

  map.setView([lat, lng]);
}

function error(err) {
  if (err.code === 1) {
    alert("Please allow geolocation to access your location ");
  } else {
    alert("Geolocation is unable to access your location");
  }
}
