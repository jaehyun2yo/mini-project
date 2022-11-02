// totop
const toTopEl = document.querySelector("#to-top");

window.addEventListener(
  "scroll",
  _.throttle(function () {
    console.log(window.scrollY);
    if (window.scrollY > 500) {
      // gsap.to(요소, 지속시간 , 옵션 )
      //버튼 보이기
      gsap.to(toTopEl, 0.2, {
        x: 0,
      });
    } else {
      //버튼 숨기기
      gsap.to(toTopEl, 0.2, {
        x: 100,
      });
    }
  }, 300)
);
toTopEl.addEventListener("click", function () {
  gsap.to(window, 0.7, {
    scrollTo: 0,
  });
});

// // 이동
// // const jaehyun = document.querySelector(".jaehyun");
// const memberEl = document.querySelectorAll(".member");
// const cardEl = document.querySelector(".card");
// const memberList = ["팀장 김인섭", "김재현", "이태언", "김채하", "변시윤"];


// // console.log(members);
// // console.log(jaehyun);
// console.log(cardEl);

// memberEl.forEach((member) => {
//   member.addEventListener("click", onClickMember);
// });

// function onClickMember(e) {
//   e.preventDefault();
//   const name = e.target.innerText;
 
//   console.log(name);
// }
