window.onload = function() {
    my_ontology_list_func();
  }
function delete_ontology(){
    location.href="{% url 'delete_ontology/' object.id %}";
}
function del_sub(subject_id)
{
    window.location = '/delete_subject/'+subject_id;
}
function subject_list_func() { 
    let but_sub = document.getElementById("subject_list_but");
    let but_my_ont = document.getElementById("my_ontology_list_but");
    let but_gl_ont = document.getElementById("gl_ontology_list_but");
    let but_obj = document.getElementById("object_list_but");
    let element = document.getElementById("subject_list");
    let element1 = document.getElementById("my_ontology_list");
    let element2 = document.getElementById("object_list");
    let element3 = document.getElementById("gl_ontology_list");
    element.style.display = 'block';
    element1.style.display = 'none'; 
    element2.style.display = 'none'; 
    element3.style.display = 'none'; 
    but_sub.style.color='#828282';
    but_my_ont.style.color='black';
    but_gl_ont.style.color='black';
    but_obj.style.color='black';
}
function my_ontology_list_func() { 
    let but_my_ont = document.getElementById("my_ontology_list_but");
    let but_gl_ont = document.getElementById("gl_ontology_list_but");
    let but_sub = document.getElementById("subject_list_but");
    let but_obj = document.getElementById("object_list_but");
    let element = document.getElementById("subject_list");
    let element1 = document.getElementById("my_ontology_list");
    let element2 = document.getElementById("object_list");
    let element3 = document.getElementById("gl_ontology_list");
    element.style.display = 'none';
    element1.style.display = 'block';
    element2.style.display = 'none';
    element3.style.display = 'none';
    but_my_ont.style.color='#828282';
    but_gl_ont.style.color='black';
    but_sub.style.color='black'; 
    but_obj.style.color='black'; 
    
}
function object_list_func() { 
    let but_my_ont = document.getElementById("my_ontology_list_but");
    let but_gl_ont = document.getElementById("gl_ontology_list_but");
    let but_sub = document.getElementById("subject_list_but");
    let but_obj = document.getElementById("object_list_but");
    let element = document.getElementById("subject_list");
    let element1 = document.getElementById("my_ontology_list");
    let element2 = document.getElementById("object_list");
    let element3 = document.getElementById("gl_ontology_list");
    element.style.display = 'none';
    element1.style.display = 'none';
    element2.style.display = 'block';
    element3.style.display = 'none';
    but_my_ont.style.color='balck';
    but_gl_ont.style.color='balck';
    but_sub.style.color='black'; 
    but_obj.style.color='#828282'; 
    
}
function gl_ontology_list_func() { 
    let but_my_ont = document.getElementById("my_ontology_list_but");
    let but_gl_ont = document.getElementById("gl_ontology_list_but");
    let but_sub = document.getElementById("subject_list_but");
    let but_obj = document.getElementById("object_list_but");
    let element = document.getElementById("subject_list");
    let element1 = document.getElementById("my_ontology_list");
    let element2 = document.getElementById("object_list");
    let element3 = document.getElementById("gl_ontology_list");
    element.style.display = 'none';
    element1.style.display = 'none';
    element2.style.display = 'none';
    element3.style.display = 'block';
    but_my_ont.style.color='black';
    but_gl_ont.style.color='#828282';
    but_sub.style.color='black'; 
    but_obj.style.color='black'; 
    
}
function clicker() {
    document.getElementsByClassName('table-2')[0].style.display = "none"
  }

function sub_click()
{
    window.location.href='/subject/' + String(subject_id); 
}
