# Third_eye_APP

This app is a Generative AI chatbot which chats with Images given to it. I called this Third eye because the 
people who have weak eyesight and unable to understand what's going on outside or if they are searching for some objects can use it effectively.
On top of it we can create our own fantasy stories based on what we see in these images and can create our own perspective to look out the world. 

Basically this AI tool consists of three models as follows:-
1. [Image captioning model](https://huggingface.co/Salesforce/blip-image-captioning-large) - which is trained on the data of images with there captions ([Dataset](https://www.kaggle.com/datasets/adityajn105/flickr8k)). Model leaarns the connection between the given text and the image feature, This model follows the Encoder-Decoder Architecture, the choice of encoder and decoders are totally dependent on the one who is training this. Either we can use CNN+RNN or VIT+GPT or CNN+GPT or any transformer as well as cnn architecture, mostly depends on the amount and quality of dataset. I have tried training thies model using CNN+LSTM on collab, Here is my repo for this multimodal architecture-
https://github.com/Rishabh20539011/Mutimodal_Network

2. [Object Detection Model](https://huggingface.co/facebook/detr-resnet-50) - This model is trained on ample objects with specific class i.e here we have understood core features of each object such as a dog or a cat or a truck etc.. unlike the captioning model which has lot other small noisy information associated with each image. Therefore it would be helpful to transfer this information along with captions to get a quality output.Additionaly we also get the location or bounding boxes of objects present in the image , so we can ask like if the object is on my LHS or RHS.

3. [Text_Generation_Model](https://openai.com/)- This OpenAI's GPT 3.5 which is trained on lot's of text data, which helps us to generate text based on the information we get from both the above models. We can make use of the results given by captioning and object detection tool from which we can generate lot other futuristic things.



