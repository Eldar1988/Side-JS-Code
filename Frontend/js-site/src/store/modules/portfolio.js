import axiosInstance from "axios";

export default {
  state: {
    portfolios: null,
    portfolio: null
  },
  actions: {
    async fetchPortfolios({commit}) {
      await axiosInstance.get(`${this.getters.getServerURL}/portfolio/`)
        .then(({data}) => {
          commit('setPortfolios', data)
        })
    },
    async fetchPortfolioDetail({commit}, slug) {
      await axiosInstance.get(`${this.getters.getServerURL}/portfolio/detail/${slug}/`)
        .then(({data}) => {
          commit('setPortfolio', data)
        })
    }
  },
  mutations: {
    setPortfolios(state, data) {
      state.portfolios = data
    },
    setPortfolio(state, data) {
      state.portfolio = data
    }
  },
  getters: {
    getPortfolios: state => state.portfolios,
    getPortfolio: state => state.portfolio
  }
}
