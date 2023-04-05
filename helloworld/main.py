#python_code 
import time  
import random
import datetime

# Create a function with countdown
def countdown(s):
    # Calculate the total number of seconds
    total_seconds = s

    # While loop that checks if total_seconds reaches zero
    # If not zero, decrement total time by one second
    while total_seconds > 0:
        # Timer represents time left on countdown
        timer = datetime.timedelta(seconds = total_seconds)

        # Prints the time left on the timer
        print(timer, end="\r")

        # Delays the program one second
        time.sleep(1)

        # Reduces total time by one second
        total_seconds -= 1

   
# Define the quiz questions
questions = {
   "What is the capital of France?": {
        "1": "Paris",
        "2": "London",
        "3": "Berlin",
        "4": "Madrid"
    },    
    "What is the currency of Japan?": {
        "1": "Yen",
        "2": "Dollar",
        "3": "Euro",
        "4": "Pound"
    },
    "What is the tallest mountain in the world?": {
        "1": "Mount Everest",
        "2": "K2",
        "3": "Kangchenjunga",
        "4": "Lhotse"
    },
    "What is the simplest programing language?":{
        "1": "python",
        "2": "java",
        "3": "c",
        "4": "ruby"
    },
    "What is the largest planet in our solar system?":{
        "1": "Earth",
        "2": "Jupiter",
        "3": "Mars",
        "4": "venus"
    },
    "How many elements in the periodic table?":{
        "1": "116",
        "2": "117",
        "3": "118",
        "4": "119"
    },
    "Which animal lays the largest eggs?":{
        "1": "whale",
        "2": "crocodile",
        "3": "elephant",
        "4": "ostrich"
    },
    "How many bones are in the human body?":{
        "1": "206",
        "2": "207",
        "3": "208",
        "4": "209"
    },
    "Which planet in the solar system is the hottest?":{
        "1": "Earth",
        "2": "Mercury",
        "3": "Mars",
        "4": "venus"
    },
    "Who discovered india?":{
        "1": "vasco da gama",
        "2": "Fahian",
        "3": "Alberuni",
        "4": "lbn battuta"
    },
    "What is the standard time line of india?":{
        "1": "82.5 degree east longitude",
        "2": "82.5 degree north longitude",
        "3": "82.5 degree west longitude",
        "4": "82.5 degree south longitude"
    },
    "In which year Arjuna Award was started?":{
        "1": "1947",
        "2": "1961",
        "3": "1949",
        "4": "1983"
    },
    "How many High courts are present in India at present?":{
        "1": "23 High courts",
        "2": "24 High courts",
        "3": "25 High courts",
        "4": "26 High courts"
    },
    "What is the first country in the world to completely ban tobacco?":{
        "1": "Japan",
        "2": "China",
        "3": "America",
        "4": "Bhutan"
    },
    "National voters day is celebrated every year on which day?":{
        "1": "24 January",
        "2": "25 January",
        "3": "25 November",
        "4": "26 January"
    },
    "Who is the constitutional head of india?":{
        "1": "Prime minister",
        "2": "President",
        "3": "Speaker of the lok sabha",
        "4": "Vice president"
    },
    "In which game is the word 'Bully' used?":{
        "1": "Cricket",
        "2": "Football",
        "3": "Hockey",
        "4": "Basketball"
    },
    "Which indian athlete is called as 'Flying Angel'?":{
        "1": "Hima Das",
        "2": "Mirabai Chanu",
        "3": "PT Usha",
        "4": "None of these"
    },
    "Which of the following city is Known as the city of Lakes?":{
        "1": "Jaipur",
        "2": "Udaipur",
        "3": "Nainital",
        "4": "Varanasi"
    },
    "Who led the Bardoli movement of 1928?":{
        "1": "Mahatma Gandhi",
        "2": "Bal Gangadhar Tilak",
        "3": "Sardar Vallabh Bhai Patel",
        "4": "Pandit Jawaharlal Nehru"
    },
    "When was Arya Samaj established?":{
        "1": "In 1875 AD",
        "2": "In 1897 AD",
        "3": "In 1901 AD",
        "4": "In 1912 AD"
    },
    "Which is the oldest veda among the vedas?":{
        "1": "Rigveda",
        "2": "Samveda",
        "3": "Yajurveda",
        "4": "Atharvaveda"
    },
    "Where is the Bhabha Atomic Research Center located ?":{
        "1": "Trombay,Mumbai",
        "2": "New Delhi",
        "3": "Bangalore",
        "4": "Kalkata"
    },
    "Who founded the Khalsa Panth?":{
        "1": "Guru Gobind Singh",
        "2": "Guru Nanak Dev",
        "3": "Angad Dev",
        "4": "Guru Ramdas"
    },
    "Who was the india's first I.P.S. officer?":{
        "1": "Sarojini naidu",
        "2": "Anandibai joshi",
        "3": "Anjum ara",
        "4": "Kiran bedi"
    },
    "In which game is the word 'Chinaman' used?":{
        "1": "Cricket",
        "2": "Hockey",
        "3": "Polo",
        "4": "Kabaddi"
    },
    "Oscar award is related to which field?":{
        "1": "Literature",
        "2": "Cinema",
        "3": "Science",
        "4": "Medicine"
    },
    "Which of the following is the hardest element?":{
        "1": "Glass",
        "2": "Diamond",
        "3": "Aluminum",
        "4": "Graphite"
    },
    "What was the ancient name of patna?":{
        "1": "Pataliputra",
        "2": "Ceylon",
        "3": "Hastinapur",
        "4": "Vaishali"
    },
    "Which of the following indian state has English as its official language?":{
        "1": "Nagaland",
        "2": "Sikkim",
        "3": "manipur",
        "4": "Kerala"
    },
    "What is the height of the geostationary satellite from the earth?":{
        "1": "36000 Kms",
        "2": "32000 Kms",
        "3": "40000 Kms",
        "4": "42000 Kms"
    },
    "How many colors are there in the rainbow?":{
        "1": "5",
        "2": "6",
        "3": "7",
        "4": "8"
    },
    "What is the frequency of ultrasonic waves?":{
        "1": "less than 20000 Hz",
        "2": "More than 20000 Hz",
        "3": "Between 20-20000 Hz",
        "4": "20 Hz"
    },
    "Durand Cup is related to which game?":{
        "1": "Hockey",
        "2": "Cricket",
        "3": "Football",
        "4": "Judo"
     },
    "Who was the first law minister of india?":{
        "1": "Dr.Sarvepalli Radhakrishna",
        "2": "Dr.Bhimrao Ambedkar",
        "3": "Sardar Vallabhbhai patel",
        "4": "Abdul kalam azad"
    },
    "In which city is the Salarjung Museum located?":{
        "1": "Hyderabad",
        "2": "Jaipur",
        "3": "Bangalore",
        "4": "Srirangapatna"
    },
    "Which is the longest river in the world?":{
        "1": "Amazon River",
        "2": "Nile River",
        "3": "Mississippi River",
        "4": "Yangtze River"
    },
    "Which minerals controls the heart beat?":{
        "1": "Potassium",
        "2": "Zinc",
        "3": "Copper",
        "4": "Aluminum"
    },
    "Which is the largest living bird in the world?":{
        "1": "Ostrich",
        "2": "Hummingbird",
        "3": "Eagle",
        "4": "Vulture"
    },
    "Which animal was first domesticated by man?":{
        "1": "Goat",
        "2": "Cat",
        "3": "Horse",
        "4": "Dog"
    },
    "How does the sky appear in space to an Astronaut?":{
        "1": "Blue",
        "2": "White",
        "3": "Black",
        "4": "Brown"
    },
    "What is the full form of ATM?":{
        "1": "Automatic Teller Machine",
        "2": "Automated Teller machine",
        "3": "All Time Money",
        "4": "None of these"
    },
    "What is the maximum number of seats in the Lok Sabha in india?":{
        "1": "78",
        "2": "80",
        "3": "82",
        "4": "95"
    },
    "Where was lord mahavir jain born?":{
        "1": "Vaishali",
        "2": "Pawapuri",
        "3": "lumbini",
        "4": "Rajgriha"
    },
    "Who discovered the proton?":{
        "1": "Rutherford",
        "2": "Chadwick",
        "3": "Goldstein",
        "4": "Albert Einstein"
    },
    "Where was india's first nuclear power house established?":{
        "1": "Tarapur",
        "2": "Udaipur",
        "3": "Hyderabad",
        "4": "Ranchi"
    },
    "Who founded Shantiniketan?":{
        "1": "Kalidas",
        "2": "Swami Vivekananda",
        "3": "Subhas Chandra Bose",
        "4": "Rabindranath Tagore"
    },
    "When did Alexander attack india?":{
        "1": "326 Bc",
        "2": "300 Bc",
        "3": "483 Bc",
        "4": "563 Bc"
    },
    "The average amount of salt in sea water is?":{
        "1": "3%",
        "2": "3.50%",
        "3": "4%",
        "4": "4.50%"
    },
    "Which is the longest national highway of india?":{
        "1": "NH -7",
        "2": "NH -44",
        "3": "NH -1",
        "4": "NH -32"
    },

}

# Set the time limit for each question (in seconds)
time_limit = 30

# Define a function to ask a question and check the answer
def ask_question(question, options, answer):
    print(question)
    for option, value in options.items():
        print(f"{option}. {value}")
    user_answer = ""
    start_time = time.time()
    while user_answer == "" and time.time() - start_time < time_limit:
        countdown(time_limit - (time.time() - start_time))
        user_answer = input("Your answer: ")
    if user_answer.lower() == answer.lower():
        return True
    else:
        return False
   
# Shuffle the quiz questions
questions_list = list(questions.items())
random.shuffle(questions_list)

score = 0
for i, (question, options) in enumerate(questions_list):
    print(f"\nQuestion {i+1}:")
    if ask_question(question, options, questions[question]['1']):
        score += 1
        print("Correct!")
    else:
        print("Incorrect.")

# Display the final score
print(f"\nYour score is {score}/{len(questions)}")
