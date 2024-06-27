function delete_ontology(){
    location.href="{% url 'delete_ontology/' object.id %}";
}
function subject_list() { 
    let element = document.getElementById("subject_list");
    let element1 = document.getElementById("ontology_list");
    element.style.display = 'block';
    element1.style.display = 'none'; 
}
function clicker() {
    let element = document.getElementById("click_subject");
    element.css('background', 'grey');
  }
