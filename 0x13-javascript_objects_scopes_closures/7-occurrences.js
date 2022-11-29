#!/usr/bin/node

exports.nbOccurences = function (list, searchElement) {
  let cnt = 0;
  const countItem = () => {
    for (const i in list) {
      if (list[i] === searchElement) {
        cnt++;
      }
    }

    return cnt;
  };
  countItem();

  return cnt;
};
