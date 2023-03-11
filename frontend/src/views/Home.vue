<script setup>
import { VueForceGraph3D } from "vue-force-graph";

import { ref } from "vue";

const costomData = {
  nodes: [
    { id: 1 }, { id: 2 }, { id: 3 }, { id: 4 }, { id: 5 }, { id: 6 }, { id: 7 }, { id: 8 }, { id: 9 }, { id: 10 }
  ],
  links: [
    { id: 1, source: 10, target: 9 },
    { id: 2, source: 10, target: 8 },
    { id: 3, source: 9, target: 8 },
    { id: 4, source: 8, target: 7 },
    { id: 5, source: 8, target: 6 },
    { id: 6, source: 6, target: 4 },
    { id: 7, source: 6, target: 5 },
    { id: 8, source: 4, target: 5 },
    { id: 9, source: 5, target: 1 },
    { id: 10, source: 5, target: 2 },
    { id: 11, source: 5, target: 3 },
    { id: 12, source: 1, target: 2 },
    { id: 13, source: 1, target: 3 },
    { id: 14, source: 2, target: 3 },
    { id: 15, source: 6, target: 7 }
  ]
}

</script>

<template>
  <h1>Home Page</h1>
  <VueForceGraph3D 
    backgroundColor="#090723"
    :linkColor="() => 'rgba(255,255,255,0.2)'"
    :graph-data="costomData" 
  />
</template>
