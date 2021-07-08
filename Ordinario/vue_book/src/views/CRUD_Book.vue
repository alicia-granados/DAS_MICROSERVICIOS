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

      <v-flex md6  v-if ="formAgregar">
        <v-card class="mb-3 pa-3">
          <v-form  v-on:submit.prevent="onSumbit" >
            <v-text-field label="Title"  id="form-title-input" name="form-title-input"  ></v-text-field>
            <v-text-field label="Subtitle" id="form-subttitle-input" name="form-subttitle-input" ></v-text-field>
            <v-text-field label="Publisher" id="form-authors-input"  name="form-authors-input"  ></v-text-field>
            <v-text-field label="Publisher"  id="form-publisher-input" name="form-publisher-input" ></v-text-field>
            <v-textarea label="Description"  id="form-description-input" name="form-description-input"  ></v-textarea>
            <v-text-field label="Page Count" id="form-pageCount-input"  name="form-pageCount-input"  ></v-text-field>
            <v-text-field label="Published Date"  id="form-publishedDate-input" name="form-publishedDate-input"  ></v-text-field>
            <v-text-field label="Categories"  id="form-categories-input"  name="form-categories-input"></v-text-field>
            <v-btn block color="success" type="submit">Insert</v-btn>
          </v-form>
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
        Book_1:{
          "title": "",
          "subtitle": "", 
          "authors": "",
          "publisher": "", 
          "publishedDate": "", 
          "description": "",
          "pageCount": "", 
          "categories": ""
        },
        snackbar: false,
        mensaje: '',
        formAgregar : true,
        indexTarea : ''

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

        onSumbit(){

          // Gets the entered values of each input
            let title = document.getElementById("form-title-input").value;
            let subtitle = document.getElementById("form-subttitle-input").value;
            let authors = document.getElementById("form-authors-input").value;
            let publisher = document.getElementById("form-publisher-input").value;
            let description = document.getElementById("form-description-input").value;
            let pageCount = document.getElementById("form-pageCount-input").value;
            let publishedDate = document.getElementById("form-publishedDate-input").value;
            let categories = document.getElementById("form-categories-input").value;
            
            if ( title === '' || subtitle=== '' || authors === '' || publisher=== '' || description === '' || pageCount=== '' || publishedDate === '' || categories=== ''){
              this.snackbar = true;
              this.mensaje = 'Ingresa todos los campos';
            } else{
                // Pass the value of each input to the variable "book"
              const book = { 
                title: title,
                subtitle: subtitle,
                authors: authors,
                publisher: publisher,
                publishedDate: publishedDate,
                description: description,
                pageCount: pageCount,
                categories: categories
              };
              //console.log(book)
              this.addBook(book); // Calls the function to insert the book, and passes the book as a parameter
            }
          
           
        
        },
        // Function to instert a book
        addBook(book) {
          
            //console.log(book);
            // Access and manipulate the API using the HTTP method
            fetch(`http://localhost:5001/libros` , {
                method: 'POST',
                body: JSON.stringify(book), // Convert the book object to a string
                mode: "cors", // Permission to access selected resources from a server  
                headers: {
                    'Content-Type': 'application/json',
                }
            })
                .then((res) => res.json()) // Returns a promise with the body of the text transformed to JSON
           
                .then(res => {
                    console.log(res); // Show the promise in the browser console
                    this.snackbar = true;
                    this.mensaje = "Inserted Book"
                    setTimeout('document.location.reload()',2000);// Reload the page after the book was inserted
                    })
            .catch(function(e) {   
                console.log(e); // In case of an error, show that error in the browser console 
            });
        },
    
        
    }
  }
</script>
