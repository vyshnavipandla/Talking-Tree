import boto3
import pyaudio
import mmap
import time

# Set up Amazon Polly client
polly = boto3.client('polly', aws_access_key_id='AKIAU74CX4XBTYUDLCPO',
                      aws_secret_access_key='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',region_name='us-east-1')
x=["Once there was a Lion in the jungle who used to kill 2-3 animals daily for his meal. All animals went to him to tell, that daily one of them will come to him for his meal.",
"So, the Lion agreed and this started going for many days. One day, it was Rabbit’s turn. When he was on his way he saw a well.",
"Now he plans to kill the lion and save himself. He went to the lion and told him that, there is another lion who claims to be more powerful than him.",
"Then the lion asks the rabbit to take him to that lion. The rabbit takes him to the well and said he lives here. When the lion looked in the well he saw his own reflection and jumped in the well and dies.",
"2. The Hunter and the Pigeons",
"One day a hunter sets a net to catch birds and placed grains and rice over the net. After some time a flock of pigeons comes by and start eating grains and get caught in the net.",
"After some time they started losing hope, then their leader asks them to fly together up in the sky. They did as they were told and carried the net away.The hunter runs after them but they flew away to their friend’s mouse hole. Then the mouse cuts the net and freed the pigeons."
,"3. Two friends and the Bear",
"4.Once there were two friends who were crossing the jungle. After some time they saw a bear coming towards them.",
"5.Then, one of the friends quickly climbed the nearby tree and the other one did not know how to climb the tree. So he lays down on the ground holding his breath.",
"6.The bear reaches near him and sniffs him in the ear. After some time bear left the place, thinking the man is dead.",
"7.Now the other friend climbs down and asked his friend, what did bear said to him in his ear? He replied, to be safe from the fake friends."," The Monkey and the Crocodile","A monkey lived on a berry tree on the River Bank. Once he saw a crocodile under the tree who looked hungry and tired. He gave the crocodile some berries, the crocodile thanked the monkey and became one of his friends.","The monkey would give berries to the crocodile every day. One day the monkey even gave the crocodile extra berries to take to his wife.","His wife enjoyed the berries but told her husband that she wanted to eat the monkey's heart. She was a wicked and cunning woman.","The crocodile was upset, but he decided that he needed to make his wife happy."
,"8.On the next day, the crocodile went to the monkey and said that his wife had called him for dinner. The crocodile carried the monkey on his back across the river","He told this monkey his wife's plan.",
"9.The monkey had to think quickly if he wanted to save himself. He told the crocodile that he left his heart at on the berry tree and that they needed to return.","On reaching the monkey climbed the tree and spoke.","I'm not getting down; you betrayed my trust and that means our friendship is over"]
def mapy(text):
		

		response = polly.synthesize_speech(Text=text, OutputFormat='pcm',
									   VoiceId='Matthew')

		audio_data = response['AudioStream'].read()

		chunk_size = 4096
		pa = pyaudio.PyAudio()
		stream = pa.open(format=pyaudio.paInt16, channels=1, rate=15000, output=True)

		with mmap.mmap(-1, len(audio_data), mmap.MAP_PRIVATE | mmap.MAP_ANONYMOUS) as mm:
			mm.write(audio_data)
			mm.seek(0)
			while True:
				data = mm.read(chunk_size)
				if not data:
					break
				stream.write(data)
		#time.sleep(5)

		stream.close()
		pa.terminate()
		mm.close()


