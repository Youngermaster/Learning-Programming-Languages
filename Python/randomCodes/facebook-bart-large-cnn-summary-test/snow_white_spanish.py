from transformers import pipeline, BartTokenizer

text = """
Había una vez, al final del invierno, una joven y bondadosa reina que, paseando por el jardín de su palacio, vio una rosa roja creciendo a pesar del frío, cuando la fue tocar se pinchó el dedo con una espina, y dejó caer tres gotas de sangre en la nieve. Fue entonces cuando la reina deseó tener una hija con la piel tan blanca como la nieve, los labios tan rojos como la sangre y el pelo negro tan negro como el ébano. Al poco tiempo, su deseo se cumplió, naciendo una encantadora princesa a quien la reina y su esposo, el rey, decidieron llamar Blancanieves. Sin embargo, la reina, madre de Blancanieves, enfermó poco después de dar a luz y esta fallece. El rey se casó posteriormente con una mujer muy bella pero fría y altiva. La nueva segunda esposa del rey, la nueva y segunda reina, la malvada madrastra de Blancanieves, realmente era una hechicera muy poderosa, y además de ser una mujer egoísta, malvada, mala y excesivamente vanidosa, era poseedora de un espejo encantado.

La Reina Malvada, la malvada madrastra de Blancanieves, solía preguntarle a su espejo cada día:

    > Espejo espejo mágico dime una cosa, ¿Qué mujer de este reino es la más hermosa?

Y el espejo mágico siempre le contestaba a la reina:

    > Usted, majestad, es la mujer más hermosa de este reino y de todos los demás.

Pero, cuando Blancanieves cumplió diecisiete años ya era tan bella como el día, y la malévola reina le preguntó a su espejo mágico lo mismo que tantas otras veces, esperando la misma respuesta, pero este le respondió:

    > Mi Reina, está llena de belleza, es cierto, pero su joven hijastra, la princesa Blancanieves, es ahora mil veces más hermosa que usted.

La malvada reina, celosa, ordenó a un cazador que matara a su hijastra Blancanieves en el bosque y, para asegurarse, le exigió que le trajera el corazón, el hígado y los pulmones de la inocente y dulce Blancanieves. El cazador no cumplió su tarea y en su lugar abandonó a la hermosa y dulce princesa Blancanieves en el bosque, y le llevó a la malvada reina el corazón, el hígado y los pulmones de un ciervo joven que luego fueron cocinados por el cocinero real y comidos por la cruel reina.

En el bosque, Blancanieves descubrió una pequeña casita en un claro y en medio del bosque que pertenecía a siete enanitos y decidió entrar para descansar. Allí, éstos se apiadaron de ella:

    > Si mantienes la casa para nosotros, cocinas, haces las camas, lavas, coses, tejes y mantienes todo limpio y ordenado, entonces puedes quedarte con nosotros y tendrás todo lo que quieras.

Le advirtieron, eso sí, que no dejara entrar a nadie mientras ellos estuvieran en las montañas. Mientras tanto, la reina malvada le preguntó a su espejo una vez más quién era la más bella de todas y, horrorizada, se enteró de que Blancanieves no sólo estaba viva y escondida en la casita del bosque, sino que la princesa seguía siendo la más hermosa de todas.

La malévola Reina usa tres disfraces para tratar de matarla mientras los siete enanitos están en las montañas. En primer lugar, disfrazada de vendedora buhonera, le ofrece a Blancanieves unas coloridas cintas para el cuello. Blancanieves se prueba una, pero la maligna reina le aprieta tan fuertemente la cinta al cuello que cae asfixiada, haciéndole pensar a la reina que la princesa está muerta. Los siete enanitos al regresar a la casa descubren a Blancanieves desmayada, le retiran la cinta del cuello y la joven se despierta.

La segunda vez la cruel reina va disfrazada de vendedora de peines y le ofrece un peine envenenado a su hijastra Blancanieves. Aunque Blancanieves se resiste a que la mujer le ponga el peine, esta logra ponérselo a la fuerza y la princesa Blancanieves cae desmayada, con el peine clavado en el pelo. Cuando llegan los siete enanitos, se dan cuenta de que la reina no alcanzó a clavarle el peine en la cabeza, sino que sólo la rasguñó. Le quitan el peine del pelo a Blancanieves y se despierta.

Por último, la reina malvada prepara una manzana envenenada, mitad blanca y mitad roja, se disfraza como una anciana vendedora y le ofrece la manzana a Blancanieves. Cuando Blancanieves se resiste a aceptar, su malvada madrastra, para que no desconfíe, corta la manzana por la mitad y se come la parte blanca y buena de la manzana, y le da la parte roja y envenenada a la princesa. Blancanieves come la parte roja de la manzana con entusiasmo e inmediatamente cae en un profundo sopor. Cuando los enanos la encuentran, no la pueden revivir. Como aún conservaba su gran belleza, los siete enanitos no tuvieron el valor para enterrarla, así que fabrican un ataúd de cristal y oro para poder verla todo el tiempo.

El tiempo pasa y un príncipe que viaja a través del reino ve a Blancanieves en el ataúd. El príncipe está encantado por su belleza y de inmediato se enamora de ella. Este le ruega a los siete enanitos que le den el cuerpo de Blancanieves y pide a sus sirvientes que trasladen el ataúd a su castillo. Al hacerlo, uno de ellos tropieza con algunos arbustos y el movimiento brusco hace que Blancanieves escupa el trozo de manzana envenenada atorado en su garganta, despertando así del sueño de muerte. El príncipe luego le declara su amor a Blancanieves y pronto la pareja planea celebrar su boda.

La maligna reina, creyendo que su hijastra Blancanieves ahora sí está muerta, pregunta una vez más a su espejo quién es la más bella de todas y, una vez más, el espejo la decepciona con su respuesta: «Usted, mi reina, es increíblemente bella, es cierto; pero la joven reina es mil veces más hermosa que usted».

Sin saber que a quien el espejo se refería era de hecho Blancanieves, la cruel reina es invitada a la boda del príncipe del país vecino. Cuando se da cuenta de que la nueva reina es la propia Blancanieves, se asusta y se desespera tratando de pasar desapercibida.

Sin embargo, el príncipe y Blancanieves ven y reconocen a la reina malvada. Entonces, Blancanieves le cuenta al príncipe todos los malos momentos que su malvada madrastra le había hecho pasar, y cómo intentó matarla tres veces. Como castigo por sus malos actos, el príncipe, ahora rey, manda confeccionar un par de zapatos de hierro y ponerlos al rojo vivo, obligando a la reina malvada a ponérselos y a bailar sin parar hasta que muera, y todos fueron felices para siempre.
"""


