$(function () {
    $('#data').DataTable({
        responsive: true,
        autoWidth: false,
        destroy: true,
        deferRender: true,
        ajax: {
            url: window.location.pathname,
            type: 'POST',
            data: {
                'action': 'searchdata'
            },
            dataSrc: ""
        },
        columns: [
            {"data": "id"},
            {"data": "title"},
            {"data": "usuario.username"},
            {"data": "price"},
            {"data": "image"},
            {"data": "audio_file"},
            {"data": "id"},
        ],
        columnDefs: [
            {
                targets: [-3],
                class: 'text-center',
                orderable: false,
                render: function (data, type, row) {
                    return '<img src="'+data+'" class="img-fluid d-block mx-auto" style="width: 20px; height: 20px;">';
                }
            },
            {
                targets: [-2],
                class: 'text-center',
                orderable: false, 
                render: function (data, type, row) {
                    return buttons = '<audio class="Audio-1" src="'+row.audio_file+'" controls style="width: 200px;"></audio>'; 
                }
            },
            {
                targets: [-1],
                class: 'text-center',
                orderable: false,
                render: function (data, type, row) {
                    var buttons = '<a href="/erp/music/update/' + row.id + '/" class="btn btn-warning btn-xs btn-flat"><i class="fas fa-edit"></i></a> ';
                    buttons += '<a href="/erp/music/delete/' + row.id + '/" type="button" class="btn btn-danger btn-xs btn-flat"><i class="fas fa-trash-alt"></i></a>';
                    return buttons;
                }
            },
        ],
        initComplete: function (settings, json) {

        }
    });
});
