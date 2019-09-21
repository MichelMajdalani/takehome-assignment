<template>
  <div>
    <p>I'm a Counter!</p>
    <p>Current count value: {{count}}</p>
    <button v-on:click="increment">Increment</button>
    <button v-on:click="decrement">Decrement</button>
  </div>
</template>

<script>
export default {
  props: {
    count: Number
  },
  methods: {
    increment: function() {
      this.count += 1
    },
    decrement: function() {
      this.count -= 1
    }
  }
};
</script>

<style>
</style>

