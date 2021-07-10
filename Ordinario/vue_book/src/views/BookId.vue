<template>
    <v-container >
          <v-layout >
            <v-flex md12>
                <v-card>
                    <v-card-text :to="{name: 'bookid', params: { id: item } }" v-for= "(item,index) of Book" v-bind:key="index">
                        <v-chip
                        ml-0
                        color="pink"
                        label
                        text-color="white"
                        >
                        Title: {{item.title}}
                        </v-chip>
                        <br/>
                        <p>Subtitle: {{item.subtitle }}</p>
                        <p>Authors: {{ item.authors }}</p>
                        <p>Publisher: {{ item.publisher }}</p>
                        <p>Description: {{ item.description }}</p>
                        <p>Page Count: {{ item.pageCount }} </p>
                        <p>Published Date: {{ item.publishedDate }}</p>
                        <p>Categories: {{ item.categories }} </p>
                        <v-btn block color ="secondary mt-4">
                            <router-link  to="/CRUD_Book">Return</router-link> 
                        </v-btn>
                    </v-card-text>
                </v-card>
            </v-flex>
        </v-layout>
        <br/><br/><br/><br/><br/><br/><br/>
    </v-container>
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