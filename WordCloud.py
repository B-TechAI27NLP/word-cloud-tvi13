from streamlit import *
from matplotlib.pyplot import *
from wordcloud import WordCloud, STOPWORDS
from PIL import Image

def main():
    set_page_config(
        page_title="My Word Cloud Generator",
        page_icon="☁️",
        layout="centered"
    )

    title("☁️ My Word Cloud Generator")
    markdown("""
        Enter your text below to generate a word cloud with your specified parameters!
    """)

    user_text = text_area(
        "Enter your text:",
        height=250,
        placeholder="Paste your text here (e.g., The quick brown fox jumps over the lazy dog)..."
    )

    if button("Generate Word Cloud"):
        if not user_text.strip():
            warning("Please enter some text to generate a word cloud.")
            return

        with spinner('Generating word cloud...'):
            stopwords = STOPWORDS

            wordcloud_params = {
                'width': 1000,
                'height': 600,
                'background_color': 'black', 
                'stopwords': stopwords,
                'min_font_size': 10,
                'max_font_size': 180,
                'max_words': 250,
                'colormap': 'viridis',
                'random_state': 42,
                'collocations': False,
                'prefer_horizontal': 0.9
            }

            try:
                wordcloud = WordCloud(**wordcloud_params).generate(user_text)

                fig, ax = subplots(figsize=(15, 10))
                ax.imshow(wordcloud, interpolation='bilinear')
                ax.axis('off')
                ax.set_title("Generated Word Cloud", fontsize=18, color='white') 
                tight_layout(pad=0)

                pyplot(fig)
                close(fig) 

                success("Word cloud displayed successfully!")

            except Exception as e:
                error(f"An error occurred: {e}")
                info("Please ensure your text is valid and try again.")

    markdown("---")
    write("This application uses your provided word cloud generation logic.")

if __name__ == "__main__":
    main()