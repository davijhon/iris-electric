$(function () {
   $('#dataSubEstacion').DataTable({
       responsive: true,
       autoWidth: false,
       destroy: true,
       deferRender: true,
       ajax: {
           url: window.location.pathname,
           type: 'POST',
           data: {
               'action': 'search_subestacion'
           },
           dataSrc: "",
       },
       columns: [
           {"data": "regional.nombre"},
           {"data": "nombre"},
           {"data": "capacidad"},
           {"data": "name"},
       ],
       columnDefs: [
        { "width": "10%", "targets": 0 },
           {
               targets: [-1],
               class: 'text-center',
               orderable: false,
               render: function (data, type, row) {
                var buttons = '<a href="/subestacion/edit-subestacion/' + row.id + '/" class="btn btn-success btn-xs btn-flat"><i class="fas fa-edit"></i></a> ';

                return buttons;
               }
           },
       ],
       initComplete: function (settings, json) {

       },
   });

});