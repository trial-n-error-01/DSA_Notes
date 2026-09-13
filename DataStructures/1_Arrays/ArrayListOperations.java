import java.util.ArrayList;

public class ArrayListOperations {
    public static void main(String[] args) {
        // Create an empty ArrayList of strings.
        ArrayList<String> names = new ArrayList<>();
        System.out.println("Created ArrayList: " + names);

        // Add elements to the end of the list.
        names.add("Alice");
        names.add("Bob");
        names.add("Charlie");
        System.out.println("After adding names: " + names);

        // Access an element by its index. Indexing starts at 0.
        System.out.println("Element at index 1: " + names.get(1));

        // Update the element at index 1.
        names.set(1, "Benjamin");
        System.out.println("After updating index 1: " + names);

        // Check whether an element exists in the list.
        System.out.println("Contains Alice: " + names.contains("Alice"));

        // Remove an element by its index.
        names.remove(0);
        System.out.println("After removing index 0: " + names);

        // Print the current size of the list.
        System.out.println("Current size: " + names.size());
    }
}
