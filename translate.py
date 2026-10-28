import re, sys, json
import os
ROOT=os.path.dirname(os.path.abspath(__file__))
SRC=os.path.join(ROOT,'index.html')
BASE='https://yishai108-bit.github.io/desert-star/'

EN={
"ערב כוכבים":"Stargazing",
"מחירים":"Prices",
"המלצות":"Reviews",
"ג'יפים והליכה":"Jeeps & hikes",
"מי מדריך":"Your guide",
"שאלות":"FAQ",
"לתיאום ערב כוכבים":"Book a stargazing night",
"ערב אחד מתחת לשביל החלב.":"One night under the Milky Way.",
"תצפית כוכבים עם טלסקופים גדולים במכתש רמון":"Stargazing with large telescopes in the Ramon Crater",
"כעשר דקות ממצפה רמון, בשמורת אור הכוכבים. עם משה קוגן, מורה דרך ותושב המקום. מתאים לזוגות, למשפחות ולקבוצות. בעברית, באנגלית וברוסית.":"Ten minutes from Mitzpe Ramon, inside the Dark Sky Reserve. With Moshe Kogan, licensed guide and local resident. For couples, families and groups. In English, Hebrew and Russian.",
"לפרטים וזמינות בוואטסאפ":"Details & availability on WhatsApp",
"גם ג'יפים והליכה":"Jeep tours & hikes too",
"שמורת אור כוכבים":"Dark Sky Reserve",
"היחידה במזרח התיכון":"the only one in the Middle East",
"מורה דרך מקומי":"Local licensed guide",
"תושב מצפה רמון מ-2014":"living in Mitzpe Ramon since 2014",
"עברית, אנגלית ורוסית":"English, Hebrew & Russian",
"הדרכה בגובה העיניים":"friendly, down-to-earth guiding",
"מעונן? מבטלים חינם":"Cloudy? Free cancellation",
"ובוחרים יחד תאריך אחר":"and we pick another date together",
"הפעילות המבוקשת":"Most popular",
"תצפית כוכבים במכתש רמון":"Stargazing in the Ramon Crater",
"שעתיים שבהן השמיים נפתחים":"Two hours when the sky opens up",
"מתמקמים על מזרונים בפינת זולה, הלייזר מצייר את קבוצות הכוכבים, ואז הטלסקופים הגדולים: ירח, פלנטות, ערפיליות וגלקסיות. בסוף מצלמים אתכם בחשיפה ארוכה על רקע הכוכבים.":"Settle onto mattresses in a cozy lounge corner, follow the laser as it traces the constellations, then look through the large telescopes: the Moon, planets, nebulae and galaxies. We end with a long-exposure photo of you under the stars.",
"טלסקופים גדולים, מזרונים, מחצלות וכסאות":"Large telescopes, mattresses, mats and chairs",
"הדרכה חיה על המזלות, המיתולוגיה והאסטרונומיה":"Live guiding: constellations, mythology and astronomy",
"תמונה שלכם בחשיפה ארוכה עם הכוכבים, במתנה":"Your long-exposure photo with the stars, as a gift",
"מגיל 5, כשעתיים, 10 דקות נסיעה ממצפה רמון":"Ages 5+, about two hours, 10 minutes' drive from Mitzpe Ramon",
"למבוגר בקבוצה פתוחה":"per adult, open group",
"ילדים 4-16: 150 ₪ · ערב פרטי לזוג החל מ-1,200 ₪ ·":"Children 4-16: 150 ₪ · private night for a couple from 1,200 ₪ · ",
"כל המחירים":"all prices",
"איך נראה הערב":"How the night goes",
"איך נראה ערב כוכבים במכתש":"What a stargazing night looks like",
"נפגשים כעשר דקות נסיעה ממצפה רמון, בשמורת אור הכוכבים. האורות כבים, העיניים מתרגלות, והשמיים מתמלאים.":"We meet about ten minutes' drive from Mitzpe Ramon, inside the Dark Sky Reserve. The lights go off, your eyes adjust, and the sky fills up.",
"מתמקמים":"Settle in",
"פינת זולה עם מזרונים על מחצלות, כסאות למי שמעדיף, ומדורה למי שמזמין אירוח מדברי.":"A lounge corner with mattresses on mats, chairs for those who prefer, and a campfire if you book the desert hospitality add-on.",
"מכירים את השמיים":"Meet the sky",
"עם סמן לייזר עוברים על קבוצות הכוכבים, המזלות וכוכב הצפון, עם סיפורים מהמיתולוגיה ומהאסטרונומיה, בגובה העיניים.":"With a laser pointer we go over the constellations, the zodiac and the North Star, with stories from mythology and astronomy, in plain language.",
"מסתכלים מקרוב":"Look closer",
"הטלסקופים הגדולים מכוונים לירח, לפלנטות, לצבירים ולגלקסיות. ובסוף, תמונה שלכם בחשיפה ארוכה עם הכוכבים.":"The large telescopes point at the Moon, the planets, star clusters and galaxies. And to finish, your long-exposure photo with the stars.",
"ומה המחיר?":"And the price?",
"מצטרפים לערב פתוח, או מזמינים ערב רק לכם. המחירים כוללים מע\"מ.":"Join an open night, or book a night just for you. Prices include VAT.",
"מצטרפים לקבוצה":"Join a group",
"ערב בהרשמה, בעברית. נפתח מ-5 משתתפים, עד 30. טלסקופ לכל 10 משתתפים.":"Scheduled night, guided in Hebrew. Runs from 5 participants, up to 30. One telescope per 10 participants.",
"מבוגר":"Adult",
"מגיל 17":"age 17+",
"ילד":"Child",
"גיל 4-16":"ages 4-16",
"מתחת לגיל 4":"Under 4",
"חינם":"Free",
"שעון חורף: מחזור ראשון 18:30, מחזור שני 21:30.":"Winter time: first session 18:30, second session 21:30.",
"מתי יש מקום?":"When is there space?",
"ערב פרטי":"Private night",
"רק אתם, בשעה שנוחה לכם. בעברית, באנגלית או ברוסית.":"Just you, at a time that suits you. In English, Hebrew or Russian.",
"זוג, אמצע שבוע":"Couple, midweek",
"ראשון עד רביעי":"Sunday to Wednesday",
"זוג, סוף שבוע":"Couple, weekend",
"חמישי עד שבת, כולל אירוח מדברי":"Thursday to Saturday, desert hospitality included",
"משפחה":"Family",
"עד 10 משתתפים":"up to 10 participants",
"קבוצה":"Group",
"עד 25 משתתפים":"up to 25 participants",
"קבוצה גדולה":"Large group",
"עד 40 משתתפים":"up to 40 participants",
"לתיאום ערב פרטי":"Book a private night",
"תוספות":"Add-ons",
"אירוח מדברי":"Desert hospitality",
"מדורה, תה ומרשמלו":"campfire, tea and marshmallows",
"טלסקופ נוסף":"Extra telescope",
"לקבוצות גדולות":"for large groups",
"מעל 40 משתתפים, מתמחרים יחד. אפשר לשלב עם טיול ג'יפים באותו אחר צהריים.":"Over 40 participants, we price it together. Can be combined with a jeep tour the same afternoon.",
"מעונן?":"Cloudy?",
"מבטלים בלי עלות. תקבלו הודעה עד שעתיים לפני, ונבחר יחד תאריך אחר.":"We cancel at no cost. You'll hear from us up to two hours before, and we'll pick another date together.",
"ביטול מצדכם: עד 14 יום לפני, החזר מלא. עד 7 ימים לפני, החזר של 50%. ביום הפעילות, ללא החזר.":"Cancellation by you: up to 14 days before, full refund. Up to 7 days before, 50% refund. On the day, no refund.",
"המלצות חמות":"Warm reviews",
"מה אומרים מטיילים שיצאו עם משה":"What travelers say after a night with Moshe",
"טטיאנה לישנצקי":"Tatiana Lishnetsky",
"תצפית כוכבים":"Stargazing",
"בפעם הראשונה בחיי ראינו את הירח, צדק ושביל החלב דרך טלסקופ. זו חוויה בלתי נשכחת לכל החיים. תודה רבה למשה!":"For the first time in my life we saw the Moon, Jupiter and the Milky Way through a telescope. An unforgettable experience for life. Thank you so much, Moshe!",
"ורדית לייבוביץ'":"Vardit Leibovitz",
"פגשנו את משה לפני 3 שנים לתצפית כוכבים עם קבוצת חברים ועכשיו חזרנו עם הילדים והנכדים. היתה חוויה מרתקת ומעניינת לכל הגילאים.":"We met Moshe 3 years ago for stargazing with a group of friends, and now we came back with the children and grandchildren. A fascinating experience for all ages.",
"שולה":"Shula",
"טיול ג'יפים במכתש רמון":"Jeep tour in the Ramon Crater",
"יצאנו קבוצה גדולה עם משה לטיול ג'יפים במכתש רמון. בזכות משה זכינו לטיול מושלם. הידע הרב שלו, אהבת המקום, אהבת האדם, הסבלנות האין סופית, החיוך.":"A big group of us went with Moshe on a jeep tour in the Ramon Crater. Thanks to Moshe it was a perfect trip: his deep knowledge, love of the place, love of people, endless patience, and that smile.",
"שלומית עמית פרנקל":"Shlomit Amit Frankel",
"טיול הליכה":"Hiking tour",
"היינו קבוצה של 18 אנשים בגילאים 5-75 ומזג אויר שלא היה לטובתינו. משה הצליח לסקרן ולעניין את כולנו. החל מטעימות בטבע, משחקים בצבע, גיאולוגיה, היסטוריה, ארכיאולוגיה והמון הומור.":"We were a group of 18, ages 5 to 75, and the weather wasn't on our side. Moshe managed to intrigue every one of us: tasting wild plants, games with color, geology, history, archaeology and lots of humor.",
"רוצים גם? לפרטים וזמינות בוואטסאפ":"Want this too? Details on WhatsApp",
"וביום? ג'יפים והליכה":"And by day? Jeeps & hikes",
"המכתש הגדול בעולם גם לאור יום. השילוב הכי מבוקש: ג'יפים אחר הצהריים וכוכבים באותו ערב.":"The world's largest erosion crater in daylight too. The most popular combo: a jeep tour in the afternoon and stars the same night.",
"ביום ובשקיעה":"Daytime & sunset",
"טיולי ג'יפים":"Jeep tours",
"עצירות בנקודות המיוחדות של המכתש, צבעי אבן החול, תופעות גאולוגיות וסיפורים על המקום. מתאים לכל גיל.":"Stops at the crater's special spots, the colored sandstone, geological wonders and stories of the place. Suitable for all ages.",
"משעתיים":"From 2 hours",
"מכתש רמון ובקעת צין":"Ramon Crater & Zin Valley",
"כל הגילאים":"All ages",
"לקבוצה, החל מ-980 ₪":"Per group, from 980 ₪",
"אפשר לשלב עם תצפית כוכבים באותו ערב":"can be combined with stargazing the same night",
"ברגל":"On foot",
"טיולי הליכה":"Hiking tours",
"פרסת נקרות, נחל ארדון, מעלה ברוש, סובב הר רמון, עין עבדת והרי אילת. מסלולים קלים למשפחות ומסלולים למיטיבי לכת, עם לינת שטח ומדורה בטיולים הארוכים.":"Nekarot Horseshoe, Ardon Wadi, Ma'ale Brosh, around Mount Ramon, Ein Avdat and the Eilat Mountains. Easy family trails and routes for serious hikers, with camping and a campfire on the longer treks.",
"חצי יום, 4-6 שעות":"Half day, 4-6 hours",
"יום שלם, 8-9 שעות":"Full day, 8-9 hours",
"2-3 ימים":"2-3 days",
"מחיר לפי מסלול וגודל קבוצה":"Price by route and group size",
"כולל הדרכה, ביטוח והקפצות":"includes guiding, insurance and transfers",
"קצת על משה":"A bit about Moshe",
"שמי משה קוגן, מורה דרך ותושב מצפה רמון. הגעתי לכאן עם ליאור, אשתי, ב-2014, וכאן הקמנו את המשפחה ואת דזרט סטאר. תמיד אהבתי לטייל במדבר ולחוות את השטח הפראי בלי תיווך.":"My name is Moshe Kogan, a licensed tour guide living in Mitzpe Ramon. I came here with my wife Lior in 2014, and this is where we built our family and Desert Star. I've always loved walking the desert and experiencing the wild as it is.",
"במכתש התאהבתי גם באסטרונומיה, למדתי וחקרתי אותה, ובימים אלה אני מתמחה בצילום אסטרונומי. עסק משפחתי קטן, שמתעקש על הדרכה שמתאימה בדיוק לקבוצה שמולו: ילדים ומבוגרים, מטיילים ותיקים ומי שזו הפעם הראשונה שלהם במדבר.":"In the crater I also fell in love with astronomy, studied it, and these days I'm specializing in astrophotography. A small family business that insists on guiding tailored to the group in front of it: children and adults, seasoned hikers and first-timers in the desert.",
"התמזל מזלי לעסוק בדבר שאני אוהב יותר מכל, ולחלוק עם מטיילים מהארץ ומהעולם את התשוקה שלי לטבע ולמדבר.":"I'm lucky to do what I love most, and to share my passion for nature and the desert with travelers from Israel and around the world.",
"שאלות ששואלים אותנו":"Questions we get asked",
"מה להביא לתצפית?":"What should I bring?",
"בגדים חמים, גם בקיץ. במדבר קר בלילה. נעליים סגורות ומים. את המזרונים, הכסאות והטלסקופים אנחנו מביאים.":"Warm clothes, even in summer. Desert nights are cold. Closed shoes and water. We bring the mattresses, chairs and telescopes.",
"ואם יהיה מעונן?":"What if it's cloudy?",
"מבטלים בלי עלות. תקבלו הודעה עד שעתיים לפני תחילת הפעילות, ונבחר יחד תאריך אחר.":"We cancel at no cost. You'll hear from us up to two hours before the start, and we'll pick another date together.",
"איפה נפגשים?":"Where do we meet?",
"בשמורת אור הכוכבים של מכתש רמון, כעשר דקות נסיעה ממצפה רמון. את נקודת המפגש המדויקת שולחים בוואטסאפ אחרי התיאום.":"In the Ramon Crater Dark Sky Reserve, about ten minutes' drive from Mitzpe Ramon. We send the exact meeting point on WhatsApp after booking.",
"באיזו שפה ההדרכה?":"Which languages?",
"עברית, אנגלית ורוסית. הקבוצה הפתוחה בכרטיסים מתקיימת בעברית בלבד. פעילות פרטית בכל אחת מהשפות.":"English, Hebrew and Russian. The open ticketed group runs in Hebrew only. Private activities in any of the three.",
"מה עם ילדים?":"What about children?",
"ילדים מוזמנים, וההדרכה מותאמת לגיל. בקבוצה הפתוחה ילדים בגיל 4-16 ב-150 ₪, מתחת לגיל 4 חינם.":"Children are welcome, and the guiding adapts to their age. In the open group, ages 4-16 are 150 ₪, under 4 free.",
"אפשר לשלב כמה פעילויות?":"Can we combine activities?",
"כן. טיול ג'יפים אחר הצהריים ותצפית כוכבים באותו ערב הוא השילוב הכי מבוקש. בטיולים של כמה ימים יש גם הדרכת אסטרונומיה ליד המדורה.":"Yes. A jeep tour in the afternoon and stargazing the same night is the most popular combo. Multi-day treks also include astronomy by the campfire.",
"נתאם לכם ערב?":"Shall we plan your night?",
"כתבו בוואטסאפ או השאירו פרטים. חוזרים אליכם עם תאריכים פנויים.":"Write on WhatsApp or leave your details. We get back to you with available dates.",
"הכי מהיר: וואטסאפ":"Fastest: WhatsApp",
"ספרו לנו מתי אתם באזור וכמה תהיו, ונחזור עם מה שפנוי.":"Tell us when you're in the area and how many you are, and we'll reply with what's available.",
"וואטסאפ 052-605-2744":"WhatsApp +972 52-605-2744",
"טלפון 052-605-2744":"Phone +972 52-605-2744",
"מצפה רמון, הנגב":"Mitzpe Ramon, Negev, Israel",
"או השאירו פרטים ונחזור אליכם":"Or leave your details and we'll get back to you",
"שם מלא":"Full name",
"מספר טלפון":"Phone number",
"מועד מבוקש":"Preferred date",
"כמה תהיו":"How many of you",
"איזו פעילות":"Activity",
"ערב כוכבים פרטי":"Private stargazing night",
"טיול ג'יפים":"Jeep tour",
"שילוב של כמה פעילויות":"A combination of activities",
"הערות":"Notes",
"שליחה בוואטסאפ":"Send on WhatsApp",
"הלחיצה פותחת וואטסאפ עם הפרטים שמילאתם. אפשר גם פשוט להתקשר.":"This opens WhatsApp with the details you filled in. You can also just call.",
"תצפיות כוכבים":"Stargazing",
"אסטרובלוג":"Astroblog",
"הצהרת נגישות":"Accessibility",
"מדיניות פרטיות":"Privacy policy",
"Desert Star · משה קוגן · מצפה רמון · 052-605-2744 ·":"Desert Star · Moshe Kogan · Mitzpe Ramon · +972 52-605-2744 ·",
"נבנה על ידי":"Built by",
"תצפיות כוכבים עם טלסקופים גדולים במכתש רמון, טיולי ג'יפים וטיולי הליכה. משה קוגן, מורה דרך ותושב מצפה רמון. הדרכה בעברית, אנגלית ורוסית.":"Stargazing with large telescopes in the Ramon Crater, jeep tours and hiking. Moshe Kogan, licensed guide living in Mitzpe Ramon. Tours in English, Hebrew and Russian.",
"Desert Star | תצפית כוכבים במכתש רמון":"Desert Star | Stargazing in the Ramon Crater",
"ערב אחד מתחת לשביל החלב, עם טלסקופים גדולים ומורה דרך תושב מצפה רמון. גם ג'יפים והליכה במכתש.":"One night under the Milky Way, with large telescopes and a local guide from Mitzpe Ramon. Jeep tours and hikes in the crater too.",
"Desert Star, לראש העמוד":"Desert Star, back to top",
"ניווט":"Navigation",
"היי משה, הגעתי מהאתר ואשמח לפרטים וזמינות לערב כוכבים":"Hi Moshe, I found you on the website. I'd love details and availability for a stargazing night",
"טלסקופ גדול על רקע שביל החלב במכתש רמון":"A large telescope against the Milky Way in the Ramon Crater",
"לגלול למטה":"Scroll down",
"קבוצה עומדת בטבעת אור ליד טלסקופ גדול, מעליהם שביל החלב":"A group standing in a ring of light next to a large telescope, the Milky Way above",
"היי משה, אשמח לפרטים וזמינות לתצפית כוכבים":"Hi Moshe, I'd love details and availability for stargazing",
"קבוצה יושבת סביב מדורה במדבר":"A group sitting around a campfire in the desert",
"מדריך מצביע עם לייזר ירוק אל השמיים ליד מדורה":"A guide pointing a green laser at the sky next to a campfire",
"אדם מביט דרך טלסקופ גדול, מעליו שביל החלב":"A man looking through a large telescope, the Milky Way above",
"קבוצה יושבת בטבעת אור מתחת לשביל החלב":"A group sitting in a ring of light under the Milky Way",
"היי משה, אשמח להצטרף לערב כוכבים בקבוצה. מתי יש מקום?":"Hi Moshe, I'd like to join a group stargazing night. When is there space?",
"זוג בטבעת אור בין שני טלסקופים מתחת לשביל החלב":"A couple in a ring of light between two telescopes under the Milky Way",
"היי משה, אשמח לפרטים על ערב כוכבים פרטי":"Hi Moshe, I'd love details about a private stargazing night",
"משפחה ליד טלסקופ מתחת לשמיים זרועי כוכבים":"A family next to a telescope under a starry sky",
"חמישה כוכבים":"Five stars",
"היי משה, אשמח לפרטים וזמינות לערב כוכבים":"Hi Moshe, I'd love details and availability for a stargazing night",
"תמונות מהשטח":"Photos from the field",
"זוג בטבעת אור ליד טלסקופ, מתחת לשביל החלב":"A couple in a ring of light next to a telescope, under the Milky Way",
"נגן עוד עומד בין שני טלסקופים מתחת לשביל החלב":"An oud player standing between two telescopes under the Milky Way",
"משפחה מצביעה לשמיים זרועי הכוכבים":"A family pointing at the starry sky",
"הירח בחצי, מצולם דרך טלסקופ":"The half Moon, photographed through a telescope",
"אוהלים בלילה בחניון שטח מתחת לכוכבים":"Tents at night in a desert campsite under the stars",
"ערפילית אוריון, צילום אסטרונומי":"The Orion Nebula, astrophotography",
"שני ילדים בונים מגדל אבנים במדבר":"Two children building a stone tower in the desert",
"אנשים עומדים על ג'יפ בשקיעה":"People standing on a jeep at sunset",
"קניון סלע בהרי אילת":"A rock canyon in the Eilat Mountains",
"דקלים ושביל בעין עבדת":"Palm trees and a trail at Ein Avdat",
"משפחה עומדת על גג ג'יפ בשקיעה מעל מכתש רמון":"A family standing on a jeep roof at sunset above the Ramon Crater",
"היי משה, אשמח לפרטים וזמינות לטיול ג'יפים":"Hi Moshe, I'd love details and availability for a jeep tour",
"קבוצת מטיילים עם תרמילים עומדת בלב מכתש רמון":"A group of hikers with backpacks in the heart of the Ramon Crater",
"היי משה, אשמח לפרטים על טיול הליכה":"Hi Moshe, I'd love details about a hiking tour",
"אדם יושב ליד מדורה במדבר, מעליו שביל החלב":"A man sitting by a campfire in the desert, the Milky Way above",
"למשל: חמישי 6.11":"e.g. Thursday, Nov 6",
"מבוגרים וילדים":"adults and children",
"איפה אתם לנים, בקשות מיוחדות, שפה...":"Where you're staying, special requests, language...",
"קישורים":"Links",
"להתקשר":"Call",
}
EN_JS={"היי משה, הגעתי מהאתר.":"Hi Moshe, I found you on the website.","שם: ":"Name: ","טלפון: ":"Phone: ","פעילות: ":"Activity: ","מועד מבוקש: ":"Preferred date: ","כמה נהיה: ":"How many: ","הערות: ":"Notes: "}
EN_AV={"ט":"T","ו":"V","ש":"S"}

