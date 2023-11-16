function connect(){
    url = "";
    fetch(url)
    .then(function(response){
        return response.json();
    })
    .catch(function(error){
        console.log("Error: "+error);
    });
}