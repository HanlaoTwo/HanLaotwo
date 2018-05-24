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
        this.getContent("", "");
        this.setShowList()
    },
    data: {
        catalog: [{'name': 'blog', 'files': ['blog.css', 'blog.html']}, {
            'name': 'index',
            'files': ['index.css', 'index.html']
        }],
        article: "### shen me dong xi",
        content: [],
        VshowList: JSON.parse("{}"),

    },
    methods: {
        getCatalog: function () {
            ins = this;
            return $.ajax({
                type: 'get',
                url: baseUrl + getContent,
                data: {},
                success: function (data) {
                    ins.catalog = JSON.parse(data);
                },
                error: function () {
                    //do something
                }
            });
        },
        getContent: function (dir, name) {
            ins = this;
            return $.ajax({
                type: 'get',
                url: baseUrl + getArticle,
                data: {
                    dir: dir == "" ? "blog" : dir,
                    name: name == "" ? "blog.js" : name
                },
                success: function (data) {
                    ins.article = marked(data);
                },
                error: function () {
                    console.log(dir + "  " + name);
                }
            });
        },
        setShowList: function () {
            ins = this;
            for (item in ins.catalog) {
                showName = item.name;
                ins.VshowList.showName = false;
            }
            console.log("----------")
        },
        setShow: function (name) {
            ins = this;
            ins.VshowList.name = !ins.VshowList.name;
        }


    }

});
