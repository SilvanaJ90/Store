const d = document,
  $title = d.querySelector("#crud-title");

let app = {
    backend: 'http://127.0.0.1:8000/api/v1',
    table : null,
    init: function() {
        app.initDatatable('#categories');

        $("#save").click(function(){
            app.save({
                name : $('#name').val(),
                description: $('#description').val()
            });
        });
        $("#save_put").click(function(){
            app.save_put({
                id : $('#id_put').val(),
                name : $('#name_put').val(),
                description: $('#description_put').val()
            
            });
        });
    },
    initDatatable : function(id) {
        app.table = $(id).DataTable({
            language: {
                "decimal": "",
                "emptyTable": "No hay información",
                "info": "Mostrando _START_ a _END_ de _TOTAL_ Entradas",
                "infoEmpty": "Mostrando 0 to 0 of 0 Entradas",
                "infoFiltered": "(Filtrado de _MAX_ total entradas)",
                "infoPostFix": "",
                "thousands": ",",
                "lengthMenu": "Mostrar _MENU_ Entradas",
                "loadingRecords": "Cargando...",
                "processing": "Procesando...",
                "search": "Buscar:",
                "zeroRecords": "Sin resultados encontrados",
                "paginate": {
                    "first": "Primero",
                    "last": "Ultimo",
                    "next": "Siguiente",
                    "previous": "Anterior"
                }
            },
            ajax : {
                url : app.backend + '/categories/',
                dataSrc : function(json) {
                    return json;
                }
            },
            dom: 'Bfrtip',
            columns: [                     
                {
                    data : null, "render": function (data, type, full, meta) {
                        return meta.row + 1;
                    }
                },
                {data : 'name'},
                {data : 'description'}
                
            ],
            
            buttons: [

                {
                    text : '<i class="fa-solid fa-chevron-left"></i>',
                    action : function(e, dt, node, config) {
                        location.href="admin";
                    }
                },


                {
                    text : '<i class="fa-solid fa-align-justify"></i>',
                    action : function(e, dt, node, config) {
                        let data = dt.rows('.table-active').data()[0];
                        app.setDataToModal(data);
                        app.load_products(data.id);
                    }
                },

                {
                    text : '<i class="fa-solid fa-plus"></i>',
                    action : function(e, dt, node, config) {
                        app.cleanForm();
                        $('#categorieModal').modal();
                    }
                },
                {
                    text : '<i class="fa-solid fa-trash-can"></i>',
                    action : function(e, dt, node, config) {
                        let data = dt.rows('.table-active').data()[0];
                        swal({
                            title: "¿Estás seguro de que deseas eliminar la categoría?",
                            text: "",
                            icon: "warning",
                            buttons: true,
                            dangerMode: true,
                            position: 'center',
                          })
                          .then((willDelete) => {
                            if (willDelete) {
                              swal('Eliminado exitosamente', '', 'success')
                              app.delete(data.id)
                            }
                          });
                    }
                },

                {
                    text : '<i class="fa-solid fa-pencil"></i>',
                    action : function(e, dt, node, config) {
                        let data = dt.rows('.table-active').data()[0];
                        app.setDataToModalPut(data);
                        $('#categoriePutModal').modal();
                    }
                }
            ]
        });

        $('#categories tbody').on('click', 'tr', function(){
            if ($(this).hasClass('table-active')) {
                $(this).removeClass('table-active');
            } else {
                app.table.$('tr.table-active').removeClass('table-active');
                $(this).addClass('table-active');
            }
        });
    },
    setDataToModal : function(data) {
        $('#name').val(data.name);
        $('#description').val(data.description);
    },
    setDataToModalPut : function(data) {
        $('#id_put').val(data.id);
        $('#name_put').val(data.name);
        $('#description_put').val(data.description);
    },
    cleanForm: function(){
        $('#name').val('');
        $('#description').val('');
    },
    save : function(data) {
        $.ajax({
            url: app.backend + '/categories/',
            data : JSON.stringify(data),
            method: 'POST',
            dataType : 'json',
            contentType: "application/json; charset=utf-8",
            success : function(json) {
                $("#msg").css("color", "#000");
                $("#msg").css("background-color", "#97fcb0");
                $("#msg").css("border", "#000 solid 1px");
                $("#msg").text('Se guardó la categoría correctamente');
                $("#msg").show();
                $('#categorieModal').modal('hide');
                app.table.ajax.reload();
            },
            error : function(error) {
                $("#msg").css("color", "#000");
                $("#msg").css("background-color", "#fc97a4");
                $("#msg").css("border", "#000 solid 1px");
                $("#msg").text('(ERROR) Excede el numero de caracteres permitidos');
                $("#msg").show();
            }
        })
    },

    save_put : function(data) {
        $.ajax({
            url: app.backend + '/categories/' + data.id,
            data : JSON.stringify(data),
            method: 'PUT',
            dataType : 'json',
            contentType: "application/json; charset=utf-8",
            success : function(json) {
                $("#msg").css("color", "#000");
                $("#msg").css("background-color", "#97fcb0");
                $("#msg").css("border", "#000 solid 1px");
                $("#msg").text('La categoría se actualizó correctamente');
                $("#msg").show();
                $('#categoriePutModal').modal('hide');
                app.table.ajax.reload();
            },
            error : function(xhr, status, error) {
                console.log(error);
                $("#msg").css("color", "#fff");
                $("#msg").css("background-color", "#ff4d4d");
                $("#msg").css("border", "#000 solid 1px");
                $("#msg").text('Error al actualizar la categoría');
                $("#msg").show();
            }
        });
    },

    delete : function(id) {
        $.ajax({
            url: app.backend + '/categories/' + id,
            method: 'DELETE',
            dataType : 'json',
            contentType: "application/json; charset=utf-8",
            success : function(json) {
                $("#msg").css("color", "#000");
                $("#msg").css("background-color", "#97fcb0");
                $("#msg").css("border", "#000 solid 1px");
                $("#msg").text('Se eliminó la categoría correctamente');
                $("#msg").show();
                app.table.ajax.reload();
            },
            error : function(error) {
                $("#msg").css("color", "#000");
                $("#msg").css("background-color", "#fc97a4");
                $("#msg").css("border", "#000 solid 1px");
                $("#msg").text('Error al eliminar la categoría');
                $("#msg").show();
            }
        })
    },
    load_products : function(id) {
        $.ajax({
            url: app.backend + '/categories/' + id + '/products/',
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

$(document).ready(function(){
    app.init();
});
