//== Class definition

var DatatableRemoteAjaxDemo = function() {
  //== Private functions

  // basic demo
  var demo = function() {
    var datatable = $('.m_datatable').mDatatable({
      // datasource definition
      data: {
        type: 'remote',
        source: {
          read: {
            // sample GET method
            method: 'GET',
            url: '/newapp/work_reports',
            map: function(raw) {
              var arr =[];
              for (var i= 0 ; i < raw['result'].length; i++) {

                arr.push(raw['result'][i]['fields']);
              }
              console.log(arr,"this is the array")
              // sample data mapping
              var dataSet = arr;
              if (typeof raw.data !== 'undefined') {
                dataSet = raw.data;
              }
              return dataSet;
            },
          },
        },
        pageSize: 10,
        saveState: {
          cookie: true,
          webstorage: true,
        },
        serverPaging: true,
        serverFiltering: true,
        serverSorting: true,
      },

      // layout definition
      layout: {
        theme: 'default', // datatable theme
        class: '', // custom wrapper class
        scroll: false, // enable/disable datatable scroll both horizontal and vertical when needed.
        footer: true // display/hide footer
      },

      // column sorting
      sortable: true,

      pagination: true,

      toolbar: {
        // toolbar items
        items: {
          // pagination
          pagination: {
            // page size select
            pageSizeSelect: [5, 10, 20, 30, 50, 100],
          },
        },
      },

      search: {
        input: $('#generalSearch'),
      },

      // columns definition
      columns: [
        {
          field: 'employeementId',
          title: 'ID',
          sortable: false, // disable sort for this column
          selector: false,
          textAlign: 'center',
        }, {
          field: 'employeeFirstName',
          title: 'First Name',
          sortable: false,
          // sortable: 'asc', // default sort
          // filterable: false, // disable or enable filtering
          // width: 150,
          // basic templating support for column rendering,
          // template: '{{OrderID}} - {{ShipCountry}}',
        },
        {
          field: 'employeeLastName',
          title: 'Last Name',
          sortable: false,
        },
         {
          field: 'employeeBirthDate',
          title: 'Birth Date',
          sortable: false,
        }, {
          field: 'employeeGender',
          title: 'Gender',
          sortable: false,
        }, 
        // {
        //   field: 'ShipDate',
        //   title: 'Ship Date',
        //   sortable: 'asc',
        //   type: 'date',
        //   format: 'MM/DD/YYYY',
        // }, {
        //   field: 'Latitude',
        //   title: 'Latitude',
        //   type: 'number',
        // }, 
        // {
        //   field: 'Status',
        //   title: 'Status',
        //   // callback function support for column rendering
        //   template: function(row) {
        //     var status = {
        //       1: {'title': 'Pending', 'class': 'm-badge--brand'},
        //       2: {'title': 'Delivered', 'class': ' m-badge--metal'},
        //       3: {'title': 'Canceled', 'class': ' m-badge--primary'},
        //       4: {'title': 'Success', 'class': ' m-badge--success'},
        //       5: {'title': 'Info', 'class': ' m-badge--info'},
        //       6: {'title': 'Danger', 'class': ' m-badge--danger'},
        //       7: {'title': 'Warning', 'class': ' m-badge--warning'},
        //     };
        //     return '<span class="m-badge ' + status[row.Status].class + ' m-badge--wide">' + status[row.Status].title + '</span>';
        //   },
        // }, 
        // {
        //   field: 'Type',
        //   title: 'Type',
        //   // callback function support for column rendering
        //   template: function(row) {
        //     var status = {
        //       1: {'title': 'Online', 'state': 'danger'},
        //       2: {'title': 'Retail', 'state': 'primary'},
        //       3: {'title': 'Direct', 'state': 'accent'},
        //     };
        //     return '<span class="m-badge m-badge--' + status[row.Type].state + ' m-badge--dot"></span>&nbsp;<span class="m--font-bold m--font-' + status[row.Type].state + '">' +
        //         status[row.Type].title + '</span>';
        //   },
        // }, 

        {
          field: 'Actions',
          width: 110,
          title: 'Actions',
          sortable: false,
          overflow: 'visible',
          template: function(row) {
            var dropup = (row.getDatatable().getPageSize() - row.getIndex()) <= 4 ? 'dropup' : '';

            return '\
						<a href="#" class="m-portlet__nav-link btn m-btn m-btn--hover-accent m-btn--icon m-btn--icon-only m-btn--pill" title="Edit details">\
							<i class="la la-edit"></i>\
						</a>\
						<a href="#" class="m-portlet__nav-link btn m-btn m-btn--hover-danger m-btn--icon m-btn--icon-only m-btn--pill" title="Delete">\
							<i class="la la-trash"></i>\
						</a>\
					';
          },
        }],
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