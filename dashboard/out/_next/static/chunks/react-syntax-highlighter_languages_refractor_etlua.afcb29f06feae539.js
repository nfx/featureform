"use strict";(self.webpackChunk_N_E=self.webpackChunk_N_E||[]).push([[8126,8119,3047],{66055:function(a,b,c){var d=c(59803),e=c(93205);function f(a){var b;a.register(d),a.register(e),(b=a).languages.etlua={delimiter:{pattern:/^<%[-=]?|-?%>$/,alias:"punctuation"},"language-lua":{pattern:/[\s\S]+/,inside:b.languages.lua}},b.hooks.add("before-tokenize",function(a){b.languages["markup-templating"].buildPlaceholders(a,"etlua",/<%[\s\S]+?%>/g)}),b.hooks.add("after-tokenize",function(a){b.languages["markup-templating"].tokenizePlaceholders(a,"etlua")})}a.exports=f,f.displayName="etlua",f.aliases=[]},59803:function(a){function b(a){a.languages.lua={comment:/^#!.+|--(?:\[(=*)\[[\s\S]*?\]\1\]|.*)/m,string:{pattern:/(["'])(?:(?!\1)[^\\\r\n]|\\z(?:\r\n|\s)|\\(?:\r\n|[^z]))*\1|\[(=*)\[[\s\S]*?\]\2\]/,greedy:!0},number:/\b0x[a-f\d]+(?:\.[a-f\d]*)?(?:p[+-]?\d+)?\b|\b\d+(?:\.\B|(?:\.\d*)?(?:e[+-]?\d+)?\b)|\B\.\d+(?:e[+-]?\d+)?\b/i,keyword:/\b(?:and|break|do|else|elseif|end|false|for|function|goto|if|in|local|nil|not|or|repeat|return|then|true|until|while)\b/,function:/(?!\d)\w+(?=\s*(?:[({]))/,operator:[/[-+*%^&|#]|\/\/?|<[<=]?|>[>=]?|[=~]=?/,{pattern:/(^|[^.])\.\.(?!\.)/,lookbehind:!0}],punctuation:/[\[\](){},;]|\.+|:+/}}a.exports=b,b.displayName="lua",b.aliases=[]},93205:function(a){function b(a){!function(a){function b(a,b){return"___"+a.toUpperCase()+b+"___"}Object.defineProperties(a.languages["markup-templating"]={},{buildPlaceholders:{value:function(c,d,e,f){if(c.language===d){var g=c.tokenStack=[];c.code=c.code.replace(e,function(a){if("function"==typeof f&&!f(a))return a;for(var e,h=g.length;-1!==c.code.indexOf(e=b(d,h));)++h;return g[h]=a,e}),c.grammar=a.languages.markup}}},tokenizePlaceholders:{value:function(c,d){if(c.language===d&&c.tokenStack){c.grammar=a.languages[d];var e=0,f=Object.keys(c.tokenStack);g(c.tokens)}function g(h){for(var i=0;i<h.length&&!(e>=f.length);i++){var j=h[i];if("string"==typeof j||j.content&&"string"==typeof j.content){var k=f[e],l=c.tokenStack[k],m="string"==typeof j?j:j.content,n=b(d,k),o=m.indexOf(n);if(o> -1){++e;var p=m.substring(0,o),q=new a.Token(d,a.tokenize(l,c.grammar),"language-"+d,l),r=m.substring(o+n.length),s=[];p&&s.push.apply(s,g([p])),s.push(q),r&&s.push.apply(s,g([r])),"string"==typeof j?h.splice.apply(h,[i,1].concat(s)):j.content=s}}else j.content&&g(j.content)}return h}}}})}(a)}a.exports=b,b.displayName="markupTemplating",b.aliases=[]}}])