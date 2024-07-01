window.onload = function() {
    make_readonly();
  }
function make_readonly()
{
    
    var idname = document.getElementById("id_name");
    var idaccess = document.getElementById("id_access");
    var subm = document.getElementById("subm");
    var edit = document.getElementById("edit");
    subm.style.display = 'none';
    if (edit)
        edit.style.display = 'block';
    idname.disabled = true;
    idaccess.disabled = true;
}
function edited()
{
    var idname = document.getElementById("id_name");
    var idaccess = document.getElementById("id_access");
    var subm = document.getElementById("subm");
    var edit = document.getElementById("edit");
    subm.style.display = 'block';
    if (edit)
        edit.style.display = 'none';
    idname.disabled = false;
    idaccess.disabled = false;
}
