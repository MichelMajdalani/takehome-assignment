<template>
  <div>
    <p>I'm a Counter!</p>
    <p>Current count value: {{currentCount}}</p>
    <button v-on:click="increment">Increment</button>
    <button v-on:click="decrement">Decrement</button>
  </div>
</template>

<script>
export default {
  props: {
    count: {
      default: 0,
      type: Number
    }
  },
  data() {
    return {
      currentCount: this.count
    }
  },
  methods: {
    increment: function() {
      this.currentCount += 1;
    },
    decrement: function() {
      this.currentCount -= 1;
    }
  }
};
</script>

<style>
</style>

