package deitel.java.collections;

import java.util.List;
import java.util.ArrayList;
import java.util.Collection;
import java.util.Iterator;

public class CollectionTest {

    public static void main(String[] args) {
        String[] colors = {"MAGENTA","RED","BLUE","CYAN"};
        List<String> list = new ArrayList<String>();

        for (String color:colors)
            list.add(color);

        String[] removeColors = {"RED","WHITE","BLUE"};
        List<String> removeList = new ArrayList<String>();

        for (String color : removeColors)
            removeList.add(color);

        System.out.println("ArrayList: ");

        for(int count = 0 ; count < list.size(); count++)
            System.out.printf("%s ", list.get(count));

        removeColors(list, removeList);

        System.out.printf("%n%nArrayList after calling removeColors%n");

        for (String color: list)
            System.out.printf("%s ", color);

    }

    private static void removeColors(Collection<String> collection1, Collection<String> collection2){

        System.out.println("Calling RemoveColors");
        Iterator<String> inter = collection1.iterator();
        int i=0;
        while(inter.hasNext()){
            if (collection2.contains(inter.next())){
                inter.remove();
            }
            System.out.println("Iteration: "+i);
            i++;
        }
    }

}
