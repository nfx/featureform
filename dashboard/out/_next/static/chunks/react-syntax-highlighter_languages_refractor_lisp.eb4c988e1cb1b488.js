"use strict";(self.webpackChunk_N_E=self.webpackChunk_N_E||[]).push([[3520],{3848:function(a){function b(a){!function(a){function b(a){return RegExp(/(\()/.source+"(?:"+a+")"+/(?=[\s\)])/.source)}function c(a){return RegExp(/([\s([])/.source+"(?:"+a+")"+/(?=[\s)])/.source)}var d=/(?!\d)[-+*/~!@$%^=<>{}\w]+/.source,e="(\\()",f="(?=\\s)",g=/(?:[^()]|\((?:[^()]|\((?:[^()]|\((?:[^()]|\((?:[^()]|\([^()]*\))*\))*\))*\))*\))*/.source,h={heading:{pattern:/;;;.*/,alias:["comment","title"]},comment:/;.*/,string:{pattern:/"(?:[^"\\]|\\.)*"/,greedy:!0,inside:{argument:/[-A-Z]+(?=[.,\s])/,symbol:RegExp("`"+d+"'")}},"quoted-symbol":{pattern:RegExp("#?'"+d),alias:["variable","symbol"]},"lisp-property":{pattern:RegExp(":"+d),alias:"property"},splice:{pattern:RegExp(",@?"+d),alias:["symbol","variable"]},keyword:[{pattern:RegExp(e+"(?:and|(?:cl-)?letf|cl-loop|cond|cons|error|if|(?:lexical-)?let\\*?|message|not|null|or|provide|require|setq|unless|use-package|when|while)"+f),lookbehind:!0},{pattern:RegExp(e+"(?:append|by|collect|concat|do|finally|for|in|return)"+f),lookbehind:!0}],declare:{pattern:b(/declare/.source),lookbehind:!0,alias:"keyword"},interactive:{pattern:b(/interactive/.source),lookbehind:!0,alias:"keyword"},boolean:{pattern:c(/nil|t/.source),lookbehind:!0},number:{pattern:c(/[-+]?\d+(?:\.\d*)?/.source),lookbehind:!0},defvar:{pattern:RegExp(e+"def(?:const|custom|group|var)\\s+"+d),lookbehind:!0,inside:{keyword:/^def[a-z]+/,variable:RegExp(d)}},defun:{pattern:RegExp(e+/(?:cl-)?(?:defmacro|defun\*?)\s+/.source+d+/\s+\(/.source+g+/\)/.source),lookbehind:!0,greedy:!0,inside:{keyword:/^(?:cl-)?def\S+/,arguments:null,function:{pattern:RegExp("(^\\s)"+d),lookbehind:!0},punctuation:/[()]/}},lambda:{pattern:RegExp(e+"lambda\\s+\\(\\s*(?:&?"+d+"(?:\\s+&?"+d+")*\\s*)?\\)"),lookbehind:!0,greedy:!0,inside:{keyword:/^lambda/,arguments:null,punctuation:/[()]/}},car:{pattern:RegExp(e+d),lookbehind:!0},punctuation:[/(?:['`,]?\(|[)\[\]])/,{pattern:/(\s)\.(?=\s)/,lookbehind:!0}]},i={"lisp-marker":RegExp("&"+d),varform:{pattern:RegExp(/\(/.source+d+/\s+(?=\S)/.source+g+/\)/.source),inside:h},argument:{pattern:RegExp(/(^|[\s(])/.source+d),lookbehind:!0,alias:"variable"},rest:h},j="\\S+(?:\\s+\\S+)*",k={pattern:RegExp(e+g+"(?=\\))"),lookbehind:!0,inside:{"rest-vars":{pattern:RegExp("&(?:body|rest)\\s+"+j),inside:i},"other-marker-vars":{pattern:RegExp("&(?:aux|optional)\\s+"+j),inside:i},keys:{pattern:RegExp("&key\\s+"+j+"(?:\\s+&allow-other-keys)?"),inside:i},argument:{pattern:RegExp(d),alias:"variable"},punctuation:/[()]/}};h.lambda.inside.arguments=k,h.defun.inside.arguments=a.util.clone(k),h.defun.inside.arguments.inside.sublist=k,a.languages.lisp=h,a.languages.elisp=h,a.languages.emacs=h,a.languages["emacs-lisp"]=h}(a)}a.exports=b,b.displayName="lisp",b.aliases=[]}}])