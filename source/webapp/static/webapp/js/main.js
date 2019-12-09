$.ajax({
    url: 'http://localhost:8000/api/v2/login/',
    method: 'POST',
    data: JSON.stringify({username: 'admin', password: 'admin'}),
    dataType: 'json',
    contentType: 'application/json',
    success: function(response, status){
        localStorage.setItem('apiToken', response.token);
        console.log(response)
},
    error: function(response, status){console.log(response);}
});

$.ajax({
     url: 'http://localhost:8000/api/v2/projects/',
     method: 'GET',
     dataType: 'json',
     contentType: 'application/json',
     success: function(response, status){console.log(response);},
     error: function(response, status){console.log(response);}
});

$.ajax({
     url: 'http://localhost:8000/api/v2/missions/',
     method: 'GET',
     dataType: 'json',
     contentType: 'application/json',
     success: function(response, status){console.log(response);},
     error: function(response, status){console.log(response);}
});

$.ajax({
    url: "http://localhost:8000/api/v2/projects/2/",
    method: 'GET',
    success: function(response, status){console.log(response.mission_project);},
    error: function(response, status){console.log(response);}
});

$.ajax({
     url: 'http://localhost:8000/api/v2/missions/',
     method: 'POST',
     headers: {'Authorization': 'Token ' + localStorage.getItem('apiToken')},
     data: JSON.stringify({summary: 'testing api', description: 'testing api task',status: 1,type:2,
     project: 7, created_by: 1,assigned_to: 1 }),
     dataType: 'json',
     contentType: 'application/json',
     success: function(response, status){console.log(response);},
     error: function(response, status){console.log(response);}
});


$.ajax({
    url: 'http://localhost:8000/api/v2/missions/23/',
    method: 'DELETE',
    dataType: 'json',
    headers: {'Authorization': 'Token ' + localStorage.getItem('apiToken')},
    contentType: 'application/json',
    success: function(response, status){console.log("ok");},
    error: function(response, status){console.log(response);}
});




