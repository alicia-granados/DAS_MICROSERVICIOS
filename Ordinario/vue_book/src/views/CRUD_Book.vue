<template>
  <v-container  grid-list-xl >
    <v-layout>
      <v-flex md6 class="mr-8">
        <v-card  class="mb-3" :to="{name: 'CRUD_Book', params: { id: item } }" v-for= "(item,index) of Book" v-bind:key="index" >
          <v-card-text>
             <v-chip
              ml-0
              color="pink"
              label
              text-color="white"
              >
                {{item.title}} 
              </v-chip>
              <br/>
            <p>{{item.subtitle }}</p>
            <p>{{ item.authors }}</p>
            <p>{{ item.publisher }}</p>
            <p>{{ item.description }}</p>
            <p>{{ item.pageCount }} </p>
            <p>{{ item.publishedDate }}</p>
            <p>{{ item.categories }} </p>
            <v-btn color="warning"  class="ml-0 mr-2">Update</v-btn>
            <v-btn color= "error"  @click="removeBook(item._id.$oid)">Delete</v-btn>
          </v-card-text>
        </v-card>
      </v-flex>

    

    </v-layout>
   <v-snackbar
      v-model="snackbar"
    >
      {{mensaje}}
      <v-btn
        color="primary"
        text
        @click="snackbar = false"
      >
        Close
      </v-btn>
    </v-snackbar>
    <!-- Fin Snackbar-->
  </v-container>
</template>

<script>
  

  export default {
    name: 'CRUD_Book',
    data(){
      return{
        Book:[], // Returns a data array for the component instance.
        snackbar: false,
        mensaje: '',

      }
    },mounted(){
       
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
            fetch(`http://localhost:5001/libros/${book_id}` , {
            method: 'DELETE',
            })
                .then(res => {
                    this.snackbar = true;
                    this.mensaje = "Deleted Book"
                    res.json(); // Returns a promise with the body of the text transformed to JSON
                    setTimeout('document.location.reload()',2000);
                    }) // or res.json() o.text
                .then(res => console.log(res)) // Show the promise in the browser console
            .catch(function(e) {
                //console.log(e);  // In case of an error, show that error in the browser console
            });
            

            
        },
    
        
    }
  }
</script>
