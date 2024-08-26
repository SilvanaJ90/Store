const d = document,
  $title = d.querySelector("#crud-title");

let app = {
    backend: 'http://127.0.0.1:8000/api/v1',
    table: null,
    init: function() {
        app.initDatatable('#categories');

        $("#save").click(function() {
            app.save({
                name: $('#name').val(),
                description: $('#description').val()
            });
        });

        $("#save_put").click(function() {
            app.save_put({
                id: $('#id_put').val(),
                name: $('#name_put').val(),
                description: $('#description_put').val()
            });
        });
    },
    initDatatable: function(id) {
        app.table = $(id).DataTable({
            language: {
                "decimal": "",
                "emptyTable": "No hay información",
                "info": "Mostrando _START_ a _END_ de _TOTAL_ Entradas",
                "infoEmpty": "Mostrando 0 a 0 de 0 Entradas",
                "infoFiltered": "(Filtrado de _MAX_ entradas totales)",
                "lengthMenu": "Mostrar _MENU_ Entradas",
                "loadingRecords": "Cargando...",
                "processing": "Procesando...",
                "search": "Buscar:",
                "zeroRecords": "Sin resultados encontrados",
                "paginate": {
                    "first": "Primero",
                    "last": "Último",
                    "next": "Siguiente",
                    "previous": "Anterior"
                }
            },
            ajax: {
                url: app.backend + '/categories/',
                dataSrc: ''
            },
            dom: 'Bfrtip',
            columns: [
                {
                    data: null,
                    render: function (data, type, full, meta) {
                        return meta.row + 1;
                    }
                },
                { data: 'name' },
                { data: 'description' }
            ],
            buttons: [
                {
                    text: '<i class="fa-solid fa-chevron-left"></i>',
                    action: function() {
                        location.href = "admin";
                    }
                },
                {
                    text: '<i class="fa-solid fa-align-justify"></i>',
                    action: function(e, dt) {
                        let data = dt.rows('.table-active').data()[0];
                        app.setDataToModal(data);
                        app.load_products(data.id);
                    }
                },
                {
                    text: '<i class="fa-solid fa-plus"></i>',
                    action: function() {
                        app.cleanForm();
                        $('#categorieModal').modal();
                    }
                },
                {
                    text: '<i class="fa-solid fa-trash-can"></i>',
                    action: function(e, dt) {
                        let data = dt.rows('.table-active').data()[0];
                        swal({
                            title: "¿Estás seguro de que deseas eliminar la categoría?",
                            icon: "warning",
                            buttons: true,
                            dangerMode: true
                        }).then((willDelete) => {
                            if (willDelete) {
                                app.delete(data.id);
                                swal('Eliminado exitosamente', '', 'success');
                            }
                        });
                    }
                },
                {
                    text: '<i class="fa-solid fa-pencil"></i>',
                    action: function(e, dt) {
                        let data = dt.rows('.table-active').data()[0];
                        app.setDataToModalPut(data);
                        $('#categoriePutModal').modal();
                    }
                }
            ]
        });

        $('#categories tbody').on('click', 'tr', function() {
            $(this).toggleClass('table-active').siblings().removeClass('table-active');
        });
    },
    setDataToModal: function(data) {
        $('#name').val(data.name);
        $('#description').val(data.description);
    },
    setDataToModalPut: function(data) {
        $('#id_put').val(data.id);
        $('#name_put').val(data.name);
        $('#description_put').val(data.description);
    },
    cleanForm: function() {
        $('#name').val('');
        $('#description').val('');
    },
    save: function(data) {
        $.ajax({
            url: app.backend + '/categories/',
            data: JSON.stringify(data),
            method: 'POST',
            dataType: 'json',
            contentType: "application/json; charset=utf-8",
            success: function() {
                $("#msg").css({
                    "color": "#000",
                    "background-color": "#97fcb0",
                    "border": "#000 solid 1px"
                }).text('Se guardó la categoría correctamente').show();
                $('#categorieModal').modal('hide');
                app.table.ajax.reload();
            },
            error: function() {
                $("#msg").css({
                    "color": "#000",
                    "background-color": "#fc97a4",
                    "border": "#000 solid 1px"
                }).text('(ERROR) Excede el número de caracteres permitidos').show();
            }
        });
    },
    save_put: function(data) {
        $.ajax({
            url: app.backend + '/categories/' + data.id,
            data: JSON.stringify(data),
            method: 'PUT',
            dataType: 'json',
            contentType: "application/json; charset=utf-8",
            success: function() {
                $("#msg").css({
                    "color": "#000",
                    "background-color": "#97fcb0",
                    "border": "#000 solid 1px"
                }).text('La categoría se actualizó correctamente').show();
                $('#categoriePutModal').modal('hide');
                app.table.ajax.reload();
            },
            error: function() {
                $("#msg").css({
                    "color": "#fff",
                    "background-color": "#ff4d4d",
                    "border": "#000 solid 1px"
                }).text('Error al actualizar la categoría').show();
            }
        });
    },
    delete: function(id) {
        $.ajax({
            url: app.backend + '/categories/' + id,
            method: 'DELETE',
            dataType: 'json',
            contentType: "application/json; charset=utf-8",
            success: function() {
                $("#msg").css({
                    "color": "#000",
                    "background-color": "#97fcb0",
                    "border": "#000 solid 1px"
                }).text('Se eliminó la categoría correctamente').show();
                app.table.ajax.reload();
            },
            error: function() {
                $("#msg").css({
                    "color": "#000",
                    "background-color": "#fc97a4",
                    "border": "#000 solid 1px"
                }).text('Error al eliminar la categoría').show();
            }
        });
    },
    load_products : function(id) {
        $.ajax({
            url: app.backend + '/categories/' + id + '/',
            method: 'GET',
            dataType : 'json',
            contentType: "application/json; charset=utf-8",
            success : function(data) {
                window.location.href = 'products?category_id=' + id;
            },
            error : function(error) {
                $("#msg").text('Error al cargar productos');
                $("#msg").show();
            }
        });
    }
};

$(document).ready(function() {
    app.init();
});

