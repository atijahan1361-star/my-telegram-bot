

import telebot

# توکن ربات شما
TOKEN = "8556687289:AAEOn3FtCDVrC0mYNRZJPrLtrd0p2kKvmwg"
bot = telebot.TeleBot(TOKEN)

# آیدی صحیح کانال شما 
CHANNEL_ID = "@ai_prompt_channel" 

# ==================== بانک پرامپت‌ها ====================
prompts_data = {
      "اسب": """* An intimate and romantic portrait of a young couple, a man and a woman, riding together on a horse.
* The woman is seated in front. Her long, dark, wavy hair falls beautifully over her shoulders. Her gaze is directed downward, and she has a gentle, calm smile on her lips.
* The man is seated behind the woman. He has neat, dark hair and a well-groomed beard and mustache. He looks at the woman with a wide, loving smile and tilts his head toward her. Their faces are preserved with complete accuracy.

Pose & Body Language
* The woman gently rests her head toward the man. Her hands are placed on the horse’s neck and mane.
* The man is behind her, wrapping his arms around the woman’s waist and embracing her. He smiles at her lovingly and pulls her close to himself. Their physical connection is warm and intimate.
* They are sitting comfortably on the horse’s saddle.

Clothing & Appearance
* The woman is dressed in a soft rural-folkloric outfit. She wears a cream-colored linen blouse with puff sleeves and an open neckline, layered with a dark burgundy velvet vest. The linen and velvet textures are clearly visible.
* The man wears a simple, comfortable white linen shirt.
* The clothing has natural folds and realistic, clearly defined fabric textures.

Environment & Background
* An open landscape, with hilly and mountainous areas in the background. Blurred, distant hills with dense trees on the left side.
* A softly cloudy sky at sunset with gentle light. The ground is covered with wild grass.
* The background is completely blurred with creamy bokeh, keeping the focus on the couple and the horse.

Props & Details
* A dark brown horse with a thick, dark mane is in the foreground. Part of the horse’s head and its mane are clearly visible.
* The horse’s leather bridle and part of the saddle are visible. The leather has a real, aged texture.
* Detailed facial skin texture, the woman’s long hair, the man’s beard, and the texture of the horse’s mane.

Lighting
* Natural, soft, gentle golden-hour light at sunset.
* Soft, diffused shadows with no harsh shadows.
* Gentle backlighting that separates the couple from the background. The overall feeling is peaceful sunset atmosphere.

Camera Settings
* Vertical portrait photography.
* 85mm f/1.8 or 50mm f/1.4 lens.
* Very shallow depth of field, creamy background bokeh.
* Precise focus on the couple’s faces and the horse in the foreground.
* Analogue photography feel with natural film grain.
* Fast shutter speed to capture the moment while preserving soft textures.

Color Grading & Style
* Warm, rich, natural colors. Burgundy, cream, and warm brown tones dominate.
* Natural analogue film aesthetic, with film texture. Soft colors and low contrast.
* Completely realistic and natural appearance.

Realism Details
* Realistic textures of fabric (linen, velvet), skin, hair, and leather. Natural skin details on the hands and faces.
* Thick, tousled mane of the horse. Natural folds in the clothing.
* Light dust particles in the air.
* Natural imperfections in the environment (wild grass, blurred tree branches).

Final Quality Tags
* 8k, ultra-photorealistic, highly detailed, professional photography, cinematic, documentary style, natural light, analogue film style.

Aspect ratio: 9:16""",

    "دلتنگ": """Use the uploaded reference image as the primary visual reference, and recreate the image as accurately and closely as possible. Preserve the exact original composition, framing, camera angle, perspective, subject placement, proportions, lighting, shadows, contrast, environment, and overall visual feeling of the reference image.

Create an ultra-realistic, cinematic black-and-white photograph of a young man sitting alone on the floor of a modern, dark living room at night.
    The young man is positioned in the lower-right portion of the frame, sitting casually with one knee bent. His body is slightly turned toward the left, while his elbow rests on his raised knee and his hand supports the side of his face. He quietly looks toward the large television screen on the left side of the room, with a distant, thoughtful, slightly melancholic expression.

The television occupies a large portion of the left side of the composition and displays a close-up black-and-white portrait of a young woman. Only part of her face and upper body are visible. She is gently resting her face against her hand, creating an intimate and emotional visual moment.

The television screen is the primary light source in the room. Its soft grayscale glow illuminates the young woman's face displayed on the screen and casts very subtle reflected light onto the young man's face, hair, arm, and the nearby floor.

Keep the rest of the living room extremely dark and dramatically underexposed, exactly like the reference image. Preserve the subtle details visible within the shadows, including a modern low TV console beneath the television, a dark sofa in the background, a tall indoor plant near the center-left, shelves containing small objects, framed photographs or artwork on the wall, and a dark textured area rug covering the floor.

Preserve the large amount of empty, dark negative space in the upper and central portions of the image. The television must remain the dominant visual element on the left side, while the young man remains clearly visible in the lower-right portion.

Strict monochrome black-and-white photography. Deep blacks, soft gray midtones, subtle highlights, natural skin texture, realistic facial details, individual realistic hair strands, authentic clothing and fabric texture, physically accurate shadows and reflections.

The image should look like a genuine spontaneous photograph captured late at night during a quiet and private moment, not like a staged studio portrait. The atmosphere should be intimate, lonely, emotional, cinematic, and contemplative. Vertical 9:16 composition. Preserve the same camera height, camera distance, perspective, framing, and spatial relationships between the television, the young man, the furniture, and the rest of the room as shown in the uploaded reference image.

Realistic low-light photography, cinematic documentary photography, subtle natural film grain, smooth tonal transitions, realistic exposure, natural lens rendering, extremely detailed textures, professional photography quality, ultra-photorealistic, 8K quality.

DO NOT change the fundamental composition of the reference image.
DO NOT move the young man from his position.
DO NOT change the placement of the television.
DO NOT brighten the room.
DO NOT add any additional people or objects.
DO NOT add any colors.
DO NOT make the scene look like a studio photograph.
Preserve the darkness, atmosphere, perspective, framing, and visual balance of the uploaded reference image as accurately as possible. NEGATIVE PROMPT""",

    "رابطه": """Structured Photography Prompt: Over-the-Shoulder Embrace

Identity & Subject

- Main Subject: A close-up over-the-shoulder portrait of a young woman embracing a man from behind and looking over his shoulder.
- Female Subject: Preserve her exact facial structure and expressive eyes. Her gaze is deep, direct, and slightly contemplative.
- Male Subject: Seen from behind, occupying most of the foreground. He has naturally dark, curly, textured hair.

Pose & Body Language

- Embrace: A warm, secure, and intimate embrace. The woman's face is positioned behind the man's shoulder, looking directly into the camera so that only her eyes and eyebrows are visible within the frame.
- Hand: Part of the woman's hand and fingers are naturally resting on the man's shoulder. The pose must feel completely natural, relaxed, and intimate.
- Connection: The emotional connection between the two subjects is conveyed primarily through the woman's gaze.

Clothing & Appearance
- Man's Clothing: A simple black T-shirt. The intricate fabric texture must be rendered with extremely high fidelity.
- Woman's Hair: Dark, slightly tousled hair falling naturally over the man's shoulder and framing her eyes.
- Man's Hair: Natural, dark curls with realistic individual strands and texture.

Environment & Background

- Location: A softly blurred outdoor environment with gentle natural light and creamy bokeh.
- Background Elements: Warm green and earthy tones reminiscent of a garden or park. The background must be completely out of focus to isolate the subjects.

Props & Details

- Extremely accurate and delicate clothing texture.
- Individually separated, naturally rendered hair strands.
- Natural catchlights and realistic reflections of light in the woman's eyes.
- Natural, soft facial skin texture.

Lighting

- Light Direction: Soft, warm, natural Golden Hour light coming from behind and slightly from the side, creating a subtle rim light along the hair and shoulders while gently illuminating the woman's face.
- Quality: Diffused, soft, warm, cinematic lighting with smooth tonal transitions.

Camera Settings

- Composition: Tight close-up, over-the-shoulder framing.
- Lens: 85mm prime lens, f/1.4.
- Aperture: Extremely shallow depth of field, f/1.8 or f/1.4. Critical focus must be exceptionally sharp on the woman's eyes and the relevant foreground textures, while the background has smooth, creamy bokeh.
- Focus: Critical, precise focus on the woman's eyes.
- Film Grain: Fine, natural film grain for an authentic analog photography aesthetic.
- Format: Full-frame sensor, RAW photography.

Color Grading & Style

- Style: Cinematic, intimate, authentic, analog film photography.
- Color Palette: Warm, organic tones including olive green, copper, deep brown, and natural skin tones. Warm color grading with a subtle desaturated finish.

Realism Details

- Subtle, natural skin imperfections.
- Visible skin pores and realistic hair follicles.
- Natural wear and subtle texture variations in the fabric.
- Natural moisture and realistic reflections in the eyes.
- No artificial skin smoothing, plastic skin, or overly polished appearance.

Final Quality Tags

RAW photo, ultra-high resolution, 8K, photorealistic, hyper-realistic, award-winning cinematography, intimate portrait, Hasselblad color.

Aspect Ratio

9:16 vertical composition""",

    
    "تراس": """Create an extremely photorealistic professional portrait of the exact same young Middle Eastern woman from the reference image. Preserve her identity, facial structure, proportions, and unique facial features exactly. Long, thick, dark, naturally wavy hair.
Seated on a black rattan chair, body slightly turned left, head facing the camera. Right hand gently lowers small dark oval sunglasses so her eyes look directly and confidently over the glasses. Left hand rests naturally on her thigh. Legs crossed.
Light cream/off-white textured linen shirt over a plain white crew-neck T-shirt, sleeves rolled to the elbows. Dark chocolate-brown leggings. Natural matte makeup emphasizing eyes and matte lips.
Small oval sunglasses with thin gold frame and dark lenses. White round-face wristwatch on left wrist. Thin layered necklaces with small gold heart pendants plus one smaller single pendant. Simple gold bracelet on right wrist. Silver ring on right index finger Outdoor urban terrace/balcony. Dark black-and-gray marble wall with white veins behind her and a black metal railing. Dense green trees with dappled sunlight behind the railing; softly blurred residential buildings in the distance. Detailed marble veining and foliage.
Warm, soft natural late-afternoon golden-hour light from front-right. Soft natural shadows, subtle backlight on foliage, warm highlights on hair and linen clothing.
Professional DSLR, 85mm prime lens, f/2.2, 1/500s, ISO 200. 3:4 vertical medium portrait. Precise focus on the eyes, shallow depth of field and natural background bokeh.
Natural realistic urban lifestyle photography, warm natural color palette, realistic skin tone and texture, individual hair strands, natural clothing folds, detailed linen and rattan textures, authentic skin pores, subtle natural film grain, RAW-photo appearance, sharp focus, no artificial or AI-generated look.""",

    "پرامپت_اول_دهه۵۰": """Portrait & Subjects
A medium portrait of a young Iranian couple, a woman and a man, with authentic Iranian appearance and identity reflecting the 1950s Persian/Iranian aesthetic. The woman (on the left) has distinctive facial features, thin arched eyebrows, and a gentle smile. The man (on the right) has a strong, angular facial structure, dark eyes, thick and well-defined eyebrows, and a gentle smile. The exact identity, facial characteristics, and facial proportions of both subjects must be preserved accurately.

Pose & Body Language
They are sitting side by side on green grass in an outdoor setting. Their pose is intimate, warm, and friendly. The man has his left arm affectionately around the woman's right shoulder, with his hand naturally hanging down. The woman gently places her right hand on the man's left hand resting on her shoulder, holding his hand affectionately. Both subjects look directly and confidently at the camera. The woman's body is slightly leaning toward the right, while the man's body is slightly leaning toward the left.

Clothing & Appearance
Woman: A colorful long-sleeved patchwork blouse made from different fabrics and patterns, including plaid, floral, and solid fabrics, in shades of red, yellow, blue, and green. Natural wrinkles and folds in the cotton fabric. Simple black trousers. Voluminous, wavy 1950s-style hair with light caramel highlights.

Man: A dark navy polo shirt with a collar and three large white buttons. Textured pique-knit polo fabric. Fine white-and-black/dark-navy houndstooth trousers. Dark, voluminous 1950s-style hair.

Environment & Background
An outdoor setting with the couple sitting on naturally green grass. The background is completely out of focus with strong, soft bokeh, featuring dense green trees, foliage, and bushes with gentle patches of diffused light. The foreground contains visible natural grass.

Props & Details
Woman: A necklace with a circular red pendant, a delicate gold chain bracelet on her right wrist, and dark red nail polish.

Man: A gold chain bracelet on his left wrist.

Show realistic fabric textures and fine details in the woman's patchwork blouse, the man's textured pique polo shirt, and his houndstooth trousers. Preserve natural hair texture and the rough, organic texture of the grass.

Lighting
Soft, warm natural daylight, suggesting late afternoon. No harsh direct sunlight. Soft shadows fall naturally across their faces and clothing. The overall atmosphere should evoke the warm, fading light of late day.

Camera Settings
Photographed with a vintage analog film camera with the aesthetic of a 1950s-era photograph. Medium focal length, approximately 80mm. Moderate aperture around f/5.6–f/8, providing controlled depth of field while keeping the background extremely soft and blurred. Precise focus on both subjects' faces. Moderate shutter speed. Authentic analog film texture with clearly visible but subtle film grain.

Color Grading & Style
Vintage analog film portrait photography. Slightly faded, warm colors with a subtle vintage tint. Clearly visible natural film grain. Natural contrast and tonal range, with no artificial digital processing or over-polishing. The image should unmistakably feel like an old photograph.

Realism Details
Highly realistic natural textures throughout: authentic cotton and textured fabric, individual strands and natural texture of the hair, rough grass, realistic skin pores, subtle veins, natural smile lines, and minor imperfections of real skin. No artificial beauty filters or excessive skin smoothing. Soft natural reflections on the gold jewelry and dark red nail polish. Clothing should show realistic wrinkles and folds consistent with their seated pose and body positioning.

Final Quality Tags
Highly realistic, authentic analogue film quality, 35mm photograph, 1950s aesthetic, vintage photography, natural textures, realistic skin, subtle film grain, candid intimate moment, sharp focus on both subjects, soft cinematic bokeh, warm faded tones, authentic old photograph, no digital look.

Aspect Ratio: 9:16
Important: The final image must have visible film grain and unmistakably look like an old vintage photograph rather than a modern digitally processed image.""",

    "پرامپت_دوم_دهه۵۰": """Identity & Subject
A portrait of a young Iranian couple with an authentic Iranian appearance and identity from the 1950s. A man with distinctive facial structure, dark and voluminous hair (cut in a short 1950s style), brown eyes, thick eyebrows, and a gentle smile. A woman with distinctive facial structure, dark hair styled in a very voluminous and distinctive 1950s bouffant, subtle makeup, and a gentle smile. The exact identity, facial structure, proportions, and unique features of both subjects must be fully preserved.

Pose & Body Language
They are sitting on large boulders in an open mountainous environment. An intimate and friendly pose. The man has his right arm affectionately around the woman's left shoulder, with his left hand resting on his leg. The woman is positioned slightly forward and leaning slightly to the right, holding her hands in front of her body and holding sunglasses in her right hand. Both look directly and warmly at the camera.

Clothing & Appearance
Woman: A short, sleeveless, light lemon-yellow dress with a textured crepe fabric and decorative buttons on the front. Voluminous 1950s bouffant hairstyle. A gold bracelet on her right wrist. A watch is visible on the man's left wrist (the arm around her shoulder).

Man: A light pink short-sleeved collared shirt (cotton) and cream-beige trousers. Dark, voluminous 1950s hair. Bare feet with thin white cotton socks. Sport shoes placed on the grass.

Environment & Background
Open outdoor hills and mountainous terrain. Large, rough boulders on which they are sitting. The foreground is filled with wild grass and native plants. Green hills are visible in the midground, with mountains in the distant background. A sky with white, puffy clouds. A smaller stone wall on the right side of the background.

Props & Details
Sunglasses (with dark frames and dark lenses) in the woman's hand. Gold bracelet on the woman's wrist. Wristwatch on the man's left wrist (the arm around the woman's shoulder). A pair of men's sport shoes (white with dark details) on the grass near the man's feet. Precise details of the texture of the boulders.

Lighting
Soft, warm natural daylight (probably late afternoon). Direct but not harsh sunlight, creating soft and natural shadows on the faces and clothing.

Camera Settings
Photographed with an analog camera (probably 35mm film from the 1950s). Medium focal length (such as 80mm). Moderate aperture for controlled depth of field (f/5.6 - f/8) so that the mountain background is slightly softened. Precise focus on both subjects' faces. Moderate shutter speed. A distinct yet subtle analog film grain texture. A square or approximately square framing with borders that evoke the feeling of an old photographic print.

Color Grading & Style
Vintage analog film photography. Warm, slightly faded colors with controlled saturation (faded but warm). 1950s color tonality with natural colors while retaining an old and nostalgic feeling. The appearance of a photographic print on old photo paper. Balanced contrast.

Realism Details
Realistic fabric textures (cotton shirt, textured woman's dress), roughness of the rocks, details of the grass and plants. Skin with natural imperfections (pores, veins, smile lines) without artificial filters. Detailed hair texture and the woman's voluminous bouffant hairstyle. Subtle reflections of light on the sunglasses and bracelet. Slight dust or mild aging/wear on the printed photograph.

Final Quality Tags
Highly realistic, analogue film quality, 35mm photograph, 1950s aesthetic, vintage photography, natural textures, candid moment, sharp focus on subjects, cinematic grain, MASTERPIECE.

Aspect Ratio: 9:16""",

    "پرامپت_سوم_دهه۵۰": """Preserve the facial identity of the reference.

A young woman with a 1950s Western/Persian-era appearance and heavy 1950s eye makeup. Eyes with prominent eyeliner and mascara, dark and well-shaped eyebrows, a calm expression, and a direct gaze. Precisely preserve the facial shape and nostalgic proportions.

Pose & Body Language
A semi-standing seated/squatting pose with a classical guitar. Left hand on the guitar fretboard, forming chords; right hand on the guitar body, ready to play. Body slightly angled while the head faces the camera. A natural pose that is engaged with the instrument.

Clothing & Appearance
A fitted turtleneck sweater with a bold geometric pattern (color blocks of yellow, orange, blue, and green). Classic blue jeans. Very short, dark, puffy, and voluminous hair in a distinctive 1950s hairstyle.

Environment & Background
A lush outdoor setting (park or garden). Trees in the background with shallow depth of field and soft bokeh. The ground has a smooth surface with a muted purple/pink color tone.

Props & Details
A classical guitar (acoustic with nylon strings), with a warm-toned wooden body. Precise attention to the placement of the fingers on the strings and frets.

Lighting
Soft, diffused natural daylight. No harsh shadows, creating the feeling of being under the shade of trees or on a bright overcast day.

Camera Settings
Simulate a 35mm analog film camera. Focal length approximately 50mm to 85mm. Wide aperture (f/2.8 to f/4) to blur the background. Sharp focus on the face and guitar.

Color Grading & Style
Vintage film look. Saturated colors in the clothing (subtle Technicolor aesthetic), with a slight green/yellow color cast in the background. Distinct film grain.

Realism Details
Knitted texture of the sweater, weave and fibers of the denim fabric, matte reflection on the wooden guitar body. Natural skin texture (without plastic retouching), mechanically accurate finger positioning while playing the guitar.

Final Quality Tags
Highly realistic, photorealistic, 1950s aesthetic, analogue film photography, 35mm lens, vintage color grading, classical guitar player, sharp focus on face, natural lighting, cinematic film grain, MASTERPIECE.

The photograph must have visible film grain and clearly look like an old photograph.""",

    "ژست": """Portrait:
A medium close-up portrait of a young woman. Her exact identity, facial proportions, and unique individual features must be fully preserved.

Hair:
Long, dark, curly and wavy hair falling naturally around her shoulders.

Pose & Body Language

- Body Angle: She is leaning toward the left side of the frame, with her head gently tilted toward her right shoulder.
- Hand Movement: Her left hand is gracefully placed behind her neck, gently touching her curly hair, with her fingers naturally immersed among the curls.
- Facial Expression & Gaze: She looks directly into the camera with a warm, intimate, friendly, and inviting smile. Her eyes are expressive and create a strong sense of connection with the viewer. Her body is gently angled toward the right.

Clothing & Appearance

- Clothing: She is wearing a dark red / burgundy off-shoulder blouse with a boat neckline, puffy sleeves, and multiple layers of delicate ruffles made from chiffon or fine sheer fabric.
- Clothing Details: The fabric has a delicate, semi-transparent texture with intricate, organic folds and wrinkles across the sleeves and neckline. Her right shoulder is completely exposed, with the natural texture of the skin clearly visible.

Environment & Background

- Environment: A simple indoor background that is heavily blurred with soft bokeh, keeping the focus entirely on the subject.
- Background Elements: A softly textured wall in a neutral tone such as cream or beige, with fabric curtains featuring subtle vertical lines in beige or light gray behind her. The environment is clean and uncluttered, keeping all attention on the subject.

Props & Details

- Scene Object: A small diamond-shaped mark, watermark, or subtle logo is visible in the lower-right corner, placed on the outer layer of her clothing.
- Additional Details: Individual strands of hair are visible within the curls, the delicate wrinkled texture of the chiffon fabric is clearly defined, and subtle natural imperfections are present in the curtain background.

Lighting

- Light Source: Soft, warm, diffused indoor light coming from the left side, creating a subtle Rembrandt lighting pattern and beautifully illuminating the face.
- Light Quality: Warm, natural, diffused light with soft, gradual shadows, creating the feeling of late afternoon or early evening. A gentle, natural catchlight is visible in her eyes.

Camera Settings

- Lens: 85mm f/1.8 prime portrait lens.
- Aperture: f/2.2 for a very shallow depth of field and extremely soft, creamy background bokeh.
- ISO: ISO 400, appropriate for the indoor lighting, with subtle and natural film grain.
- Shutter Speed: 1/250 sec to capture fine hair details and prevent motion blur.
- Framing: Medium close-up, with the camera positioned slightly below eye level while maintaining a natural eye-level perspective.
- Image Format: RAW, with no artificial filters or artificial-looking processing.

Color Grading & Style

- Visual Style: Soft, cinematic studio portrait photography with warm, natural tones.
- Color Palette: A harmonious combination of the deep burgundy clothing, warm natural skin tones, dark hair, and a neutral beige background. Balanced, natural contrast. Film-inspired color processing with subtle grain while maintaining crisp digital clarity.

Realism Details

- Photorealistic Details: Natural skin texture with visible pores, subtle natural skin moisture, and extremely delicate freckles on the shoulder and cheek. Individual strands of curly hair are clearly defined. The delicate, wrinkled texture of the chiffon fabric is visible, along with subtle natural imperfections in the curtain background. Natural reflections and catchlights are present in the eyes.

Final Quality Tags

Photorealistic, 8K UHD, professional photography, studio portrait quality, natural look, extremely detailed, cinematic bokeh, 35mm film grain, DSLR, RAW, photorealistic masterpiece.""",

    "شهر": """Preserve the identity of the reference face, 9:16 frame.
The subject is walking and taking a step, with her body slightly turned and facing the camera. One hand is fully above her head, holding the strings of the balloons; the other hand is down and slightly away from the body. One of her legs is in the process of taking a step. Her head and gaze are directed upward, straight toward the balloons. A warm and natural smile. Her hair, clothing, and the balloons are affected by movement and wind.
A light cream-colored thick teddy/sherpa jacket with dense, fluffy texture, a wide collar, loose fit, visible stitching, and a large pocket/patch on the front. Long sleeves with natural fabric folds. Dark clothing is slightly visible underneath the jacket. Several delicate gold bracelets.
Very long, thick, dark hair, worn loose and free over the shoulders and down the back, with natural waves and slightly messy movement caused by motion and wind, along with realistic flyaways. Wide, dark eyebrows, long and full eyelashes, defined eyeliner, skin with a natural glow, glossy pink/nude lips.

A city street at night; dark trees and vegetation in the background, the street and passing cars. Car headlights appear as light streaks due to motion. Warm streetlights in the background. A real, natural, non-studio environment.

A large cluster of black, bright pink, pastel pink, and off-white/pinkish-white latex balloons above her head. Several balloons are close to the camera and appear larger, with some balloons extending outside the frame. Long, thin ribbons moving in the wind. Natural reflections of light on the glossy balloon surfaces.

Nighttime street lighting with warm light around 2800–3500K. Warm light on the face, hair, and clothing. Direct and very soft smartphone-flash-like light on the face and front of the clothing. Vertical 3:4, knee-up framing, straight-on camera angle. 35–40mm full-frame equivalent, f/2.0–f/2.8, 1/15–1/30 sec, ISO 800–1600. Focus on the face and eyes with subtle motion blur on moving elements. Medium depth of field; the background remains recognizable. Candid and spontaneous composition.""",

    "عشق": """This image shows a romantic and intimate portrait of a young couple on a beach by the sea. The male subject has a warm and friendly smile. The female subject has a face matching the reference photo and long, dark hair with a natural wavy texture. The identity, facial structure, proportions, and unique facial features of both subjects are preserved with complete accuracy.

The couple is in an intimate and natural embrace. The man is standing on the left and warmly embracing the woman. The woman rests her head calmly against the man's shoulder and chest and looks directly at the camera. The man's right hand is placed gently and supportively on the woman's cheek and jawline. His left hand is gently wrapped around the woman's waist. The woman places her left hand on the man's shoulder, while her right hand is also wrapped around the man's waist. The poses are completely natural, soft, and expressive of deep affection and intimacy.

The man is wearing a long-sleeved linen shirt with a vertical striped pattern (white and navy/black), with the fabric texture and natural folds clearly visible. He is also wearing light-colored pants (probably white or cream linen). The woman is wearing a simple black strappy beach dress (Slip dress), with the texture of the black fabric visible. Her long, dark hair is naturally and slightly tousled by the gentle breeze on the beach.

The scene takes place on a sandy beach during golden hour (sunset or sunrise). The background features a calm ocean with gentle, foamy waves forming the horizon line. The sky is covered with dramatic, dense, and textured clouds in shades of gray, dark blue, and a slight golden hue (caused by the sunlight during sunset). Wet sandy beach is visible in the foreground and beneath their feet. The environment has a calm, romantic, and natural atmosphere.

The texture of the skin, details of facial pores, individual strands of hair, the fabric texture of the dresses, and the details of the ocean waves are clearly visible.

Natural, soft, and warm Golden Hour lighting. The setting sun shines from the right side of the image, illuminating the right halves of their faces and clothing with warm, golden light. The shadows are soft and high-quality, providing good depth to the faces and clothing. The light from the cloudy background sky provides soft and diffused illumination throughout the scene. The image conveys the feeling of late afternoon, close to sunset.

The camera angle is at eye level (Eye-level). The composition is a medium portrait shot (Medium shot), framing both subjects from the waist up. The framing is vertical. A shallow depth of field (Shallow depth of field) is used; the subjects (the couple) are completely sharp and in focus, while the background (ocean waves and cloudy sky) is softly blurred (Bokeh) to keep the focus on the couple. A portrait lens with a focal length of approximately 85mm and a wide aperture (for example, f/2.2) is used.

Realistic, cinematic, and professional photographic style inspired by analog photography (Film look). Warm and rich color grading with natural skin tones, dark blue and gray colors in the sky and sea, and the golden warmth of sunlight. Extremely high image quality, with soft and natural film grain (Film grain). Realistic color processing without excessive saturation.

Natural skin texture, detailed individual strands of hair, linen and black fabric textures, natural imperfections of the environment (wet sand, irregular waves), and subtle reflections of light in the subjects' eyes. No signs of excessive skin smoothing or an artificial AI-generated appearance.

Ultra-realistic, Photorealistic, High-resolution portrait, Cinematic lighting, Natural light photography, Golden Hour, Sharp focus on subjects, Shallow depth of field, Professional photography, Film grain texture, Kodak Portra 400 style, Unedited raw photo quality.

Frame 9:16""",

    "سفر": """A young woman with long dark hair tied in a ponytail at the back of her head. The subject’s face is exactly identical to the reference image, in profile view facing right, with her eyes closed and a gentle smile that conveys a sense of peace and freedom. The facial structure, jawline, and facial proportions must be fully preserved.

The subject is standing outside the vehicle with her body facing right, but her chest and head are tilted upward and backward toward the sky. Her right arm is fully extended upward into the air, and her left arm is tilted downward and backward parallel to her body (as in the reference image). This is a pose of liberation, freedom, and enjoying nature. The body appears elongated, and the mechanics of the movement look completely natural and flexible.

She is wearing a vibrant red cotton crop-top with short sleeves and a round neckline. Off-white comfortable jogger pants with three classic vertical red side stripes along the thigh and calf (as in the reference image). The cotton texture of the fabrics, natural folds in the clothing caused by the body’s movement, and a partial view of the midriff area must be precisely maintained.

The scene is framed from inside the rear cabin of a modern and luxurious SUV. The rear right door of the vehicle is fully open, and the subject is standing in the open space outside the car. The exterior background consists of a vast, lush, and dense mountainous landscape of hilly forests. The sky is completely overcast, gray, and gloomy, with a layer of heavy fog/mist visible over the distant peaks. Small plants and weeds are visible on the rocky ground at the subject’s feet.

The foreground of the image is framed by the interior components of the vehicle: the edge of the black leather seat at the bottom and right side, the interior pillars of the vehicle, and the black leather panel of the open door with silver and dark wood trim details. The chrome door handle, power window controls, and stitching details on the door panel should be visible in high clarity. The vehicle windows are slightly tinted with subtle reflections.

Natural, soft, overcast day lighting. The light comes from the gray sky, with no harsh shadows. The lighting conveys the feeling of humidity and fresh mountain air. The subject’s skin and clothing are illuminated with soft, natural light.

A medium shot from inside the vehicle, at the subject’s eye level.

Lens type: 35mm lens with a natural field of view.

Aperture: f/4.0 to f/5.6 to maintain clarity of the subject and foreground details (car door) while creating a soft and natural depth of field in the mountainous background.

Shutter: 1/500s to accurately capture the moment and prevent motion blur.

ISO: ISO 200 (considering the overcast daylight).

Framing: “framing within a framing” technique using the car door and vehicle body as the inner frame.

Color Grading & Style:
Realistic lifestyle photography, with natural and rich contrast. The color palette includes vibrant red clothing, white, gray sky, various shades of dark green forest, and black vehicle interior. Natural color grading with subtle film grain and a matte finish, without excessive color saturation (desaturated, natural look).

The texture of the leather seat and vehicle door panel, skin pores and natural strands of the subject’s hair, cotton texture and folds of the clothing, possible tiny water droplets on the glass or vehicle body, humidity in the air, and distant mist.

f/5.6, 1/500s, ISO 200, 35mm lens, photorealistic, 8k UHD, RAW photo, dslr, highly detailed textures, realistic film grain, natural light, atmospheric depth, cinematic framing.

Aspect ratio 3:4""",

    "مادر": """Строго сохранить внешность 1:1 по загруженному фото: черты лица, пропорции, возраст, форму глаз, носа, губ, линию челюсти, текстуру кожи, цвет глаз; без идеализации. Если на фото мама и дочь, сохранить внешность обеих 1:1 по загруженному фото. Фотореалистичный семейный портрет матери и взрослой дочери в студии, кадр по грудь.
Женщины стоят очень близко друг к другу, мама находится справа в кадре, дочь слева. Дочь слегка прижимается к плечу матери, её голова расположена немного ниже. Мама нежно обнимает дочь за плечи, руки аккуратно лежат поверх её рук.
Обе смотрят прямо в камеру с мягким спокойным выражением лица, без широкой улыбки, создавая ощущение тепла, доверия и семейной близости. На обеих белые льняные рубашки свободного кроя с расстёгнутым воротником и естественной фактурой ткани. Волосы дочери свободно распущены, мягкими объемными волнами ниспадают на плечи.
Макияж дочери натуральный и элегантный: ровный тон кожи, деликатный контуринг, длинные ресницы, аккуратные брови, нюдовые губы. Мама выглядит естественно и благородно, без чрезмерной ретуши, сохранены возрастные особенности кожи и индивидуальные черты лица. Фон глубокого чёрного цвета без деталей, создающий выразительный контраст с белыми рубашками.
Свет мягкий студийный, направлен спереди и немного сбоку, деликатно подчёркивает объём лиц, текстуру кожи и ткани, без жёстких теней.
Реалистичная кожа с видимыми порами и естественной текстурой, высокая детализация глаз, волос, рук и ткани рубашек. Атмосфера дорогой семейной фотосессии, эмоциональная связь поколений, классический timeless portrait, премиальная студийная фотография, вертикальный формат 9:16.""",

    "آینه": """100% facial identity of the reference must be preserved* Image Type: A High-Resolution Mirror Selfie Portrait.* Subject: An Extreme Close-up of the face of an attractive young woman.* Subject Features: Hazel green eyes with long mascara-coated lashes and full eyebrows. Full, glossy lips with glossy brown-pink lipstick and cat-eye eyeliner. Black, shiny, wet curly hair falling around the face, partially covering the forehead and cheek. The head angle is completely tilted, with the chin raised.* Composition: A mirror selfie in which the smartphone camera (an iPhone with a three-camera system on the left side) is clearly reflected in the mirror and frames the face. The face is at a three-quarter angle and the subject’s gaze is directed at the phone lens in her hand.*
* Lighting: Hard, directional light from a single source (probably strong artificial light or studio light from above and to the right) that strongly emphasizes the shine of the wet hair and lips and creates dramatic, well-defined shadows. A catch-light is visible in the subject’s eyes.* Camera Technical Details: Simulating a photo taken with a flagship smartphone with a large sensor (such as an iPhone), a very wide aperture (F/1.8 or lower) for a blurred background (Bokeh), and extremely high clarity in skin and hair texture.* Style & Atmosphere: Fashionable, modern, confident. Extremely detailed and high-resolution skin texture.* Colors: Warm and natural colors with an emphasis on shine and moisture.  Part of the phone is visible in the frame  The framing extends from the forehead to the chin  Frame: 1:1""",

    "خودرو": """The identity of the reference face and the hairstyle must be preserved exactly; do not change the face, facial shape, features, or overall appearance of the subject.

An ultra-photorealistic and natural photo of a young woman with very long, dark hair exactly matching the reference image, reaching down to the chest and naturally falling around her face and shoulders. Makeup exactly matching the reference image, with winged eyeliner and thick, long eyelashes. She is seated in the driver’s seat of a luxurious Mercedes-Benz with a panoramic glass roof, with white sunglasses resting on top of her head.

Outfit: a light blue Calvin Klein T-shirt, loose dark navy jeans, white sneakers, and a small white CK crossbody bag. She is holding a cup of iced coffee with a black straw in her right hand, while her left hand is making a natural, spontaneous gesture; candid moment, without an artificial pose.

Shot from the front passenger seat, 24mm wide-angle lens, slightly elevated camera angle
Natural daylight entering through the panoramic roof and windows, soft and even illumination, bright and slightly warm but natural color grading, completely realistic skin tone with no orange cast. Trees and lush greenery visible outside the vehicle with shallow depth of field and naturally blurred background.

The car interior is black, luxurious, and highly detailed, including a Mercedes-Benz steering wheel, digital display, and realistic, high-quality materials.

Completely photorealistic skin: visible pores, fine skin texture, natural micro-texture, subtle imperfections, realistic facial texture, physically accurate highlights and light reflections. No plastic, waxy, or overly smooth skin, no beauty filter and no artificial retouching.

iPhone 17 Pro Max quality, 8K detail, ultra-photorealistic, HDR, sharp focus, realistic smartphone photography, natural dynamic range, authentic lighting and exposure, premium smartphone camera aesthetic, Instagram aesthetic.
Vertical 9:16""",

    "سلفی": """Нельзя менять лицо. Очень близкая фотография в зеркало, селфи на титановый iPhone 16 PRO MAX со вспышкой. Девушка стоит очень близко к зеркалу, телефон повёрнут горизонтально, виден только его край. Фона не видно совсем, он полностью чёрный. Видны только глаза, брови и ресницы – остальная часть лица скрыта тенью или кадрирована. Стрелки длинные, с острым передним уголком, взгляд направлен не прямо в камеру, а как будто слегка вниз, сквозь объектив, мимо него – отстранённый, томный, дерзкий, с поволокой, веки полуприкрыты, создавая эффект тяжёлого уставшего взгляда. Восточные стрелки, растушеванные тени, длинные пушистые ресницы. Брови слегка опущены, но сохраняют изгиб. Фотография затемнённая, с лёгкой замыленностью, глубокими тенями, лёгкая зернистость, естественная текстура кожи, без ретуши. Маникюр молочный, миндаль, ровный, аккуратный.""",

    "رفیق": """- پوشش: زن با پیراهن سفید آف‌شولدر بافت‌دار (طرح توری/سوزن‌دوزی) و گردنبند ظریف طلا؛ مرد با پیراهن آستین‌کوتاه سفید یقه باز.
- سوژه‌ها پشت میز در کنار هم ایستاده‌اند، اما با فاصله‌ای بسیار کم و تماس فیزیکی نزدیک که حس صمیمیت بالایی را منتقل می‌کند.
- وضعیت سر و گردن: سر مرد به آرامی به سمت پایین خم شده و به شکل حمایتگرانه‌ای مماس با سر/شقیقه زن قرار گرفته است. سر زن نیز با ظرافت به سمت مرد متمایل شده است. سوژه‌ها با لبخندی ملایم و عاشقانه به چشمان یکدیگر نگاه می‌کنند (ارتباط چشمی متقابل بین دو سوژه). 
- ترکیب‌بندی و لایه‌ها:
  - پیش‌زمینه: گل‌های رز سفید و شمع‌های میله‌ای باریک روشن با افکت بوکه/محو.
  - میانه: زوج و کیک سفید تزیین‌شده با گل طبیعی و شمع‌های روشن.
  - پس‌زمینه: پرده عمودی پلیسه سفید و یکدست.
- دوربین و نورپردازی: کادر عمودی پرتره (Medium Shot)، زاویه هم‌سطح چشم، لنز احتمالی ۸۵ میلی‌متری با دیافراگم باز، نورپردازی کلیدِ نرم و ملایم ترکیب‌شده با گرمای طبیعی نور شمع‌ها، پالت رنگی مونوکروم سفید با ته‌رنگ‌های گرم پوستی.
- کادر ۹:۱۶""",

    "شب": """Very natural and photorealistic. Visible skin pores, natural skin micro-texture, and a completely realistic environment. Natural highlights and realistic light reflections on the skin. Photo quality similar to a smartphone shot taken with an iPhone 17 Pro Max. Natural skin tone with no orange tint.

The girl has black layered hair reaching down to her chest. A completely photorealistic and natural nighttime portrait of a young woman with black, layered, chest-length hair falling naturally over her shoulders and the front of her body. She is standing on a high-rise balcony or terrace, with her body facing almost directly toward the camera, while her face is turned toward the right side of the image as she looks outside the frame.

One hand is raised in front of her forehead and through her hair, with part of the hand naturally positioned in front of her face. She is wearing a strapless black crop top and high-waisted white pants. A thin black belt with a gold buckle is visible aaround the waist.
She wears a white/shell necklace, several silver metallic bracelets, a dark watch or accessory on her wrist, a delicate ring, and long white nails. Her makeup is defined nighttime makeup, featuring elongated black eyeliner, prominent eyelashes, neatly shaped eyebrows, and glossy red/rose-toned lipstick. Her skin looks warm yet naturally toned and realistic, with no orange cast. A few loose strands of hair naturally fall across her face.

The photo is taken at night using direct smartphone camera flash. The subject is brightly illuminated, sharp, and naturally lit by the warm flash, while the background remains very dark. Behind her is an elevated nighttime city view with low-rise buildings, illuminated windows, streetlights, trees, and a glass balcony railing. Distant city lights are slightly soft and naturally out of focus, creating subtle background bokeh. The sky is almost completely black with little to no visible detail.
The overall feeling should resemble a spontaneous, casually captured smartphone photo for social media rather than a professional or studio photoshoot. The pose should feel candid, relaxed, and caught in the moment. Include slight, realistic motion blur on the raised hand, while keeping the face and body relatively sharp and clear.

Strong natural contrast caused by the direct flash, realistic skin and hair detail, visible pores and skin micro-texture, natural highlights and reflections on the skin, no excessive retouching, no artificial smoothing, no plastic-looking skin, and no beauty-filter effect.

Vertical 9:16 composition, framed from slightly above the head to approximately the upper thighs. The subject is positioned approximately in the center, slightly toward the right side of the frame. Eye-level camera angle. Realistic smartphone night photography, iPhone 17 Pro Max photo quality, direct flash, candid nightlife portrait, high realism, natural skin texture""",

    "بام": """Create an ultra-photorealistic close-up portrait with a vertical 9:16 aspect ratio of exactly the same couple from the reference photo; preserve the identities of both people, facial proportions, eyes, nose, lips, skin tone.

The man is wearing a fitted black shirt with a silver chain necklace and looking directly at the camera; his facial expression is calm and serious. The woman is wearing an oversized light pink blouse and standing very close beside him, resting her head on the man's shoulder and looking lovingly at his face.
The woman's long dark hair is loosely tied with a black patterned scarf.

Warm golden-hour sunlight creates a soft orange glow across both of their faces. The background should include blurred hills and buildings that are out of focus. Preserve natural and realistic lens depth of field, realistic skin pore texture, subtle and natural facial imperfections, highly detailed individual hair strands, and authentic fabric texture.

The image style should resemble a cinematic yet completely natural and realistic photograph; without any beauty filter, without smooth plastic skin, without a cartoon appearance, without CGI, and without an artificial or AI-generated appearance. Ultra-high quality, 8K photorealism, extremely detailed, natural lighting.""",

    "مشکی": """Создай фотореалистичное cinematic-фото, сохрани черты лица и цвет глаз. Очень близкий анфас, 85mm, 9:16. Очень длинные прямые блестящие волосы развеваются и частично закрывают лицо, мягкая полуулыбка, томный взгляд. Руки обнимают за плечи. Чёрное платье легкое тонкая вязка, открытые плечо, длинные рукава закрывают кисти . Фокус на глазах и губах, малая ГРИП, размытый светлый морской фон справа. Влажный морской свет + вспышка, плёночная зернистость, живой артхаусный кадр, высокая детализация.""",

    "نارنجی": """(An extremely close-up view of the reference face, with only half of the face visible in the frame).

Makeup: striking, creative eye makeup; very thick and long false eyelashes, black eyeliner with an extended wing, and softly glossy lips.

Several decorative piercings along with dangling earrings are visible on the ear; the hair is tied back in a ponytail, with straight, sleek curtain bangs in the front; the nails are manicured and painted orange.

Facial expression: intimate and mysterious; a direct, intense gaze into the camera, while the lower part of the face (mouth and chin) is covered by the hand and fingers.

Clothing: only the edge of a dark garment on the shoulder and a delicate silver chain around the neck are visible.
Background: a blurred, out-of-focus interior of a room; on the right side, a white shelf with several books or discs is visible, while the wall is in shadow.

Lighting: dramatic two-tone neon lighting; the left side of the face is illuminated by intense warm orange-red light, while the right side of the face and the background are in deep shadow with a purple-blue tint. A distinct boundary between light and shadow is visible across the nose and cheek.

Camera angle: an extremely close-up (Macro Close-up), at eye level, with only the left half of the face visible in the frame (eye, nose, lips, and ear).

Body position: the head is slightly turned, with the head and chin tilted downward, and the hand raised toward the face, covering part of the mouth, while the gaze remains directed into the camera lens.

Image quality: similar to photos taken with an iPhone 15; with slight digital noise, soft sharpness, subtle grain, and the natural, vivid feel of a real photograph.

Aspect ratio: 3:4""",

    "نور": """A beautiful portrait with an ultra-close and extreme close-up composition, with the camera positioned very close to the subject. Only the lower part of the face, natural glossy lips, chin, part of the neck, and one shoulder are visible in the frame. Almost the entire face is covered by long, loose hair, with a few individual, unruly strands naturally resting over the lips and face. One elbow is raised upward, with part of it entering the frame.

The hair is voluminous and styled with a round brush, featuring a layered, cascading hairstyle. A few strands of hair move freely in the air and partially cover the face, creating a sense of natural movement.

The skin is slightly tanned, with the natural skin texture fully visible. Preserve the makeup from the reference image, including winged eyeliner; the main emphasis is on full, glossy lips in a rich, glossy peach color.

A delicate silver chain with a small pendant is worn around the neck.
A black bracelet made of round beads is visible on the wrist.
Strong, direct, warm white sunlight, accompanied by deep, natural shadows and warm golden highlights reflecting in the hair and across the face, with extremely high contrast.
The image has the feel of a luxurious summer editorial photoshoot. Shot with a Canon G7X Mark III with flash, featuring an editorial lifestyle aesthetic.
Very high quality, 4K, hyper-realistic, RAW photo, luxury editorial, Pinterest aesthetic, Instagram photography style, extremely sharp details, completely realistic skin texture, subtle film grain, 100% facial resemblance to the person in the reference.
3:4 frame.""",

    "باغ": """Subject:
Medium shot of a beautiful young woman with long hair matching the reference image. She has a warm and natural smile and looks directly at the camera.
Pose & Figure:
She is standing, with a soft 3/4 body pose, slightly turned toward the camera. She delicately holds a woven wicker basket with both hands, positioned at her waist height. Her body posture is natural, elegant, and graceful.
Body Angle:
The body is angled approximately 30 degrees to her left (from the camera’s perspective), while her head is fully turned toward the camera with a direct gaze.
Attire & Accessories:
Top:
A light grey or silver silk/satin blouse with an asymmetrical draped design on the front, loose dolman sleeves, and a long flowing tail extending from the right side of the garment.
Bottom:
Dark plum or deep burgundy tailored trousers with a refined and well-fitted design.
Accessories:
Two delicate layered gold chain necklaces with small circular pendants; small gold hoop earrings; vibrant deep red nail polish on her fingernails.
Angle & Composition:
The image is captured at eye level. The frame is set as a medium shot (waist-up), with a perfectly balanced and centered composition. Blurred leaves in the foreground create a natural frame around the subject, and a shallow depth of field separates the subject from the background.
Framing:
Medium shot from the waist up, ensuring that both the subject and the main element of the image, the small wicker basket, are clearly visible.
Lighting:
Soft, diffused natural light (such as golden hour sunlight or gentle overcast daylight).
The lighting creates subtle highlights on her hair and face while producing soft and natural shadows.
Environment & Background:
An outdoor setting in a blackberry farm or a lush green garden. The background consists of a dense, blurred composition of green leaves, tangled stems, and hints of ripe and unripe blackberries growing on the bushes. The background should have a beautiful natural bokeh effect.
Props:
A small natural handled wicker basket filled with a generous amount of ripe blackberries and a few red raspberries.
Camera Details (Optional):
Captured with a Canon EOS R5 camera and an 85mm f/1.4 lens. Aperture set to f/1.8 to create a shallow depth of field and smooth background blur. Featuring a subtle film grain texture to create a professional and cinematic photography feel.""",

    "موتور": """هویت چهره مرجع ۱۰۰ درصد حفظ شود * نوع عکس: عکس لایف‌استایل و پرتره خیابانی تمام قد در فضای باز. * سوژه: زن جوانی با ظاهر خاورمیانه‌ای، با موهای تیره و براق که به صورت دم‌اسبی صاف و تمیز بسته شده است، و با لبخندی گرم و ملایم با لبهای بسته رو به دوربین نگاه می‌کند. * پوشش: او یک تی‌شرت سفید اورسایز با یک چاپ گرافیکی از یک اسکوتر صورتی که گلهایی روی آن است، به همراه یک شلوار جین گشاد (باگی) به رنگ آبی روشن و قد بریده شده (کالوت) پوشیده است. او جوراب‌های ساده سفید و کفش‌های کتانی صورتی و سفید ساق‌دار (مانند کانورس) به پا دارد. یک گردنبند ظریف نیز به گردن دارد.
اشیاء: او در کنار (به اسکوتر تکیه داده) یک اسکوتر وِسپا کلاسیک با رنگ صورتی پاستلی ملایم مات و جذاب ایستاده است. اسکوتر دارای یک شیشه جلوی شفاف، آینه‌های کرومی گرد و چراغ جلوی گرد است و یک جعبه حمل عقب صورتی هماهنگ. روی زین اسکوتر، یک دسته گل بزرگ و پرپشت از گل‌های پئونی (صدتومانی) و گل‌های دیگر در رنگ‌های صورتی، زرد، نارنجی و کرم قرار گرفته است. * ژست: دست های سوژه روی دسته های فرمان اسکوتر را گرفته است به طوریکه انگشتانش به دور دسته فرمان پیچیده شده اند. پای راست که روی پای چپ قرار گرفته است، در وضعیت راحتی ایستاده است.
پس‌زمینه: یک خیابان سنگفرش شده دنج در فضای باز. در قسمت پیاده رو یک دیوار سنگی قدیمی که بخشی از دیوار با پیچک‌های سبز تیره پوشیده شده است. در پس‌زمینه، قسمت پیاده رو یک درختی با تنه خمیده و برگ‌های سبز متراکم دیده می‌شوند. نور خورشید بعدازظهر از لای درختان عبور می‌کند و الگوی نوری ملایم و گرم (dappled light) ایجاد می‌کند. * نورپردازی: نور طبیعی و نرم خورشید بعدازظهر، با کمی افکت تابش گرم (ساعت طلایی)، که سوژه را به طور یکنواخت روشن کرده است. * ترکیب‌بندی: نمای تمام قد از زن و اسکوتر. اسکوتر در سمت چپ و زن در سمت راست قرار گرفته‌اند و توازن خوبی در قاب ایجاد شده است. پس‌‌زمینه سنگفرش و پوشش گیاهی روی بخشی از دیوار عمق ایجاد می‌کند. * سبک و تکنیک: عکس شارپ با فوکوس دقیق روی چهره زن و اسکوتر. عمق میدان کم (دیافراگم باز) برای ایجاد بوکه زیبا در پس‌زمینه . عکاسی لایف‌استایل با کیفیت سینمایی و بافت‌های دقیق در لباس و سنگفرش. کادر ۳:۴""",

    "عروس": """کلوزآپ مدیوم، زاویه سطح چشم، نمای نیم‌رخ راست از پهلو، دوربین از پهلو گرفته شده. کادر عمودی ۹:۱۶
نمای کادر از سر تا گردن و بخشی از شانه چپ
شانه راست در کادر دیده نمی شود
زن: یک زن جوان با پوست صاف و آرایش دقیق (رژ لب قرمز مات تند، خط چشم کشیده، سایه ملایم) با موهای پر پشت و از ریشه حجم دار. ناخن های مانیکور شده کوتاه به رنگ لیمویی .او یک تاپ کرم رنگ پوشیده است.
پرنده: یک عروس هلندی لوتینو (Cockatiel) زرد روشن با گونه‌های نارنجی متمایز، تاج (crest) زرد و چشمان تیره. پای پرنده روی انگشت زن قرار گرفته است.
[عمل/تعامل]: پیشانی زن و سر عروس هلندی (درست در جلوی تاج) دقیقاً با یکدیگر در تماس هستند. سر زن کمی به سمت عروس هلندی متمایل است یا به سمت پایین متمایل شده و نگاه زن به سمت عروس هلندی است ، که تصویری از یک پیوند عاطفی عمیق، اعتماد و آرامش را خلق می‌کند. زن لبخن ملایم با لبهای بسته دارد
[تنظیمات/پس‌زمینه]: پس‌زمینه بوکه فوق‌العاده نرم و محو با رنگ‌های گرم و مات (طلایی، بژ، قهوه‌ای)، که فضایی دنج، صمیمی و رویایی ایجاد کرده است.
نورپردازی]: نور طبیعی، نرم و پخش‌شده (Soft, diffused light) که بافت‌های مختلف از جمله پرهای ظریف، و نورپردازی جانبی ملایمی روی صورت زن دارد.
[جزئیات فنی]: عمق میدان بسیار کم (Very shallow depth of field)، با فوکوس فوق‌العاده دقیق روی چشم‌های هر دو سوژه (چشم عسلی زن و چشم تیره پرنده). بافت پرها و موی زن با جزئیات بالا ثبت شده است.
[پالت رنگ و حس]: پالت گرم (کرم، طلایی، زرد، قرمز تند). حس آرامش، صمیمیت، پیوند عاطفی عمیق و اعتماد.""",

    "چشم": """Создай ультрареалистичный премиальный портрет, полностью сохранив мою индивидуальность и узнаваемость. Не изменяй мои естественные черты лица, форму и пропорции, геометрию лица, костную структуру, форму глаз, носа, губ, бровей, натуральную текстуру кожи, возраст, выражение лица и причёску. Лицо должно остаться максимально похожим на исходное изображение. Разрешено изменять только макияж, освещение и художественную обработку.
Композиция: Экстремально крупный план (Extreme Close-Up). В кадре главным объектом является один видимый глаз, который частично выглядывает сквозь длинные волосы с мягкими крупными волнами, падающими на лицо. Остальная часть лица находится в естественном мягком размытии (Soft Blur) и частично скрыта или обрезана. Внимание полностью сосредоточено на глазе и взгляде.
Макияж глаз — роскошный современный Instagram Editorial Glam:
Очень длинные, густые, идеально разделённые объёмные ресницы (Wispy Volume Lashes).
Аккуратные выразительные нижние ресницы.
Глубокая чёрная верхняя стрелка с идеально острым вытянутым кончиком (Sharp Winged Eyeliner).
Профессиональная растушёвка теней в оттенках шампань, бежевый, тауп и тёплый коричневый.
Лёгкое сияние в центре века для создания объёма и глубины.
Деликатный шампанский хайлайт во внутреннем уголке глаза.
Максимально подчёркнутая линия роста ресниц.
Густые натуральные пушистые брови с аккуратной мягкой формой.
Взгляд должен быть глубоким, выразительным, роскошным и гипнотизирующим, но без чрезмерно тяжёлого или неестественного макияжа.
Макияж кожи и лица:
Гладкая кожа с сохранением естественной текстуры и реалистичных деталей.
Тёплый загорелый оттенок кожи.
Очень мягкий профессиональный контуринг.
Лёгкий персиково-تёплый румянец.
Губы оттенка Dusty Rose с немного более тёмным контуром, мягкой растушёвкой и матовым бархатным финишем.
Освещение и атмосфера:
Мягкий тёплый золотистый солнечный свет с пониженной интенсивностью.
Избегать сильных пересветов и слишком ярких бликов.
Деликатное подсвечивание ресниц и глаза мягким золотым светом.
Атмосфера аналоговой плёнки 35mm Film.
Лёгкое плёночное зерно.
Тонкие золотистые световые засветы (Golden Light Leaks).
Небольшой кинематографичный наклон кадра.
Ностальгическое настроение премиальной fashion-съёмки.
Фокус и качество:
Очень малая глубина резкости (Shallow Depth of Field).
Абсолютно резкий фокус только на видимом глазе.
Остальные детали мягко размыты естественным образом.
Максимально реалистичная фотография уровня премиальной рекламной кампании косметики..
Luxury fashion editorial aesthetic.
Фотореализм, высокая детализация, натуральная кожа, реалистичный свет.
Важно: Не менять личность, не менять форму лица, не добавлять новые черты, не омолаживать и не старить, не менять цвет и структуру волос, не делать искусственный или пластиковый эффект кожи. Только профессиональный ماкияж, мягкое освещение и кинематографическая обработка.""",

    "هرمز": """یک عکس تمام‌قد سینمایی و فوق‌العاده واقع‌گرایانه با وضوح بالا از یک زن جوان متفکر خاورمیانه‌ای که به صورت چهارزانو (نیمه‌نیلوفری) روی مجموعه‌ای بزرگ از صخره‌های رسوبی قرمز و خشن(جزیره هرمز) نشسته است. صحنه در امتداد یک خط ساحلی صخره‌ای قرار دارد و دریای پهناور به رنگ آبی فیروزه‌ای عمیق و آرام تا افق آبی کم‌رنگ زیر نور گرم آفتاب اواخر بعدازظهر گسترش یافته است. زن پوشش اصیل بندری/ایرانی با جزئیات ظریف گلدوزی‌شده بر تن دارد. تونیک سفید او دارای الگوهای سنتی گلدوزی‌شده پرجزئیات و رنگارنگ (طلایی، قرمز، سبز، آبی) روی یقه، جلو سینه و سرآستین‌ها است. او شلوار سرخابی هماهنگ با همان الگوی گلدوزی را پوشیده است. یک چادر (شال) بزرگ و شفاف سرخابی روی سر، شانه‌ها و بدنش آویخته شده و بیشتر دامن و پاهایش را پوشانده است و بخشی از آن روی صخره‌های قرمز کشیده شده است. پاهای برهنه او روی صخره‌ها قرار دارند. دست‌ها به آرامی روی دامن قرار گرفته‌اند و او با حالتی متفکر و عمیق به سمت راست (خارج از کادر) نگاه می‌کند. نور گرم و طبیعی ساعت طلایی از کنار می‌تابد و چهره‌اش را روشن می‌کند و بافت‌های گلدوزی، پوست و صخره‌ها را برجسته می‌کند. ترکیب‌بندی متوازن است و دریا پس‌زمینه پهناور و صخره‌های خشن پیش‌زمینه را قاب می‌کنند. تمرکز کامل بر روی زن و لباسش است و عمق میدان روی دریا و خط افق ملایم‌تر است. بافت‌ها بسیار دقیق و واضح هستند.""",

    "طبیعت": """Create an ultra-realistic casual smartphone photo of a young woman outdoors sitting on grass. She has long voluminous dark-brown wavy hair, parted naturally, and tilts her head slightly toward the camera with a warm genuine smile. She wears a white sleeveless fitted dress with a soft flowing skirt and thin metallic bracelets. Her arms rest crossed naturally in front of her. Bright natural afternoon sunlight creates soft highlights and gentle shadows across her face and hair, with a blurred green garden background. Slightly soft low-quality smartphone camera, natural imperfect exposure, subtle compression and grain, authentic candid photography, no flash, 2:3, no artificial AI look.
Ultra-realistic natural skin texture, clearly visible fine pores and micro-pores, realistic peach fuzz, subtle skin lines, tiny imperfections and natural unevenness in skin tone. Keep the original facial identity and facial structure unchanged. Skin is smooth only where naturally smooth, never artificially perfect. No skin retouching, no airbrushing, no blur, no beauty filter, no waxy or plastic appearance. Realistic sebaceous shine and tiny specular highlights on the nose, cheeks and lips, highly detailed pores visible in close-up, authentic smartphone photography skin texture."""
}

