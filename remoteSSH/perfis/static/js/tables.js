$(document).ready(function () {
    $('#tableComputer').DataTable({
      "scrollY": "140px",
      "scrollCollapse": true,
      "paging": false,
      "bInfo": false,
      "language": {
                 "sZeroRecords": "Sem resultados!",
                 "search": "Buscar:"
      }
      
    });
    $('.dataTables_length').addClass('bs-select');
  });

  $(document).ready(function () {
    $('#tableCommand').DataTable({
      "scrollY": "140px",
      "scrollCollapse": true,
      "paging": false,
      "bInfo": false,
      "language": {
        "sZeroRecords": "Sem resultados!",
        "search": "Buscar:"
      }
    });
    $('.dataTables_length').addClass('bs-select');
  });