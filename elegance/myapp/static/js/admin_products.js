let app_products = {
    backend: 'http://127.0.0.1:5001/api/v1',
    table: null,
    init: function() {
        const urlParams = new URLSearchParams(window.location.search);
        const categoryId = urlParams.get('category_id');
        const $title = document.querySelector("#crud-title");

        $.ajax({
            url: app_products.backend + '/categories/' + categoryId,
            success: function(category) {
                $title.textContent = 'Productos de la categoría: ' + category.name;
            },
            error: function() {
                console.error('Error al obtener la categoría.');
            }
        });

        app_products.initDatatable('#products', app_products.backend + '/categories/' + categoryId + '/products');

        $("#Productsave").click(function() {
            app_products.Productsave(app_products.backend + '/categories/' + categoryId + '/products', {
                name: $('#ProductName').val(),
                description: $('#description_post').val(),
                price: $('#price_post').val(),
                available_units: $('#available_units_post').val(),
                image: $('#image_post').val(),
                brand: $('#brand_post').val()
            });
        });

        $("#ProductSavePut").click(function() {
            app_products.ProductSavePut({
                id: $('#ProductIdPut').val(),
                name: $('#ProductNamePut').val(),
                description: $('#description_put').val(),
                price: $('#price_put').val(),
                available_units: $('#available_units_put').val(),
                image: $('#image_put').val(),
                brand: $('#brand_put').val()
            });
        });
    },

    initDatatable: function(id, url) {
        app_products.table = $(id).DataTable({
            language: {
                "decimal": "",
                "emptyTable": "No hay información",
                "info": "Mostrando _START_ a _END_ de _TOTAL_ Entradas",
                "infoEmpty": "Mostrando 0 a 0 de 0 Entradas",
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
                    "last": "Último",
                    "next": "Siguiente",
                    "previous": "Anterior"
                }
            },
            ajax: {
                url: url,
                dataSrc: ''
            },
            dom: 'Bfrtip',
            columns: [
                { data: null, render: function(data, type, full, meta) {
                    return meta.row + 1;
                }},
                { data: 'name' },
                { data: 'description' },
                { data: 'price' },
                { data: 'available_units' },
                { data: 'image', render: function(data) {
                    return `<img src="${data}" alt="Product Image" style="width: 50px; height: auto;">`;
                }},
                { data: 'brand' }
            ],
            buttons: [
                {
                    text: '<i class="fa-solid fa-chevron-left"></i>',
                    action: function() {
                        location.href = "admin";
                    }
                },
                {
                    text: '<i class="fa-solid fa-plus"></i>',
                    action: function() {
                        app_products.cleanForm();
                        $('#ProductModal').modal();
                    }
                },
                {
                    text: '<i class="fa-solid fa-trash-can"></i>',
                    action: function(e, dt) {
                        let data = dt.rows('.table-active').data()[0];
                        swal({
                            title: "¿Estás seguro de que deseas eliminar el producto?",
                            icon: "warning",
                            buttons: true,
                            dangerMode: true,
                        }).then((willDelete) => {
                            if (willDelete) {
                                swal('Eliminado exitosamente', '', 'success');
                                app_products.delete(data.id);
                            }
                        });
                    }
                },
                {
                    text: '<i class="fa-solid fa-pencil"></i>',
                    action: function(e, dt) {
                        let data = dt.rows('.table-active').data()[0];
                        app_products.setDataToModalPut(data);
                        $('#ProductPutModal').modal();
                    }
                }
            ]
        });

        $('#products tbody').on('click', 'tr', function() {
            $(this).toggleClass('table-active').siblings().removeClass('table-active');
        });
    },

    setDataToModal: function(data) {
        $('#ProductName').val(data.name);
        $('#description_post').val(data.description);
        $('#price_post').val(data.price);
        $('#available_units_post').val(data.available_units);
        $('#image_post').val(data.image);
        $('#brand_post').val(data.brand);
    },

    setDataToModalPut: function(data) {
        $('#ProductIdPut').val(data.id);
        $('#ProductNamePut').val(data.name);
        $('#description_put').val(data.description);
        $('#price_put').val(data.price);
        $('#available_units_put').val(data.available_units);
        $('#image_put').val(data.image);
        $('#brand_put').val(data.brand);
    },

    cleanForm: function() {
        $('#ProductName').val('');
        $('#description_post').val('');
        $('#price_post').val('');
        $('#available_units_post').val('');
        $('#image_post').val('');
        $('#brand_post').val('');
    },

    Productsave: function(url, data) {
        $.ajax({
            url: url,
            data: JSON.stringify(data),
            method: 'POST',
            dataType: 'json',
            contentType: "application/json; charset=utf-8",
            success: function() {
                $("#msg").css({"color": "#000", "background-color": "#97fcb0", "border": "#000 solid 1px"})
                    .text('Se guardó el producto correctamente').show();
                $('#ProductModal').modal('hide');
                app_products.table.ajax.reload();
            },
            error: function() {
                $("#msg").css({"color": "#000", "background-color": "#fc97a4", "border": "#000 solid 1px"})
                    .text('(ERROR) Excede el número de caracteres permitidos').show();
            }
        });
    },

    ProductSavePut: function(data) {
        $.ajax({
            url: app_products.backend + '/products/' + data.id,
            data: JSON.stringify(data),
            method: 'PUT',
            dataType: 'json',
            contentType: "application/json; charset=utf-8",
            success: function() {
                $("#msg").css({"color": "#000", "background-color": "#97fcb0", "border": "#000 solid 1px"})
                    .text('Producto actualizado correctamente').show();
                $('#ProductPutModal').modal('hide');
                app_products.table.ajax.reload();
            },
            error: function() {
                $("#msg").css({"color": "#000", "background-color": "#fc97a4", "border": "#000 solid 1px"})
                    .text('(ERROR) No se pudo actualizar el producto').show();
            }
        });
    },

    delete: function(id) {
        $.ajax({
            url: app_products.backend + '/products/' + id,
            method: 'DELETE',
            dataType: 'json',
            contentType: "application/json; charset=utf-8",
            success: function() {
                $("#msg").css({"color": "#000", "background-color": "#97fcb0", "border": "#000 solid 1px"})
                    .text('Producto eliminado correctamente').show();
                app_products.table.ajax.reload();
            },
            error: function() {
                $("#msg").css({"color": "#000", "background-color": "#fc97a4", "border": "#000 solid 1px"})
                    .text('(ERROR) No se pudo eliminar el producto').show();
            }
        });
    }
};

$(document).ready(function() {
    app_products.init();
});
