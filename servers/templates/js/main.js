import Vue from 'vue'
import axios from 'axios'
import VueAxios from 'vue-axios'
Vue.prototype.$axios = axios



Vue.use(VueAxios, axios)