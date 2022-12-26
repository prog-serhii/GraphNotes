<template>
    <v-card class="mx-auto px-6 py-8" max-width="344">
        <v-form v-model="form" @submit.prevent="handleLogin">
            <v-text-field v-model="email" variant="underlined" :readonly="loading" :rules="[required]" class="mb-2"
                clearable label="Email"></v-text-field>
            <v-text-field v-model="password" variant="underlined" :readonly="loading" :rules="[required]" clearable
                label="Password" placeholder="Enter your password"></v-text-field>
            <br>
            <v-card-actions>
                <v-spacer></v-spacer>
                <v-btn :disabled="!form" :loading="loading" variant="outlined" color="success" type="submit">
                    Login
                    <v-icon icon="mdi-chevron-right" end></v-icon>
                </v-btn>
            </v-card-actions>
            {{ message }}
        </v-form>
    </v-card>
</template>

<script>
export default {
    name: 'LoginForm',
    data: () => ({
        form: false,
        email: null,
        password: null,
        loading: false,
        message: '',
    }),
    computed: {
        loggedIn() {
            return this.$store.state.auth.status.loggedIn;
        }
    },
    created() {
        if (this.loggedIn) {
            this.$router.push('/');
        }
    },
    methods: {
        handleLogin(user) {
            if (!this.form) return

            this.loading = true;

            this.$store.dispatch('auth/login', user).then(
                () => {
                    this.$router.push('/');
                },
                (error) => {
                    this.loading = false;
                    this.message =
                        (error.response &&
                            error.response.data &&
                            error.response.data.message) ||
                        error.message ||
                        error.toString();
                }
            );
        },
        required(v) {
            return !!v || 'Field is required'
        },
    },
};
</script>