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
                    label: "Searching",
                    items: [
                        {
                            label: "Linear Search",
                            link: "/searching/linear-search",
                        },
                        {
                            label: "Binary Search",
                            link: "/searching/binary-search",
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
                    label: "HashMap",
                    items: [],
                },
                {
                    label: "Stack & Queue",
                    items: [],
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
                {
                    label: "Backtracking",
                    items: [
                        {
                            label: "General",
                            link: "/backtracking/general",
                        },
                    ],
                },
                {
                    label: "Greedy",
                    items: [],
                },

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
                            link: "/two-pointer/pointers-with-binary-search",
                        },
                    ],
                },
                {
                    label: "String",
                    items: [],
                },
                {
                    label: "ArrayList",
                    items: [],
                },
                {
                    label: "Tree",
                    items: [],
                },
                {
                    label: "Disjoint Set",
                    items: [],
                },
                {
                    label: "Graph",
                    items: [
                        {
                            label: "Overview",
                            link: "/graph/overview",
                        },
                        {
                            label: "Graph Representaion",
                            link: "/graph/representation",
                        },
                        {
                            label: "BFS & DFS",
                            link: "/graph/bfs-dfs",
                        },
                        {
                            label: "Minimum Spanning Tree",
                            link: "/graph/mst",
                        },
                        {
                            label: "Shortest Path",
                            link: "/graph/shortest-path",
                        },

                        {
                            label: "Topological Sort",
                            link: "/graph/topological-sort",
                        },
                    ],
                },
                {
                    label: "Math",
                    items: [],
                },
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
