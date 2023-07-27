<template>
  <!-- Основной контент -->
  <!-- <div :[attr]="login">
      <h1>About</h1>
  </div> -->
  <div class="post" v-for="post in posts" :key="post.id">
    <h1>{{ post.title }}</h1>
    <p>{{ post.content }}</p>
    <p>{{ post.time_create }}</p>

  </div>

</template>

<script>
// import компонентов
export default{
  data () {    // Переменные
      return {
          posts: [ ]
      }
  },
  async mounted() { // Компонент монтирован
      const data = await fetch('http://127.0.0.1:8000/api/v1/')
      this.posts = await data.json()
  },
}
</script>

<!-- Стили, если scoped, то только для компонента -->
<style scoped> 
.post{
  width: 400px;
  height: max-content;
  margin-top: 10px;
  background-color: rgb(179, 130, 58);
  color: rgb(0, 0, 0);
}
</style>