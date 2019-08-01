//== Class definition

var DatatableRemoteAjaxDemo = function() {
  //== Private functions

  // basic demo
  var demo = function() {

    var arr =[];
    $.ajax({
      url: "/newapp/work_reports",
      type:"GET",
      cache: false,
      data:{},
      success: function(response){
        console.log(response,"this is the response")
        
        // for (var i = 0; i<response['result'].length ; i++) {
        //  arr.push(response['result'])
        // }
        
        console.log(response,"this is the response")
        for (var i= 0 ; i < response['result'].length; i++) {
          arr.push(response['result'][i]['fields']);
        }
      console.log(arr,"this is the response")
    var datatable = $('.m_datatable').mDatatable({
      // order: [ 0, 'desc' ],
      // datasource definition
      data: {
        type: 'local',
        source: arr,
        pageSize: 10, // display 20 records per page
        // saveState: {
        //  cookie: true,
        //  webstorage: true
        // }
      },

      // layout definition
      layout: {
        theme: 'default',
        scroll: false,
        height: null,
        footer: false
      },

      // order : [ 0, 'desc' ],

      sortable: false,

      filterable: false,

      pagination: true,

      // sortable: [ 4, 'desc' ],
      // detail: {
      //  title: 'Load sub table',
      //  content: subTableInit
      // },

      search: {
        input: $('#generalSearch')
      },

      // columns definition
      columns: [
      {
        field: "employeementId",
        title: "Employeement ID",
        
      },
      //{
      //  field: "employeementId",
      //  title: "Employee ID"
      // }, 
      {
        field: "employeeFirstName",
        title: "First Name"
      }, {
        field: "employeeLastName",
        title: "Last Name"
      }, {
        field: "employeeBirthDate",
        title: "Birth Date",
        order : [ 0, 'desc' ],
      }, {
        field: "employeeGender",
        title: "Gender"
      }, {
        field: "Actions",
        width: 110,
        title: "Actions",
        sortable: false,
        overflow: 'visible',
        template: function (row) {
          var dropup = (row.getDatatable().getPageSize() - row.getIndex()) <= 4 ? 'dropup' : '';
          
          return '\
            <a href="#" class="m-portlet__nav-link btn m-btn m-btn--hover-accent m-btn--icon m-btn--icon-only m-btn--pill" title="Edit details">\
              <i class="la la-edit"></i>\
            </a>\
            <a href="#" class="m-portlet__nav-link btn m-btn m-btn--hover-danger m-btn--icon m-btn--icon-only m-btn--pill" title="Delete">\
              <i class="la la-trash"></i>\
            </a>\
          ';
        }
      }]
    });
    var query = datatable.getDataSourceQuery();
    $('#m_form_status').on('change', function() {
      // shortcode to datatable.getDataSourceParam('query');
      var query = datatable.getDataSourceQuery();
      query.Status = $(this).val().toLowerCase();
      // shortcode to datatable.setDataSourceParam('query', query);
      datatable.setDataSourceQuery(query);
      datatable.load();
    }).val(typeof query.Status !== 'undefined' ? query.Status : '');

    $('#m_form_type').on('change', function() {
      // shortcode to datatable.getDataSourceParam('query');
      var query = datatable.getDataSourceQuery();
      query.Type = $(this).val().toLowerCase();
      // shortcode to datatable.setDataSourceParam('query', query);
      datatable.setDataSourceQuery(query);
      datatable.load();
    }).val(typeof query.Type !== 'undefined' ? query.Type : '');

    $('#m_form_status, #m_form_type').selectpicker();
}

    });
    
  };

  return {
    // public functions
    init: function() {
      demo();
    },
  };
}();

jQuery(document).ready(function() {
  DatatableRemoteAjaxDemo.init();
});