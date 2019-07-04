function apiService(data) 
{
    var apiUrl = 'http://192.168.0.191:8000/newapp/persoanldetails';
    $.ajax({
        url : apiUrl,
        method: 'POST',
        type: 'jsonp',
        data: data,
    }).success(function(response) {
        console.log(response);
    });
}
function apiServiceForFormData(form) 
{
    var response={}
    var apiUrl = 'http://192.168.0.191:8000/newapp/persoanldetails';
    $.ajax({
        url : apiUrl,
        type: 'POST',
        data: form,
        cache:false,
        contentType: false,
        processData: false,
        mimeType: "multipart/form-data",
    }).success(function(response) {
        response =response
        console.log('call')
    });
    console.log('call2')
    return response
}

function scroll_to_class(element_class, removed_height) {
	var scroll_to = $(element_class).offset().top - removed_height;
	if($(window).scrollTop() != scroll_to) {
		$('html, body').stop().animate({scrollTop: scroll_to}, 0);
	}
}

function bar_progress(progress_line_object, direction) {
	var number_of_steps = progress_line_object.data('number-of-steps');
	var now_value = progress_line_object.data('now-value');
	var new_value = 0;
	if(direction == 'right') {
		new_value = now_value + ( 100 / number_of_steps );
	}
	else if(direction == 'left') {
		new_value = now_value - ( 100 / number_of_steps );
	}
	progress_line_object.attr('style', 'width: ' + new_value + '%;').data('now-value', new_value);
}

