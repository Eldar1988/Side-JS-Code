import Vue from 'vue'
import Vuex from 'vuex'
import portfolio from './modules/portfolio'

// import example from './module-example'

Vue.use(Vuex)

/*
 * If not building with SSR mode, you can
 * directly export the Store instantiation;
 *
 * The function below can be async too; either use
 * async/await or return a Promise which resolves
 * with the Store instance.
 */

export default function (/* { ssrContext } */) {
  const Store = new Vuex.Store({
    modules: {
      portfolio
    },
    state: {
      // serverURL: 'http://192.168.0.199:8000'
      serverURL: 'https://api.js-code.ru'
    },
    getters: {
      getServerURL: state => state.serverURL
    },

    // enable strict mode (adds overhead!)
    // for dev mode only
    strict: process.env.DEBUGGING
  })

  return Store
}
