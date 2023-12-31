$(document).ready(function(){
    let base64Image;
    $("#image-selector").change(function(){
        let reader = new FileReader();
        reader.onload = function(e){
            let dataURL = reader.result;
            $("#selected-image").attr("src", dataURL)
            base64Image = dataURL.replace("data:image/jpeg;base64,", "");
            console.log(base64Image);
        }
        reader.readAsDataURL($("#image-selector")[0].files[0]);
        $("#dog-prediction").text("");
        $("#cat-prediction").text("");
    })
    $("#predict-button").click(function(event){
        let message = {
            image: base64Image
        }
        console.log(message);
        $.post("/predict", JSON.stringify(message), function(response){
            console.log(response);
            $("#dog-prediction").text(response.prediction.dog.toFixed(2));
            $("#cat-prediction").text(response.prediction.cat.toFixed(2));
            console.log(response)
        })
    })

});