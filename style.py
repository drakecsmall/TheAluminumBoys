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
		.tooltip {
    position: relative;
    display: inline-block;
    border-bottom: 1px dotted black; /* If you want dots under the hoverable text */
}

/* Tooltip text */
.tooltip .tooltiptext {
    visibility: hidden;
    width: 120px;
    background-color: black;
    color: #fff;
    text-align: center;
    padding: 5px 0;
    border-radius: 6px;
 
    /* Position the tooltip text - see examples below! */
    position: absolute;
    z-index: 1;
}

/* Show the tooltip text when you mouse over the tooltip container */
.tooltip:hover .tooltiptext {
    visibility: visible;
}
               </style>''' 
