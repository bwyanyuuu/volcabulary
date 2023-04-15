$(document).ready(function(){
    var new_cnt = 1;
    var isEditColumn = false;
    $(".btn-addColumn").click(function(){
        console.log("btn-addColumn");
        $("tbody").append(`
            <tr>
                <th scope="row"><button type="button" class="btn btn-danger btn-rmvColumn">刪除</button></th>
                <td></td>
                <td><input type="text" name="new-cixing"></td>
                <td><input type="text" name="new-mean"></td>
            </tr>
        `);
        new_cnt += 1;
    });
    $("#test-appear").click(function(){
        $("#test-explain").show();
        // $(this).hide();
    });
    $(function() {
        $('#select-options').change(function() {
          $('#select-form').submit();
        });
    });
    $(".view-editColumn").click(function(){
        console.log("view-editColumn");
        if(!isEditColumn){
            // $(".edit").each(function() {
            //     $(this).removeClass("hidden");
            // });
            // $(".view-deleteColumn").show();
            // $(".view-addColumn").show();
            $(this).text("取消管理");
            $("#edit-form").addClass("editing-form");
            isEditColumn = true;
        }
        else{
            // $(".edit").each(function() {
            //     $(this).addClass("hidden");
            // });
            $(this).text("管理");
            // $(".view-deleteColumn").hide();
            // $(".view-addColumn").hide();
            $("#edit-form").removeClass("editing-form");
            isEditColumn = false;
        }        
    });
    $(".view-edit").click(function(){
        var c = $(this).parent("td").siblings("td");
        c.eq(0).html('<input type="text" name="word" value="' + c.eq(0).text() + '">');
        c.eq(1).html('<input type="text" name="cixing" value="' + c.eq(1).text() + '">');
        c.eq(2).html('<input type="text" name="explain" value="' + c.eq(2).text() + '">');
        $(this).parent("td").siblings("th").first().children("input").prop('checked', true);
        $(this).siblings(".view-edited").show();
        $(this).hide();
    });
    $(".view-addColumn").click(function(){
        $("#edit-form tbody").append(`
            <tr>
                <th class="edit-only"></th>
                <td><input type="text" name="new-word"></td>
                <td><input type="text" name="new-cixing"></td>
                <td><input type="text" name="new-explain"></td>
                <td class="edit-only">
                    <button type="button" class="btn btn-danger btn-rmvColumn">刪除</button>
                </td>
            </tr>
        `)
    });
    $(".view-deleteList").click(function(){
        
        if (confirm("這個動作將會刪除本單字表裡的所有內容，你確定意繼續嗎？")) {
            // 如果使用者點擊確定，則提交表單
            $("#edit-form").submit()
        }
        else {
        // 如果使用者點擊取消，則不提交表單
            // e.preventDefault();
            return false;
        }
    });
    // $('#edit-form').submit(function(event) {
    //     // Prevent default form submission action
    //     event.preventDefault();

    //     // Serialize form data into JSON format
    //     var formData = $(this).serialize();
    //     console.log(formData);

    //     // Send Ajax POST request to server
    //     $.ajax({
    //         url: '/view',
    //         type: 'POST',
    //         data: formData,
    //         dataType: 'json',
    //         success: function(data) {
    //             if(data.action == "delete"){
    //                 for(var i= 0; i < data.idxs.count; i++){
    //                     $("input[name='idx', value='"+ data.idxs[i] + "']").parent("tr").delete();
    //                 }                    
    //             }
                
    //         },
    //         error: function(xhr, status, error) {
    //             // Display error message if request fails
    //             console.log(xhr.responseText);
    //         }
    //     });
    // });
  });
$(document).on("click", ".btn-rmvColumn", function(){
    // console.log("btn-rmvColumn");
    $(this).closest("tr").remove();
});
$(document).on("click", ".view-addRemove", function(){
    // console.log("btn-rmvColumn");
    $(this).closest("tr").remove();
});