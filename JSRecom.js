var typeShow;
var typeGenre;

    document.getElementById('myDropdown').addEventListener('change', function() 
    {
        typeGenre = this.value;
    });

    document.getElementById('myDropdown2').addEventListener('change', function() 
    {
        typeShow = this.value;
    });

function getShow()
{  
    let genreId;

    // Reset the image container
    document.getElementById("imageContainer").innerHTML = "";


    if (typeShow === "movie")
    {
        switch (typeGenre) {
        case "Crime":
        genreId = 80;
            break;
        case "Romance":
        genreId = 10749;
            break;
        case "Comedy":
        genreId = 35;
            break;
        case "Mystery":
        genreId = 9648;
            break;
        case "Science Fiction":
        genreId = 878;
            break;
        case "Action":
        genreId = 28;
            break;
        }
    }else{
        switch (typeGenre) {
        case "Crime":
        genreId = 80;
            break;
        case "Romance":
        genreId = 10749;
            break;
        case "Comedy":
        genreId = 35;
            break;
        case "Mystery":
        genreId = 9648;
            break;
        case "Science Fiction":
        genreId = 10765;
            break;
        case "Action":
        genreId = 10759;
            break;
        }
    }  

    fetch("https://api.themoviedb.org/3/discover/"+typeShow+"?api_key=8569488978d7c948011c66a22ea99ff0&with_genres="+genreId)
        .then( (response) => response.json())
        .then( (data) => parseShow(data))
        .catch( (error) => console.log(error))
    }

    function parseShow(json)
    {
    const baseImageUrl = "https://image.tmdb.org/t/p/w500";
    const results = json.results;

    for (let i = 0; i < results.length; i++) 
    {

        let movieImage = baseImageUrl + results[i].poster_path;

        // Create a container div for each movie
        let containerDiv = document.createElement("div");
        containerDiv.className = "movie-container";  // Optional: add a class for styling

        // Create an img element
        let imgElement = document.createElement("img");
        imgElement.src = movieImage;
        imgElement.alt = "Movie Poster " + (i + 1);
        imgElement.id = "showImg" + (i + 1);

        // Create a p element for the movie name
        let nameElement = document.createElement("p");
        nameElement.className = "movie-name";  // Optional: add a class for styling
        if (typeShow === "movie") nameElement.innerText = results[i].title;  // Use results[i].name for TV shows
        else nameElement.innerText = results[i].original_name; 


        // Append the img and name elements to the container div
        containerDiv.appendChild(imgElement);
        containerDiv.appendChild(nameElement);

        // Append the container div to the image container
        document.getElementById("imageContainer").appendChild(containerDiv);
    }
    // Reset dropdowns after processing
    document.getElementById('myDropdown').selectedIndex = 0;
    document.getElementById('myDropdown2').selectedIndex = 0;
}