RU={
"ערב כוכבים":"Звёзды",
"מחירים":"Цены",
"המלצות":"Отзывы",
"ג'יפים והליכה":"Джипы и походы",
"מי מדריך":"Гид",
"שאלות":"Вопросы",
"לתיאום ערב כוכבים":"Записаться на звёзды",
"ערב אחד מתחת לשביל החלב.":"Одна ночь под Млечным Путём.",
"תצפית כוכבים עם טלסקופים גדולים במכתש רמון":"Наблюдение звёзд в большие телескопы в кратере Рамон",
"כעשר דקות ממצפה רמון, בשמורת אור הכוכבים. עם משה קוגן, מורה דרך ותושב המקום. מתאים לזוגות, למשפחות ולקבוצות. בעברית, באנגלית וברוסית.":"Десять минут от Мицпе-Рамона, в заповеднике тёмного неба. С Моше Коганом, лицензированным гидом и местным жителем. Для пар, семей и групп. На русском, иврите и английском.",
"לפרטים וזמינות בוואטסאפ":"Подробности и даты в WhatsApp",
"גם ג'יפים והליכה":"Также джипы и походы",
"שמורת אור כוכבים":"Заповедник тёмного неба",
"היחידה במזרח התיכון":"единственный на Ближнем Востоке",
"מורה דרך מקומי":"Местный гид с лицензией",
"תושב מצפה רמון מ-2014":"живёт в Мицпе-Рамоне с 2014 года",
"עברית, אנגלית ורוסית":"Русский, иврит и английский",
"הדרכה בגובה העיניים":"живо, просто и понятно",
"מעונן? מבטלים חינם":"Облачно? Отмена бесплатно",
"ובוחרים יחד תאריך אחר":"и вместе выбираем другую дату",
"הפעילות המבוקשת":"Самое популярное",
"תצפית כוכבים במכתש רמון":"Наблюдение звёзд в кратере Рамон",
"שעתיים שבהן השמיים נפתחים":"Два часа, когда небо открывается",
"מתמקמים על מזרונים בפינת זולה, הלייזר מצייר את קבוצות הכוכבים, ואז הטלסקופים הגדולים: ירח, פלנטות, ערפיליות וגלקסיות. בסוף מצלמים אתכם בחשיפה ארוכה על רקע הכוכבים.":"Устраиваемся на матрасах в уютном уголке, лазер рисует созвездия, а затем большие телескопы: Луна, планеты, туманности и галактики. В конце снимаем вас на длинной выдержке на фоне звёзд.",
"טלסקופים גדולים, מזרונים, מחצלות וכסאות":"Большие телескопы, матрасы, коврики и стулья",
"הדרכה חיה על המזלות, המיתולוגיה והאסטרונומיה":"Живой рассказ о созвездиях, мифологии и астрономии",
"תמונה שלכם בחשיפה ארוכה עם הכוכבים, במתנה":"Ваше фото на длинной выдержке со звёздами, в подарок",
"מגיל 5, כשעתיים, 10 דקות נסיעה ממצפה רמון":"С 5 лет, около двух часов, 10 минут езды от Мицпе-Рамона",
"למבוגר בקבוצה פתוחה":"за взрослого в открытой группе",
"ילדים 4-16: 150 ₪ · ערב פרטי לזוג החל מ-1,200 ₪ ·":"Дети 4-16: 150 ₪ · частный вечер для пары от 1 200 ₪ · ",
"כל המחירים":"все цены",
"איך נראה הערב":"Как проходит вечер",
"איך נראה ערב כוכבים במכתש":"Как проходит звёздная ночь в кратере",
"נפגשים כעשר דקות נסיעה ממצפה רמון, בשמורת אור הכוכבים. האורות כבים, העיניים מתרגלות, והשמיים מתמלאים.":"Встречаемся примерно в десяти минутах езды от Мицпе-Рамона, в заповеднике тёмного неба. Свет гаснет, глаза привыкают, и небо наполняется звёздами.",
"מתמקמים":"Устраиваемся",
"פינת זולה עם מזרונים על מחצלות, כסאות למי שמעדיף, ומדורה למי שמזמין אירוח מדברי.":"Уголок с матрасами на ковриках, стулья для тех, кому удобнее, и костёр для тех, кто заказал пустынное гостеприимство.",
"מכירים את השמיים":"Знакомимся с небом",
"עם סמן לייזר עוברים על קבוצות הכוכבים, המזלות וכוכב הצפון, עם סיפורים מהמיתולוגיה ומהאסטרונומיה, בגובה העיניים.":"С лазерной указкой проходим по созвездиям, знакам зодиака и Полярной звезде, с историями из мифологии и астрономии, простым языком.",
"מסתכלים מקרוב":"Смотрим вблизи",
"הטלסקופים הגדולים מכוונים לירח, לפלנטות, לצבירים ולגלקסיות. ובסוף, תמונה שלכם בחשיפה ארוכה עם הכוכבים.":"Большие телескопы направлены на Луну, планеты, звёздные скопления и галактики. А в конце ваше фото на длинной выдержке со звёздами.",
"ומה המחיר?":"Сколько это стоит?",
"מצטרפים לערב פתוח, או מזמינים ערב רק לכם. המחירים כוללים מע\"מ.":"Присоединяйтесь к открытому вечеру или закажите вечер только для вас. Цены включают НДС.",
"מצטרפים לקבוצה":"В группе",
"ערב בהרשמה, בעברית. נפתח מ-5 משתתפים, עד 30. טלסקופ לכל 10 משתתפים.":"Вечер по записи, на иврите. От 5 участников, до 30. Один телескоп на 10 человек.",
"מבוגר":"Взрослый",
"מגיל 17":"от 17 лет",
"ילד":"Ребёнок",
"גיל 4-16":"4-16 лет",
"מתחת לגיל 4":"До 4 лет",
"חינם":"Бесплатно",
"שעון חורף: מחזור ראשון 18:30, מחזור שני 21:30.":"Зимнее время: первый сеанс 18:30, второй 21:30.",
"מתי יש מקום?":"Когда есть места?",
"ערב פרטי":"Частный вечер",
"רק אתם, בשעה שנוחה לכם. בעברית, באנגלית או ברוסית.":"Только вы, в удобное вам время. На русском, иврите или английском.",
"זוג, אמצע שבוע":"Пара, будни",
"ראשון עד רביעי":"с воскресенья по среду",
"זוג, סוף שבוע":"Пара, выходные",
"חמישי עד שבת, כולל אירוח מדברי":"с четверга по субботу, включая пустынное гостеприимство",
"משפחה":"Семья",
"עד 10 משתתפים":"до 10 участников",
"קבוצה":"Группа",
"עד 25 משתתפים":"до 25 участников",
"קבוצה גדולה":"Большая группа",
"עד 40 משתתפים":"до 40 участников",
"לתיאום ערב פרטי":"Заказать частный вечер",
"תוספות":"Дополнительно",
"אירוח מדברי":"Пустынное гостеприимство",
"מדורה, תה ומרשמלו":"костёр, чай и маршмеллоу",
"טלסקופ נוסף":"Дополнительный телескоп",
"לקבוצות גדולות":"для больших групп",
"מעל 40 משתתפים, מתמחרים יחד. אפשר לשלב עם טיול ג'יפים באותו אחר צהריים.":"Больше 40 участников — договариваемся о цене. Можно совместить с джип-туром в тот же день.",
"מעונן?":"Облачно?",
"מבטלים בלי עלות. תקבלו הודעה עד שעתיים לפני, ונבחר יחד תאריך אחר.":"Отменяем без оплаты. Мы сообщим не позднее чем за два часа, и вместе выберем другую дату.",
"ביטול מצדכם: עד 14 יום לפני, החזר מלא. עד 7 ימים לפני, החזר של 50%. ביום הפעילות, ללא החזר.":"Отмена с вашей стороны: за 14 дней — полный возврат. За 7 дней — возврат 50%. В день мероприятия — без возврата.",
"המלצות חמות":"Тёплые отзывы",
"מה אומרים מטיילים שיצאו עם משה":"Что говорят путешественники после вечера с Моше",
"טטיאנה לישנצקי":"Татьяна Лишнецкая",
"תצפית כוכבים":"Наблюдение звёзд",
"בפעם הראשונה בחיי ראינו את הירח, צדק ושביל החלב דרך טלסקופ. זו חוויה בלתי נשכחת לכל החיים. תודה רבה למשה!":"Впервые в жизни мы увидели Луну, Юпитер и Млечный Путь в телескоп. Незабываемое впечатление на всю жизнь. Огромное спасибо Моше!",
"ורדית לייבוביץ'":"Вардит Лейбович",
"פגשנו את משה לפני 3 שנים לתצפית כוכבים עם קבוצת חברים ועכשיו חזרנו עם הילדים והנכדים. היתה חוויה מרתקת ומעניינת לכל הגילאים.":"Мы познакомились с Моше 3 года назад на наблюдении звёзд с друзьями, а теперь вернулись с детьми и внуками. Увлекательно и интересно для всех возрастов.",
"שולה":"Шула",
"טיול ג'יפים במכתש רמון":"Джип-тур по кратеру Рамон",
"יצאנו קבוצה גדולה עם משה לטיול ג'יפים במכתש רמון. בזכות משה זכינו לטיול מושלם. הידע הרב שלו, אהבת המקום, אהבת האדם, הסבלנות האין סופית, החיוך.":"Большой группой мы поехали с Моше на джип-тур по кратеру Рамон. Благодаря Моше поездка получилась идеальной: его глубокие знания, любовь к месту, любовь к людям, бесконечное терпение и улыбка.",
"שלומית עמית פרנקל":"Шломит Амит Франкель",
"טיול הליכה":"Пеший поход",
"היינו קבוצה של 18 אנשים בגילאים 5-75 ומזג אויר שלא היה לטובתינו. משה הצליח לסקרן ולעניין את כולנו. החל מטעימות בטבע, משחקים בצבע, גיאולוגיה, היסטוריה, ארכיאולוגיה והמון הומור.":"Нас было 18 человек от 5 до 75 лет, и погода была не на нашей стороне. Моше сумел увлечь каждого: дегустация растений, игры с цветом, геология, история, археология и много юмора.",
"רוצים גם? לפרטים וזמינות בוואטסאפ":"Хотите так же? Напишите в WhatsApp",
"וביום? ג'יפים והליכה":"А днём? Джипы и походы",
"המכתש הגדול בעולם גם לאור יום. השילוב הכי מבוקש: ג'יפים אחר הצהריים וכוכבים באותו ערב.":"Самый большой эрозионный кратер в мире и при свете дня. Самое популярное сочетание: джип-тур после обеда и звёзды тем же вечером.",
"ביום ובשקיעה":"Днём и на закате",
"טיולי ג'יפים":"Джип-туры",
"עצירות בנקודות המיוחדות של המכתש, צבעי אבן החול, תופעות גאולוגיות וסיפורים על המקום. מתאים לכל גיל.":"Остановки в особых точках кратера, цветные песчаники, геологические чудеса и истории этого места. Подходит для любого возраста.",
"משעתיים":"От 2 часов",
"מכתש רמון ובקעת צין":"Кратер Рамон и долина Цин",
"כל הגילאים":"Любой возраст",
"לקבוצה, החל מ-980 ₪":"За группу, от 980 ₪",
"אפשר לשלב עם תצפית כוכבים באותו ערב":"можно совместить с наблюдением звёзд тем же вечером",
"ברגל":"Пешком",
"טיולי הליכה":"Пешие походы",
"פרסת נקרות, נחל ארדון, מעלה ברוש, סובב הר רמון, עין עבדת והרי אילת. מסלולים קלים למשפחות ומסלולים למיטיבי לכת, עם לינת שטח ומדורה בטיולים הארוכים.":"Подкова Некарот, вади Ардон, подъём Брош, вокруг горы Рамон, Эйн-Авдат и Эйлатские горы. Лёгкие семейные маршруты и маршруты для опытных, с ночёвкой и костром в длинных походах.",
"חצי יום, 4-6 שעות":"Полдня, 4-6 часов",
"יום שלם, 8-9 שעות":"Целый день, 8-9 часов",
"2-3 ימים":"2-3 дня",
"מחיר לפי מסלול וגודל קבוצה":"Цена зависит от маршрута и размера группы",
"כולל הדרכה, ביטוח והקפצות":"включает сопровождение, страховку и трансферы",
"קצת על משה":"Немного о Моше",
"שמי משה קוגן, מורה דרך ותושב מצפה רמון. הגעתי לכאן עם ליאור, אשתי, ב-2014, וכאן הקמנו את המשפחה ואת דזרט סטאר. תמיד אהבתי לטייל במדבר ולחוות את השטח הפראי בלי תיווך.":"Меня зовут Моше Коган, я лицензированный гид и живу в Мицпе-Рамоне. Мы с женой Лиор приехали сюда в 2014 году, здесь создали семью и Desert Star. Я всегда любил ходить по пустыне и чувствовать дикую природу как она есть.",
"במכתש התאהבתי גם באסטרונומיה, למדתי וחקרתי אותה, ובימים אלה אני מתמחה בצילום אסטרונומי. עסק משפחתי קטן, שמתעקש על הדרכה שמתאימה בדיוק לקבוצה שמולו: ילדים ומבוגרים, מטיילים ותיקים ומי שזו הפעם הראשונה שלהם במדבר.":"В кратере я влюбился и в астрономию, изучал её, а сейчас осваиваю астрофотографию. Маленький семейный бизнес, который подбирает экскурсию точно под группу: дети и взрослые, опытные путешественники и те, кто в пустыне впервые.",
"התמזל מזלי לעסוק בדבר שאני אוהב יותר מכל, ולחלוק עם מטיילים מהארץ ומהעולם את התשוקה שלי לטבע ולמדבר.":"Мне повезло заниматься тем, что я люблю больше всего, и делиться своей страстью к природе и пустыне с путешественниками из Израиля и со всего мира.",
"שאלות ששואלים אותנו":"Частые вопросы",
"מה להביא לתצפית?":"Что взять с собой?",
"בגדים חמים, גם בקיץ. במדבר קר בלילה. נעליים סגורות ומים. את המזרונים, הכסאות והטלסקופים אנחנו מביאים.":"Тёплую одежду, даже летом. Ночью в пустыне холодно. Закрытую обувь и воду. Матрасы, стулья и телескопы привозим мы.",
"ואם יהיה מעונן?":"А если будет облачно?",
"מבטלים בלי עלות. תקבלו הודעה עד שעתיים לפני תחילת הפעילות, ונבחר יחד תאריך אחר.":"Отменяем без оплаты. Мы сообщим не позднее чем за два часа до начала, и вместе выберем другую дату.",
"איפה נפגשים?":"Где встречаемся?",
"בשמורת אור הכוכבים של מכתש רמון, כעשר דקות נסיעה ממצפה רמון. את נקודת המפגש המדויקת שולחים בוואטסאפ אחרי התיאום.":"В заповеднике тёмного неба кратера Рамон, примерно в десяти минутах езды от Мицпе-Рамона. Точное место встречи отправляем в WhatsApp после записи.",
"באיזו שפה ההדרכה?":"На каком языке экскурсия?",
"עברית, אנגלית ורוסית. הקבוצה הפתוחה בכרטיסים מתקיימת בעברית בלבד. פעילות פרטית בכל אחת מהשפות.":"Русский, иврит и английский. Открытая группа по билетам проходит только на иврите. Частные экскурсии на любом из трёх языков.",
"מה עם ילדים?":"А с детьми?",
"ילדים מוזמנים, וההדרכה מותאמת לגיל. בקבוצה הפתוחה ילדים בגיל 4-16 ב-150 ₪, מתחת לגיל 4 חינם.":"Дети приглашаются, рассказ подстраивается под возраст. В открытой группе дети 4-16 лет — 150 ₪, до 4 лет бесплатно.",
"אפשר לשלב כמה פעילויות?":"Можно совместить несколько активностей?",
"כן. טיול ג'יפים אחר הצהריים ותצפית כוכבים באותו ערב הוא השילוב הכי מבוקש. בטיולים של כמה ימים יש גם הדרכת אסטרונומיה ליד המדורה.":"Да. Джип-тур после обеда и звёзды тем же вечером — самое популярное сочетание. В многодневных походах есть и астрономия у костра.",
"נתאם לכם ערב?":"Спланируем ваш вечер?",
"כתבו בוואטסאפ או השאירו פרטים. חוזרים אליכם עם תאריכים פנויים.":"Напишите в WhatsApp или оставьте данные. Мы ответим со свободными датами.",
"הכי מהיר: וואטסאפ":"Быстрее всего: WhatsApp",
"ספרו לנו מתי אתם באזור וכמה תהיו, ונחזור עם מה שפנוי.":"Напишите, когда вы будете в наших краях и сколько вас, и мы ответим, что свободно.",
"וואטסאפ 052-605-2744":"WhatsApp +972 52-605-2744",
"טלפון 052-605-2744":"Телефон +972 52-605-2744",
"מצפה רמון, הנגב":"Мицпе-Рамон, Негев, Израиль",
"או השאירו פרטים ונחזור אליכם":"Или оставьте данные, и мы свяжемся с вами",
"שם מלא":"Имя и фамилия",
"מספר טלפון":"Номер телефона",
"מועד מבוקש":"Желаемая дата",
"כמה תהיו":"Сколько вас",
"איזו פעילות":"Активность",
"ערב כוכבים פרטי":"Частная звёздная ночь",
"טיול ג'יפים":"Джип-тур",
"שילוב של כמה פעילויות":"Сочетание нескольких активностей",
"הערות":"Комментарии",
"שליחה בוואטסאפ":"Отправить в WhatsApp",
"הלחיצה פותחת וואטסאפ עם הפרטים שמילאתם. אפשר גם פשוט להתקשר.":"Откроется WhatsApp с заполненными данными. Можно и просто позвонить.",
"תצפיות כוכבים":"Наблюдение звёзд",
"אסטרובלוג":"Астроблог",
"הצהרת נגישות":"Доступность",
"מדיניות פרטיות":"Конфиденциальность",
"Desert Star · משה קוגן · מצפה רמון · 052-605-2744 ·":"Desert Star · Моше Коган · Мицпе-Рамон · +972 52-605-2744 ·",
"נבנה על ידי":"Сайт сделал",
"תצפיות כוכבים עם טלסקופים גדולים במכתש רמון, טיולי ג'יפים וטיולי הליכה. משה קוגן, מורה דרך ותושב מצפה רמון. הדרכה בעברית, אנגלית ורוסית.":"Наблюдение звёзд в большие телескопы в кратере Рамон, джип-туры и пешие походы. Моше Коган, лицензированный гид из Мицпе-Рамона. Экскурсии на русском, иврите и английском.",
"Desert Star | תצפית כוכבים במכתש רמון":"Desert Star | Наблюдение звёзд в кратере Рамон",
"ערב אחד מתחת לשביל החלב, עם טלסקופים גדולים ומורה דרך תושב מצפה רמון. גם ג'יפים והליכה במכתש.":"Одна ночь под Млечным Путём, с большими телескопами и местным гидом из Мицпе-Рамона. А также джип-туры и походы по кратеру.",
"Desert Star, לראש העמוד":"Desert Star, наверх",
"ניווט":"Навигация",
"היי משה, הגעתי מהאתר ואשמח לפרטים וזמינות לערב כוכבים":"Здравствуйте, Моше! Я с сайта. Хочу узнать подробности и свободные даты для звёздной ночи",
"טלסקופ גדול על רקע שביל החלב במכתש רמון":"Большой телескоп на фоне Млечного Пути в кратере Рамон",
"לגלול למטה":"Прокрутить вниз",
"קבוצה עומדת בטבעת אור ליד טלסקופ גדול, מעליהם שביל החלב":"Группа в кольце света рядом с большим телескопом, над ними Млечный Путь",
"היי משה, אשמח לפרטים וזמינות לתצפית כוכבים":"Здравствуйте, Моше! Хочу узнать подробности и свободные даты для наблюдения звёзд",
"קבוצה יושבת סביב מדורה במדבר":"Группа сидит у костра в пустыне",
"מדריך מצביע עם לייזר ירוק אל השמיים ליד מדורה":"Гид показывает зелёным лазером на небо у костра",
"אדם מביט דרך טלסקופ גדול, מעליו שביל החלב":"Человек смотрит в большой телескоп, над ним Млечный Путь",
"קבוצה יושבת בטבעת אור מתחת לשביל החלב":"Группа сидит в кольце света под Млечным Путём",
"היי משה, אשמח להצטרף לערב כוכבים בקבוצה. מתי יש מקום?":"Здравствуйте, Моше! Хочу присоединиться к групповой звёздной ночи. Когда есть места?",
"זוג בטבעת אור בין שני טלסקופים מתחת לשביל החלב":"Пара в кольце света между двумя телескопами под Млечным Путём",
"היי משה, אשמח לפרטים על ערב כוכבים פרטי":"Здравствуйте, Моше! Хочу узнать подробности о частной звёздной ночи",
"משפחה ליד טלסקופ מתחת לשמיים זרועי כוכבים":"Семья у телескопа под звёздным небом",
"חמישה כוכבים":"Пять звёзд",
"היי משה, אשמח לפרטים וזמינות לערב כוכבים":"Здравствуйте, Моше! Хочу узнать подробности и свободные даты для звёздной ночи",
"תמונות מהשטח":"Фотографии",
"זוג בטבעת אור ליד טלסקופ, מתחת לשביל החלב":"Пара в кольце света у телескопа под Млечным Путём",
"נגן עוד עומד בין שני טלסקופים מתחת לשביל החלב":"Музыкант с удом между двумя телескопами под Млечным Путём",
"משפחה מצביעה לשמיים זרועי הכוכבים":"Семья показывает на звёздное небо",
"הירח בחצי, מצולם דרך טלסקופ":"Половина Луны, снято через телескоп",
"אוהלים בלילה בחניון שטח מתחת לכוכבים":"Палатки ночью в пустынном лагере под звёздами",
"ערפילית אוריון, צילום אסטרונומי":"Туманность Ориона, астрофотография",
"שני ילדים בונים מגדל אבנים במדבר":"Двое детей строят башню из камней в пустыне",
"אנשים עומדים על ג'יפ בשקיעה":"Люди стоят на джипе на закате",
"קניון סלע בהרי אילת":"Скальный каньон в Эйлатских горах",
"דקלים ושביל בעין עבדת":"Пальмы и тропа в Эйн-Авдат",
"משפחה עומדת על גג ג'יפ בשקיעה מעל מכתש רמון":"Семья на крыше джипа на закате над кратером Рамон",
"היי משה, אשמח לפרטים וזמינות לטיול ג'יפים":"Здравствуйте, Моше! Хочу узнать подробности и свободные даты для джип-тура",
"קבוצת מטיילים עם תרמילים עומדת בלב מכתש רמון":"Группа туристов с рюкзаками в сердце кратера Рамон",
"היי משה, אשמח לפרטים על טיול הליכה":"Здравствуйте, Моше! Хочу узнать подробности о пешем походе",
"אדם יושב ליד מדורה במדבר, מעליו שביל החלב":"Человек сидит у костра в пустыне, над ним Млечный Путь",
"למשל: חמישי 6.11":"например: четверг, 6.11",
"מבוגרים וילדים":"взрослые и дети",
"איפה אתם לנים, בקשות מיוחדות, שפה...":"Где вы остановились, особые пожелания, язык...",
"קישורים":"Ссылки",
"להתקשר":"Позвонить",
}
RU_JS={"היי משה, הגעתי מהאתר.":"Здравствуйте, Моше! Я с сайта.","שם: ":"Имя: ","טלפון: ":"Телефон: ","פעילות: ":"Активность: ","מועד מבוקש: ":"Желаемая дата: ","כמה נהיה: ":"Сколько нас: ","הערות: ":"Комментарии: "}
RU_AV={"ט":"Т","ו":"В","ש":"Ш"}

