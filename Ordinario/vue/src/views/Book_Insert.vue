<template>
    <div class="book">
        <br/><br/>
        <!-- A form to instert book -->
        <form id="form-book-group" v-on:submit.prevent="onSumbit" >
            <div class="form-group">
                <label for="form-title-input">Title</label>
                <input type="text" class="form-control" id="form-title-input" name="form-title-input" placeholder="Title" required>
                <br/>
                <label for="form-subtitle-input">Subtitle</label>
                <input type="text" class="form-control" id="form-subttitle-input" name="form-subttitle-input"  placeholder="Subtitle" required>
                <br/>
                <label for="form-authors-input">Authors</label>
                <input type="text" class="form-control" id="form-authors-input"  name="form-authors-input" placeholder="Authors" required>
                <br/>
                <label for="form-publisher-input">Publisher</label>
                <input type="text" class="form-control" id="form-publisher-input" name="form-publisher-input"  placeholder="Publisher" required>
                <br/>
                <label for="form-description-input">Description</label>
                <input type="text" class="form-control" id="form-description-input" name="form-description-input" placeholder="Description" required>
                <br/>
                <label for="form-pageCount-input">Page Count</label>
                <input type="text" class="form-control" id="form-pageCount-input"  name="form-pageCount-input" placeholder="Page Count" required>
                <br/>
                <label for="form-publishedDate-input">Publish Date</label>
                <input type="text" class="form-control" id="form-publishedDate-input" name="form-publishedDate-input" placeholder="Publish Date" required>
                <br/>
                <label for="form-categories-input">Categories</label>
                <input type="text" class="form-control" id="form-categories-input"  name="form-categories-input" placeholder="Categories" required>
                <br/>
                <button type="submit" class="btn btn-primary" >Insert</button>
            </div>
        </form>
    </div>
</template>

<script>
   
    export default {
    name: 'book',
    components: {
    },
    // A function that returns a data object for the component instance.
    data(){
        return {
            Book:{
                "title": "",
                "subtitle": "", 
                "authors": "",
                "publisher": "", 
                "publishedDate": "", 
                "description": "",
                "pageCount": "", 
                "categories": ""
            }
        }
    }, 
     methods:{
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
                    this.Alert(); // Call the function "Alert" to say that the book was inserted
                    location.reload(); // Reload the page after the book was inserted
                    })
            .catch(function(e) {   
                console.log(e); // In case of an error, show that error in the browser console 
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
        
        },Alert(){
            alert('Inserted book'); // Shows an alert after insert a book
        }        
    }
    }
</script>