<template>
    <div class="bookid_update">
        <form id="form-book-group" v-on:submit.prevent="onSumbit"  :to="{name: 'Book', params: { id: item } }"
                    v-for= "(item,index) of Book" v-bind:key="index">
            <div class="form-group" >
                <br/><br/>
                <label for="form-title-input">Title</label>
                <input type="text" class="form-control" id="form-title-input" name="form-title-input" v-model="item.title" placeholder="Title" required>
                <br/>
                <label for="form-subtitle-input">Subtitle</label>
                <input type="text" class="form-control" id="form-subttitle-input" name="form-subttitle-input"   v-model="item.subtitle" placeholder="Subtitle" required>
                <br/>
                <label for="form-authors-input">Authors</label>
                <input type="text" class="form-control" id="form-authors-input"  name="form-authors-input"  v-model="item.authors" placeholder="Authors" required>
                <br/>
                <label for="form-publisher-input">Publisher</label>
                <input type="text" class="form-control" id="form-publisher-input" name="form-publisher-input"  v-model="item.publisher" placeholder="Publisher" required>
                <br/>
                <label for="form-description-input">Description</label>
                <input type="text" class="form-control" id="form-description-input" name="form-description-input"  v-model="item.description" placeholder="Description" required>
                <br/>
                <label for="form-pageCount-input">Page Count</label>
                <input type="text" class="form-control" id="form-pageCount-input"  name="form-pageCount-input" v-model="item.pageCount" placeholder="Page Count" required>
                <br/>
                <label for="form-publishedDate-input">Publish Date</label>
                <input type="text" class="form-control" id="form-publishedDate-input" name="form-publishedDate-input" v-model="item.publishedDate" placeholder="Publish Date" required>
                <br/>
                <label for="form-categories-input">Categories</label>
                <input type="text" class="form-control" id="form-categories-input"  name="form-categories-input" v-model="item.categories" placeholder="Categories" required>
                <br/>
                <button type="submit" class="btn btn-warning" >Update</button>
            </div>
        </form>
    </div>
</template>

<script>

    export default {
    name: 'bookid_update',
    components: {
    },
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
            }
        }
    },mounted(){
        let book_id = this.$route.params.id;
        fetch(`http://localhost:5001/libros/${book_id}` , {
                method: 'GET',
                mode: "cors",
                headers: {
                    'Content-Type': 'application/json',
                }
            })
            
                .then((res) =>   res.json().then( data =>   this.Book.push(data) ))
           
                .then(res => {   
                    console.log(res) 
                    })
            .catch(function(e) {
                console.log(e); 
            });
      
    },methods:{
        Updated_Book(book) {
            //console.log(book);
            let book_id = this.$route.params.id;
            fetch(`http://localhost:5001/libros/${book_id}` , {
                method: 'PUT',
                body: JSON.stringify(book),
                mode: "cors",
                headers: {
                    'Content-Type': 'application/json',
                }
            })
                .then((res) => res.json() )
           
                .then(res => {
                    console.log(res) 
                    this.Alert();
                    location.reload()
                    })
            .catch(function(e) {
                console.log(e); 
            })
        },
        onSumbit(){
            let title = document.getElementById("form-title-input").value;
            let subtitle = document.getElementById("form-subttitle-input").value;
            let authors = document.getElementById("form-authors-input").value;
            let publisher = document.getElementById("form-publisher-input").value;
            let description = document.getElementById("form-description-input").value;
            let pageCount = document.getElementById("form-pageCount-input").value;
            let publishedDate = document.getElementById("form-publishedDate-input").value;
            let categories = document.getElementById("form-categories-input").value;
            
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
            this.Updated_Book(book);
        
        },Alert(){
            alert('Updated book')
        }        
    }
    }
            
</script>