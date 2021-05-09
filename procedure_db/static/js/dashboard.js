function update_background(url, cb_id_name) {
  $('#' + cb_id_name + ' .poke_r2 ').css("background", "url(" + url + ")");
  $('#' + cb_id_name + ' .poke_r2 ').css("background-size", "100%");
  $('#' + cb_id_name + ' .poke_r2 ').css("background-repeat", "no-repeat");


};

$(document).ready(function() {
  // Multiselect boxes initialization
  $('#arch').multiselect();
  $('#file_type').multiselect();
  $('#os_version').multiselect();
  $('#intended_for').multiselect();

  // setup datatable
  $('#sim_table').DataTable({
    dom: "Bfrtip",
    responsive: true,
    idSrc: 'uid',
    data: search_results,
    order: [[1, 'asc']],
    columns: [
      {
        title: "Name",
        data: "name",
      },
      {
        title: "Arch",
        data: "arch",
      },
      {
        title: "File Type",
        data: "file_type",
      },
      {
        title: "Models OS",
        data: "models_os",
      },
      {
        title: "Models Libs",
        data: "models_libs",
      },
    ],
    select: true
  });

  // Store the rsult of ajax poke_main request
  var api_result = {}

  $('#web_search').on('click', function() {
    var jdata = { 
      'search_fields': {
        'arch': $('#arch').val(),
        'file_type': $('#file_type').val(),
        'os_version': $('#os_version').val(),
        'contains_bytes': $('#contains_bytes').val(),
        'models_os': $('#models_os').is(':checked'),
        'models_libs': $('#models_libs').is(':checked')
       }
     };
    $.ajax({
      url: "/web_search_simprocedure",
      type: "POST",
      dataType: 'json',
      contentType: 'application/json;charset=UTF-8',
      data: JSON.stringify(jdata),
      success: function(result) {
          console.log(result)
        }, function(error) {
          console.log(error);
        }
      });
  });

});
