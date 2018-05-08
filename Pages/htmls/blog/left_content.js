/**
 * Created by hq on 2018/5/7.
 * /.
 */
Vue.component('left', {
    template: '#left',
    //replace: true,
    props: ['ci'],
    data: function () {
        return {
            host_stata: [
                {title: 'sdasasasdasda', date: "2017.01.01"},
                {title: 'hs0xzczxczx1', date: "2017.01.01"},
                {title: 'hszxczxvcvnbv01', date: "2017.01.01"},
                {title: 'hs2342342342301', date: "2017.01.01"},
                {title: 'hghjgfhjghjgs01', date: "2017.01.01"}]
        }
    },

    methods: {
        fresh: function (key) {
            console.log("hahahahahhahaha")
        },
        stop: function (key) {
            this.host_stata = [{host: 'hs02', state: "active"}]
        },
        start: function (key) {
            this.host_stata = [{host: 'hs03', state: "active"}]
        },
        restart: function (key) {
            this.host_stata = [{host: 'hs04', state: "active"}]
        }
    }
});