jQuery(document).ready(function() {

    $(document).on('input','.num', function (event) {
   this.value = this.value.replace(/[^0-9]/g, '');
});
    $(document).on('input','.alph', function (event) {
   this.value = this.value.replace(/[^a-zA-Z]+$/g, '');
});
    $.backstretch("assets/img/backgrounds/1.jpg");
    
    $('#top-navbar-1').on('shown.bs.collapse', function(){
    	$.backstretch("resize");
    });
    $('#top-navbar-1').on('hidden.bs.collapse', function(){
    	$.backstretch("resize");
    });
    $('.f1 fieldset:first').fadeIn('slow');
    
    $('#datejoin,#positiondd,#jobstatuseffectivedate,#employmentstatuseffectivedate,#countrydd,#employeeid,#firstname,#lastname,#birthdate,#nationalid').on('focus', function() {
    	$(this).removeClass('input-error');
    });

    // next step
    $('.f1 .btn-next').on('click', function() {
    	var parent_fieldset = $(this).parents('fieldset');
        var selectedid = ($(this).parents('fieldset').attr('id'))
        console.log(selectedid)
    	var next_step = true;
    	// navigation steps / progress steps
    	var current_active_step = $(this).parents('.f1').find('.f1-step.active');
    	var progress_line = $(this).parents('.f1').find('.f1-progress-line');

        
      //  fields validation
        parent_fieldset.find('#datejoin,#positiondd,#jobstatuseffectivedate,#employmentstatuseffectivedate,#countrydd,#employeeid,#firstname,#lastname,#birthdate,#nationalid').each(function() {
         if( $(this).val() == "" ) {
             $(this).addClass('input-error');
             next_step = false;
         }
        else{
                $(this).removeClass('input-error');
            }

        });
                next_step = false;
                var data = {};
                var i =0
                if (selectedid =='personalfield'){
                    var form = new FormData();
                    form.append("employeeid", $('#employeeid').val());
                    form.append("firstname", $('#firstname').val());
                    form.append("middlename", $('#middlename').val());
                    form.append("lastname", $('#lastname').val());
                    form.append("gendern", $('#gendern').val());
                    form.append("birthdate", $('#birthdate').val());
                    form.append("nationalitydd",$('#nationalitydd').val());
                    form.append("nationalid", $('#nationalid').val());
                    form.append("image", $('#image').prop('files')[0]);
                    var response={}
                    var apiUrl = 'http://192.168.0.191:8000/newapp/persoanldetails';
                    $.ajax({
                        url : apiUrl,
                        type: 'POST',
                        data: form,
                        async: false,
                        cache:false,
                        contentType: false,
                        processData: false,
                        mimeType: "multipart/form-data",
                    }).success(function(response) {
                        res=JSON.parse(response)
                        console.log(res,res['status'])                        
                        if(res['status']==200){
                            next_step =true
                            $('.action').show()
                            $('.action').addClass('alert-success');
                            $('.action').removeClass('alert-danger');
                            $('.action').text(res['msg'])
                        }else{
                            $('.action').show()
                            $('.action').removeClass('alert-success');
                            $('.action').addClass('alert-danger');
                            $('.action').text(res['msg'])
                        }
                         // $('.action').show()
                    });
                   }
                else if (selectedid =='jobfield'){
                    data[$('#datejoin').attr('name')] = $('#datejoin').val();
                    data[$('#endofprobation').attr('name')] = $('#endofprobation').val();
                    data[$('#positiondd').attr('name')] = $('#positiondd').val();
                    data[$('#jobstatuseffectivedate').attr('name')] = $('#jobstatuseffectivedate').val();
                    data[$('#linemanagedd').attr('name')] = $('#linemanagedd').val();
                    data[$('#departmentdd').attr('name')] = $('#departmentdd').val();
                    data[$('#branchdd').attr('name')] = $('#branchdd').val();
                    data[$('#leveldd').attr('name')] = $('#leveldd').val();
                    data[$('#jobtypedd').attr('name')] = $('#jobtypedd').val();
                    data[$('#employmentstatuseffectivedate').attr('name')] = $('#employmentstatuseffectivedate').val();
                    data[$('#jobstatusdd').attr('name')] = $('#jobstatusdd').val();
                    data[$('#workdays').attr('name')] = $('#workdays').val(); 
                    data[$('#holidaysdd').attr('name')] = $('#holidaysdd').val(); 
                    data[$('#termstartdd').attr('name')] = $('#termstartdd').val(); 
                    data[$('#termend').attr('name')] = $('#termend').val(); 
                    apiService(data);
                    }

                else if (selectedid =='familyfield'){
                    data[$('#maritalstatus').attr('name')] = $('#maritalstatus').val();
                    data[$('#spouseworking').attr('name')] = $('#spouseworking').val();
                    data[$('#numberofchild').attr('name')] = $('#numberofchild').val();
                    data[$('#spousefirstname').attr('name')] = $('#spousefirstname').val();
                    data[$('#spousemiddlename').attr('name')] = $('#spousemiddlename').val();
                    data[$('#spousenationality').attr('name')] = $('#spousenationality').val();
                    data[$('#spousebirthdate').attr('name')] = $('#spousebirthdate').val();
                    data[$('#spousepassport').attr('name')] = $('#spousepassport').val();
                    data[$('#spouseethnicity').attr('name')] = $('#spouseethnicity').val();
                    data[$('#spouserelegion').attr('name')] = $('#spouserelegion').val();
                    apiService(data);
                }
                else if (selectedid =='contactfield'){
                    data[$('#email').attr('name')] = $('#email').val();
                    data[$('#bloghomepage').attr('name')] = $('#bloghomepage').val();
                    data[$('#office').attr('name')] = $('#office').val();
                    data[$('#mobile').attr('name')] = $('#mobile').val();
                    data[$('#home').attr('name')] = $('#home').val();
                    data[$('#address1').attr('name')] = $('#address1').val();
                    data[$('#address2').attr('name')] = $('#address2').val();
                    data[$('#city').attr('name')] = $('#city').val();
                    data[$('#state').attr('name')] = $('#state').val();
                    data[$('#countrydd').attr('name')] = $('#countrydd').val();
                    data[$('#coefirstname').attr('name')] = $('#coefirstname').val();
                    data[$('#coelastname').attr('name')] = $('#coelastname').val();
                    data[$('#coemiddlename').attr('name')] = $('#coemiddlename').val();
                    data[$('#coerelationship').attr('name')] = $('#coerelationship').val();
                    data[$('#coemobile').attr('name')] = $('#coemobile').val();
                    data[$('#coehousephone').attr('name')] = $('#coehousephone').val();
                    data[$('#officephone').attr('name')] = $('#officephone').val();
                    apiService(data);
                }
                else if (selectedid =='healthfield'){
                    data[$('#height').attr('name')] = $('#height').val();
                    data[$('#weight').attr('name')] = $('#weight').val();
                    data[$('#bloodgroup').attr('name')] = $('#bloodgroup').val();
                    apiService(data);
                }
                   console.log(next_step,'console.log(next_step)')
                  
   

            

          
    //    fields validation
        

    	
    	// fields validation
    	// parent_fieldset.find('input[type="text"], input[type="password"], textarea').each(function() {
    	// 	if( $(this).val() == "" ) {
    	// 		$(this).addClass('input-error');
    	// 		next_step = false;
    	// 	}
    	// 	else {
    	// 		$(this).removeClass('input-error');
    	// 	}
    	// });
    	// fields validation
    	
    	if( next_step ) {
    		parent_fieldset.fadeOut(400, function() {
    			// change icons
    			current_active_step.removeClass('active').addClass('activated').next().addClass('active');
    			// progress bar
    			bar_progress(progress_line, 'right');
    			// show next step
	    		$(this).next().fadeIn();
	    		// scroll window to beginning of the form
    			scroll_to_class( $('.f1'), 20 );
	    	});
    	}
    	
    });
    
    // previous step
    $('.f1 .btn-previous').on('click', function() {
    	// navigation steps / progress steps
    	var current_active_step = $(this).parents('.f1').find('.f1-step.active');
    	var progress_line = $(this).parents('.f1').find('.f1-progress-line');
    	
    	$(this).parents('fieldset').fadeOut(400, function() {
    		// change icons
    		current_active_step.removeClass('active').prev().removeClass('activated').addClass('active');
    		// progress bar
    		bar_progress(progress_line, 'left');
    		// show previous step
    		$(this).prev().fadeIn();
    		// scroll window to beginning of the form
			scroll_to_class( $('.f1'), 20 );
    	});
    });
    
    //submit
    $('.f1').on('submit', function(e) {
    	
    	// fields validation
    	$(this).find('#datejoin,#positiondd,#jobstatuseffectivedate,#employmentstatuseffectivedate,#countrydd,#employeeid,#firstname,#lastname,#birthdate,#nationalid').each(function() {
    		if( $(this).val() == "" ) {
    			e.preventDefault();
    			$(this).addClass('input-error');
    		}
    		else {
    			$(this).removeClass('input-error');
    		}
    	});
    	// fields validation
    	
    });
    
    
});
