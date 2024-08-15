import static com.mongodb.client.model.Filters.eq;

import java.util.ArrayList;

import org.bson.Document;

import com.mongodb.client.FindIterable;
import com.mongodb.client.MongoClient;
import com.mongodb.client.MongoClients;
import com.mongodb.client.MongoCollection;
import com.mongodb.client.MongoDatabase;

public class assignment3 {
    public static void main(String[] args) {

        // Replace the placeholder with your MongoDB deployment's connection string
        String uri = "mongodb://localhost:27017";

        try (MongoClient mongoClient = MongoClients.create(uri)) {
            MongoDatabase database = mongoClient.getDatabase("octalol");
            MongoCollection<Document> collection = database.getCollection("users");

            Document doc = collection.find(eq("name", "Akash Patel")).first();
            if (doc != null) {
                System.out.println(doc.toJson());
            } else {
                System.out.println("No matching documents found.");
            }
            Document newUser = new Document("name", "New User")
                    .append("username", "newUse3@example.com")
                    .append("countrycode", "+1")
                    .append("phone", 12345890)
                    .append("photo", "default.jpg")
                    .append("gender", "Not set")
                    .append("role", "user")
                    .append("password", "**HASHED_PASSWORD**")
                    .append("active", true)
                    .append("isverified", false)
                    .append("googleuser", false)
                    .append("watchlist", new ArrayList<>()) // Empty array for watchlist
                    .append("referralCode", "generatedReferralCode") // Replace with generated code
                    .append("__v", 0);

            collection.insertOne(newUser);

            collection.insertOne(newUser);
            Document query = new Document("role", "user");
            FindIterable<Document> usersWithRoleUser = collection.find(query);
            for (Document user : usersWithRoleUser) {
                System.out.println(user.toJson());
            }
            Document projection = new Document("name", 1).append("email", 1); // Include name and email
            FindIterable<Document> projectedUsers = collection.find().projection(projection);
            for (Document user : projectedUsers) {
                System.out.println(user.toJson());
            }
            Document filter = new Document("name", "Akash Patel");
            Document update = new Document("$set", new Document("phone", 98));
            collection.updateOne(filter, update);
            Document filter2 = new Document("name", "Akash Patel1");
            collection.deleteOne(filter2);

        }
    }
}