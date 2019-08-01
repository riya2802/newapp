// function apiServiceData(apiUrl,data) 
// {
//     var res=''
//     $.ajax({
//         url : apiUrl,
//         type: 'POST',
//         data: data,
//         async: false,
//     }).success(function(response){

//         res=JSON.parse(JSON.stringify(response))
//     });
//     return res
// }

// function justcalling() 
// {
//     $.ajax({
// 			url: "/newapp/work_reports",
// 			type:"GET",
// 			cache: false,
// 			data:{},
// 			success: function(response){
// 			res=JSON.parse(JSON.stringify(response))
// 			console.log(response,"sdhjasd")
// 			return res;
// 			}
// 		});
// }

//== Class definition
var DatatableChildDataLocalDemo = function () {
	//== Private functions

	var subTableInit = function (e) {
		$('<div/>').attr('id', 'child_data_local_').appendTo(e.detailCell)
			// .mDatatable({
			// 	data: {
			// 		type: 'local',
			// 		source: e.data.Orders,
			// 		pageSize: 10,
			// 		saveState: {
			// 			cookie: true,
			// 			webstorage: true
			// 		}
			// 	},

			// 	// layout definition
			// 	layout: {
			// 		theme: 'default',
			// 		scroll: true,
			// 		height: 300,
			// 		footer: false,

			// 		// enable/disable datatable spinner.
			// 		spinner: {
			// 			type: 1,
			// 			theme: 'default'
			// 		}
			// 	},

			// 	sortable: true,

			// 	// columns definition
			// 	columns: [{
			// 		field: "OrderID",
			// 		title: "Order ID",
			// 		sortable: false
			// 	}, {
			// 		field: "ShipCountry",
			// 		title: "Country",
			// 		width: 100
			// 	}, {
			// 		field: "ShipAddress",
			// 		title: "Ship Address"
			// 	}, {
			// 		field: "ShipName",
			// 		title: "Ship Name"
			// 	}]
			// });
	}

	// demo initializer
	var mainTableInit = function () {
		var arr =[];
		$.ajax({
			url: "/newapp/work_reports",
			type:"GET",
			cache: false,
			data:{},
			success: function(response){
				console.log(response,"this is the response")
				
				// for (var i = 0; i<response['result'].length ; i++) {
				// 	arr.push(response['result'])
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
				// 	cookie: true,
				// 	webstorage: true
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
			// 	title: 'Load sub table',
			// 	content: subTableInit
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
			// 	field: "employeementId",
			// 	title: "Employee ID"
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
						<div class="dropdown '+ dropup +'">\
							<a href="#" class="btn m-btn m-btn--hover-accent m-btn--icon m-btn--icon-only m-btn--pill" data-toggle="dropdown">\
                                <i class="la la-ellipsis-h"></i>\
                            </a>\
						  	<div class="dropdown-menu dropdown-menu-right">\
						    	<a class="dropdown-item" href="#"><i class="la la-edit"></i> Edit Details</a>\
						    	<a class="dropdown-item" href="#"><i class="la la-leaf"></i> Update Status</a>\
						    	<a class="dropdown-item" href="#"><i class="la la-print"></i> Generate Report</a>\
						  	</div>\
						</div>\
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
}
		});
	};

	return {
		//== Public functions
		init: function () {
			// init dmeo
			mainTableInit();
		}
	};
}();

jQuery(document).ready(function () {
	DatatableChildDataLocalDemo.init();
});