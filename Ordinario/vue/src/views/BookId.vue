<template>
    <div class="bookid">
        <br/><br/>
        <div div class="card"  :to="{name: 'Book', params: { id: item } }"
                    v-for= "(item,index) of Book" v-bind:key="index">
            <div class="card-body">
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
                    <router-link  class="navbar-brand" to="/library">Return</router-link>   
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
            Book: []
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
            
                .then((res) =>   res.json().then( data =>   this.Book.push(data) )
                  
                )
           
                .then(res => {   
                    console.log(res) 
                    })
            .catch(function(e) {
                console.log(e); 
            });
      
    }
    }
            
</script>