!function(e){var t={};function r(n){if(t[n])return t[n].exports;var o=t[n]={i:n,l:!1,exports:{}};return e[n].call(o.exports,o,o.exports,r),o.l=!0,o.exports}r.m=e,r.c=t,r.d=function(e,t,n){r.o(e,t)||Object.defineProperty(e,t,{enumerable:!0,get:n})},r.r=function(e){"undefined"!=typeof Symbol&&Symbol.toStringTag&&Object.defineProperty(e,Symbol.toStringTag,{value:"Module"}),Object.defineProperty(e,"__esModule",{value:!0})},r.t=function(e,t){if(1&t&&(e=r(e)),8&t)return e;if(4&t&&"object"==typeof e&&e&&e.__esModule)return e;var n=Object.create(null);if(r.r(n),Object.defineProperty(n,"default",{enumerable:!0,value:e}),2&t&&"string"!=typeof e)for(var o in e)r.d(n,o,function(t){return e[t]}.bind(null,o));return n},r.n=function(e){var t=e&&e.__esModule?function(){return e.default}:function(){return e};return r.d(t,"a",t),t},r.o=function(e,t){return Object.prototype.hasOwnProperty.call(e,t)},r.p="",r(r.s=0)}([function(e,t,r){"use strict";r(1),r(2)},function(e,t){const r=document.querySelectorAll("#Sidebar .sidebar-link"),n=document.querySelectorAll("#Questions .question-filter");let{pathname:o}=window.location;"/index.html"===o&&(o="/"),r.forEach(e=>o===e.pathname?e.classList.add("active"):null);const a=()=>{const{hash:e}=window.location;n.forEach(t=>{t.hash===e?t.classList.add("active"):t.classList.remove("active")})};a(),window.addEventListener("hashchange",a)},function(e,t){const r=e=>{e.style.height="inherit";const t=window.getComputedStyle(e),r=parseFloat(t.getPropertyValue("border-top-width"),10)+parseFloat(t.getPropertyValue("padding-top"),10)+e.scrollHeight+parseFloat(t.getPropertyValue("padding-bottom"),10)+parseFloat(t.getPropertyValue("border-bottom-width"),10);e.style.height=r+"px"};document.querySelectorAll("textarea").forEach(e=>{r(e),e.addEventListener("input",e=>r(e.currentTarget))})}]);