<script setup>
const props = defineProps({
  note: Object
})
const noteFolders = props.note.folders.map(obj => ({ ...obj, disabled: false }))
</script>

<template>
  <v-hover v-slot="{ isHovering, props }" open-delay="20" close-delay="20">
    <v-card dark outlined shaped :elevation="isHovering ? 16 : 2" :class="{ 'on-hover': isHovering }" class="mx-auto"
      color="#f8e456" max-width="400" v-bind="props">
      <v-card-title>
        {{ note.title }}
      </v-card-title>

      <v-card-subtitle>
        <v-icon size="small" icon="mdi-clock-outline"></v-icon>
        {{ note.datetime }}
      </v-card-subtitle>
      <v-card-text>
        <v-breadcrumbs :items="noteFolders">
          <template v-slot:prepend>
            <v-icon icon="mdi-folder-outline"></v-icon>
          </template>
          <template v-slot:divider>
            <v-icon icon="mdi-chevron-right"></v-icon>
          </template>
        </v-breadcrumbs>
        {{ note.text }}
        <br />
        <br />
        <v-divider />
        <v-chip variant="outlined" color="secondary" class="ma-2" :href="tag.href" :key="tag.href" v-for="tag in note.tags">
          {{ tag.title }}
        </v-chip>

      </v-card-text>
      <v-card-actions>
        <v-spacer></v-spacer>

        <v-btn icon>
          <v-icon>
            mdi-file-edit-outline
          </v-icon>
          <v-tooltip activator="parent" location="top">
            Edit Note
          </v-tooltip>
        </v-btn>

        <v-btn icon>
          <v-icon>
            mdi-delete-outline
          </v-icon>
          <v-tooltip activator="parent" location="top">
            Delete Note
          </v-tooltip>
        </v-btn>

        <v-btn icon>
          <v-icon>
            mdi-heart-outline
          </v-icon>
          <v-tooltip activator="parent" location="top">
            Like Note
          </v-tooltip>
        </v-btn>

      </v-card-actions>
    </v-card>
  </v-hover>
</template>