def BuildStyle():
    return  '''<style>
                   body { background-image: url("https://i.imgur.com/xM8ffTh.png");
                          background-repeat: no-repeat;
                          background-size: 100vw 100vh;
                   }
                   #frame { position: fixed;
                               top: 18vh;
                               left: 31vw;
                               width: 38vw;
                               height: 50vh;
                            background-color: rgb(240,235,225);
                            box-shadow: 10px
                   }
                  .cute {position:fixed; height: 75px;}
a.tooltip {outline:none; }
a.tooltip strong {line-height:30px;}
a.tooltip:hover {text-decoration:none;} 
a.tooltip span {
    z-index:10;display:none; padding:14px 20px;
    margin-top:60px; margin-left:-160px;
    width:300px; line-height:16px;
}
a.tooltip:hover span{
    display:inline; position:absolute; 
    border:2px solid #FFF;  color:#EEE;
    background:#333 url(http://www.menucool.com/tooltip/cssttp/css-tooltip-gradient-bg.png) repeat-x 0 0;
}

.callout {z-index:20;position:absolute;border:0;top:-14px;left:120px;}
    
/*CSS3 extras*/
a.tooltip span
{
    border-radius:2px;        
    box-shadow: 0px 0px 8px 4px #666;
    /*opacity: 0.8;*/
}
</style>''' 
