/**
 * Created by hanqian18790 on 2018/5/8.
 * .
 */
Vue.component('mid', {
    template: '#mid',
    //replace: true,
    props: ['ci'],
    data: function () {
        return {
           content : "这里请避免使用 <select> 元素，因为 WebKit 浏览器不能完全绘制它的样式。"
        }
    }
});