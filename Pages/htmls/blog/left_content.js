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
            host_stata: []
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
