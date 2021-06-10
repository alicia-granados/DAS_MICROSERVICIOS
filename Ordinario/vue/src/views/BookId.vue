<template>
    <div class="bookid">
        <br/><br/>
        <!-- A card to view book -->
        <div div class="card"  :to="{name: 'Book', params: { id: item } }"
                    v-for= "(item,index) of Book" v-bind:key="index"> <!-- Generates a for loop to get each variable of the book -->
            <div class="card-body">
                <!-- Accessing each value in the book through a for loop and assigning it -->
                <h2 class="card-title">Title: {{item.title}}</h2><br/>
                <h5 class="card-subtitle mb-2 text-muted">Subtitle: {{item.subtitle}}</h5><br/>
                <p class="card-text">Authors: {{item.authors}}</p><br/>
                <p class="card-text">Publisher: {{item.publisher}}</p><br/>
                <p class="card-text">Published Date: {{item.publishedDate}}</p><br/>
                <p class="card-text">Description: {{item.description}}</p><br/>
                <p class="card-text">Page Count: {{item.pageCount}}</p><br/>
                <p class="card-text">Categories: {{item.categories}}</p><br/>

                <button type="button"
                        class="btn btn-light btn-sm" >
                    <router-link  class="navbar-brand" to="/library">Return</router-link>  <!-- Returns to the Library view -->  
                </button>
            </div>
        </div>
    
    </div>
</template>

<script>

    export default {
    name: 'bookid',
    components: {
    },
    data(){
        return {
            Book: [] // Returns a data array for the component instance.
        }
    },mounted(){

        let book_id = this.$route.params.id; //Get the book id

        // Access and manipulate the API using the HTTP method
        fetch(`http://localhost:5001/libros/${book_id}` , {
                method: 'GET',
                mode: "cors", // Permission to access selected resources from a server
                headers: {
                    'Content-Type': 'application/json',
                }
            })
                // Returns a promise with the body of the text transformed to JSON and adds a book
                .then((res) =>   res.json().then( data =>   this.Book.push(data) )
                  
                )
           
                .then(res => {   
                    console.log(res); // Show the promise in the browser console
                    })
            .catch(function(e) {
                console.log(e);  // In case of an error, show that error in the browser console
            });
      
    }
    }
            
</script>