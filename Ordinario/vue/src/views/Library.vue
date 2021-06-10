<template >
    <div class="catalogo  table-responsive">
        <br/>
        <!-- A table to view books -->
        <table class="table table-bordered table-dark  ">
            <thead>
                <tr>
                <th scope="col">#</th>
                <th scope="col">Title</th>
                <th scope="col">Subtitle</th>
                <th scope="col">Authors</th>
                <th scope="col">Publisher</th>
                <th scope="col">Description</th>
                <th scope="col">Page Count</th>
                <th scope="col">Publish Date</th>
                <th scope="col">Categories</th>
                <th scope="col">Options</th>
                </tr>
            </thead>
            <tbody>
                <!-- Generates a for loop to obtain each variable a book and shows all the books that exist -->
                <tr :to="{name: 'Book', params: { id: item } }"
                    v-for= "(item,index) of Book" v-bind:key="index" >
                <!-- Accessing each value in the book through a for loop and assigning it -->
                <th scope="row">{{index}}</th>
                <td>{{ item.title }}</td>
                <td>{{ item.subtitle }}</td>
                <td>{{ item.authors }}</td>
                <td>{{ item.publisher }}</td>
                <td>{{ item.description }}</td>
                <td>{{ item.pageCount }} </td>
                <td>{{ item.publishedDate }}</td>
                <td>{{ item.categories }} </td>
                <td id ="ruta"><br/>
                    <!-- call the delete function and send the id item of the book -->
                    <button
                        type="button"
                        class="btn btn-danger btn-sm"
                        @click="removeBook(item)" >
                      Delete
                    </button>
                    <br/><br/>
                    <!-- Return a view to see a book, and send the id of the book -->
                    <button type="button"
                        class="btn btn-light btn-sm" >
                        <router-link  :to="{name:'bookid', params:{id:item._id.$oid}}">View</router-link> 
                       
                    </button> <br/><br/>
                    <!-- Return a view to update a book and send the id of the book -->
                    <button  type="button"
                        class="btn btn-light btn-sm " >
                        <router-link  :to="{name:'bookidup', params:{id:item._id.$oid}}">Update</router-link>   
                    </button>                 
                </td>      
                </tr>        
            </tbody>
        </table>
    </div>
</template>
<style>
    /* Add styles to HTML*/
    #ruta a {
    font-weight: small;
    color: #f02a68;
    font-size:93%
  }

</style>

<script>
    
    export default {
    name: 'catalogo',
    components: {
       
    },
    data(){
        return {
            Book:[] // Returns a data array for the component instance.
        }
    }, mounted(){
       
        // Access and manipulate the API using the HTTP method
        fetch(`http://localhost:5001/libros`)
            .then((res) =>  {
                res.json().then(data => {
                    data.forEach(dt => this.Book.push(dt));  // Returns a promise with the body of the text transformed to JSON and adds a book
                });
            })
            .then((res) => console.log(res)) // Show the promise in the browser console
        .catch(function(e) {
            console.log(e);  // In case of an error, show that error in the browser console
        });
    },
     methods:{
        
        // Function to DELETE a book
        removeBook(book_id) {
            // Access and manipulate the API using the HTTP method
            fetch(`http://localhost:5001/libros/${book_id._id.$oid}` , {
            method: 'DELETE',
            })
                .then(res => {
                    res.json(); // Returns a promise with the body of the text transformed to JSON
                    this.Alert(); // Call the function "Alert"
                    location.reload(); // Reload the page after Updated
                    }) // or res.json() o.text
                .then(res => console.log(res)) // Show the promise in the browser console
            .catch(function(e) {
                console.log(e);  // In case of an error, show that error in the browser console
            });
        },
        
        Alert(){
            alert('Deleted book'); // Shows an alert after deleted the book
        }    
        
    }
    }
</script>