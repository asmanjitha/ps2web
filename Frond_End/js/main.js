$(function () {
  $.ajax({
    type: "GET",
    url: "http://127.0.0.1:5000/images/mobile",
    success: function (data) {
      var dataArr = JSON.parse(data);
      var imageName = [];
      var source = [];

      for (i = 0; i < dataArr.length; i++) {
        imageName.push(dataArr[i].split(" ").join(""));

        source.push("http://127.0.0.1:5000/static/mobile/" + imageName[i]);
      }

      for (var k = 0; k < dataArr.length; k++) {
        console.log(k)
        $( "#pics" ).append(' <div class="col-lg-3 col-md-4 col-6 zoom edit-image"><a href="#" class="d-block mb-4 h-100"><img class="img-fluid img-thumbnail" src='+source[k]+'></a><input data-toggle="modal" data-target="#exampleModal" class="update btn btn-primary btn-sm" type="button" value="Update" /><input class="delete btn btn-danger btn-sm" type="button" value="Delete" /></div>');  
      }
    },
  });
});


//Update

// $(document).ready(function(){
//   $("#updateChanges").click(function(){
//     alert("The button was clicked.");

//       $.ajax({
//           type: "PUT",
//           url: 'http://localhost:5000/updateimage?replacefilename="travel1.jpg"', 

//           success: function(response){
//             console.log("data Here");
            
//             var jsonData = JSON.parse(response);
//             console.log(jsonData);

//           },
//           error: function(error){
//            alert(error);
//           }
//       });
//   });
// });


// Upload 
$(document).ready(function(){

  $("#btn_upload").click(function(){

      var fd = new FormData();
      var files = $('#file')[0].files[0];
      fd.append('file',files);

      $.ajax({
          url: 'http://localhost:5000/updateimage?replacefilename='+fd+'"',
          type: 'POST',
          data: fd,
          contentType: false,
          processData: false,
          success: function(response){
              if(response != 0){
                alert("ok")
                  $("#img").attr("src",response); 
                  $(".preview img").show(); // Display image element
              }else{
                  alert('file not uploaded');
              }
          },
      });
  });
});