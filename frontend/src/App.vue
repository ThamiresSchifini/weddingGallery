<template>
  <div>
    <div class="header-container">
      <HeaderComponent :userName="userName" @login="onClickLogin"/>
    </div>

    <div class="body-container">
      <PhotoListComponent :photos="photos"/>
    </div>

    <button class="btn btn-primary w-100 fixed-bottom upload" @click="onClickAddPhoto">
      <h1>ADD PHOTO</h1>
    </button>

    <PhotoUploadModalComponent
        v-show="showUploadPhotoModal"
        @upload="onUploadPhoto"
        @close="closeUploadPhotoModal"
      />

    <LoginModalComponent
        :warning="loginWarning"
        v-show="showLoginModal"
        @login="onLogin"
        @close="closeLoginModal"
      />
  </div>
</template>

<script>
import HeaderComponent from './components/Header'
import PhotoListComponent from './components/PhotoList'
import PhotoUploadModalComponent from './components/PhotoUploadModal'
import {photoService} from "@/services/Photo.service";
import {userService} from "@/services/User.service";
import LoginModalComponent from "@/components/LoginModal";


export default {
  name: 'App',
  components: {
    LoginModalComponent,
    HeaderComponent,
    PhotoListComponent,
    PhotoUploadModalComponent
  },
  methods: {
    // eslint-disable-next-line no-unused-vars
    async onLogin($event, inputName, password) {
      this.loginWarning = '';

      const {name, token} = await userService.postLogin(inputName, password);

      if (!token) {
        this.loginWarning = 'Invalid credentials.';
        return;
      }

      this.userName = name;
      localStorage.setItem('authToken', token);
      localStorage.setItem('authName', name);

      this.closeLoginModal();

      location.reload();
    },
    logout() {
      this.userName = null;

      localStorage.removeItem('authToken');
      localStorage.removeItem('authName');

      this.closeLoginModal();

      location.reload();
    },
    // eslint-disable-next-line no-unused-vars
    async onUploadPhoto($event, description, author, file) {
      await photoService.postPhoto(description, author, file);

      this.closeUploadPhotoModal();
    },
    onClickAddPhoto() {
      this.showUploadPhotoModal = true;
    },
    closeUploadPhotoModal() {
      this.showUploadPhotoModal = false;
    },
    onClickLogin() {
      if ( this.userName ) {
        this.logout();
        return;
      }

      this.showLoginModal = true;
    },
    closeLoginModal() {
      this.showLoginModal = false;
    }
  },
  data() {
    return {
      userName: localStorage.getItem('authName'),
      photos: [],
      showUploadPhotoModal: false,
      loginWarning: '',
      showLoginModal: false,
    }
  },
  async created() {
    this.photos = await photoService.getPhotos();
  },
}
</script>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
}

.body-container {
  position: relative;
  top: 70px;
}

.modal-backdrop {
  position: fixed;
  top: 0;
  bottom: 0;
  left: 0;
  right: 0;
  background-color: rgba(0, 0, 0, 0.3);
  display: flex;
  justify-content: center;
  align-items: center;
}

.modal {
  background: white;
  box-shadow: 2px 2px 20px 1px;
  overflow-x: hidden;
  display: flex;
  flex-direction: column;
  min-width: 75%;
  min-height: 50%;

  max-width: 75%;
  max-height: 60%;
}

.modal-header,
.modal-footer {
  padding: 15px;
  display: flex;
}

.modal-header {
  position: relative;
  border-bottom: 1px solid #eeeeee;
  justify-content: space-between;
}

.modal-footer {
  border-top: 1px solid #eeeeee;
  flex-direction: column;
}

.modal-body {
  position: relative;
  padding: 20px 10px;
}

.btn-close {
  position: absolute;
  top: 0;
  right: 0;
  border: none;
  font-size: 20px;
  padding: 10px;
  cursor: pointer;
  font-weight: bold;
  background: transparent;
}

.modal-fade-enter,
.modal-fade-leave-to {
  opacity: 0;
}

.modal-fade-enter-active,
.modal-fade-leave-active {
  transition: opacity .5s ease;
}

.upload {
    border-radius: 15px 15px 0 0;
}

</style>
