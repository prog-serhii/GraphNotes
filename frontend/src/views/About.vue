<template>
  <h1>About Page</h1>
  <NoteCard :note="note_example"/>
</template>

<script setup>
import NoteCard from "@/components/NoteCard.vue"
</script>

<script>
import NotesService from "@/services/NotesService"

export default {
  name: "About",
  data: () => ({
    note_example: {
      title: "Some title",
      datetime: "10.10.22 22:22",
      folders: [
        {
          title: "Folder 1",
          href: "folder-1"
        },
        {
          title: "Folder 2",
          href: "folder-2"
        }
      ],
      text: "Some text",
      tags: [
        {
          title: "Title 1",
          href: "tag-1"
        },
        {
          title: "Title 2",
          href: "tag-2"
        },
        {
          title: "Title 2",
          href: "tag-2"
        }
      ],
      href: "note-1"
    },
  }),
  methods: {
    retrieveNotes() {
      NotesService.getAll()
        .then(response => {
          this.notes = response.data;
          console.log(response.data)
        })
        .catch(e => {
          console.log(e);
        });
    }
  },
  mounted() {
    // this.retrieveNotes();
  }
};
</script>