heb=re.compile(r'[֐-׿]')
def norm(t): return re.sub(r'\s+',' ',t.strip())

def build(lang, D, JS, AV, fonts, dirattr):
    s=strip_lang(open(SRC).read())
    missing=set()
    def sub_text(m):
        t=m.group(1)
        if not heb.search(t): return m.group(0)
        k=norm(t)
        if k in D: return '>'+D[k]+'<'
        if k in AV: return '>'+AV[k]+'<'
        missing.add(k); return m.group(0)
    s=re.sub(r'>([^<>]*)<',sub_text,s)
    def sub_attr(m):
        v=m.group(2)
        if not heb.search(v): return m.group(0)
        k=norm(v)
        if k in D: return m.group(1)+'="'+D[k]+'"'
        missing.add(k); return m.group(0)
    s=re.sub(r'(alt|aria-label|data-wa|placeholder|content|title)="([^"]*)"',sub_attr,s)
    for k,v in JS.items(): s=s.replace("'"+k+"'","'"+v+"'").replace("'"+k,"'"+v)
    # html attrs
    s=s.replace('<html lang="he" dir="rtl">','<html lang="%s" dir="ltr">'%lang)
    s=s.replace('<div id="page" lang="he">','<div id="page" lang="%s">'%lang)
    s=s.replace('#page{direction:rtl;','#page{direction:ltr;')
    # fonts
    s=s.replace("family=Varela+Round&family=Assistant:wght@300;400;600;700",fonts[0])
    s=s.replace("--display:'Varela Round','Assistant','Arial Hebrew',Arial,sans-serif;","--display:%s;"%fonts[1])
    s=s.replace("--body:'Assistant','Heebo','Arial Hebrew',Arial,system-ui,sans-serif;","--body:%s;"%fonts[2])
    # LTR alignment fixes
    s=s.replace('.offer-t h2{text-align:right}','.offer-t h2{text-align:left}')
    s=s.replace('.inc li{text-align:right}','.inc li{text-align:left}')
    s=s.replace('.about-t{text-align:right}','.about-t{text-align:left}')
    s=s.replace('.step .n{position:absolute;top:12px;right:12px;','.step .n{position:absolute;top:12px;left:12px;')
    s=s.replace('.offer-img .badge{position:absolute;top:14px;right:14px;','.offer-img .badge{position:absolute;top:14px;left:14px;')
    # paths one level up
    # og + canonical + hreflang
    s=s.replace('<meta property="og:url" content="%s">'%BASE,'<meta property="og:url" content="%s%s/">\n<meta property="og:locale" content="%s">'%(BASE,lang,{'en':'en_US','ru':'ru_RU'}[lang]))
    s=s.replace('<title>Desert Star</title>','<title>Desert Star</title>\n<link rel="canonical" href="%s%s/">'%(BASE,lang)+HREFLANG)
    s=s.replace('<meta name="claude:viewport-fit-sides" content="cover">\n','')
    return s, missing

