<template>
    <div class="container" id="signupContainer">
        <!-- <div class="container">
        <div class="c1">
            
            <div class="c11">
                <h1 class="mainhead">PICK YOUR SPOT</h1>
                <p class="mainp">Just click the buttons below to toggle between SignIn & SignUp</p>
            </div>
            <div id="left"><h1 class="s1class"><span>SIGN</span><span class="su">IN</span>
            </h1></div>
            <div id="right"><h1 class="s2class"><span>SIGN</span><span class="su">UP</span></h1></div>
        </div>
        <div class="c2">
            <form class="signup">
                <h1 class="signup1">SIGN UP</h1>
                <br><br><br><br>
                    <input name="username" type="text" placeholder="Username*" class="username"/>
                    
                    <input name="email" type="text" placeholder="Email*" class="username"/>
                    
                    <input name="password" type="password" placeholder="Password*" class="username"/>
                
                <button class="btn">Sign Up</button>
            </form>
            <form class="signin">
                
                <h1 class="signup1">SIGN IN</h1>
                <br><br><br><br>
                <input name="username" type="text" placeholder="Username*" class="username"/>
                    
                    <input name="password" type="password" placeholder="Password*" class="username"/>
                
                <button class="btn">Get Started</button>
                
                <br><br><br><br>
                <a href=""><p class="signup2">Forget Password?</p></a>
            </form>
            
        </div>
        </div> -->





        <!-- <h1>Sign Up</h1> -->
        <form @submit.prevent="signUp">
            <input
                id="username"
                class="formInput"
                type="text"
                v-model="username"
                placeholder="ID">
            <br>
            <input
                id="password1"
                class="formInput"
                type="password"
                v-model="password1"
                placeholder="PASSWORD">
            <br>
            <input
                id="password2"
                class="formInput"
                type="password"
                v-model="password2"
                placeholder="PASSWORD CONFIRM">
            <br>            
            
            <input
                type="submit"
                value="Sign Up"
                class="submitBtn">
        </form>
    </div>
</template>

<script>
export default {
    name: 'SignUpView',
    data() {
        return {
            username : null,
            password1 : null,
            password2 : null
        }
    },
    methods: {
        // 회원가입 후 회원정보 객체에 담아 store에 저장해주기
        signUp() {
            const username = this.username
            const password1 = this.password1
            const password2 = this.password2

            const payload = {
                username, password1, password2
            }
            
            this.$store.dispatch('signUp', payload)
        }
    }
}


</script>

<style>
@import '@/style/login_signup.css';
</style>