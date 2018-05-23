/**
 * Created by hanqian18790 on 2018/5/8.
 * .
 */
Vue.component('mid', {

    template: '#mid',
    props: ['ci'],
    created: function () {
        console.log("-----------")
        this.getArticlebyTitle('查看hdfs根目录下使用量');
    },
    data: function () {
        return {
            content: "<h1>hello</h1>"
        }
    },
    methods: {
        getArticlebyTitle: function (title) {
            md = this;
            return $.ajax({
                type: 'get',
                url: baseUrl + '/get_article/' + title,
                success: function (data) {
                    md.content = marked(JSON.parse(data).content);
                    //document.getElementById('content').innerHTML = md.content;
                },
                error: function () {}
            });
        },
    }

});