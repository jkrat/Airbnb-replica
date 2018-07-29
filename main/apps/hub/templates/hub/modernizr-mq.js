/*! modernizr 3.6.0 (Custom Build) | MIT *
 * https://modernizr.com/download/?-cookies-cssgrid_cssgridlegacy-flash-flexbox-sessionstorage-addtest-mq-setclasses !*/
!function(e,n,t){function o(e,n){return typeof e===n}function r(){var e,n,t,r,i,s,a;for(var l in _)if(_.hasOwnProperty(l)){if(e=[],n=_[l],n.name&&(e.push(n.name.toLowerCase()),n.options&&n.options.aliases&&n.options.aliases.length))for(t=0;t<n.options.aliases.length;t++)e.push(n.options.aliases[t].toLowerCase());for(r=o(n.fn,"function")?n.fn():n.fn,i=0;i<e.length;i++)s=e[i],a=s.split("."),1===a.length?Modernizr[a[0]]=r:(!Modernizr[a[0]]||Modernizr[a[0]]instanceof Boolean||(Modernizr[a[0]]=new Boolean(Modernizr[a[0]])),Modernizr[a[0]][a[1]]=r),w.push((r?"":"no-")+a.join("-"))}}function i(e){var n=k.className,t=Modernizr._config.classPrefix||"";if(x&&(n=n.baseVal),Modernizr._config.enableJSClass){var o=new RegExp("(^|\\s)"+t+"no-js(\\s|$)");n=n.replace(o,"$1"+t+"js$2")}Modernizr._config.enableClasses&&(n+=" "+t+e.join(" "+t),x?k.className.baseVal=n:k.className=n)}function s(e,n){if("object"==typeof e)for(var t in e)b(e,t)&&s(t,e[t]);else{e=e.toLowerCase();var o=e.split("."),r=Modernizr[o[0]];if(2==o.length&&(r=r[o[1]]),"undefined"!=typeof r)return Modernizr;n="function"==typeof n?n():n,1==o.length?Modernizr[o[0]]=n:(!Modernizr[o[0]]||Modernizr[o[0]]instanceof Boolean||(Modernizr[o[0]]=new Boolean(Modernizr[o[0]])),Modernizr[o[0]][o[1]]=n),i([(n&&0!=n?"":"no-")+o.join("-")]),Modernizr._trigger(e,n)}return Modernizr}function a(){return"function"!=typeof n.createElement?n.createElement(arguments[0]):x?n.createElementNS.call(n,"http://www.w3.org/2000/svg",arguments[0]):n.createElement.apply(n,arguments)}function l(){var e=n.body;return e||(e=a(x?"svg":"body"),e.fake=!0),e}function u(e,t,o,r){var i,s,u,f,c="modernizr",d=a("div"),p=l();if(parseInt(o,10))for(;o--;)u=a("div"),u.id=r?r[o]:c+(o+1),d.appendChild(u);return i=a("style"),i.type="text/css",i.id="s"+c,(p.fake?p:d).appendChild(i),p.appendChild(d),i.styleSheet?i.styleSheet.cssText=e:i.appendChild(n.createTextNode(e)),d.id=c,p.fake&&(p.style.background="",p.style.overflow="hidden",f=k.style.overflow,k.style.overflow="hidden",k.appendChild(p)),s=t(d,e),p.fake?(p.parentNode.removeChild(p),k.style.overflow=f,k.offsetHeight):d.parentNode.removeChild(d),!!s}function f(e,n){return!!~(""+e).indexOf(n)}function c(e){return e.replace(/([a-z])-([a-z])/g,function(e,n,t){return n+t.toUpperCase()}).replace(/^-/,"")}function d(e,n){return function(){return e.apply(n,arguments)}}function p(e,n,t){var r;for(var i in e)if(e[i]in n)return t===!1?e[i]:(r=n[e[i]],o(r,"function")?d(r,t||n):r);return!1}function h(e){return e.replace(/([A-Z])/g,function(e,n){return"-"+n.toLowerCase()}).replace(/^ms-/,"-ms-")}function m(n,t,o){var r;if("getComputedStyle"in e){r=getComputedStyle.call(e,n,t);var i=e.console;if(null!==r)o&&(r=r.getPropertyValue(o));else if(i){var s=i.error?"error":"log";i[s].call(i,"getComputedStyle returning null, its possible modernizr test results are inaccurate")}}else r=!t&&n.currentStyle&&n.currentStyle[o];return r}function v(n,o){var r=n.length;if("CSS"in e&&"supports"in e.CSS){for(;r--;)if(e.CSS.supports(h(n[r]),o))return!0;return!1}if("CSSSupportsRule"in e){for(var i=[];r--;)i.push("("+h(n[r])+":"+o+")");return i=i.join(" or "),u("@supports ("+i+") { #modernizr { position: absolute; } }",function(e){return"absolute"==m(e,null,"position")})}return t}function g(e,n,r,i){function s(){u&&(delete E.style,delete E.modElem)}if(i=o(i,"undefined")?!1:i,!o(r,"undefined")){var l=v(e,r);if(!o(l,"undefined"))return l}for(var u,d,p,h,m,g=["modernizr","tspan","samp"];!E.style&&g.length;)u=!0,E.modElem=a(g.shift()),E.style=E.modElem.style;for(p=e.length,d=0;p>d;d++)if(h=e[d],m=E.style[h],f(h,"-")&&(h=c(h)),E.style[h]!==t){if(i||o(r,"undefined"))return s(),"pfx"==n?h:!0;try{E.style[h]=r}catch(y){}if(E.style[h]!=m)return s(),"pfx"==n?h:!0}return s(),!1}function y(e,n,t,r,i){var s=e.charAt(0).toUpperCase()+e.slice(1),a=(e+" "+N.join(s+" ")+s).split(" ");return o(n,"string")||o(n,"undefined")?g(a,n,r,i):(a=(e+" "+z.join(s+" ")+s).split(" "),p(a,n,t))}function C(e,n,o){return y(e,t,t,n,o)}var w=[],_=[],S={_version:"3.6.0",_config:{classPrefix:"",enableClasses:!0,enableJSClass:!0,usePrefixes:!0},_q:[],on:function(e,n){var t=this;setTimeout(function(){n(t[e])},0)},addTest:function(e,n,t){_.push({name:e,fn:n,options:t})},addAsyncTest:function(e){_.push({name:null,fn:e})}},Modernizr=function(){};Modernizr.prototype=S,Modernizr=new Modernizr,Modernizr.addTest("cookies",function(){try{n.cookie="cookietest=1";var e=-1!=n.cookie.indexOf("cookietest=");return n.cookie="cookietest=1; expires=Thu, 01-Jan-1970 00:00:01 GMT",e}catch(t){return!1}}),Modernizr.addTest("sessionstorage",function(){var e="modernizr";try{return sessionStorage.setItem(e,e),sessionStorage.removeItem(e),!0}catch(n){return!1}});var b,k=n.documentElement,x="svg"===k.nodeName.toLowerCase();!function(){var e={}.hasOwnProperty;b=o(e,"undefined")||o(e.call,"undefined")?function(e,n){return n in e&&o(e.constructor.prototype[n],"undefined")}:function(n,t){return e.call(n,t)}}(),S._l={},S.on=function(e,n){this._l[e]||(this._l[e]=[]),this._l[e].push(n),Modernizr.hasOwnProperty(e)&&setTimeout(function(){Modernizr._trigger(e,Modernizr[e])},0)},S._trigger=function(e,n){if(this._l[e]){var t=this._l[e];setTimeout(function(){var e,o;for(e=0;e<t.length;e++)(o=t[e])(n)},0),delete this._l[e]}},Modernizr._q.push(function(){S.addTest=s}),Modernizr.addAsyncTest(function(){var t,o,r=function(e){k.contains(e)||k.appendChild(e)},i=function(e){e.fake&&e.parentNode&&e.parentNode.removeChild(e)},u=function(e,n){var t=!!e;if(t&&(t=new Boolean(t),t.blocked="blocked"===e),s("flash",function(){return t}),n&&h.contains(n)){for(;n.parentNode!==h;)n=n.parentNode;h.removeChild(n)}};try{o="ActiveXObject"in e&&"Pan"in new e.ActiveXObject("ShockwaveFlash.ShockwaveFlash")}catch(f){}if(t=!("plugins"in navigator&&"Shockwave Flash"in navigator.plugins||o),t||x)u(!1);else{var c,d,p=a("embed"),h=l();if(p.type="application/x-shockwave-flash",h.appendChild(p),!("Pan"in p||o))return r(h),u("blocked",p),void i(h);c=function(){return r(h),k.contains(h)?(k.contains(p)?(d=p.style.cssText,""!==d?u("blocked",p):u(!0,p)):u("blocked"),void i(h)):(h=n.body||h,p=a("embed"),p.type="application/x-shockwave-flash",h.appendChild(p),setTimeout(c,1e3))},setTimeout(c,10)}});var T=function(){var n=e.matchMedia||e.msMatchMedia;return n?function(e){var t=n(e);return t&&t.matches||!1}:function(n){var t=!1;return u("@media "+n+" { #modernizr { position: absolute; } }",function(n){t="absolute"==(e.getComputedStyle?e.getComputedStyle(n,null):n.currentStyle).position}),t}}();S.mq=T;var P="Moz O ms Webkit",N=S._config.usePrefixes?P.split(" "):[];S._cssomPrefixes=N;var z=S._config.usePrefixes?P.toLowerCase().split(" "):[];S._domPrefixes=z;var j={elem:a("modernizr")};Modernizr._q.push(function(){delete j.elem});var E={style:j.elem.style};Modernizr._q.unshift(function(){delete E.style}),S.testAllProps=y,S.testAllProps=C,Modernizr.addTest("flexbox",C("flexBasis","1px",!0)),Modernizr.addTest("cssgridlegacy",C("grid-columns","10px",!0)),Modernizr.addTest("cssgrid",C("grid-template-rows","none",!0)),r(),i(w),delete S.addTest,delete S.addAsyncTest;for(var A=0;A<Modernizr._q.length;A++)Modernizr._q[A]();e.Modernizr=Modernizr}(window,document);