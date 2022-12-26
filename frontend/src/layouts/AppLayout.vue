<template>
    <v-app>
        <SideBar />
        <v-app-bar color="grey-lighten-2">
            <BottomMenu />
        </v-app-bar>
        <v-main>
            <router-view />
        </v-main>
    </v-app>
</template>

<script setup>
import SideBar from '@/components/SideBar.vue';
import BottomMenu from '@/components/BottomMenu.vue'
</script>

<script>
export default {}
</script>