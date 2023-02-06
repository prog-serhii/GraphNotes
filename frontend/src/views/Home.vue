<script setup>
import { VueForceGraph3D } from "vue-force-graph";

const costomData = {
  nodes: [
    {id: 1, group: 1}, {id: 2, group: 2}, {id: 3, group: 5}, {id: 4, group: 3}, {id: 5, group: 4}
  ],
  links: [
    {id: 1, source: 1, target: 2},
    {id: 2, source: 2, target: 3},
    {id: 3, source: 4, target: 3},
    {id: 4, source: 5, target: 3}
  ]
}
</script>

<template>
  <h1>Home Page</h1>
  <VueForceGraph3D backgroundColor="#ffffff" nodeAutoColorBy="group" :linkColor="() => 'rgba(0,0,0,0.5)'" :graph-data="costomData" />
</template>
