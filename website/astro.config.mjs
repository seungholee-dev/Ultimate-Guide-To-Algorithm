import { defineConfig } from "astro/config";
import starlight from "@astrojs/starlight";

// https://astro.build/config
export default defineConfig({
    integrations: [
        starlight({
            title: "Ultimate Algorithm",
            social: {
                github: "https://github.com/PricelessCode/Ultimate-Guide-To-Algorithm",
            },
            sidebar: [
                {
                    label: "Basics",
                    items: [
                        {
                            label: "Big O Notation",
                            link: "/basics/big-o-notation",
                        },
                        {
                            label: "Time Complexity",
                            link: "/basics/time-complexity",
                        },
                        {
                            label: "Space Complexity",
                            link: "/basics/space-complexity",
                        },
                    ],
                },
                {
                    label: "Sorting",
                    items: [
                        {
                            label: "Bubble Sort",
                            link: "/sorting/bubble-sort",
                        },
                        {
                            label: "Selection Sort",
                            link: "/sorting/selection-sort",
                        },
                        {
                            label: "Insertion Sort",
                            link: "/sorting/insertion-sort",
                        },
                        {
                            label: "Merge Sort",
                            link: "/sorting/merge-sort",
                        },
                        {
                            label: "Quick Sort",
                            link: "/sorting/quick-sort",
                        },
                        {
                            label: "Counting Sort",
                            link: "/sorting/counting-sort",
                        },
                        {
                            label: "Radix Sort",
                            link: "/sorting/radix-sort",
                        },
                        {
                            label: "Bucket Sort",
                            link: "/sorting/bucket-sort",
                        },
                    ],
                },
                {
                    label: "Dynamic Programming",
                    items: [
                        {
                            label: "Knapsack Problems",
                            link: "/dp/knapsack",
                        },
                        {
                            label: "Kadane's Algorithm",
                            link: "/dp/kadanes-algorithm",
                        },
                    ],
                },
                // {
                //     label: "Searching",
                //     items: [
                //         {
                //             label: "Bubble Sort",
                //             link: "/sorting/bubble-sort",
                //         },
                //     ],
                // },
                // {
                //     label: "Hash Map",
                //     items: [
                //         {
                //             label: "Bubble Sort",
                //             link: "/sorting/bubble-sort",
                //         },
                //     ],
                // },
                // {
                //     label: "Hash Set",
                //     items: [
                //         {
                //             label: "Bubble Sort",
                //             link: "/sorting/bubble-sort",
                //         },
                //     ],
                // },
                // {
                //     label: "Searching",
                //     items: [
                //         {
                //             label: "Bubble Sort",
                //             link: "/sorting/bubble-sort",
                //         },
                //     ],
                // },
                // {
                //     label: "Linked List",
                //     items: [
                //         {
                //             label: "Bubble Sort",
                //             link: "/sorting/bubble-sort",
                //         },
                //     ],
                // },
                {
                    label: "Two Pointer",
                    items: [
                        {
                            label: "Overview",
                            link: "/two-pointer/overview",
                        },
                        {
                            //https://leetcode.com/discuss/study-guide/1905453/master-in-two-pointer
                            //https://tarunjain07.medium.com/two-pointers-notes-4d1400357437
                            label: "Collision Pointers",
                            link: "/two-pointer/collision-pointers",
                        },
                        {
                            label: "Forward Pointers",
                            link: "/two-pointer/forward-pointers",
                        },
                        {
                            label: "Parallel Pointers",
                            link: "/two-pointer/parallel-pointers",
                        },
                        {
                            label: "Fast and Slow Pointer",
                            link: "/two-pointer/fast-slow-pointers",
                        },
                        {
                            label: "Two Pointers with Binary Search",
                            link: "/two-pointer/fast-slow-pointers",
                        },
                    ],
                },
                // {
                //     label: "Tree",
                //     items: [
                //         {
                //             label: "Bubble Sort",
                //             link: "/sorting/bubble-sort",
                //         },
                //     ],
                // },
                // {
                //     label: "Graph",
                //     items: [
                //         {
                //             label: "Bubble Sort",
                //             link: "/sorting/bubble-sort",
                //         },
                //     ],
                // },
                // {
                //     label: "Disjoint Set",
                //     items: [
                //         {
                //             label: "Bubble Sort",
                //             link: "/sorting/bubble-sort",
                //         },
                //     ],
                // },
            ],
        }),
    ],
    // Process images with sharp: https://docs.astro.build/en/guides/assets/#using-sharp
    image: {
        service: {
            entrypoint: "astro/assets/services/sharp",
        },
    },
});
