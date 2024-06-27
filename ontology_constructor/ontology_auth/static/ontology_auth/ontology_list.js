function delete_ontology(){
    location.href="{% url 'delete_ontology/' object.id %}";
}
function subject_list_func() { 
    let but_sub = document.getElementById("subject_list_but");
    let but_ont = document.getElementById("ontology_list_but");
    let but_obj = document.getElementById("object_list_but");
    let element = document.getElementById("subject_list");
    let element1 = document.getElementById("ontology_list");
    let element2 = document.getElementById("object_list");
    element.style.display = 'block';
    element1.style.display = 'none'; 
    element2.style.display = 'none'; 
    but_sub.style.color='#828282';
    but_ont.style.color='black';
    but_obj.style.color='black';
}
function ontology_list_func() { 
    let but_ont = document.getElementById("ontology_list_but");
    let but_sub = document.getElementById("subject_list_but");
    let but_obj = document.getElementById("object_list_but");
    let element = document.getElementById("subject_list");
    let element1 = document.getElementById("ontology_list");
    let element2 = document.getElementById("object_list");
    element.style.display = 'none';
    element1.style.display = 'block';
    element2.style.display = 'none';
    but_ont.style.color='#828282';
    but_sub.style.color='black'; 
    but_obj.style.color='black'; 
    
}
function object_list_func() { 
    let but_ont = document.getElementById("ontology_list_but");
    let but_sub = document.getElementById("subject_list_but");
    let but_obj = document.getElementById("object_list_but");
    let element = document.getElementById("subject_list");
    let element1 = document.getElementById("ontology_list");
    let element2 = document.getElementById("object_list");
    element.style.display = 'none';
    element1.style.display = 'none';
    element2.style.display = 'block';
    but_ont.style.color='balck';
    but_sub.style.color='black'; 
    but_obj.style.color='#828282'; 
    
}
function clicker() {
    document.getElementsByClassName('table-2')[0].style.display = "none"
  }
