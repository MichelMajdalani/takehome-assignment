<template>
  <div>
    <Instructions complete />
    <Show
      v-for="show in shows"
      :key="show.id"
      :id="show.id"
      :name="show.name"
      :episodes_seen="show.episodes_seen"
    />
    <input placeholder="name">
    <button type="button" v-on:click="add_data">Submit</button>
  </div>
</template>

<script>
import Instructions from "./Instructions.vue";
import Show from "./Show.vue";

export default {
  components: {
    Instructions,
    Show
  },
  methods: {
    add_data: function (event) {
      let name = document.querySelector("input").value;
      this.shows.push({id: (this.shows.length+1), name: name, episodes_seen: 0});
      document.querySelector("input").value = "";
    }
  },
  data() {
    return {
      shows: [
        { id: 1, name: "Game of Thrones", episodes_seen: 0 },
        { id: 2, name: "Naruto", episodes_seen: 220 },
        { id: 3, name: "Black Mirror", episodes_seen: 3 }
      ]
    };
  }
};
</script>

<style>
</style>


