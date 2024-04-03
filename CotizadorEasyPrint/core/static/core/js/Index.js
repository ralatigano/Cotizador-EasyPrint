

/* Funcionalidad para evitar la eliminación de objetos listados en la cotización por un click involuntario. */
(function () {
    const btnEliminacion = document.querySelectorAll(".btnEliminacion");
    btnEliminacion.forEach(btn=>{
        btn.addEventListener("click", (e)=>{
            const confirmacion = confirm("¿Está segur@ de que desea eliminar este elemento?");
            if(!confirmacion){
                e.preventDefault();
            }    
        });
    });
})();



let dataTable;
let dataTableIsInitilized=false;
const initDataTable=async() => {
    if(dataTableIsInitilized){
        dataTable.destroy();
    }
    dataTable=$("#NuevoPresupuesto").DataTable({
        language: {
            lengthMenu: 'Mostrar _MENU_ productos por página',
            zeroRecords: 'No hay productos registrados',
            info: 'Mostrando de _START_ a _END_ de _TOTAL_ productos',
            infoEmpty: 'No hay productos',
            InfoFiltered: '(filtrado de _MAX_ productos totales)',
            search: 'Buscar:',
            LoadingRecords: 'Cargando...',
            paginate: {
                first: 'Primero',
                last: 'Ultimo',
                next: 'Siguiente',
                previous: 'Anterior'
            }
        }
    });
    dataTableIsInitilized=true;
    dataTable.on('draw.dt', function() {
        footerCallback(null, dataTable.data(), 0, dataTable.data().length, {});
    });


};


window.addEventListener("load", async() => {
    await initDataTable();
    document.getElementById("nav_item_inicio").style.fontWeight = "bold";
});