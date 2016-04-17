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
                       alert("Some thing went wrong,Please Try after sometime");                    }

                }
            });
    }

    }