HREFLANG='\n<link rel="alternate" hreflang="he" href="%s">\n<link rel="alternate" hreflang="en" href="%sen/">\n<link rel="alternate" hreflang="ru" href="%sru/">\n<link rel="alternate" hreflang="x-default" href="%s">'%(BASE,BASE,BASE,BASE)

# language switcher markup injected into header (all three pages)
def switcher(cur):
    items=[('he','עב',BASE),('en','EN',BASE+'en/'),('ru','RU',BASE+'ru/')]
    return '<nav class="lang" aria-label="Language">'+''.join('<a href="%s"%s>%s</a>'%(u,' aria-current="page"' if c==cur else '',l) for c,l,u in items)+'</nav>'
LANG_CSS='@media (max-width:640px){.top .btn{display:none}}\n.lang{display:flex;gap:4px;font-family:var(--display);font-size:14px}\n.lang a{text-decoration:none;color:var(--fg-dim);padding:6px 8px;border-radius:999px;border:1px solid transparent}\n.lang a[aria-current]{color:#fff;border-color:var(--line);background:rgba(255,255,255,.06)}\n.lang a:hover{color:#fff}\n.top .right{display:flex;align-items:center;gap:10px}\n'

def strip_lang(s):
    # make the Hebrew source idempotent: drop a previously injected switcher, hreflang block and og:locale
    s=re.sub(r'<nav class="lang"[^>]*>.*?</nav>','',s,flags=re.S)
    s=s.replace('<div class="right">','').replace('</a></div>\n  </div>\n</header>','</a>\n  </div>\n</header>')
    s=re.sub(r'\n<link rel="canonical"[^>]*>','',s)
    s=re.sub(r'\n<link rel="alternate" hreflang=[^>]*>','',s)
    s=re.sub(r'\n<meta property="og:locale"[^>]*>','',s)
    s=s.replace(LANG_CSS,'')
    return s

