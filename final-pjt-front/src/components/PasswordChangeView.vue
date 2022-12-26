<template>
  <div>
    <h1>비밀번호 변경</h1>
    <form>
      <label for="username"> username : {{loginUser.username}}</label><br>
      <label for="password"> password : </label>
      <input type="password" v-model="new_password1" /><br>
      <label for="password"> password 확인 : </label>
      <input type="password" v-model="new_password2" /><br>
      <button @click="updatePassword">비밀번호 변경</button>
    </form>
  </div>
</template>

<script>
import axios from "axios"
const API_URL = "http://localhost:8000"

export default {
  name: "PasswordChangeView",
  data(){
    return{
        new_password1 : null,
        new_password2 : null,
    }
  },
  computed : {
    loginUser() {
      return this.$store.getters.getUser;
    },
  },
  methods : {
    updatePassword(){
      axios({
        method: 'post',
        url: `${API_URL}/accounts/password/change/`,
        data: {
            new_password1 : this.new_password1,
            new_password2 : this.new_password2,
        },
        headers: {
          Authorization: `Token ${this.$store.state.token}`,
        },
      })
      .then(() => {
          alert('비밀번호가 변경되었습니다.')
        })
        .catch(error => {
          console.log(error)
        })
    },
  }
};
</script>

<style>
</style>