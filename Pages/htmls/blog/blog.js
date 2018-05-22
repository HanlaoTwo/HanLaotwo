/**
 * Created by hq on 2018/5/7.
 * ,.
 */
var baseUrl = "http://127.0.0.1:5000";
var demo = new Vue({
    el: '#blog',
    created: function () {
        //this.getClusters()
    },
    data: {
        clusters:["1","2"],
        clusters0: [],
        gridColumns: ['host', 'state'],
        gridData: []
    },
    methods: {
        getClusters: function () {
            ins = this;
            return $.ajax({
                type: 'get',
                url: baseUrl + '/getComps',
                data: {},
                success: function (data) {
                    console.log(data);
                    ins.clusters = setClusters(data);
                    console.log(ins.clusters)
                },
                error: function () {
                    //do something
                }
            });
        }

    }

});
