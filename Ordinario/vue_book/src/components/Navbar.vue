<template>
    <v-main xl > 
        <v-app-bar  app class="primary">

            <v-app-bar-nav-icon @click="drawer= !drawer">
                <v-icon
                    large
                    color=" darken-2"
                >
                mdi-dialpad
                </v-icon>
            </v-app-bar-nav-icon>
            <v-toolbar-title>BookStore</v-toolbar-title>


        </v-app-bar>

        <v-navigation-drawer  app v-model="drawer" temporary >
            <v-layout mt-4 column align-center>
                <v-flex>
                    <v-list-item-avatar>
                        <v-img src="@/assets/book.jpg" ></v-img>
                    </v-list-item-avatar>
                </v-flex>
                <v-flex>
                    <p class="dark--text mt-3 headlined">BookStore</p>
                </v-flex>
            </v-layout>
            <v-layout column>
                <v-flex ma-2>
                    <v-btn
                        block
                        color="success"
                        class="mb-3"
                        :to="{name:'Home'}"
                    >
                        Home
                    </v-btn>
                    <v-btn
                        block
                        color="success"
                        class="mb-3"
                        :to="{name:'CRUD_Book'}"
                    >
                        LIST OF BOOKS
                    </v-btn>
                </v-flex>
            </v-layout>
        </v-navigation-drawer>

    </v-main>
</template>

<script>
    export default{
        name: 'Navbar',
        data(){
            return{
                drawer:true
            }
        }
    }
</script>