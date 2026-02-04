Sentiment Analysis Web Application

This project is a sentiment analysis web application developed using Python and Streamlit. The application analyzes user provided text and determines whether the sentiment expressed is positive negative or neutral. The system is designed to be lightweight easy to deploy and suitable for learning demonstration and cloud deployment purposes. This project does not use MLflow or any experiment tracking framework.

Project Overview

Sentiment analysis is a natural language processing task that identifies emotional tone in textual data. This application performs real time sentiment analysis on text entered by the user through a web interface. The focus of this project is simplicity transparency and fast execution without relying on complex machine learning pipelines.

The application is ideal for beginners students and developers who want to understand sentiment analysis fundamentals and deploy a working application on cloud platforms such as AWS.

Features

The application accepts user input text in real time
The sentiment of the text is classified as positive negative or neutral
The application uses a simple and clean web interface built with Streamlit
The system is lightweight and runs efficiently on low resource environments
The project is easy to deploy locally or on AWS EC2

Technology Stack

The application is developed using Python as the programming language. Streamlit is used for building the web interface. Natural language processing is handled using lexicon based sentiment analysis libraries such as TextBlob NLTK or VADER depending on the implementation. Pandas is used for basic data handling where required.

Project Structure

The project consists of a main application file which contains the Streamlit logic and sentiment analysis code. A requirements file is used to list the Python dependencies. The README file provides documentation and usage instructions. A virtual environment may be used optionally for dependency isolation.

Installation and Setup

To run the project locally first extract or clone the project folder. Navigate to the project directory and create a Python virtual environment. Activate the virtual environment and install the required dependencies listed in the requirements file. Once the dependencies are installed the application can be started using the Streamlit run command.

If the requirements file is not available the required libraries such as Streamlit Pandas NLTK and TextBlob can be installed manually using pip.

Running the Application

After installation the application is launched using Streamlit. Once the server starts the application can be accessed through a web browser using the local host address. The user can enter text into the input field and submit it for analysis. The application processes the text and displays the detected sentiment.

AWS Deployment Overview

The application can be deployed on AWS using an EC2 instance. An Ubuntu based EC2 instance is recommended. Python and required dependencies must be installed on the server. The application is then started using Streamlit with the server address configured to allow external access. The EC2 security group must allow inbound traffic on the Streamlit port.

Once deployed the application can be accessed using the public IP address of the EC2 instance.

Sentiment Analysis Approach

The sentiment analysis logic is based on a lexicon based approach. The input text is processed and compared against predefined sentiment dictionaries. Each word contributes to an overall sentiment score. Based on the final score the sentiment is classified as positive negative or neutral. This approach allows fast execution and does not require training data.

Text Preprocessing

Before analysis the input text is normalized by converting it to lowercase and removing unnecessary whitespace. Depending on the library used tokenization and basic linguistic processing may be applied. These steps help improve sentiment detection consistency.

Performance and Efficiency

The application is optimized for low computational overhead. It does not require a GPU or large memory resources. The application runs efficiently on free tier cloud instances and provides fast response times for real time user interaction.

Limitations

The application may not accurately detect sarcasm or context dependent sentiment. The lexicon based approach may struggle with domain specific language. Complex emotional expressions may not be fully captured.

Future Enhancements

The project can be extended by integrating machine learning based sentiment classifiers. Support for multiple languages can be added. User inputs and results can be stored in a database for analysis. The application can be containerized using Docker. Authentication and user management features can be implemented.

Conclusion

This sentiment analysis web application demonstrates a practical implementation of natural language processing concepts using a simple and accessible approach. The project is suitable for educational use cloud deployment and rapid prototyping. By avoiding complex machine learning pipelines the application remains easy to understand maintain and deploy.

License

This project is open for educational and learning purposes and can be modified and extended as required.
