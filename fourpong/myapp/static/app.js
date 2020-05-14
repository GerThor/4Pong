
//LeaderBoards Scores
//Adapted from class example, https://stackoverflow.com/questions/36572540/vue-js-auto-reload-refresh-data-with-timer
var app = new Vue({
  el: '#wins',
  data: {
    wins : [],
  },
  created: function() {
    this.getWinsList();
    this.timer = setInterval(this.getWinsList, 10000); //originally 10000
  },
  methods: {
    getWinsList: function() {
      axios
        .get('/getWins/')
        .then(response => (this.wins = response.data.wins))
    },
    cancelAutoUpdate: function() { clearInterval(this.timer) }
  },
  beforeDestroy() {
    this.cancelAutoUpdate();
  }
})