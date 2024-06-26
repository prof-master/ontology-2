function delete_ontology(){
    location.href="{% url 'delete_ontology/' object.id %}";
}