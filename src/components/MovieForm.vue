<template>
    <form @submit.prevent="saveMovie" id='movieForm' class="row g-3"> 

        <div v-if = "response_type == 'success'" class="alert alert-success">
            {{ response.message }}
        </div>

        <div v-if = "response_type == 'error'" class="alert alert-danger">
            <ul>
                <li v-for="error in response.errors">
                    {{ error }}
                </li>
            </ul>
        </div>

        <div class="col-12">
            <label for="title" class="form-label">Title</label>
            <input type="text" name="title" class="formcontrol" />
        </div>
        
        <div class="mb-3">
            <label for="description" class="form-label">Desciption</label>
            <textarea type="text" name="description" class="formcontrol"></textarea>
        </div>
        
        <div>
            <label for="poster" class="form-label">Poster</label>
            <input 
                type="file" 
                name="poster"
                class="formcontrol" 
                accept=".jpg, .jpeg, .png, .gif"/>
        </div>
        
        <div>
            <input type="submit" value="Submit">
        </div>
        
        
    </form>
</template>

<style>
    body {
        padding: 5rem;
    }
    Label{
    display: flex;
    flex-direction: column;
}
Input{
    width: 25%;
    padding: 12px 20px;
    box-sizing: border-box;
    border: 2px solid #ccc;
    border-radius: 4px;
}
textarea{
    width: 50%;
    height: 150px;
    padding: 12px 20px;
    box-sizing: border-box;
    border: 2px solid #ccc;
    border-radius: 4px; 
}
#submit {
    float: left;
    width: 200px;
    background-color: #04ab9d;
    color: white;
}
    
</style>

<script setup>

    import { ref, onMounted } from "vue"; onMounted(() => {     
        getCsrfToken(); 
    }); 

    let csrf_token = ref("");  
    let response = ref([]);
    let response_type = ref("");

    function getCsrfToken() {     
        fetch('/api/v1/csrf-token')       
        .then((response) => response.json())       
        .then((data) => {         
            console.log(data);         
            csrf_token.value = data.csrf_token;       
        })   
    } 

    const saveMovie = () =>{

        let movieForm = document.getElementById('movieForm'); 
        let form_data = new FormData(movieForm);

        fetch("/api/v1/movies", {     
            method: 'POST', 
            body: form_data,
            headers: {             
                'X-CSRFToken': csrf_token.value         
                }  
            })     
            .then(function (response) {         
                return response.json();     
            })     
            .then(function (data) {         
                // display a success message         
                console.log(data);

                if(data.hasOwnProperty('errors')){
                    response.value = data;
                    response_type.value = 'error';
                }   
                else{
                    response.value = data;
                    response_type.value = 'success';
                }  
            })     
            .catch(function (error) {         
                console.log(error, 'Error');     
            });
    }
</script>