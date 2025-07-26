<script>
import Aside from '@/components/Aside.vue';

export default {
    components: {
        Aside,
    }
}
</script>

<template>
    <div class="row g-5">
        <div class="col-md-8">
            <h2 class="display-4 text-center">Categories</h2>

            <div class="container">
                <div class="row">

                        <div class="col-md-6 mb-4">
                            <a href="">
                            <div class="card">
                                <img src="../assets/1.jpeg" alt="" class="card-img-top">
                                <div class="card-body">
                                    <h5 class="card-title text-center">Category 1</h5>
                                </div>
                            </div>
                            </a>
                        </div>

                        <div class="col-md-6 mb-4">
                            <a href="">
                            <div class="card">
                                <img src="../assets/1.jpeg" alt="" class="card-img-top">
                                <div class="card-body">
                                    <h5 class="card-title text-center">Category 1</h5>
                                </div>
                            </div>
                            </a>
                        </div>

                        <div class="col-md-6 mb-4">
                            <a href="">
                            <div class="card">
                                <img src="../assets/1.jpeg" alt="" class="card-img-top">
                                <div class="card-body">
                                    <h5 class="card-title text-center">Category 1</h5>
                                </div>
                            </div>
                            </a>
                        </div>

                        <div class="col-md-6 mb-4">
                            <a href="">
                            <div class="card">
                                <img src="../assets/1.jpeg" alt="" class="card-img-top">
                                <div class="card-body">
                                    <h5 class="card-title text-center">Category 1</h5>
                                </div>
                            </div>
                            </a>
                        </div>

                </div>
            </div>
        </div>

        <Aside />
    </div>
</template>

<style>
.card img {
    height: 300px;
    object-fit: cover;
}
</style>