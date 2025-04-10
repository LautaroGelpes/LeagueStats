document.addEventListener("DOMContentLoaded", () => {
   const game = document.body.getAttribute("data-game");

   const sectionMap = {
       "League_of_legends": "stats-league",
       "Valorant": "stats-valorant",
       "tft": "stats-tft"
   };

   const section = sectionMap[game];
   if (section) {
       document.getElementById(section).style.display = "block";
   }
});