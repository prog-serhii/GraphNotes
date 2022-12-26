import { createWebHistory, createRouter } from 'vue-router';

import Home from '@/views/Home.vue';
import About from '@/views/About.vue';
import Login from '@/views/Login.vue';
import NotFound from '@/views/NotFound.vue';


const routes = [
    {
        path: '/',
        name: 'Home',
        component: Home,
    },
    {
        path: '/login',
        name: 'Login',
        component: Login,
        meta: {
            layout: 'auth-layout'
        },
    },
    {
        path: '/sign-up',
        name: 'SignUp',
        component: Home,
        meta: {
            layout: 'auth-layout'
        }
    },
    {
        path: '/about',
        name: 'About',
        component: About,
    },
    {
        path: '/:catchAll(.*)',
        component: NotFound,
    },
];

const router = createRouter({
    history: createWebHistory(),
    routes
});

// handle unauthorized access
router.beforeEach((to, from, next) => {
    const publicPages = ['/login', '/sign-up', '/'];
    const authRequired = !publicPages.includes(to.path);
    const loggedIn = localStorage.getItem('user');

    // trying to access a restricted page + not logged in
    // redirect to login page
    if (authRequired && !loggedIn) {
        next('/login');
    } else {
        next();
    }
});

export default router;

