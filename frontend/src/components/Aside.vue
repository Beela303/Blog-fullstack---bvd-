<script>
import axios from 'axios';

export default {
    data() {
        return {
            recentPosts: []
        };
    },

    mounted() {
        this.fetchRecentPosts();
    },

    methods: {
        fetchRecentPosts() {
            axios
                .get("posts/recentposts/")
                .then(response => {
                    this.recentPosts = response.data
                })
                .catch(error => {
                    console.log(error)
                })
        },
    
        formatDate(dateString) {
            const date = new Date(dateString);
            return date.toLocaleDateString('en-US', {
                month: 'long',
                day: 'numeric',
                year: 'numeric'
            });
        }
    },
}
</script>

<template>
    <div class="col-md-4">
        <div class="position-sticky" style="top: 2rem;">
            <div class="p-4 mb-3 bg-body-tertiary rounded text-black">
                <h4 class="fst-italic bg-dark text-white">About</h4>
                <p class="mb-0">This a Blog Project by Nabila Abubakar (@beela303)</p>
            </div>
            <div>
                <h4 class="fst-italic">Recent posts</h4>
                <ul class="list-unstyled" v-for="recentPost in recentPosts" :key="recentPost.id">
                    <li>
                        <router-link
                            class="d-flex flex-column flex-lg-row gap-3 align-items-start align-items-lg-center py-3 link-body-emphasis text-decoration-none border-top text-white"
                            :to="recentPost.get_absolute_url">
                            <img src="../assets/1.jpeg" alt="">
                            <div class="col-lg-8">
                                <h6 class="mb-0">{{ recentPost.title }}</h6>
                                <small class="text-body-secondary">{{ formatDate(recentPost.created_on) }} </small>
                            </div>
                        </router-link>
                    </li>
                </ul>
            </div>
            <!--
            <div class="p-4">
                <h4 class="fst-italic">Archives</h4>
                <ol class="list-unstyled mb-0">
                    <li><a href="#">March 2021</a></li>
                    <li><a href="#">February 2021</a></li>
                    <li><a href="#">January 2021</a></li>
                    <li><a href="#">December 2020</a></li>
                    <li><a href="#">November 2020</a></li>
                    <li><a href="#">October 2020</a></li>
                    <li><a href="#">September 2020</a></li>
                    <li><a href="#">August 2020</a></li>
                    <li><a href="#">July 2020</a></li>
                    <li><a href="#">June 2020</a></li>
                    <li><a href="#">May 2020</a></li>
                    <li><a href="#">April 2020</a></li>
                </ol>
            </div>
            -->
            <div class="p-4">
                <h4 class="fst-italic">Elsewhere</h4>
                <ol class="list-unstyled">
                    <li><a href="https://github.com/beela303" target="_blank" rel="noopener noreferrer">GitHub</a></li>
                    <li><a href="https://x.com/beela303" target="_blank" rel="noopener noreferrer">X</a></li>
                    <li><a href="https://beela303.vercel.app" target="_blank" rel="noopener noreferrer">Website</a></li>
                </ol>
            </div>
        </div>
    </div>
</template>

<style>
.d-flex img {
    width: fit-content;
    height: 96px;
}
</style>