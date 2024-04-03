/* Configuraciones de los select2 */
$(function (){
    $("#sidebarToggler").click();
    $("#producto").select2({
        theme: "classic",
        placeholder: "primero selecciona una categoría",
        allowClear: true
    });
    $("#categoria").select2({
        theme: "classic",
        placeholder: "Selecciona una categoría",
        allowClear: true
    });
    $("#producto").val("{{obj.producto.nombre}}").change();
    $("#categoria").val("{{obj.categoria.nombre}}").change();
    $("#producto").chained("#categoria");
});