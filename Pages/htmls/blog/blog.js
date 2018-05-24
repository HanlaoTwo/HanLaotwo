/**
 * Created by hq on 2018/5/7.
 * ,.
 */
var baseUrl = "http://127.0.0.1:5000";
var getArticle = "/get_article";
var getContent = "/get_conetnt";
var demo = new Vue({
    el: '#blog',
    created: function () {
        this.getCatalog();
        this.getContent("","")
    },
    data: {
        catalog:[{'name': 'blog', 'files': ['blog.css', 'blog.html']}, {'name': 'index', 'files': ['index.css', 'index.html']}],
        article: "### shen me dong xi",
        content: [],
    },
    methods: {
        getCatalog: function () {
            ins = this;
            return $.ajax({
                type: 'get',
                url: baseUrl + getContent,
                data: {},
                success: function (data) {
                    console.log(data);
                    ins.catalog = JSON.parse(data);
                    console.log(ins.catalog)
                },
                error: function () {
                    //do something
                }
            });
        },
        getContent: function (dir,name) {
            ins = this;
            return $.ajax({
                type: 'get',
                url: baseUrl + getArticle,
                data: {
                    dir:dir==""?"blog":dir,
                    name:name==""?"blog.js":name
                },
                success: function (data) {
                    console.log(data);
                    ins.article =  marked(data);
                    console.log(ins.article)
                },
                error: function () {
                    console.log(dir+"  "+name);
                }
            });
        }

    }

});
