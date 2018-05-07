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
                {title: 'dasdasdasd', date: "active"},
                {title: 'hs0xzczxczx1', date: "active"},
                {title: 'hszxczxvcvnbv01', date: "active"},
                {title: 'hs2342342342301', date: "active"},
                {title: 'hghjgfhjghjgs01', date: "active"}]
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
