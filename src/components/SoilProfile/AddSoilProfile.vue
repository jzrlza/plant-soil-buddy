<template>
  <div>
    <h1>{{ username }} : Add Soil Profile</h1>

    <h3 class="warning" v-if="failed">{{ failed_msg }}</h3>

    <h3>Soil Name : <input v-model="name"></h3>
    <h3>Soil Location : <input v-model="location"></h3>

    <button id="trig-btn" class="normal-btn normal-btn soil-btn submit-btn" v-on:click="add">Add</button>
    <button id="trig-btn" class="normal-btn normal-btn soil-btn" v-on:click="cancel">Cancel</button>

    <loading :active.sync="action" 
        :can-cancel="false" 
        :is-full-page="true"></loading>
    
  </div>
</template>

<script>
import axios from 'axios'
import router from '@/router'

import Loading from 'vue-loading-overlay'
import 'vue-loading-overlay/dist/vue-loading.css'

export default {
  name: 'AddSoilProfile',
  components: { 
    Loading
  },
  data () {
    return {
      username: '',
      name: '',
      location: '',
      failed: false,
      failed_msg: '',
      action: false
    }
  },
  methods: {
    add() {
      this.action = true
      axios.post("/add_soil_profile", {
        'username' : this.username,
        'name': this.name,
        'location': this.location
      })
            .then((response) => {
              
              this.$notify({
                  group: 'notify',
                  title: 'Add Soil Profile',
                  text: response.data
                })
              router.push('main')
              
            })
            .catch((error) => {
              this.action = false
          if (error.response.status >= 400 && error.response.status < 500) {
            this.failed = true
            this.failed_msg = error.response.data
          } else {
            this.failed = true
            this.failed_msg = 'Internal Server Error'
          }
        })
    },
    cancel() {
      router.push('main')
    }


  },
  mounted(){
      this.username = this.$store.state.authUser
  }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
h1 {
  color: #42b983;
}
input {
  height: 25px;
  border: 3px solid #555;
}
input:focus {
  background-color: lightblue;
}
.normal-btn {
  background-color: #4CAF50; /* Green */
  border: none;
  color: white;
  padding: 5px 12px;
  text-align: center;
  text-decoration: none;
  font-size: 16px;
  height: 35px;
  margin-bottom: 30px;
}
.submit-btn {
  background-color: blue;
}
input, .normal-btn {
  width: 200px;
}
.soil-btn {
  margin-left: 10px;
  margin-right: 10px;
}
.warning {
  color: red;
}
</style>