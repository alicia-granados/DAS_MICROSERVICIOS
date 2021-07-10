import Vue from 'vue';
import Vuetify from 'vuetify/lib/framework';

Vue.use(Vuetify);

export default new Vuetify({
  theme: {
      options: {
        customProperties: true,
        icons: {
          iconfont: 'mdi', // 'mdi' || 'mdiSvg' || 'md' || 'fa' || 'fa4' || 'faSvg'
        },
      },
    themes: {
      light: {
        primary: '#FF4081',
        secondary: '#FCE4EC',
        accent: '#82B1FF',
        error: '#FF5252',
        info: '#F5F5F5',
        success: '#37474F',
        warning: '#FFC107'
      },
    },
  },
  icons: {
    iconfont: 'md',
  },
});