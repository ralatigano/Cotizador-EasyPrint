let dataTable;
let dataTableIsInitilized=false;

const initDataTable=async() => {
    if(dataTableIsInitilized){
        dataTable.destroy();
    }
    dataTable=$("#Pedidos").DataTable({
        language: {
            lengthMenu: 'Mostrar _MENU_ pedidos por página',
            zeroRecords: 'No hay pedidos registrados',
            info: 'Mostrando de _START_ a _END_ de _TOTAL_ pedidos',
            infoEmpty: 'No hay pedidos',
            InfoFiltered: '(filtrado de _MAX_ pedidos totales)',
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
    document.getElementById("nav_item_pedidos").style.fontWeight = "bold";
});


const cambiarEstadoModal = document.getElementById('cambiarEstadoModal')
cambiarEstadoModal.addEventListener('show.bs.modal', event => {
  // Button that triggered the modal
  const button = event.relatedTarget
  // Extract info from data-bs-* attributes
  const recipient = button.getAttribute('data-bs-whatever')
  // If necessary, you could initiate an AJAX request here
  // and then do the updating in a callback.
  //
  // Update the modal's content.
  const modalTitle = cambiarEstadoModal.querySelector('.modal-title-estado')
  const modalBodyInput = cambiarEstadoModal.querySelector('.modal-body input')
  const modalPedidoInput = cambiarEstadoModal.querySelector('.cambiarPedido_estado')

  modalTitle.textContent = `Nuevo estado para el pedido: ${recipient}`
  modalBodyInput.value = recipient
});

const cambiarEncargadoModal = document.getElementById('cambiarEncargadoModal')
cambiarEncargadoModal.addEventListener('show.bs.modal', event => {
  const button = event.relatedTarget
  const recipient = button.getAttribute('data-bs-whatever')
  const modalTitle = cambiarEncargadoModal.querySelector('.modal-title-enc')
  const modalBodyInput = cambiarEncargadoModal.querySelector('.modal-body input')
  const modalPedidoInput = cambiarEncargadoModal.querySelector('.cambiarPedido_enc')

  modalTitle.textContent = `Nuevo encargado para el pedido: ${recipient}`
  modalBodyInput.value = recipient
});

const agregarDescripcionModal = document.getElementById('agregarDescripcionModal')
agregarDescripcionModal.addEventListener('show.bs.modal', event => {
  const button = event.relatedTarget
  const recipient = button.getAttribute('data-bs-whatever')
  const modalTitle = agregarDescripcionModal.querySelector('.modal-title-desc')
  const modalBodyInput = agregarDescripcionModal.querySelector('.modal-body input')
  const modalPedidoInput = agregarDescripcionModal.querySelector('.cambiarPedido_desc')

  modalTitle.textContent = `Nueva anotación para el pedido: ${recipient}`
  modalBodyInput.value = recipient
});

const agregarSeniaModal = document.getElementById('agregarSeniaModal')
agregarSeniaModal.addEventListener('show.bs.modal', event => {
  const button = event.relatedTarget
  const recipient = button.getAttribute('data-bs-whatever')
  const modalTitle = agregarSeniaModal.querySelector('.modal-title-senia')
  const modalBodyInput = agregarSeniaModal.querySelector('.modal-body input')
  const modalPedidoInput = agregarSeniaModal.querySelector('.cambiarPedido_senia')

  modalTitle.textContent = `Agregar seña para el pedido: ${recipient}`
  modalBodyInput.value = recipient
})
