/*
Given an array of strings strs, group the anagrams together. You can return the answer in any order.
An anagram is a word ot pharse formed by rearranging the letters of a different word or pharse, typically using all the original letter exactly once.
Example:
input  = ['eat','tea','tan','ate','nat','bat']
output = [['bat'],['nat','tan'],['ate','eat','tea']]
*/

class Anagrams {
  group_anagrams(list) {
    let anagram_map = {};
    let results = [];

    for (let i = 0; i < list.length; i++) {
      let sorted_word = list[i].split("").sort();
      if (anagram_map[sorted_word] === undefined) {
        anagram_map[sorted_word] = [];
        anagram_map[sorted_word].push(list[i]);
      } else {
        anagram_map[sorted_word].push(list[i]);
      }
    }

    for (let key in anagram_map) {
      results.push(anagram_map[key]);
    }

    console.log(results);
    return results;
  }
}

let input = ["eat", "tea", "tan", "ate", "nat", "bat"];
let anagram = new Anagrams();
anagram.group_anagrams(input);
