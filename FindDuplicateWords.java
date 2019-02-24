public void findDuplicateWord(String input){
  String[] inputArr = input.split(" ");
  boolean found = false;
  Map<String, Integer> countMap = new HashMap<String, Integer>();
  for (int i = 0; i < inputArr.length; i++) {
      if (countMap.containsKey(inputArr[i])) {
          int count = countMap.get(inputArr[i]);
          countMap.put(inputArr[i], ++count);
      } else {
          countMap.put(inputArr[i], 1);
      }
  }

  for (String s : countMap.keySet()) {
      if (countMap.get(s) > 1) {
          System.out.println("Word \"" + s + "\" " + "repeated " + countMap.get(s) + " times.");
          found = true;
      }
  }
  if (!found) {
      System.out.println("No Duplicate Word found");
  }
}