# ==================== تابع پیام خوش‌آمدگویی و منو ====================
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    # ساخت دکمه‌های شیشه‌ای به صورت دو ستونی
    keyboard = []
    keys = list(prompts_data.keys())
    for i in range(0, len(keys), 2):
        row = [InlineKeyboardButton(keys[i], callback_data=keys[i])]
        if i + 1 < len(keys):
            row.append(InlineKeyboardButton(keys[i+1], callback_data=keys[i+1]))
        keyboard.append(row)
    
    reply_markup = InlineKeyboardMarkup(keyboard)
    
    welcome_text = (
        "سلام! به ربات آرشیو پرامپت‌های تخصصی خوش آمدید. 🌸\n\n"
        "لطفاً از منوی زیر پرامپت مورد نظر خود را انتخاب کنید تا متن آن برایتان ارسال شود:"
    )
    
    await update.message.reply_text(welcome_text, reply_markup=reply_markup)

# ==================== تابع مدیریت کلیک روی دکمه‌ها ====================
async def button_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()
    
    selected_key = query.data
    if selected_key in prompts_data:
        prompt_text = prompts_data[selected_key]
        # ارسال متن پرامپت در فرمت کد (قابل کپی با یک تپ)
        await query.message.reply_text(f"پرامپت **{selected_key}**:\n\n`{prompt_text}`", parse_mode="Markdown")
    else:
        await query.message.reply_text("پرامپت مورد نظر یافت نشد.")

# ==================== اجرای اصلی ربات ====================
def main():
    # ساخت اپلیکیشن و اتصال توکن
    app = ApplicationBuilder().token(TOKEN).build()
    
    # ثبت دستورات و هندلرها
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CallbackQueryHandler(button_handler))
    
    print("ربات با موفقیت روشن شد و در حال دریافت پیام است...")
    # شروع به کار ربات
    app.run_polling()

if __name__ == "__main__":
    main()
