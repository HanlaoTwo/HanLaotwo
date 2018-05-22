/**
 * Created by hq on 2018/5/7.
 * /.
 */
Vue.component('left', {
    template: '#left',
    props: ['ci'],
    created: function () {
        this.getList();
    },
    data: function () {
        return {
            lcdata: [{'title': 'test'}, {'title': 'test'}, {'title': 'test'}, {'title': 'test'}]
        }
    },

    methods: {
        getList: function () {
            lc = this;
            return $.ajax({
                type: 'get',
                url: baseUrl + '/get_list',
                success: function (data) {
                    lc.lcdata =  JSON.parse(data)
                },
                error: function () {}
            });
        },

    }
});
