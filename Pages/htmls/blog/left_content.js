/**
 * Created by hq on 2018/5/7.
 * /.
 */
Vue.component('left', {
    template: '#left',
    //replace: true,
    props: ['ci'],
    created: function () {
        this.getList();
    },
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
        getList:function () {
            ins = this;
            return $.ajax({
                type: 'get',
                url: baseUrl + '/get_list',
                data: {},
                success: function (data) {
                    console.log(data);
                    ins.host_stata = data;
                },
                error: function () {
                    //do something
                }
            });
        }
    }
});
