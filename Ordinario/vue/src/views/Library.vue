<template >
    <div class="catalogo  table-responsive">
        <br/>
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
                <tr :to="{name: 'Book', params: { id: item } }"
                    v-for= "(item,index) of Book" v-bind:key="index" >
                <th scope="row">{{index}}</th>
                <td>{{ item.title }}</td>
                <td>{{ item.subtitle }}</td>
                <td>{{ item.authors }}</td>
                <td>{{ item.publisher }}}</td>
                <td>{{ item.description }}</td>
                <td>{{ item.pageCount }} </td>
                <td>{{ item.publishedDate }}</td>
                <td>{{ item.categories }} </td>
                <td>
                    <button
                        type="button"
                        class="btn btn-danger btn-sm"
                        @click="removeBook(item)" >
                      Delete
                    </button>
                </td>
            
                </tr>
                
            </tbody>
        </table>
    </div>
</template>

<script>
    
    export default {
    name: 'catalogo',
    components: {
       
    },
    data(){
        return {
            Book:[]
        }
    }, mounted(){
       
        fetch(`http://localhost:5001/libros`)
            .then((res) =>  {
                res.json().then(data => {
                    data.forEach(dt => this.Book.push(dt));
                });
            })


            .then((res) => console.log(res))
        .catch(function(e) {
            console.log(e); 
        });
    },
     methods:{
        removeBook(book_id) {
            fetch(`http://localhost:5001/libros/${book_id._id.$oid}` , {
            method: 'DELETE',
            })
                .then(res => {
                    res.json()
                    this.Alert();
                    location.reload()
                    }) // or res.json() o.text
                .then(res => console.log(res))
            .catch(function(e) {
                console.log(e); 
            });
        },
        Alert(){
            alert('Deleted book')
        }    
        
    }
    }
</script>