def find_last_occurance(text, search):
    
    last_char = len(text) - 1
    ssize = len(search)
    iteration = 0

    prev_char, next_char = None, None
    while last_char > 1:
        lst_idx = (last_char + len(search))
        prev_char = text[last_char-1:][0]
        if iteration >= len(search):
            next_char = text[last_char+lst_idx:]
            
        if text[last_char:lst_idx] == search and text[last_char-1:][0] in [' ',''] and text[last_char+ssize:][0] in [' ','']:
            break
        else:
            last_char = last_char - 1
        
        iteration = iteration + 1
    
    return { 
            'found':text[last_char:lst_idx],
            'pos': last_char,
            'prev': text[last_char-10:][0],
    }




search1 = 'vulputate' #851
text1 = '''
Lorem ipsum dolor sit amet, consectetur adipiscing elit. Aliquam sem odio, varius nec aliquam nec, tempor commodo ante. Pellentesque sit amet augue vel ante dictum placerat ut ut sapien. Proin maximus eu diam in posuere. Suspendisse in lectus in lectus finibus auctor. Nam sed porttitor arcu. Vestibulum augue odio, posuere quis libero sed, pharetra sollicitudin est. Donec sit amet nunc eu nisi malesuada elementum id ut purus.Nunc sit amet % massa rhoncus, venenatis eros sit amet, ornare augue. Nunc a mi sed est tincidunt facilisis at nec diam. Donec nec ex lorem. Morbi vitae diam tincidunt, dignissim arcu ut, facilisis nisi. Maecenas non felis #ullamcorper, viverra augue id, consequat_nunc. Suspendisse potenti. Proin tempor, sapien ut ornare placerat, sapien mauris luctus sapien, eget aliquam turpis urna at quam. Sed a&eros vel@ ante vestibulum vulputate. Suspendisse vitae vulputate velit. Suspendisse! ligula nisl, semper ut sodales et, ultricies porttitor felis. Nunc ac mattis erat, aliquet pretium risus. Nullam quis congue lacus, et mollis nulla. Nunc laoreet in nisi sit amet facili*sis. Cras rutrum justo ut eros mollis volutpat. Sed quis mi nunc. Nunc sed bibendum nibh, quis bibendum tortor.
'''

result = find_last_occurance(text1, search1)
print(result)
print(text1[851:891])
print(text1[886:926])
print()
print()
print()

search2 = 'and' #369
text2 = '''
A paragraph is a group of words put together to form &a group that is usuall%y longer than a sentence. Paragraphs are often made up of several sentences. There are usually between three and ei#ght sentences. Paragraphs can begin with an indentatio*n (about five spaces), or by missing a line out, and then starting again. This makes it easier to see when one paragraph ends and another begins.
'''

result = find_last_occurance(text2, search2)
print(result)
print(text2[375:415])
print(text2[369:409])



search2 = 'he' #650
odd = '''
Nehru was elected by the Congress to assume office *as independent India's first Prime Minister, although the question of leadership had been settled as far ba_ck as 1941, when Gandhi acknowledged Nehru as his political heir and succe@ssor. As Prime Minister, he set out to realise his_ vision of India. The Constitution of India was enacted in 1950, after which he embarked on an ambitious program of economic, social and political reforms. Chiefly, he oversaw !India's transition from a colony to a republic, while nurturing a plural, multi-party system. In foreign policy, he% took a leading role in the Non-Aligned Movement while projecting India as a regional hegemon in South Asia. 
'''

search1 = 'salt' #512
dd = '''
The same year Gandhi adopted the Indian loincloth, or short dhoti and, in the winter, a shawl, both woven with +yarn hand-spun on a traditional Indian spinning wheel, or charkha, as a mark of identification with India's rural poor. Thereafter, he lived modestly in a self-sufficient residential community, ate simple vegetarian food, and! undertook long fasts as a means of self-purification and political protest. Bringing anti-colonial nationalism to the common Indians, Gandhi led them in challenging the British-imposed salt tax with the 400 km (250 mi) Dandi Salt March in 1930, and later in calling for the British to Quit India in 1942. He was imprisoned for many years, upon many occasions, in both@ South Africa and India.
'''