<script>
import axios from 'axios';
import Aside from '@/components/Aside.vue';

export default {
    components : {
      Aside,
    },

    props: [
      'postSlug'
    ],

    data() {
      return {
        postDetail: {},

        comments: [],

        newComment: {
          name : "",
          email : "",
          body : ""
        }
      }
    },

    mounted() {
      this.getPostDetail(),
      this.getPostComments(),
      this.addComment()
    },

    //created(){
     // axios.get('/')
      //  .then(response => {
       //   this.comments = response.data;
        //})
        //.catch(error => {
         // console.log(error);
        //});
    //},

    methods: {
        getPostDetail() {
            const category_slug = this.$route.params.category_slug
            const post_slug = this.$route.params.post_slug

            axios
                .get(`${category_slug}/${post_slug}`)
                .then(response => {
                    this.postDetail= response.data 
                })
                .catch(error => {
                    console.log(error)
                })
        },

        formatDate(date) {
          const dateObject = new Date(date)
          const day = dateObject.getDate().toString().padStart(2, '0')
          const month = (dateObject.getMonth() + 1).toString().padStart(2, '0')
          const year = dateObject.getFullYear()
          return `${day}/${month}/${year}`
        },

        getPostComments() {
            const post_slug = this.$route.params.post_slug

            axios
                .get(`comments/${post_slug}`)
                .then(response => {
                    this.comments= response.data 
                })
                .catch(error => {
                    console.log(error)
                })
        },

        addComment() {
          const post_slug = this.$route.params.post_slug

          axios
            .post(`comments/${post_slug}`, this.newComment)
            .then(response => {
              this.comments.push(response.data);
              this.newComment.name = "";
              this.newComment.email = "";
              this.newComment.body = "";
            })
            .catch(error => {
              console.error(error);
            });
        }
    }
}
</script>

<template>
  <div class="row g-5">
    <div class="col-md-8">
      <h3 class="pb-4 mb-4 fst-italic border-bottom">
        From the Empress
      </h3>
      <article class="blog-post">
        <h2 class="display-5 link-body-emphasis mb-1">{{ postDetail.title }}</h2>
        <h3>Category: {{ postDetail.category }}</h3>
        <p class="blog-post-meta">Created on : {{ formatDate(postDetail.created_on) }} by <a href="#">{{ postDetail.author }}</a></p>
        <p class="blog-post-meta">Updated on : {{ formatDate(postDetail.updated_on) }}</p>
        <p>{{ postDetail.content }}</p>
        <!--<p>This blog post shows a few different types of content that’s supported and styled with Bootstrap.
          Basic typography, lists, tables, images, code, and more are all supported as expected.</p>
        <hr>
        <p>This is some additional paragraph placeholder content. It has been written to fill the available
          space and show how a longer snippet of text affects the surrounding content. We'll repeat it
          often to keep the demonstration flowing, so be on the lookout for this exact same string of
          text.</p>
        <h2>Blockquotes</h2>
        <p>This is an example blockquote in action:</p>
        <blockquote class="blockquote">
          <p>Quoted text goes here.</p>
        </blockquote>
        <p>This is some additional paragraph placeholder content. It has been written to fill the available
          space and show how a longer snippet of text affects the surrounding content. We'll repeat it
          often to keep the demonstration flowing, so be on the lookout for this exact same string of
          text.</p>
        <h3>Example lists</h3>
        <p>This is some additional paragraph placeholder content. It's a slightly shorter version of the
          other highly repetitive body text used throughout. This is an example unordered list:</p>
        <ul>
          <li>First list item</li>
          <li>Second list item with a longer description</li>
          <li>Third list item to close it out</li>
        </ul>
        <p>And this is an ordered list:</p>
        <ol>
          <li>First list item</li>
          <li>Second list item with a longer description</li>
          <li>Third list item to close it out</li>
        </ol>
        <p>And this is a definition list:</p>
        <dl>
          <dt>HyperText Markup Language (HTML)</dt>
          <dd>The language used to describe and define the content of a Web page</dd>
          <dt>Cascading Style Sheets (CSS)</dt>
          <dd>Used to describe the appearance of Web content</dd>
          <dt>JavaScript (JS)</dt>
          <dd>The programming language used to build advanced Web sites and applications</dd>
        </dl>
        <h2>Inline HTML elements</h2>
        <p>HTML defines a long list of available inline tags, a complete list of which can be found on the
          <a href="https://developer.mozilla.org/en-US/docs/Web/HTML/Element">Mozilla Developer
            Network</a>.
        </p>
        <ul>
          <li><strong>To bold text</strong>, use <code
              class="language-plaintext highlighter-rouge">&lt;strong&gt;</code>.</li>
          <li><em>To italicize text</em>, use <code class="language-plaintext highlighter-rouge">&lt;em&gt;</code>.</li>
          <li>Abbreviations, like <abbr title="HyperText Markup Language">HTML</abbr> should use <code
              class="language-plaintext highlighter-rouge">&lt;abbr&gt;</code>, with an optional <code
              class="language-plaintext highlighter-rouge">title</code> attribute for the full phrase.
          </li>
          <li>Citations, like <cite>— Mark Otto</cite>, should use <code
              class="language-plaintext highlighter-rouge">&lt;cite&gt;</code>.</li>
          <li><del>Deleted</del> text should use <code class="language-plaintext highlighter-rouge">&lt;del&gt;</code>
            and <ins>inserted</ins>
            text should use <code class="language-plaintext highlighter-rouge">&lt;ins&gt;</code>.</li>
          <li>Superscript <sup>text</sup> uses <code class="language-plaintext highlighter-rouge">&lt;sup&gt;</code> and
            subscript
            <sub>text</sub> uses <code class="language-plaintext highlighter-rouge">&lt;sub&gt;</code>.
          </li>
        </ul>
        <p>Most of these elements are styled by browsers with few modifications on our part.</p>
        <h2>Heading</h2>
        <p>This is some additional paragraph placeholder content. It has been written to fill the available
          space and show how a longer snippet of text affects the surrounding content. We'll repeat it
          often to keep the demonstration flowing, so be on the lookout for this exact same string of
          text.</p>
        <h3>Sub-heading</h3>
        <p>This is some additional paragraph placeholder content. It has been written to fill the available
          space and show how a longer snippet of text affects the surrounding content. We'll repeat it
          often to keep the demonstration flowing, so be on the lookout for this exact same string of
          text.</p>
        <pre><code>Example code block</code></pre>
        <p>This is some additional paragraph placeholder content. It's a slightly shorter version of the
          other highly repetitive body text used throughout.</p> -->
      </article>
      <nav class="blog-pagination" aria-label="Pagination"> <a class="btn btn-outline-primary rounded-pill"
          href="#">Older</a> <a class="btn btn-outline-secondary rounded-pill disabled" aria-disabled="true">Newer</a>
      </nav>

      <div id="details">
        <h2>Comments</h2>

        <ul>
          <li v-for="comment in comments" :key="comment.id">
            {{ comment.name }} at  {{ formatDate(comment.created_on) }}  : {{ comment.body }}
          </li>
        </ul>

        <form @submit.prevent="addComment">
          <input v-model="newComment.name" placeholder="Name">
          <input v-model="newComment.email" placeholder="E-mail">
          <textarea v-model="newComment.body" placeholder="Content"></textarea>

          <button type="submit" v-on:click="addComment">Add Comment</button>
        </form>
      </div>
    </div>

  <Aside />

  </div>
</template>

<style>

</style>