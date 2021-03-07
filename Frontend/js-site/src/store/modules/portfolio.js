import axiosInstance from "axios";

export default {
  state: {
    portfolios: null
  },
  actions: {
    async fetchPortfolios({commit}) {
      await axiosInstance.get(`${this.getters.getServerURL}/portfolio/`)
        .then(({data}) => {
          commit('setPortfolios', data)
        })
    }
  },
  mutations: {
    setPortfolios(state, data) {
      state.portfolios = data
    }
  },
  getters: {
    getPortfolios: state => state.portfolios
  }
}
