
function fetchDogs(event) {
    event.preventDefault();

    const searchTerm = document.querySelector('#searchTerm').value;
    const URL = `https://api.rescuegroups.org/v5/public/animals/search/available/${searchTerm}`;

    const API_KEY = 'Lmj5V8qG';

    const settings = {
        method : 'GET',
        headers : {
            'Authorization' : API_KEY
        }
    };

    fetch(URL, settings)
        .then(function(response){
            if(response.ok){
                return response.json();
            }
        })
        .then(function(data){
            console.log(data);
            const results = document.querySelector('.results');
            results.innerHTML = '';

            for(let i = 0; i < data.data.length; i ++){
                results.innerHTML += `
                    <div class="container">
                        <div class="animalImageContainer d-flex">
                            <div class="img">                            
                                <img src="${data.data[i].attributes.pictureThumbnailUrl} class="animalImage">
                            </div>
                            <div class="info ms-5">                            
                                <p>Age: ${data.data[i].attributes.ageString}</p>
                                <p>Qualities: ${data.data[i].attributes.qualities}</p>
                                <p><a href="${data.data[i].attributes.url}">More info</a></p>
                            </div>
                        </div>
                    <h2 class="name my-3">
                        ${data.data[i].attributes.name} | ${data.data[i].attributes.sex} | ${data.data[i].attributes.breedString}
                    </h2>

                    <p class="description">
                    <label>
                        <strong>Pet Description:</strong> 
                    </label>
                        ${data.data[i].attributes.descriptionText}
                    </p>

                    </div>
                `;
            }

        });

}


function init() {
    const dogSearch = document.querySelector('#dogSearch');
    dogSearch.addEventListener('submit', fetchDogs);
}

init();