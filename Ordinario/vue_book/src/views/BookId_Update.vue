<template>
    <v-container >
        <v-layout class="bookid_update">
            <v-flex md12 >
                <v-card class="mb-3 pa-3">
                <v-form  v-on:submit.prevent="onSumbit"  :to="{name: 'Book', params: { id: item } }"
                    v-for= "(item,index) of Book" v-bind:key="index" class="mx-8" >
                    <v-text-field label="Title"  id="form-title-input" name="form-title-input"  v-model="item.title" ></v-text-field>
                    <v-text-field label="Subtitle" id="form-subttitle-input" name="form-subttitle-input" v-model="item.subtitle"></v-text-field>
                    <v-text-field label="Publisher" id="form-authors-input"  name="form-authors-input" v-model="item.authors"></v-text-field>
                    <v-text-field label="Publisher"  id="form-publisher-input" name="form-publisher-input" v-model="item.publisher"></v-text-field>
                    <v-textarea label="Description"  id="form-description-input" name="form-description-input"  v-model="item.description"></v-textarea>
                    <v-text-field label="Page Count" id="form-pageCount-input"  name="form-pageCount-input"  v-model="item.pageCount"></v-text-field>
                    <v-text-field label="Published Date"  id="form-publishedDate-input" name="form-publishedDate-input"  v-model="item.publishedDate"></v-text-field>
                    <v-text-field label="Categories"  id="form-categories-input"  name="form-categories-input" v-model="item.categories"></v-text-field>
                    <v-btn block color="primary mt-2" type="submit">Update</v-btn>
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
    name: 'bookid_update',
    components: {
    },
    // Returns an object data array for the component instance
    data(){
        return {
            Book: [],
            Book_update:{
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
        }
    },mounted(){ 
        let book_id = this.$route.params.id; // Gets the book id
        // Access and manipulate the API using the HTTP method
        fetch(`http://localhost:5001/libros/${book_id}` , {
                method: 'GET',
                mode: "cors", // Permission to access selected resources from a server
                headers: {
                    'Content-Type': 'application/json',
                }
            })
                // Returns a promise with the body of the text transformed to JSON and adds it to a book
                .then((res) =>   res.json().then( data =>   this.Book.push(data) ))
           
                .then(res => {   
                    console.log(res);  // Show the promise in the browser console
                    })
            .catch(function(e) {  
                console.log(e); // In case of an error, show that error in the browser console
            });
      
    },methods:{
        // Function to update a book
        Updated_Book(book) {
            //console.log(book);
            let book_id = this.$route.params.id;
             // Access and manipulate the API using the HTTP method
            fetch(`http://localhost:5001/libros/${book_id}` , {
                method: 'PUT',
                body: JSON.stringify(book), // Convert the book object to a string
                mode: "cors", // Permission to access selected resources from a server  
                headers: {
                    'Content-Type': 'application/json',
                }
            })
                .then((res) => res.json() ) // Returns a promise with the body of the text transformed to JSON
           
                .then(res => {
                    console.log(res); // Show the promise in the browser console
                    this.snackbar = true; //"Alert" to say that the book was updated
                    this.mensaje = "Updated Book"
                    setTimeout('document.location.reload()',2000); // Reload the page after the book was updated
                    })
            .catch(function(e) {
                console.log(e);  // In case of an error, show that error in the browser console 
            })
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
            this.Updated_Book(book); // Calls the function to update the book, and passes the book as a parameter
        
        }        
    }
    }
            
</script>