$(document).ready(function () {
    $('#clientesTable').DataTable({
        ajax: {
            url: '/api/clients',
            dataSrc: '',
        },
        columns: [
            { data: 'id' },
            { data: 'first_name' },
            { data: 'last_name' },
            { data: 'email' },
            { data: 'phone' },
            { data: 'address' },
        ],
        paging: true,
        searching: true,
        ordering: true,
        pageLength: 20,
        lengthChange: false,
        info: true,
    });
});