$(document).ready(function () 
{ 
    var btn = $("#zaButton");
    var text = $('#username');
    var check = $('#permit');

    btn.on('click', function () 
    { 
        if (!text.val() || check.prop("checked") !==true){
            alert("All required fields cannot be empty");
            return false;
        }
        else {
            btn.removeClass("inputtop").addClass("disabled");
            btn.html('Generating your WordCloud...');
            setTimeout(function() {
                    btn.attr('disabled', true); 
                    }, 500);
        }
    }); 
});
var modal = document.getElementById('id01');
    window.onclick = function(event) {
      if (event.target == modal) {
        modal.style.display = "none";
      }
    }