$(document).ready(function () {
    $("#schedule_repayment").on('submit', function (e) {
        $.ajax({
            type: "POST",
            data: $('#schedule_repayment').serialize(),
            success: function (data) {
                if (data.success) {
                    $(".response_message").addClass("error");
                    $(".response_message").addClass("success");
                    $(".response_message").text(data.message);
                    $(':input[type="submit"]').prop('disabled', true);
                    location.reload(true);
                } else {
                    $(".response_message").addClass("success");
                    $(".response_message").addClass("error");
                    $(".response_message").text(data.message);
                }
            }
        });
        e.preventDefault();

    });
    $('#end_date_toggle').hide();
    $('#end_date').click (function () {
        $('#end_date_toggle').show(500);
        $('#end_date').hide();
    });
    var d = new Date(),
        month = d.getMonth() + 2,
        year = d.getFullYear();
    if (month > 12)
        month = 1;
    if (month < 10)
        min = (year + '-' + '0' + month);
    else
        min = (year + '-' + month);
    $("#start-date, #end-date").attr({
        "min": min
    });
    $('#repayment_entry').hide();
    $('#button1').hide();
    $("#button, #button1").click(function () {
        $('#repayment_entry, #repayment_table').toggle(600);
        $('#button, #button1').toggle();
    });
    $('#search_button').remove();
    $('#repayment-schedule').hide();
    $(".project-name").change(function () {
        $('#repayment-schedule').show();
        var repayment_schedule = '#repayment-schedule';
        if ($.fn.dataTable.isDataTable(repayment_schedule)) {
            $(repayment_schedule).DataTable().ajax.reload();
        } else {
            table = $('#repayment-schedule').DataTable({
                // "processing": true,
                // "serverSide": true,
                "dom": 'lfrtip',
                "scrollX": true,
                buttons: [
                    'print',
                    {
                        extend: 'pdfHtml5',
                        orientation: 'landscape',
                        pageSize: 'LEGAL'
                    },
                    {
                        extend: 'excelHtml5',
                        orientation: 'landscape'
                    },
                    {
                        extend: 'csvHtml5',
                        orientation: 'landscape'
                    }

                ],
                // "order": [[ 4, "desc" ]],
                "ajax": {
                    url: '/repayment_config/',
                    "data": function (d) {
                        project_id = $('.project-name')[0].value;
                        d.project_id = project_id;
                    },
                    "dataSrc": "data"

                },
                "columns": [
                    {"data": "year"},
                    {"data": "month"},
                    {"data": "amount"}

                ]
            });
        }
    });
});