tokenizer = BartTokenizer.from_pretrained("facebook/bart-large-cnn")

# * Dynamic chunking
def chunk_text(text, max_chunk_size):
    sentences = text.split('.')
    current_chunk = 0 
    chunks = []
    
    for sentence in sentences:
        sentence_tokens = len(tokenizer.encode(sentence))
        if sentence_tokens > max_chunk_size:
            continue  # Skip this sentence as it's too long. Alternatively, you can split this sentence further.
        
        if len(chunks) == current_chunk + 1:
            if len(tokenizer.encode(chunks[current_chunk])) + sentence_tokens <= max_chunk_size:
                chunks[current_chunk] = chunks[current_chunk] + ' ' + sentence
            else:
                current_chunk += 1 
                chunks.append(sentence)
        else:
            chunks.append(sentence)

    return chunks

# Set up the summarization pipeline
smr_bart = pipeline(task="summarization", model="facebook/bart-large-cnn")

# Using the function
max_chunk_size = 1000  # slightly less than 1024 for safety
chunks = chunk_text(text, max_chunk_size)

# Summarize each chunk and combine
summarized_chunks = [smr_bart(chunk, max_length=500)[0]['summary_text'] for chunk in chunks]
final_summary = ' '.join(summarized_chunks)

print(final_summary)