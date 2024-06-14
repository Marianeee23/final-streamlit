import streamlit as st
import pickle

# Load the trained NaiveBayesClassifier from the saved file
filename = 'pages\imdb.sav'
with open(filename, 'rb') as file:
    loaded_model = pickle.load(file)

st.title("🎥 IMDb Movie Predictor 🎥")
st.subheader("Enter movie details to predict its IMDb rating:")

# User inputs for movie details
runtime_input = st.slider("Runtime (minutes): ", 60, 300)
genres_input = st.selectbox("Genre: ", ["Action", "Adventure", "Animation", "Biography", "Comedy", "Crime", "Documentary", "Drama", "Family", "Fantasy", "Film-Noir", "History", "Horror", "Music", "Musical", "Mystery", "Romance", "Sci-Fi", "Sport", "Thriller", "War", "Western"])
average_rating_input = st.slider("Average Rating (1-10): ", 1.0, 10.0, 5.0)
num_votes_input = st.slider("Number of Votes: ", 0, 1000000)

# Function to make a prediction
def predict_imdb_rating(runtime, genre, average_rating, num_votes):
    # Features function to convert inputs into a dictionary format expected by the model
    def features(runtime, genre, average_rating, num_votes):
        # Encode genre as binary features (you may need a more sophisticated encoding depending on your model)
        genre_features = {g: (genre == g) for g in ["Action", "Adventure", "Animation", "Biography", "Comedy", "Crime", "Documentary", "Drama", "Family", "Fantasy", "Film-Noir", "History", "Horror", "Music", "Musical", "Mystery", "Romance", "Sci-Fi", "Sport", "Thriller", "War", "Western"]}
        return {
            'runtime': runtime,
            'average_rating': average_rating,
            'num_votes': num_votes,
            **genre_features
        }

    # Apply features function to user inputs
    test_data = features(runtime, genre, average_rating, num_votes)

    # Use the model to get the predicted IMDb rating
    prediction = loaded_model.classify(test_data)
    return prediction

# Display button and result
if st.button('Predict'):
    predicted_rating = predict_imdb_rating(runtime_input, genres_input, average_rating_input, num_votes_input)
    st.text("The predicted IMDb rating based on the given movie details is:")
    st.text_area(label="", value=str(predicted_rating), height=100)