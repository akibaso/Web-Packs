function adBlockNotDetected() {
    console.log("Ok~");
}
function adBlockDetected() {
    if (Cookies.get("ad_notice") !== "0") {
        $j("#skiplinks").after("<div style='background: #efd1d1;border-bottom: 1px solid #900;font-size: .875em;' id='ad-notice'><div class='userstuff' style='padding: .643em .875em'> <p class='important'>您的浏览器屏蔽了我们的广告！</p><ol><li>为了保证此镜像的可持续运行，我们需要展示广告，如果可以，请您对本网站禁用广告屏蔽器</li><li>如果您不知道如何操作，可以尝试参考<a href='https://zh.wikihow.com/%E7%A6%81%E7%94%A8-Adblock'>WikiHow</a></li></ol><p class='submit' style='margin-bottom: 0'><button class='action' type='button' id='ad-notice-dismiss'>Dismiss Notice</button></p></div></div><script>\n//<![CDATA[\n\n  \$j(document).ready(function() {\n    \$j(\"#ad-notice-dismiss\").on(\"click\", function() {\n      Cookies.set(\"ad_notice\", \"0\", { expires: 7 });\n      \$j(\"#ad-notice\").slideUp();\n    });\n  });\n\n//]]]]><![CDATA[>\n<\/script>");
    }
}
if(typeof blockAdBlock !== 'undefined' || typeof BlockAdBlock !== 'undefined') {
    adBlockDetected();
} else {
    var importFAB = document.createElement('script');
    importFAB.onload = function() {
        blockAdBlock.onDetected(adBlockDetected)
        blockAdBlock.onNotDetected(adBlockNotDetected);
    }
    importFAB.onerror = function() {
        adBlockDetected(); 
    }
    importFAB.crossOrigin = 'anonymous';
    importFAB.src = 'https://static.hyh.ink/npm/blockadblock@3.2.1/blockadblock.min.js';
    document.head.appendChild(importFAB);
}