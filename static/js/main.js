/**
 * Created by ambika on 4/17/16.
 */

function deletecat(cat) {
    result= confirm("Are you sure to delete this tag ?")
    if(result){
             $.ajax({
                type: "GET",
                //data: cat_id,
                url: "delete/"+cat+"/",
                cache: false,
                success: function(d) {
                    if (d == 'success') {
                            window.location.href = "/category/";
                        }
                    else {
                       alert("Some thing went wrong,Please Try after sometime");
                    }

                }
            });
    }

    }

function deleteques(ques) {
    result= confirm("Are you sure to delete this question ?")
    if(result){
             $.ajax({
                type: "GET",
                //data: cat_id,
                url: "/question/delete/"+ques+"/",
                cache: false,
                success: function(d) {
                    if (d == 'success') {
                            window.location.href = "/";
                        }
                    else {
                       alert("Some thing went wrong,Please Try after sometime");
                    }

                }
            });
    }

    }

$(".select").change(function(){
    questype=$('#questype').val()
    usercategory=$("#usercategory").val()
    window.location.href="/?questype="+questype +"&usercategory="+usercategory

});