def inject_switcher(s,cur):
    s=s.replace('/* header */\n','/* header */\n'+LANG_CSS)
    old_btn_start=s.index('<a class="btn btn-main btn-sm" href="https://wa.me/972526052744"')
    old_btn_end=s.index('</a>',old_btn_start)+4
    btn=s[old_btn_start:old_btn_end]
    s=s[:old_btn_start]+'<div class="right">'+switcher(cur)+btn+'</div>'+s[old_btn_end:]
    return s

if __name__=='__main__':
    import os
    en,miss=build('en',EN,EN_JS,EN_AV,("family=Varela+Round&family=Assistant:wght@300;400;600;700","'Varela Round','Assistant',Arial,sans-serif","'Assistant',Arial,system-ui,sans-serif"),'ltr')
    print('EN missing',miss)
    ru,miss=build('ru',RU,RU_JS,RU_AV,("family=Nunito:wght@400;600;700&family=Rubik:wght@300;400;600;700","'Nunito','Rubik',Arial,sans-serif","'Rubik','Nunito',Arial,system-ui,sans-serif"),'ltr')
    print('RU missing',miss)
    en=inject_switcher(en,'en'); ru=inject_switcher(ru,'ru')
    ru=ru.replace('.nav{display:none;gap:24px;font-size:17px;font-weight:600}','.nav{display:none;gap:18px;font-size:16px;font-weight:600}')
    os.makedirs(os.path.join(ROOT,'en'),exist_ok=True); os.makedirs(os.path.join(ROOT,'ru'),exist_ok=True)
    open(os.path.join(ROOT,'en/index.html'),'w').write(en)
    open(os.path.join(ROOT,'ru/index.html'),'w').write(ru)
    # hebrew page: switcher + hreflang + canonical
    he=strip_lang(open(SRC).read())
    if True:
        he=inject_switcher(he,'he')
        he=he.replace('<title>Desert Star</title>','<title>Desert Star</title>\n<link rel="canonical" href="%s">'%BASE+HREFLANG)
        he=he.replace('<meta property="og:url" content="%s">'%BASE,'<meta property="og:url" content="%s">\n<meta property="og:locale" content="he_IL">'%BASE)
        open(SRC,'w').write(he)
    for f in ['en','ru']:
        t=open(os.path.join(ROOT,f,'index.html')).read()
        print(f,'hebrew left:',len(heb.findall(t)))
