mapboxgl.accessToken = 'pk.eyJ1IjoiZmlsaXB0ZXN0IiwiYSI6ImNrd3V5NjhzdjFyY3YydXJ0bGl5dmhtNTUifQ.ew77j1B9ZXb20GBYznPLbQ';
const bounds = [
[17.597991, 51.518052], //  coordinates
[18.513122, 52.061509] //  coordinates
];

const map = new mapboxgl.Map({
container: 'map', // container id
style: 'mapbox://styles/mapbox/streets-v11',
center: [18.0853, 51.7573],// starting position
zoom: 13.6, // starting zoom
maxZoom: 17,
minZoom: 10,
maxBounds: bounds // Set the map's geographical boundaries. (granice)
});


// obiekt przechowujący wszystkie markery na stronie
let baza_markerow = {
    type: 'FeatureCollection',
    features: []
};

// funkcja dodająca markery
function dodaj_marker(x,y) {
  let nowe_markery = {
    type: 'FeatureCollection',
    features: 
    [{
      type: 'Feature',
      geometry: 
        {
        type: 'Point',
        coordinates: [x,y]
        },
      properties: {
          title: 'Mapbox',
          description: 'Washington, D.C.'
        }
    }]
  };
  
  baza_markerow.features.push(nowe_markery);
  
  // add markers to map
  for (const feature of nowe_markery.features) {
    // create a HTML element for each feature
    const el = document.createElement('div');
    el.className = 'marker';
    el.classList.add("kategoria1");

    // sprawdz czy marker jest klikniety
    el.addEventListener("click", function() {
      clicked = true;
    }, false);
    
    // make a marker for each feature and add to the map

    new mapboxgl.Marker(el).setLngLat(feature.geometry.coordinates).addTo(map);
  }
};






// funkcja otwierająca boczne menu
// function openNav() {
//   document.getElementById("mySidenav").style.width = "250px";
//   document.getElementById("123").style.display = "none";
// }

// // funkcja zamykająca boczne menu
// function closeNav() {
//   document.getElementById("mySidenav").style.width = "0";
//   document.getElementById("123").style.display = "block";
// }


// // Add geolocate control to the map.
// map.addControl(
//   new mapboxgl.GeolocateControl({
//   positionOptions: {
//   enableHighAccuracy: true
//   },
//   // When active the map will receive updates to the device's location as it changes.
//   trackUserLocation: true,
//   // Draw an arrow next to the location dot to indicate which direction the device is heading.
//   showUserHeading: true
//   })
// );


// function dodaj_input() {

//   // usuń ewentualne poprzednie formularze
//   function deleteElement(elementId){
//     var element = document.getElementById(elementId);
//     if (typeof(element) != 'undefined' && element != null)
//     {
//       element.remove();
//     }
//   }

//   deleteElement("button");
//   deleteElement("select");
//   deleteElement("input");

//   // tworzenie formularzy pod mapą
//   var form = document.getElementById('form');
//   var input = document.createElement("input");
//   input.id = 'input';
//   input.class = 'input';
//   input.type = 'text';
//   input.name = 'name';
//   form.appendChild(input);
  
//   var select_kategoria = document.createElement("select");
//   select_kategoria.id = "select";
//   select_kategoria.class = "select";
//   var option1 = document.createElement("option");
//   option1.text = "kategoria1";
//   var option2 = document.createElement("option");
//   option2.text = "kategoria2";
//   var option3 = document.createElement("option");
//   option3.text = "kategoria3";
//   select_kategoria.add(option1);
//   select_kategoria.add(option2);
//   select_kategoria.add(option3);
//   form.appendChild(select_kategoria);

//   var button = document.createElement("button");
//   button.id="button";
//   button.class="button";
//   button.innerHTML = "button";
//   form.appendChild(button);

//   // funkcja która sprawdza czy przycisk pod submit został klikniety
//   button.addEventListener("click", function() {    
//     var text = input.value;
//     var kategoria = select_kategoria.value;
    
//     // usuń formularz
//     deleteElement("button");
//     deleteElement("select");
//     deleteElement("input");

//     if(text.length > 0) dodaj_marker(x, y, text, kategoria);
//     else alert("brak nazwy");
//   });
// };

// // potencjalne problemy:
// // - przy większej ilości markerów mapa sie zacina (jesli obnizymy jakość i wielkość obrazków laguje mniej)

