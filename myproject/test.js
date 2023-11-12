<script>

let Okteto = new URL('https://useritem-api-service-skemil.cloud.okteto.net/');

function getReviews() {


    let request = new XMLHttpRequest();

    // Define a function (set of operations) to get restaurant information.
    // Creates a variable that will take the URL from above and makes sure it displays as a string. 
    // We then add the word 'restaurant" so the API endpoint becomes https://x715-fe9c-6426.n7.xano.io/api:Iw1iInWB/restaurant
    let url = Okteto.toString() + 'reviews/'; // Fix: Change xanoUrl to Okteto

    // Remember the 'request' was defined above as the standard way to access an API in Javascript.
    // GET is the verb we're using to GET data from Xano
    request.open('GET', url, true)

    // When the 'request' or API request loads, do the following...
    request.onload = function() {

        // Store what we get back from the Xano API as a variable called 'data' and converts it to a javascript object
        let data = JSON.parse(this.response)

        // Status 200 = Success. Status 400 = Problem.  This says if it's successful and no problems, then execute 
        if (request.status >= 200 && request.status < 400) {

            // Map a variable called cardContainer to the Webflow element called "Cards-Container"
            const cardContainer = document.getElementById("review-container")

            // This is called a For Loop. This goes through each object being passed back from the Xano API and does something.
            // Specifically, it says "For every element in Data (response from API), call each individual item restaurant"
            data.forEach(review => {

                // For each restaurant, create a div called card and style with the "Sample Card" class
                const style = document.getElementById('samplestyle')
                // Copy the card and it's style
                const card = style.cloneNode(true)

                card.setAttribute('id', '');
                card.style.display = 'block';

                // For each restaurant, Create an image and use the restaurant image coming from the API
                //const img = card.getElementsByTagName('IMG')[0]
                //img.src = restaurant.banner.url + "?tpl=big:box"; // using Xano's template engine to re-size the pictures down and make them a box

                // For each restaurant, create an h3 and set the text content to the restaurant's title
                const h3 = card.getElementsByTagName('H3')[0]
                h3.textContent = review.owner_id;

                // For each restaurant, create an paragraph and set the text content to the restaurant's description
                const p = card.getElementsByTagName('P')[0]
                p.textContent = `${review.description.substring(0, 240)}` // Limit to 240 chars

                // Place the card into the div "Cards-Container" 
                cardContainer.appendChild(card);
            })
        }
    }

    // Send Restaurant request to API
    request.send();
}

// This fires all of the defined functions when the document is "ready" or loaded
(function() {
    getReviews();
})();

</script>
