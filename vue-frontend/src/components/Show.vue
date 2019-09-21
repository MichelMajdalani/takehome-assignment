<template>
  <div>
    <h3>{{name}}</h3>
    <Counter :count="episodes_seen"></Counter>
  </div>
</template>

<script>
import Counter from "./Counter.vue";

export default {
  components: {
    Counter
  },
  props: {
    id: Number,
    name: String,
    episodes_seen: Number
  }
};
</script>
<style>
</style>
