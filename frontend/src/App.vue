<template>
    <v-app>
        <component v-bind:is="layout"></component>
    </v-app>
</template>

<script>
import AppLayout from '@/layouts/AppLayout.vue';
import AuthLayout from '@/layouts/AuthLayout.vue';

export default {
    computed: {
        layout() {
            return this.$route.meta.layout || 'app-layout';
        }
    },
    components: {
        'app-layout': AppLayout,
        'auth-layout': AuthLayout
    }
};
</script>
