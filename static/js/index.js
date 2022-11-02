const router = async () => {
  const routes = [
    { path: "/", view: () => console.log("Home") },
    { path: "/inseop", view: () => console.log("inseop") },
    { path: "/jaehyun", view: () => console.log("jaehyun") },
    { path: "/taeyeon", view: () => console.log("taeyeon") },
    { path: "/chaeha", view: () => console.log("chaeha") },
    { path: "/siyoon", view: () => console.log("siyoon") },
  ];
  const potentialMatches = routes.map((route) => {
    return {
      route,
      isMatch: location.pathname === route.path,
    };
  });

  // let match = pageMatches.find((pageMatch) => pageMatch.isMatch);
  console.log(potentialMatches);
};

// document.addEventListener("DOMContentLoaded", () => {
//     document.body.addEventListener("click", (e) => {
//         if (e.target.matches("[data-link]")) {
//             e.preventDefault();
//             history.pushState(null, null, e.target.href)
//             router();
//         }
//     });
//     router()
// })
