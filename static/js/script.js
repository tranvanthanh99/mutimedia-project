$(document).ready(function () {

    $('#submit-form').submit(function (e) {
        e.preventDefault()
        var formData = new FormData(this);

        if (document.getElementById("fileUpload").files.length == 0) alert("please upload an image!!!")
        else {
            // Object.assign(formData, { algo: $("select").val()})
            console.log(formData)

            $("#output-img").attr("src", "../static/img/spinner.gif")
            $.ajax({
                url: window.location.pathname,
                type: 'POST',
                data: formData,
                headers: { Algo: $("select").val() },
                success: function (data) {
                    $("#output-img").attr("src", `data:image/${data.file_type};base64, ${data.src}`)
                },
                cache: false,
                contentType: false,
                processData: false
            });
        }

    })

    $("#fileUpload").on('change', function () {

        //Get count of selected files
        var countFiles = $(this)[0].files.length;

        var imgPath = $(this)[0].value;
        var extn = imgPath.substring(imgPath.lastIndexOf('.') + 1).toLowerCase();
        // var image_holder = $("#image-holder");
        // image_holder.empty();

        if (extn == "gif" || extn == "png" || extn == "jpg" || extn == "jpeg") {
            if (typeof (FileReader) != "undefined") {

                //loop for each file selected for uploaded.
                for (var i = 0; i < countFiles; i++) {

                    var reader = new FileReader();
                    reader.onload = function (e) {
                        // $("<img />", {
                        //     "src": e.target.result,
                        //     "class": "thumb-image materialboxed"
                        // }).appendTo(image_holder);
                        $("#upload-img").attr("src", e.target.result)
                    }

                    // image_holder.show();
                    reader.readAsDataURL($(this)[0].files[i]);
                }
            } else {
                alert("This browser does not support FileReader.");
            }
        } else {
            alert("Pls select only images");
        }
    });

    // $('.materialboxed').materialbox();
    M.AutoInit()
})