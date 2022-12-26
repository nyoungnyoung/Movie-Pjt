<template>
  <div>
    <form class="input_box">
      <h1>{{ username }} 프로필 편집</h1>
      <button @click.prevent="passwordForm">비밀번호 변경</button>
      <div v-show="password">
        <h1>비밀번호 변경</h1>
        <form>
          <p> username : {{ loginUser.username }}</p>
          <label for="password"> password : </label>
          <input type="password" v-model="new_password1" /><br />
          <label for="password"> password 확인 : </label>
          <input type="password" v-model="new_password2" /><br />
          <button @click="updatePassword">비밀번호 변경</button>
        </form>
      </div>
      <div>
        <div class="input_content">
          <h5>이름</h5>
          <input type="text" v-model="realname" />
        </div>
        <div class="input_content">
          <h5>소개</h5>
          <input type="text" v-model="introduction" />
        </div>
        <div class="input_content">
        </div>
        <button type="submit" @click="setUser">수정 완료</button>      
      </div>
    </form>
      <!-- <h5>프로필 이미지</h5>
    <form @submit.prevent="onInputImage" enctype="multipart/form-data">
    <input type="file" id="fileInput">
    <input type="submit" value="아아 가라좀">
    </form> -->
  </div>
</template>

<script>
import axios from "axios";
const API_URL = "http://localhost:8000";
export default {
  name: "ProfileEditView",
  data() {
    return {
      image: null,
      user: null,
      username: this.$route.params.username,
      realname: null,
      introduction: null,
      password: false,
      new_password1 : null,
        new_password2 : null,
    };
  },

  computed:{
    loginUser() {
      return this.$store.getters.getUser;
    },
  },
  methods: {
    onInputImage() {
            const fileInput = document.querySelector("#fileInput")
            var formData = new FormData()
            formData.append('image', fileInput.files[0])
            axios({
                method: 'post',
                url: `${API_URL}/accountsinfo/${this.username}/hihi/`,
                data: formData,
                headers: {
                    'Authorization': `Token ${ this.$store.state.token }`,
                    'Content-Type': 'multipart/form-data', // Content-Type을 변경해야 파일이 전송됨
                },
            })
            .then((res) => {
                console.log(res)
            })
            .catch((err => {
                console.log(err)
            }))
        },
    passwordForm() {
      this.password = !this.password;
    },
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
    uploadImage() {
      const file = document.querySelector('#inputFile')
      let form = new FormData()
      form.append('img',file.files[0])
      axios({
        method: "post",
        url: `${API_URL}/accountsinfo/hihi/`,
        data : form,
        headers: {
          Authorization: `Token ${this.$store.state.token}`,
          'Content-Type':'multipart/form-data',
        },
      })
        .then((res) => {
          console.log("받은것", res.data);
        })
        .catch((error) => {
          console.log(error);
        });
    },
    setUser() {
      axios({
        method: "post",
        url: `${API_URL}/accountsinfo/${this.username}/update/`,
        headers: {
          Authorization: `Token ${this.$store.state.token}`,
        },
        data: {
          introduction: this.introduction,
          realname: this.realname,
        },
      })
        .then(() => {
          
        })
        .catch((error) => {
          console.log(error);
        });
    },
    getUserInfo() {
      axios({
        method: "get",
        url: `${API_URL}/accountsinfo/${this.username}/`,
        headers: {
          Authorization: `Token ${this.$store.state.token}`,
        },
      })
        .then((response) => {
          this.user = response.data;
          this.introduction = this.user?.introduction;
          this.realname = this.user?.name;
          this.profile_image_url = this.user?.profile_image_url;
        })
        .catch(() => {
          alert("존재하지 않는 사용자입니다.");
          this.$router.go(-1);
        });
    },
    created() {
      this.getUserInfo();
    },
  },
};
</script>

<style>
.input_box {
  padding: 20px;
  margin: 10px;
  border: 3px solid rgb(176, 176, 176);
  border-radius: 20px;
}
.input_content {
  margin: 20px;
  padding: 20px;
}
.input_content input[type="text"] {
  border: 2px solid gray;
  border-radius: 10px;
  height: 40px;
}
.input_box button {
  width: 300px;
  height: 40px;
  border-radius: 5px;
  border: none;
  background-color: rgb(156, 156, 156);
  color: white;
  font-weight: bolder;
}
.input_box h5 {
  font-weight: bolder;
}
</style>