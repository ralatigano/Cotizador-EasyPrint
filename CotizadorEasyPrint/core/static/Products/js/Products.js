
let dataTable;
let dataTableIsInitilized=false;

const initDataTable=async() => {
    if(dataTableIsInitilized){
        dataTable.destroy();
    }
    dataTable=$("#Productos").DataTable({
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
}

window.addEventListener("load", async() => {
     await initDataTable();
     document.getElementById("nav_item_productos").style.fontWeight = "bold";
});

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


const editarProductoModal = document.getElementById('editarProductoModal')
editarProductoModal.addEventListener('show.bs.modal', event => {
  //botón que lanza el modal
  const button = event.relatedTarget
  //obtengo el código del producto y su nombre para mostrarlo en el modal
  const recipient = button.getAttribute('data-bs-whatever')
  console.log(recipient);
  var partes = recipient.split('|');
  const codigo = partes[0];
  const nombre = partes[1];
  const ancho = partes[2];
  const alto = partes[3];
  const precio = partes[4];
  const categoria = partes[5];
  const caso_part = partes[6];
  //cambio el texto del título del modal
  const modalTitle = editarProductoModal.querySelector('.modal-title-prod')
  modalTitle.textContent = `Editar producto: ${codigo + ' ' + nombre}`

  var tooltipTriggerList = [].slice.call(document.querySelectorAll('[data-bs-toggle="tooltip"]'))
  var tooltipList = tooltipTriggerList.map(function (tooltipTriggerEl) {
    return new bootstrap.Tooltip(tooltipTriggerEl)
  });


  $("#codigo").val(codigo);
  $("#nombre").val(nombre);
  $("#ancho").val(ancho);
  $("#alto").val(alto);
  $("#precio").val(precio);
  $("#categ").val(categoria);
  if (caso_part === 'True') {
    $('#caso_part').prop('checked', true);
  } else {
    $('#caso_part').prop('checked', false);
  }

});

const agregarProductoModal = document.getElementById('agregarProductoModal')
agregarProductoModal.addEventListener('show.bs.modal', event => {
  const button = event.relatedTarget
  const modalTitle = agregarProductoModal.querySelector('.modal-title-add')

  modalTitle.textContent = `Agregar un nuevo producto`
  
  var tooltipTriggerList = [].slice.call(document.querySelectorAll('[data-bs-toggle="tooltip"]'))
  var tooltipList = tooltipTriggerList.map(function (tooltipTriggerEl) {
    return new bootstrap.Tooltip(tooltipTriggerEl)
  });


});

