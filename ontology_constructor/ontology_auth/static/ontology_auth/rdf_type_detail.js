window.onload = function() {
    make_readonly();
  }
function make_readonly()
{
    
    var idname = document.getElementById("id_name");
    var idaccess = document.getElementById("id_description");
    var idontology = document.getElementById("id_ontology");
    var idsubject = document.getElementById("id_subject");
    var idobject = document.getElementById("id_object");
    var subm = document.getElementById("subm");
    var edit = document.getElementById("edit");
    subm.style.display = 'none';
    edit.style.display = 'block';
    idname.disabled = true;
    idaccess.disabled = true;
    idontology.disabled = true;
    idsubject.disabled = true;
    idobject.disabled = true;
}
function edited()
{
    var idname = document.getElementById("id_name");
    var idaccess = document.getElementById("id_description");
    var idontology = document.getElementById("id_ontology");
    var idsubject = document.getElementById("id_subject");
    var idobject = document.getElementById("id_object");
    var subm = document.getElementById("subm");
    var edit = document.getElementById("edit");
    subm.style.display = 'block';
    edit.style.display = 'none';
    idname.disabled = false;
    idaccess.disabled = false;
    idontology.disabled = false;
    idsubject.disabled = false;
    idobject.disabled = false;
}