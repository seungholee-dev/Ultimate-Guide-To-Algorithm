import { defineConfig } from "astro/config";
import starlight from "@astrojs/starlight";


// https://astro.build/config
export default defineConfig({
  integrations: [starlight({
    title: "Ultimate Algorithm",
    social: {
      github: "https://github.com/PricelessCode/Ultimate-Guide-To-Algorithm"
    },
    sidebar: [{
      label: "Basics",
      items: [{
        label: "Big O Notation",
        link: "/basics/big-o-notation"
      }, {
        label: "Time Complexity",
        link: "/basics/time-complexity"
      }, {
        label: "Space Complexity",
        link: "/basics/space-complexity"
      }]
    }, {
      label: "Sorting",
      items: [{
        label: "Bubble Sort",
        link: "/sorting/bubble-sort"
      }]
    }]
  })],
  // Process images with sharp: https://docs.astro.build/en/guides/assets/#using-sharp
  image: {
    service: {
      entrypoint: "astro/assets/services/sharp"
    }
  }
});