#!/usr/bin/env python
# coding: utf-8

# In[3]:
# In[5]:
#saya menggunakan library beatifulsoup4 untuk mengambil datanya terlebih dahulu
# pip install requests beautifulsoup4 at terminal


import requests
from bs4 import BeautifulSoup
import pandas as pd

# URL of the website to scrape
url = 'https://www.pikiran-rakyat.com/'

# Set a user-agent header to make the request appear like it's coming from a browser
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'}

# Send a GET request to the URL with the headers
response = requests.get(url, headers=headers)

# Check if the request was successful (status code 200)
if response.status_code == 200:
    # Parse the HTML content of the page
    soup = BeautifulSoup(response.text, 'html.parser')

    # Extract relevant information from the HTML
    logo_img = soup.find('div', class_='logo').find('img')['data-src']
    date = soup.find('date').text.strip()
    network_links = [link['href'] for link in soup.select('.network__menu--more a')]
    social_links = [link['href'] for link in soup.select('.social__link')]

    # Create a dictionary to store the scraped data
    scraped_data = {
        'logo_img': logo_img,
        'date': date,
        'network_links': network_links,
        'social_links': social_links
    }

    # Convert the dictionary to a DataFrame
    df = pd.DataFrame([scraped_data])

    # Save the data to CSV and JSON files
    df.to_csv('scraped_data.csv', index=False)
    df.to_json('scraped_data.json', orient='records')

    print('Scraped data saved to CSV and JSON files.')
else:
    print('Failed to retrieve the page. Status code:', response.status_code)


# In[12]:


#header mengambil link dari header
import requests
from bs4 import BeautifulSoup
import pandas as pd

# The HTML code you provided
html_content = """
<div class="col-offset-fluid clearfix">
<div class="col-bs10-10">
<nav class="nav">
<div class="nav__home">
<a href="https://lubuklinggau.pikiran-rakyat.com/" title="Home">
<span class="icon icon-home"><img src="https://assets.pikiran-rakyat.com/www/network/desktop/images/favicon291.ico?v=916" alt="Klik Lubuklinggau"></span>
</a>
</div>

<ul class="nav__wrap">
<li><a href="https://lubuklinggau.pikiran-rakyat.com/sumsel" rel="”noreferred”">Sumsel</a>
<ul class="more">
<li><a href="https://lubuklinggau.pikiran-rakyat.com/musi-rawas" rel="”noreferred”">Musi Rawas</a></li>
<li><a href="https://lubuklinggau.pikiran-rakyat.com/lubuklinggau" rel="”noreferred”">Lubuklinggau</a></li>
<li><a href="https://lubuklinggau.pikiran-rakyat.com/muratara" rel="”noreferred”">Muratara</a></li>
</ul>
</li>
<li><a href="https://lubuklinggau.pikiran-rakyat.com/nasional" rel="”noreferred”">Nasional</a>
</li>
<li><a href="https://lubuklinggau.pikiran-rakyat.com/advetorial" rel="”noreferred”">Advetorial</a>
</li>
<li><a href="https://lubuklinggau.pikiran-rakyat.com/kesehatan" rel="”noreferred”">Kesehatan</a>
</li>
<li><a href="https://lubuklinggau.pikiran-rakyat.com/politik" rel="”noreferred”">Politik</a>
</li>
<li><a href="https://lubuklinggau.pikiran-rakyat.com/ekonomi-bisnis" rel="”noreferred”">Ekonomi Bisnis</a>
</li>
<li><a href="https://lubuklinggau.pikiran-rakyat.com/olahraga" rel="”noreferred”">Olahraga</a>
</li>
<li><a href="https://lubuklinggau.pikiran-rakyat.com/khazanah" rel="”noreferred”">Khazanah</a>
</li>
<li><a href="https://lubuklinggau.pikiran-rakyat.com/entertainment" rel="”noreferred”">Entertainment</a>
</li>
<li><a href="https://lubuklinggau.pikiran-rakyat.com/zodiak" rel="”noreferred”">Zodiak</a>
</li>
<li><a href="https://lubuklinggau.pikiran-rakyat.com/wisata" rel="”noreferred”">Wisata</a>
</li></ul>
</nav>
</div>
</div>
"""

# Parse HTML content
soup = BeautifulSoup(html_content, 'html.parser')

# Find all 'a' tags within the 'nav__wrap' class
links = soup.select('ul.nav__wrap a')

# Extract links and store them in a DataFrame
df = pd.DataFrame({'Links': [link.get('href') for link in links]})

# Save DataFrame to CSV and JSON files
df.to_csv('linksheader.csv', index=False)
df.to_json('linksheader.json', orient='records')

print("Links extraction and saving successful.")


# In[16]:


#mengambil body 1
from bs4 import BeautifulSoup
import pandas as pd

html_content = """
<div class="col-bs12-4">
                    
<style type="text/css">
.ads__giant__banner {
    padding: 0;
    position: relative;
    text-align: center;
    width: 300px;
    height: 600px;
    max-width: 300px;
    max-height: 600px;
    font-size: 16px;
    flex: 1;
    min-height: 300px;
    align-items: center;
    color: #fff;
    display: block;
    align-items: center;
    align-content: center;
    justify-content: center;
    overflow: hidden;
}
.box__inside__giant {
    width: 300px;
    display: flex;
    justify-content: center;
    align-items: center;
}
.giant__text__brand {
    color: #fff;
    font-size: 22px;
    font-weight: 700;
}
.caleg {
    width: 100px;
}
.caleg img:hover {
    -ms-transform: scale(1.1);
    -webkit-transform: scale(1.1);
     transform: scale(1.1); 
}
.caleg img {
    transition: .3s; 
}
</style>
<div class="ads__giant__banner mt3 clearfix" style="height:300px !important;">
	<div style="width:300px;height:300px;background-image: url('https://nos.wjv-1.neo.id/assets-prmn/www/2019/desktop/images/banner/capres_bg.png');">
		<div class="box__inside__giant" style="height:50px;">
			<label class="giant__text__brand" style="text-align:center;text-transform:uppercase;">Capres 2024</label>
		</div>
		<div class="box__inside__giant" style="height:175px;">
			<div class="caleg" style="padding-left:10px;padding-top:7%;">
				<a href="https://www.pikiran-rakyat.com/tag/Anies-Baswedan">
					<img alt="Capres Anies Baswedan PRMN" src="https://nos.wjv-1.neo.id/assets-prmn/www/2019/desktop/images/banner/capres_anies.png">
				</a>
			</div>
			<div class="caleg" style="padding-top:7%;">
				<a href="https://www.pikiran-rakyat.com/tag/Prabowo-Subianto">
					<img alt="Capres Prabowo Subianto PRMN" src="https://nos.wjv-1.neo.id/assets-prmn/www/2019/desktop/images/banner/capres_prabowo.png">
				</a>
			</div>
			<div class="caleg" style="padding-right:10px;padding-top:7%;">
				<a href="https://www.pikiran-rakyat.com/tag/Ganjar-Pranowo">
					<img alt="Capres Ganjar Pranowo PRMN" src="https://nos.wjv-1.neo.id/assets-prmn/www/2019/desktop/images/banner/capres_ganjar.png">
				</a>
			</div>
		</div>
		<div style="width:300px;height:75px;background-image: url('https://nos.wjv-1.neo.id/assets-prmn/www/2019/desktop/images/banner/capres_box.png');background-position:bottom;background-repeat:no-repeat;"></div>
	</div>
</div>
<section class="most mt1 clearfix" id="survei">
    <h3 class="title"><span>Polling Pikiran Rakyat</span></h3>
	<iframe frameborder="0" id="iframe" scrolling="no" src="https://ulasan.pikiran-rakyat.com/" height="300px" width="300px"></iframe>
</section>

                    <!-- most -->
<section class="most mt2 clearfix">
    <h3 class="title title6"><span>Terpopuler</span></h3>
    <div class="most__wrap">
                <div class="most__item">
            <div class="most__number">1</div>
            <div class="most__right">
                <a href="https://www.pikiran-rakyat.com/bola/pr-017150444/score-808-live-streaming-timnas-indonesia-u-24-vs-china-taipei-di-asian-games-2023-ilegal-nonton-di-rcti" class="most__link">
                    <h2 class="most__title">Score 808 Live Streaming Timnas Indonesia U-24 vs China Taipei di Asian Games 2023 Ilegal, Nonton di RCTI</h2>
                </a>
            </div>
        </div>
                        <div class="most__item">
            <div class="most__number">2</div>
            <div class="most__right">
                <a href="https://www.pikiran-rakyat.com/nasional/pr-017149885/penerimaan-cpns-dan-pppk-kemenkumham-2023-dibuka-hari-ini-simak-formasi-dan-persyaratannya" class="most__link">
                    <h2 class="most__title">Penerimaan CPNS dan PPPK Kemenkumham 2023 Dibuka Hari Ini, Simak Formasi dan Persyaratannya</h2>
                </a>
            </div>
        </div>
                        <div class="most__item">
            <div class="most__number">3</div>
            <div class="most__right">
                <a href="https://www.pikiran-rakyat.com/nasional/pr-017147121/hasto-pdip-bakal-dipolisikan-buntut-isu-prabowo-subianto-tampar-dan-cekik-wakil-menteri" class="most__link">
                    <h2 class="most__title">Hasto PDIP Bakal Dipolisikan Buntut Isu Prabowo Subianto Tampar dan Cekik Wakil Menteri</h2>
                </a>
            </div>
        </div>
                        <div class="most__item">
            <div class="most__number">4</div>
            <div class="most__right">
                <a href="https://www.pikiran-rakyat.com/nasional/pr-017150810/penyanyi-malaysia-bantah-jiplak-lagu-pok-ame-ame-kita-punya-banyak-kesamaan" class="most__link">
                    <h2 class="most__title">Penyanyi Malaysia Bantah Jiplak Lagu Pok Ame Ame, Kita Punya Banyak Kesamaan!</h2>
                </a>
            </div>
        </div>
                        <div class="most__item">
            <div class="most__number">5</div>
            <div class="most__right">
                <a href="https://www.pikiran-rakyat.com/nasional/pr-017151983/ahy-minta-prabowo-subianto-lanjutkan-pencapaian-jokowi" class="most__link">
                    <h2 class="most__title">AHY Minta Prabowo Subianto Lanjutkan Pencapaian Jokowi</h2>
                </a>
            </div>
        </div>
                        <div class="most__item">
            <div class="most__number">6</div>
            <div class="most__right">
                <a href="https://www.pikiran-rakyat.com/entertainment/pr-017147478/kondisi-terkini-indra-bruggman-terungkap-berat-badan-sempat-turun-15-kg-akibat-hipertiroid" class="most__link">
                    <h2 class="most__title">Kondisi Terkini Indra Bruggman Terungkap, Berat Badan Sempat Turun 15 Kg Akibat Hipertiroid</h2>
                </a>
            </div>
        </div>
                        <div class="most__item">
            <div class="most__number">7</div>
            <div class="most__right">
                <a href="https://www.pikiran-rakyat.com/bandung-raya/pr-017147832/pemulung-di-tps-darurat-sarimukti-dilarang-pungut-sampah-bantuan-pemerintah-dipertanyakan" class="most__link">
                    <h2 class="most__title">Pemulung di TPS Darurat Sarimukti Dilarang Pungut Sampah, Bantuan Pemerintah Dipertanyakan</h2>
                </a>
            </div>
        </div>
                        <div class="most__item">
            <div class="most__number">8</div>
            <div class="most__right">
                <a href="https://www.pikiran-rakyat.com/bola/pr-017150502/sedang-berlangsung-live-streaming-indonesia-u-24-vs-china-taipei-di-asian-games-nonton-kualitas-hd-di-sini" class="most__link">
                    <h2 class="most__title">SEDANG BERLANGSUNG Live Streaming Indonesia U-24 vs China Taipei di Asian Games, Nonton Kualitas HD di Sini</h2>
                </a>
            </div>
        </div>
                        <div class="most__item">
            <div class="most__number">9</div>
            <div class="most__right">
                <a href="https://www.pikiran-rakyat.com/nasional/pr-017150909/7-janji-ganjar-pranowo-jika-jadi-presiden-pengamat-wanti-wanti-jangan-cuma-jargon" class="most__link">
                    <h2 class="most__title">7 Janji Ganjar Pranowo jika Jadi Presiden, Pengamat Wanti-wanti Jangan Cuma Jargon</h2>
                </a>
            </div>
        </div>
                        <div class="most__item">
            <div class="most__number">10</div>
            <div class="most__right">
                <a href="https://www.pikiran-rakyat.com/bola/pr-017150841/link-live-streaming-rcti-tonton-pertandingan-indonesia-u-24-vs-china-taipei-kamis-21-september-2023-live" class="most__link">
                    <h2 class="most__title">Link Live Streaming RCTI, Tonton Pertandingan Indonesia U-24 vs China Taipei Kamis 21 September 2023 LIVE!</h2>
                </a>
            </div>
        </div>
            </div>
</section>
                    <!-- ads square -->
<div class="ads mt2 clearfix">
    <div class="ads__box">
        <div id="div-gpt-ad-MR1">
		  
		<div id="google_ads_iframe_/5197741/PikiranRakyat/_4__container__" style="border: 0pt none; display: inline-block;"></div></div>
    </div>
</div>
                    <!-- most -->
<section class="most mt2 clearfix">
    <h3 class="title title6"><span>Pemilu di Daerah</span></h3>
    <div class="most__wrap">
                <div class="most__item">
            <div class="most__number">1</div>
            <div class="most__right">
                <a href="https://buol.pikiran-rakyat.com/parlemen/pr-3457369301/polri-tetap-netral-meski-ada-keluarga-polri-ikut-nyaleg?taging=pemilu-di-daerah&amp;utm_medium=pemilu2024&amp;utm_campaign=pemilu2024" class="most__link">
                    <h2 class="most__title">Polri Tetap Netral Meski ada Keluarga Polri Ikut Nyaleg</h2>
                </a>
            </div>
        </div>
                        <div class="most__item">
            <div class="most__number">2</div>
            <div class="most__right">
                <a href="https://lubuklinggau.pikiran-rakyat.com/politik/pr-2917366127/paket-lengkap-ini-daftar-calon-tetap-anggota-dprd-kabupaten-takalar-periode-2024-2029-dari-golkar?taging=pemilu-di-daerah&amp;utm_medium=pemilu2024&amp;utm_campaign=pemilu2024" class="most__link">
                    <h2 class="most__title">Paket Lengkap, Ini Daftar Calon Tetap Anggota DPRD Kabupaten Takalar periode 2024-2029 dari Golkar</h2>
                </a>
            </div>
        </div>
                        <div class="most__item">
            <div class="most__number">3</div>
            <div class="most__right">
                <a href="https://boltim.pikiran-rakyat.com/politik/pr-3087369435/tantangan-timnas-amin-sangat-besar-relawan-pro-anies-sarankan-hal-ini?taging=pemilu-di-daerah&amp;utm_medium=pemilu2024&amp;utm_campaign=pemilu2024" class="most__link">
                    <h2 class="most__title">Tantangan Timnas AMIN Sangat Besar, Relawan Pro Anies Sarankan hal Ini  </h2>
                </a>
            </div>
        </div>
                        <div class="most__item">
            <div class="most__number">4</div>
            <div class="most__right">
                <a href="https://bogorraya.pikiran-rakyat.com/artikel/pr-3017369340/berikut-daftar-nama-caleg-hanura-kota-depok-dapil-1-2-3-4-5-dan-6-lengkap-di-pemilu-2024?taging=pemilu-di-daerah&amp;utm_medium=pemilu2024&amp;utm_campaign=pemilu2024" class="most__link">
                    <h2 class="most__title">Berikut Daftar Nama Caleg Hanura Kota Depok Dapil 1 2 3 4 5 dan 6 Lengkap di Pemilu 2024</h2>
                </a>
            </div>
        </div>
                        <div class="most__item">
            <div class="most__number">5</div>
            <div class="most__right">
                <a href="https://yogyakarta.pikiran-rakyat.com/news/pr-2787369352/hasil-survei-elektabilitas-capres-terbaru-versi-lpi-ganjar-mahfud-38-persen-ini-bocoran-dari-ganjar?taging=pemilu-di-daerah&amp;utm_medium=pemilu2024&amp;utm_campaign=pemilu2024" class="most__link">
                    <h2 class="most__title">Hasil Survei Elektabilitas Capres Terbaru Versi LPI Ganjar - Mahfud 38 Persen, Ini Bocoran dari Ganjar</h2>
                </a>
            </div>
        </div>
            </div>
</section>
                    <!-- opinion -->
<section class="opinion mt2 clearfix">
    <h3 class="title"><span><a href="https://www.pikiran-rakyat.com/kolom">Kolom</a></span></h3>
    <div class="opinion__wrap">
                        <div class="opinion__item">
            <div class="opinion__img" style="width: 60px !important; height: 60px !important;">
                <a href="https://www.pikiran-rakyat.com/kolom-author/5282/masduki-duryat">
                    <img class="lazyload" data-src="https://assets.pikiran-rakyat.com/crop/0x0:0x0/120x120/webp/photo/2021/08/24/4113908901.jpg" src="https://assets.pikiran-rakyat.com/www/2019/desktop/images/blank120x120.png?v=" width="120" height="120" alt="Masduki Duryat" data-loaded="true">
                </a>
            </div>
            <div class="opinion__right" style="width: calc(100% - 70px) !important;">
                <h3 class="opinion__author">
                    <a href="https://www.pikiran-rakyat.com/kolom/pr-017369108/moderasi-beragama-dan-peran-lembaga-pendidikan-islam-studi-kasus-di-cirebon" class="opinion__link">Moderasi Beragama dan Peran Lembaga Pendidikan (Islam): Studi Kasus di Cirebon</a>
                </h3>
                <div class="opinion__author__title">Masduki Duryat</div>
            </div>
        </div>
                        <div class="opinion__item">
            <div class="opinion__img" style="width: 60px !important; height: 60px !important;">
                <a href="https://www.pikiran-rakyat.com/kolom-author/10228/opini">
                    <img class="lazyload" data-src="https://assets.pikiran-rakyat.com/crop/0x0:0x0/120x120/webp/photo/2023/08/28/422748883.png" src="https://assets.pikiran-rakyat.com/www/2019/desktop/images/blank120x120.png?v=" width="120" height="120" alt="Opini" data-loaded="true">
                </a>
            </div>
            <div class="opinion__right" style="width: calc(100% - 70px) !important;">
                <h3 class="opinion__author">
                    <a href="https://www.pikiran-rakyat.com/kolom/pr-017368609/gibran-rakabuming-memanfaatkan-jalan-tol-di-mk" class="opinion__link">Gibran Rakabuming Memanfaatkan ‘Jalan Tol’ di MK</a>
                </h3>
                <div class="opinion__author__title">Opini</div>
            </div>
        </div>
            </div>
</section>
<!--
<section class="opinion mt2 clearfix">
    <h3 class="title"><span><a href="https://www.pikiran-rakyat.com/hukum">Hukum</a></span></h3>
    <div class="opinion__wrap">
        <div class="opinion__item">
            <div class="opinion__img">
                <a href="https://www.pikiran-rakyat.com/konsultasi-hukum">
                    <img class="lazyload" data-src="https://assets.pikiran-rakyat.com/www/2019/otang-faryana.jpg" src="https://assets.pikiran-rakyat.com/www/2019/desktop/images/blank120x120.png?v=" width="120" height="120" alt="otang-faryana" data-loaded="true">
                </a>
            </div>
            <div class="opinion__right">
                <h3 class="opinion__author">
                    <a href="https://www.pikiran-rakyat.com/konsultasi-hukum" class="opinion__link">Otang Fharyana, S.H., M.H.</a>
                </h3>
            </div>
        </div>
        <div class="opinion__item">
            <div class="opinion__img">
                <a href="https://www.pikiran-rakyat.com/konsultasi-hukum">
                    <img class="lazyload" data-src="https://assets.pikiran-rakyat.com/www/2019/aprian-setiawan.jpg" src="https://assets.pikiran-rakyat.com/www/2019/desktop/images/blank120x120.png?v=" width="120" height="120" alt="agus-indra-firdaus" data-loaded="true">
                </a>
            </div>
            <div class="opinion__right">
                <h3 class="opinion__author">
                    <a href="https://www.pikiran-rakyat.com/konsultasi-hukum" class="opinion__link">Aprian Setiawan, S.H., M.H.</a>
                </h3>
            </div>
        </div>

        <div class="opinion__item">
            <div class="opinion__img">
                <a href="https://www.pikiran-rakyat.com/konsultasi-hukum">
                    <img class="lazyload" data-src="https://assets.pikiran-rakyat.com/www/2019/agus-indra-firdaus.jpg" src="https://assets.pikiran-rakyat.com/www/2019/desktop/images/blank120x120.png?v=" width="120" height="120" alt="agus-indra-firdaus" data-loaded="true">
                </a>
            </div>
            <div class="opinion__right">
                <h3 class="opinion__author">
                    <a href="https://www.pikiran-rakyat.com/konsultasi-hukum" class="opinion__link">Agus Indra Firdaus., S.H.</a>
                </h3>
            </div>
        </div>

    </div>
</section>
-->                                                        </div>
"""

soup = BeautifulSoup(html_content, 'html.parser')

# Extract titles and links
news_articles = soup.find_all('div', class_='most__item')

data = []
for article in news_articles:
    number = article.find('div', class_='most__number').text.strip()
    title = article.find('h2', class_='most__title').text.strip()
    link = article.find('a', class_='most__link')['href']

    data.append({
        'Number': number,
        'Title': title,
        'Link': link
    })

# Create a DataFrame
df = pd.DataFrame(data)

# Save to CSV and JSON
df.to_csv('body1.csv', index=False)
df.to_json('body1.json', orient='records', lines=True)


# In[22]:


from bs4 import BeautifulSoup
import pandas as pd

html_content = """
<div class="ads__giant__banner mt3 clearfix" style="height:300px !important;">
	<div style="width:300px;height:300px;background-image: url('https://nos.wjv-1.neo.id/assets-prmn/www/2019/desktop/images/banner/capres_bg.png');">
		<div class="box__inside__giant" style="height:50px;">
			<label class="giant__text__brand" style="text-align:center;text-transform:uppercase;">Capres 2024</label>
		</div>
		<div class="box__inside__giant" style="height:175px;">
			<div class="caleg" style="padding-left:10px;padding-top:7%;">
				<a href="https://www.pikiran-rakyat.com/tag/Anies-Baswedan">
					<img alt="Capres Anies Baswedan PRMN" src="https://nos.wjv-1.neo.id/assets-prmn/www/2019/desktop/images/banner/capres_anies.png">
				</a>
			</div>
			<div class="caleg" style="padding-top:7%;">
				<a href="https://www.pikiran-rakyat.com/tag/Prabowo-Subianto">
					<img alt="Capres Prabowo Subianto PRMN" src="https://nos.wjv-1.neo.id/assets-prmn/www/2019/desktop/images/banner/capres_prabowo.png">
				</a>
			</div>
			<div class="caleg" style="padding-right:10px;padding-top:7%;">
				<a href="https://www.pikiran-rakyat.com/tag/Ganjar-Pranowo">
					<img alt="Capres Ganjar Pranowo PRMN" src="https://nos.wjv-1.neo.id/assets-prmn/www/2019/desktop/images/banner/capres_ganjar.png">
				</a>
			</div>
		</div>
		<div style="width:300px;height:75px;background-image: url('https://nos.wjv-1.neo.id/assets-prmn/www/2019/desktop/images/banner/capres_box.png');background-position:bottom;background-repeat:no-repeat;"></div>
	</div>
</div>
<section class="most mt1 clearfix" id="survei">
    <h3 class="title"><span>Polling Pikiran Rakyat</span></h3>
	<iframe frameborder="0" id="iframe" scrolling="no" src="https://ulasan.pikiran-rakyat.com/" height="300px" width="300px"></iframe>
</section>
"""

soup = BeautifulSoup(html_content, 'html.parser')

# Extract titles and links
news_articles = soup.find_all('div', class_='most__item')

data = []
for article in news_articles:
    number = article.find('div', class_='most__number').text.strip()
    title = article.find('h2', class_='most__title').text.strip()
    link = article.find('a', class_='most__link')['href']

    data.append({
        'Number': number,
        'Title': title,
        'Link': link
    })

# Create a DataFrame
df = pd.DataFrame(data)

# Save to CSV and JSON
df.to_csv('body3.csv', index=False)
df.to_json('body3.json', orient='records', lines=True)

print("DataFrame berhasil di buat.")


# In[23]:


#mengambil berita populer
from bs4 import BeautifulSoup
import pandas as pd

html_content = """
<section class="most mt2 clearfix" style="height: auto !important;">
    <h3 class="title title6"><span>Terpopuler</span></h3>
    <div class="most__wrap">
        <div class="most__item">
            <div class="most__number">1</div>
            <div class="most__right">
                <a href="https://www.pikiran-rakyat.com/kolom/pr-017364567/asn-sulit-dipecat-pemerintah-terjebak-aturan-sendiri" class="most__link">
                    <h2 class="most__title">ASN Sulit Dipecat, Pemerintah Terjebak Aturan Sendiri</h2>
                </a>
            </div>
        </div>
        <div class="most__item">
            <div class="most__number">2</div>
            <div class="most__right">
                <a href="https://www.pikiran-rakyat.com/gaya-hidup/pr-017358731/sering-dikira-restoran-cepat-saji-asal-luar-negeriricheese-factory-berasal-dari-bandung-indonesia" class="most__link">
                    <h2 class="most__title">Sering Dikira Restoran Cepat Saji Asal Luar Negeri, Richeese Factory Berasal dari Bandung-Indonesia</h2>
                </a>
            </div>
        </div>
        <div class="most__item">
            <div class="most__number">3</div>
            <div class="most__right">
                <a href="https://www.pikiran-rakyat.com/bola/pr-017366019/live-vision-link-streaming-filipina-vs-vietnam-di-kualifikasi-piala-dunia-2026-16-november-2023" class="most__link">
                    <h2 class="most__title">Live Vision+! Link Streaming Filipina vs Vietnam di Kualifikasi Piala Dunia 2026 16 November 2023</h2>
                </a>
            </div>
        </div>
        <div class="most__item">
            <div class="most__number">4</div>
            <div class="most__right">
                <a href="https://www.pikiran-rakyat.com/bola/pr-017365446/link-live-streaming-gratis-indonesia-vs-maroko-piala-dunia-u-17-kick-off-pukul-1900-wib" class="most__link">
                    <h2 class="most__title">Link Live Streaming Gratis Indonesia vs Maroko Piala Dunia U-17, Kick-Off Pukul 19.00 WIB</h2>
                </a>
            </div>
        </div>
        <div class="most__item">
            <div class="most__number">5</div>
            <div class="most__right">
                <a href="https://www.pikiran-rakyat.com/bola/pr-017357697/piala-dunia-u-17-meksiko-vs-venezuela-prediksi-skor-susunan-pemain-dan-head-to-head" class="most__link">
                    <h2 class="most__title">Piala Dunia U-17 Meksiko vs Venezuela: Prediksi Skor, Susunan Pemain, dan Head to Head</h2>
                </a>
            </div>
        </div>
        <div class="most__item">
            <div class="most__number">6</div>
            <div class="most__right">
                <a href="https://www.pikiran-rakyat.com/bola/pr-017367961/hasil-akhir-maroko-u17-vs-indonesia-u17-hampir-pupus-harapan-garuda-asia-lolos-ke-babak-16-besar" class="most__link">
                    <h2 class="most__title">Hasil Akhir Maroko U17 vs Indonesia U17: Hampir Pupus Harapan Garuda Asia Lolos ke Babak 16 Besar</h2>
                </a>
            </div>
        </div>
        <div class="most__item">
            <div class="most__number">7</div>
            <div class="most__right">
                <a href="https://www.pikiran-rakyat.com/bola/pr-017360701/prediksi-skor-argentina-vs-uruguay-di-kualifikasi-piala-dunia-2026-pemain-bintang-ramaikan-starting-lineup" class="most__link">
                    <h2 class="most__title">Prediksi Skor Argentina vs Uruguay di Kualifikasi Piala Dunia 2026, Pemain Bintang Ramaikan Starting Lineup</h2>
                </a>
            </div>
        </div>
        <div class="most__item">
            <div class="most__number">8</div>
            <div class="most__right">
                <a href="https://www.pikiran-rakyat.com/nasional/pr-017366883/ghisca-debora-penipu-tiket-konser-coldplay-di-jakarta-raup-keuntungan-rp15-miliar" class="most__link">
                    <h2 class="most__title">Ghisca Debora, Penipu Tiket Konser Coldplay di Jakarta, Raup Keuntungan Rp15 Miliar</h2>
                </a>
            </div>
        </div>
        <div class="most__item">
            <div class="most__number">9</div>
            <div class="most__right">
                <a href="https://www.pikiran-rakyat.com/gaya-hidup/pr-017362239/apakah-wolbachia-berbahaya-bagi-lingkungan" class="most__link">
                    <h2 class="most__title">Apakah Wolbachia Berbahaya bagi Lingkungan?</h2>
                </a>
            </div>
        </div>
        <div class="most__item">
            <div class="most__number">10</div>
            <div class="most__right">
                <a href="https://www.pikiran-rakyat.com/bola/pr-017361227/prediksi-skor-meksiko-u17-vs-venezuela-u17-di-piala-dunia-statistik-head-to-head-susunan-pemain" class="most__link">
                    <h2 class="most__title">Prediksi Skor Meksiko U17 vs Venezuela U17 di Piala Dunia: Statistik, Head to Head, Susunan Pemain</h2>
                </a>
           
            </div>
        </div>
    </div>
    <div class="google-auto-placed" style="width: 100%; height: auto; clear: none; text-align: center;">
        <ins data-ad-format="auto" class="adsbygoogle adsbygoogle-noablate" data-ad-client="ca-pub-3987315829323386" data-adsbygoogle-status="done" style="display: block; margin: 20px auto 10px; background-color: transparent; height: 280px;" data-ad-status="unfilled">
            <div id="aswift_1_host" style="border: none; height: 280px; width: 337px; margin: 0px; padding: 0px; position: relative; visibility: visible; background-color: transparent; display: inline-block; overflow: visible;" tabindex="0" title="Advertisement" aria-label="Advertisement">
                <iframe id="aswift_1" name="aswift_1" browsingtopics="true" style="left: 0; position: absolute; top: 0; border: 0; width: 337px; height: 280px;" sandbox="allow-forms allow-popups allow-popups-to-escape-sandbox allow-same-origin allow-scripts allow-top-navigation-by-user-activation" width="337" height="280" frameborder="0" marginwidth="0" marginheight="0" vspace="0" hspace="0" allowtransparency="true" scrolling="no" allow="attribution-reporting" src="https://googleads.g.doubleclick.net/pagead/ads?gdpr=0&amp;client=ca-pub-3987315829323386&amp;output=html&amp;h=280&amp;adk=1025406284&amp;adf=1812116851&amp;pi=t.aa~a.1606767341~rp.4&amp;w=337&amp;fwrn=4&amp;fwrnh=100&amp;lmt=1700191844&amp;rafmt=1&amp;to=qs&amp;pwprc=8218215102&amp;format=337x280&amp;url=https%3A%2F%2Fwww.pikiran-rakyat.com%2F&amp;ea=0&amp;fwr=0&amp;pra=3&amp;rpe=1&amp;resp_fmts=3&amp;wgl=1&amp;fa=40&amp;uach=WyJXaW5kb3dzIiwiMTQuMC4wIiwieDg2IiwiIiwiMTE5LjAuNjA0NS4xNjAiLG51bGwsMCxudWxsLCI2NCIsW1siR29vZ2xlIENocm9tZSIsIjExOS4wLjYwNDUuMTYwIl0sWyJDaHJvbWl1bSIsIjExOS4wLjYwNDUuMTYwIl0sWyJOb3Q_QV9CcmFuZCIsIjI0LjAuMC4wIl1dLDBd&amp;dt=1700191844262&amp;bpp=2&amp;bdt=2814&amp;idt=-M&amp;shv=r20231109&amp;mjsv=m202311140101&amp;ptt=9&amp;saldr=aa&amp;abxe=1&amp;cookie=ID%3Dc6591f9338d91376%3AT%3D1700191384%3ART%3D1700191838%3AS%3DALNI_MYkCFdxZtajohnpWvwMzzc802DxJQ&amp;gpic=UID%3D00000c8accc6b231%3AT%3D1700191384%3ART%3D1700191838%3AS%3DALNI_MYNT8ZEZWjrLFZIkEBtpJleLUqGjg&amp;prev_fmts=0x0&amp;nras=2&amp;correlator=5504629316476&amp;frm=20&amp;pv=1&amp;ga_vid=1590894287.1700191378&amp;ga_sid=1700191843&amp;ga_hid=2120572605&amp;ga_fc=1&amp;u_tz=420&amp;u_his=4&amp;u_h=1080&amp;u_w=1920&amp;u_ah=1032&amp;u_aw=1920&amp;u_cd=24&amp;u_sd=1&amp;dmc=8&amp;adx=765&amp;ady=2065&amp;biw=1134&amp;bih=911&amp;scr_x=0&amp;scr_y=700&amp;eid=44759875%2C44759926%2C31079606%2C31079628%2C44798934%2C44809316%2C31078297%2C31079756%2C44807764%2C44808149%2C44808285%2C44809056%2C31078663%2C31078665%2C31078668%2C31078670&amp;oid=2&amp;pvsid=47335097678357&amp;tmod=32634814&amp;uas=0&amp;nvt=3&amp;fc=1920&amp;brdim=0%2C0%2C0%2C0%2C1920%2C0%2C1920%2C1032%2C1151%2C911&amp;vis=1&amp;rsz=%7C%7Cs%7C&amp;abl=NS&amp;fu=128&amp;bc=31&amp;td=1&amp;psd=W251bGwsbnVsbCxudWxsLDNd&amp;nt=1&amp;ifi=2&amp;uci=a!2&amp;btvi=1&amp;fsb=1&amp;dtd=368" data-google-container-id="a!2" data-google-query-id="CP-1upeMyoIDFW9RnQkdMswGUg" data-load-complete="true"></iframe>
            </div>
        </ins>
    </div>
</section>
"""

soup = BeautifulSoup(html_content, 'html.parser')

# Extract titles and links
most_items = soup.find_all('div', class_='most__item')

data = []
for item in most_items:
    number = item.find('div', class_='most__number').text.strip()
    title = item.find('h2', class_='most__title').text.strip()
    link = item.find('a', class_='most__link')['href']

    data.append({
        'Number': number,
        'Title': title,
        'Link': link
    })

# Create a DataFrame
df = pd.DataFrame(data)

# Save to CSV and JSON
df.to_csv('berita populer.csv', index=False)
df.to_json('berita populer.json', index=False)


# In[25]:


#Mengambil Headline Berita
from bs4 import BeautifulSoup

html_content = """
<section class="hl mt3 clearfix">
    <div class="hl__big js--big slick-initialized slick-slider slick-dotted" role="toolbar">
                    <div aria-live="polite" class="slick-list draggable"><div class="slick-track" role="listbox" style="opacity: 1; width: 2812px;"><div class="hl__b-item slick-slide" data-slick-index="0" aria-hidden="true" tabindex="-1" role="option" aria-describedby="slick-slide00" style="width: 703px; position: relative; left: 0px; top: 0px; z-index: 998; opacity: 0; transition: opacity 500ms ease 0s;">
                <div class="hl__b-img">
                    <div class="hl__b-cat">Headline</div>
                    <img src="https://assets.pikiran-rakyat.com/crop/0x0:0x0/635x381/webp/photo/2023/02/02/3781301368.jpg" alt="Mengapa Kita Sangat Gaduh Masalah Nepotisme?">
                </div>
                <div class="hl__b-box">
                    <h4 class="hl__b-subtitle"><a class="hl__link" href="https://www.pikiran-rakyat.com/kolom" tabindex="-1">Kolom</a></h4>
                    <h1 class="hl__b-title"><a class="hl__link" href="https://www.pikiran-rakyat.com/kolom/pr-017368511/mengapa-kita-sangat-gaduh-masalah-nepotisme" tabindex="-1">Mengapa Kita Sangat Gaduh Masalah Nepotisme?</a></h1>
                </div>
            </div><div class="hl__b-item slick-slide" data-slick-index="1" aria-hidden="true" tabindex="-1" role="option" aria-describedby="slick-slide01" style="width: 703px; position: relative; left: -703px; top: 0px; z-index: 998; opacity: 0; transition: opacity 500ms ease 0s;">
                <div class="hl__b-img">
                    <div class="hl__b-cat">Headline</div>
                    <img src="https://assets.pikiran-rakyat.com/crop/0x0:0x0/635x381/webp/photo/2023/11/15/1281904373.jpg" alt="Bawaslu Pastikan Nomor Urut Pilpres Bukan 'Settingan': Sesuai Prosedur dan Teknis KPU">
                </div>
                <div class="hl__b-box">
                    <h4 class="hl__b-subtitle"><a class="hl__link" href="https://www.pikiran-rakyat.com/nasional" tabindex="-1">Nasional</a></h4>
                    <h1 class="hl__b-title"><a class="hl__link" href="https://www.pikiran-rakyat.com/nasional/pr-017368722/bawaslu-pastikan-nomor-urut-pilpres-bukan-settingan-sesuai-prosedur-dan-teknis-kpu" tabindex="-1">Bawaslu Pastikan Nomor Urut Pilpres Bukan 'Settingan': Sesuai Prosedur dan Teknis KPU</a></h1>
                </div>
            </div><div class="hl__b-item slick-slide slick-current slick-active" data-slick-index="2" aria-hidden="false" tabindex="-1" role="option" aria-describedby="slick-slide02" style="width: 703px; position: relative; left: -1406px; top: 0px; z-index: 999; opacity: 1;">
                <div class="hl__b-img">
                    <div class="hl__b-cat">Headline</div>
                    <img src="https://assets.pikiran-rakyat.com/crop/0x0:0x0/635x381/webp/photo/2023/11/17/3331455582.png" alt="Coldplay Donasi Kapal Pembersih Sampah untuk Indonesia: Sungai Cisadane Jadi Fokus">
                </div>
                <div class="hl__b-box">
                    <h4 class="hl__b-subtitle"><a class="hl__link" href="https://www.pikiran-rakyat.com/musik" tabindex="0">Musik</a></h4>
                    <h1 class="hl__b-title"><a class="hl__link" href="https://www.pikiran-rakyat.com/entertainment/pr-017369119/coldplay-donasi-kapal-pembersih-sampah-untuk-indonesia-sungai-cisadane-jadi-fokus" tabindex="0">Coldplay Donasi Kapal Pembersih Sampah untuk Indonesia: Sungai Cisadane Jadi Fokus</a></h1>
                </div>
            </div><div class="hl__b-item slick-slide" data-slick-index="3" aria-hidden="true" tabindex="-1" role="option" aria-describedby="slick-slide03" style="width: 703px; position: relative; left: -2109px; top: 0px; z-index: 998; opacity: 0; transition: opacity 500ms ease 0s;">
                <div class="hl__b-img">
                    <div class="hl__b-cat">Headline</div>
                    <img src="https://assets.pikiran-rakyat.com/crop/0x0:0x0/635x381/webp/photo/2023/11/17/4284863555.jpg" alt="Kapan Kiamat Datang? Nabi Ungkap Harinya">
                </div>
                <div class="hl__b-box">
                    <h4 class="hl__b-subtitle"><a class="hl__link" href="https://www.pikiran-rakyat.com/khazanah-islam" tabindex="-1">Khazanah</a></h4>
                    <h1 class="hl__b-title"><a class="hl__link" href="https://www.pikiran-rakyat.com/khazanah-islam/pr-017368821/kapan-kiamat-datang-nabi-ungkap-harinya" tabindex="-1">Kapan Kiamat Datang? Nabi Ungkap Harinya</a></h1>
                </div>
            </div></div></div>
                    
                    
                    
            <ul class="slick-dots" style="display: block;" role="tablist"><li class="" aria-hidden="true" role="presentation" aria-selected="true" aria-controls="navigation00" id="slick-slide00"><button type="button" data-role="none" role="button" tabindex="0">1</button></li><li aria-hidden="true" role="presentation" aria-selected="false" aria-controls="navigation01" id="slick-slide01" class=""><button type="button" data-role="none" role="button" tabindex="0">2</button></li><li aria-hidden="false" role="presentation" aria-selected="false" aria-controls="navigation02" id="slick-slide02" class="slick-active"><button type="button" data-role="none" role="button" tabindex="0">3</button></li><li aria-hidden="true" role="presentation" aria-selected="false" aria-controls="navigation03" id="slick-slide03" class=""><button type="button" data-role="none" role="button" tabindex="0">4</button></li></ul></div>
    <div class="hl__small js--small slick-initialized slick-slider">
                <div aria-live="polite" class="slick-list draggable"><div class="slick-track" role="listbox" style="opacity: 1; width: 704px; transform: translate3d(0px, 0px, 0px);"><div class="hl__s-item slick-slide slick-active" data-slick-index="0" aria-hidden="false" tabindex="-1" role="option" aria-describedby="slick-slide10" style="width: 176px;">
            <div class="hl__s-img">
                <img src="https://assets.pikiran-rakyat.com/crop/0x0:0x0/157x94/webp/photo/2023/02/02/3781301368.jpg" alt="Mengapa Kita Sangat Gaduh Masalah Nepotisme?">
            </div>
            <div class="hl__s-box">
                <h2 class="hl__s-title"><a class="hl__link" href="https://www.pikiran-rakyat.com/kolom/pr-017368511/mengapa-kita-sangat-gaduh-masalah-nepotisme" tabindex="0">Mengapa Kita Sangat Gaduh Masalah Nepotisme?</a></h2>
            </div>
        </div><div class="hl__s-item slick-slide slick-active" data-slick-index="1" aria-hidden="false" tabindex="-1" role="option" aria-describedby="slick-slide11" style="width: 176px;">
            <div class="hl__s-img">
                <img src="https://assets.pikiran-rakyat.com/crop/0x0:0x0/157x94/webp/photo/2023/11/15/1281904373.jpg" alt="Bawaslu Pastikan Nomor Urut Pilpres Bukan 'Settingan': Sesuai Prosedur dan Teknis KPU">
            </div>
            <div class="hl__s-box">
                <h2 class="hl__s-title"><a class="hl__link" href="https://www.pikiran-rakyat.com/nasional/pr-017368722/bawaslu-pastikan-nomor-urut-pilpres-bukan-settingan-sesuai-prosedur-dan-teknis-kpu" tabindex="0">Bawaslu Pastikan Nomor Urut Pilpres Bukan 'Settingan': Sesuai Prosedur dan Teknis KPU</a></h2>
            </div>
        </div><div class="hl__s-item slick-slide slick-current slick-active" data-slick-index="2" aria-hidden="false" tabindex="-1" role="option" aria-describedby="slick-slide12" style="width: 176px;">
            <div class="hl__s-img">
                <img src="https://assets.pikiran-rakyat.com/crop/0x0:0x0/157x94/webp/photo/2023/11/17/3331455582.png" alt="Coldplay Donasi Kapal Pembersih Sampah untuk Indonesia: Sungai Cisadane Jadi Fokus">
            </div>
            <div class="hl__s-box">
                <h2 class="hl__s-title"><a class="hl__link" href="https://www.pikiran-rakyat.com/entertainment/pr-017369119/coldplay-donasi-kapal-pembersih-sampah-untuk-indonesia-sungai-cisadane-jadi-fokus" tabindex="0">Coldplay Donasi Kapal Pembersih Sampah untuk Indonesia: Sungai Cisadane Jadi Fokus</a></h2>
            </div>
        </div><div class="hl__s-item slick-slide slick-active" data-slick-index="3" aria-hidden="false" tabindex="-1" role="option" aria-describedby="slick-slide13" style="width: 176px;">
            <div class="hl__s-img">
                <img src="https://assets.pikiran-rakyat.com/crop/0x0:0x0/157x94/webp/photo/2023/11/17/4284863555.jpg" alt="Kapan Kiamat Datang? Nabi Ungkap Harinya">
            </div>
            <div class="hl__s-box">
                <h2 class="hl__s-title"><a class="hl__link" href="https://www.pikiran-rakyat.com/khazanah-islam/pr-017368821/kapan-kiamat-datang-nabi-ungkap-harinya" tabindex="0">Kapan Kiamat Datang? Nabi Ungkap Harinya</a></h2>
            </div>
        </div></div></div>
                
                
                
            </div>
</section>
"""

soup = BeautifulSoup(html_content, 'html.parser')

# Extract big headlines
big_headlines = soup.find('div', class_='hl__big')
big_items = big_headlines.find_all('div', class_='hl__b-item')

big_headline_data = []
for item in big_items:
    category = item.find('div', class_='hl__b-cat').text.strip()
    image_src = item.find('img')['src']
    article_url = item.find('a', class_='hl__link')['href']
    title = item.find('h1', class_='hl__b-title').text.strip()

    big_headline_data.append({
        'Category': category,
        'ImageSrc': image_src,
        'ArticleURL': article_url,
        'Title': title
    })

soup = BeautifulSoup(html_content, 'html.parser')

# Extract big headlines
big_headlines = soup.find('div', class_='hl__big')
big_items = big_headlines.find_all('div', class_='hl__b-item')

big_headline_data = []
for item in big_items:
    category = item.find('div', class_='hl__b-cat').text.strip()
    image_src = item.find('img')['src']
    article_url = item.find('a', class_='hl__link')['href']
    title = item.find('h1', class_='hl__b-title').text.strip()

    big_headline_data.append({
        'Category': category,
        'ImageSrc': image_src,
        'ArticleURL': article_url,
        'Title': title
    })

# Extract small headlines
small_headlines = soup.find('div', class_='hl__small')
small_items = small_headlines.find_all('div', class_='hl__s-item')

small_headline_data = []
for item in small_items:
    image_src = item.find('img')['src']
    article_url = item.find('a', class_='hl__link')['href']
    title = item.find('h2', class_='hl__s-title').text.strip()

    small_headline_data.append({
        'ImageSrc': image_src,
        'ArticleURL': article_url,
        'Title': title
    })

# Print or process the extracted data as needed
print("Big Headlines:")
print(big_headline_data)
print("\nSmall Headlines:")
print(small_headline_data)

# Create DataFrames
df_big = pd.DataFrame(big_headline_data)
df_small = pd.DataFrame(small_headline_data)

# Save to CSV and JSON
df_big.to_csv('big_headline_data.csv', index=False)
df_small.to_json('small_headline_data.json', orient='records', lines=True)


# In[27]:


#pilihan editor
import pandas as pd
from bs4 import BeautifulSoup

html_content = """
<section class="editors mt3 clearfix">
    <h3 class="title3"><span>Pilihan Editor</span></h3>
    <div class="editors__wrap js--editors slick-initialized slick-slider"><a href="#" class="arrow arrow--left slick-arrow" aria-disabled="false" style="display: block;"><span class="icon icon-angle-left"></span></a>
                <div aria-live="polite" class="slick-list draggable"><div class="slick-track" role="listbox" style="opacity: 1; width: 1344px; transform: translate3d(-672px, 0px, 0px);"><div class="editors__item slick-slide" data-slick-index="0" aria-hidden="true" tabindex="-1" role="option" aria-describedby="slick-slide20" style="width: 224px;">
            <div class="editors__img">
                <a href="https://www.pikiran-rakyat.com/nasional/pr-017368543/populer-hari-ini-kpk-tahan-kajari-bondowoso-hingga-megawati-dianggap-aneh-tkn-prabowo-gibran" tabindex="-1">
                    <img class=" ls-is-cached lazyloaded" data-src="https://assets.pikiran-rakyat.com/crop/0x0:0x0/191x114/webp/photo/2023/11/16/1460266400.jpg" src="https://assets.pikiran-rakyat.com/crop/0x0:0x0/191x114/webp/photo/2023/11/16/1460266400.jpg" alt="POPULER HARI INI: KPK Tahan Kajari Bondowoso hingga Megawati Dianggap Aneh TKN Prabowo-Gibran" data-loaded="true">
                </a>
            </div>
            <div class="editors__box">
                <h4 class="editors__subtitle"><a href="https://www.pikiran-rakyat.com/nasional" tabindex="-1">Nasional</a></h4>
                <h2 class="editors__title">
                    <a href="https://www.pikiran-rakyat.com/nasional/pr-017368543/populer-hari-ini-kpk-tahan-kajari-bondowoso-hingga-megawati-dianggap-aneh-tkn-prabowo-gibran" class="editors__link" tabindex="-1">POPULER HARI INI: KPK Tahan Kajari Bondowoso hingga Megawati Dianggap Aneh TKN Prabowo-Gibran</a>
                </h2>
            </div>
        </div><div class="editors__item slick-slide" data-slick-index="1" aria-hidden="true" tabindex="-1" role="option" aria-describedby="slick-slide21" style="width: 224px;">
            <div class="editors__img">
                <a href="https://www.pikiran-rakyat.com/internasional/pr-017368460/terjemahan-bagian-1-surat-osama-bin-laden-a-letter-to-america-viral-bikin-as-ketar-ketir" tabindex="-1">
                    <img class=" ls-is-cached lazyloaded" data-src="https://assets.pikiran-rakyat.com/crop/0x0:0x0/191x114/webp/photo/2021/04/27/4005624653.jpg" src="https://assets.pikiran-rakyat.com/crop/0x0:0x0/191x114/webp/photo/2021/04/27/4005624653.jpg" alt="Terjemahan Bagian 1 Surat Osama bin Laden 'A Letter to America', Viral Bikin AS Ketar-ketir" data-loaded="true">
                </a>
            </div>
            <div class="editors__box">
                <h4 class="editors__subtitle"><a href="https://www.pikiran-rakyat.com/internasional" tabindex="-1">Internasional</a></h4>
                <h2 class="editors__title">
                    <a href="https://www.pikiran-rakyat.com/internasional/pr-017368460/terjemahan-bagian-1-surat-osama-bin-laden-a-letter-to-america-viral-bikin-as-ketar-ketir" class="editors__link" tabindex="-1">Terjemahan Bagian 1 Surat Osama bin Laden 'A Letter to America', Viral Bikin AS Ketar-ketir</a>
                </h2>
            </div>
        </div><div class="editors__item slick-slide" data-slick-index="2" aria-hidden="true" tabindex="-1" role="option" aria-describedby="slick-slide22" style="width: 224px;">
            <div class="editors__img">
                <a href="https://www.pikiran-rakyat.com/nasional/pr-017368920/ganjar-pranowo-hari-ini-masyarakat-butuh-banyak-lapangan-kerja" tabindex="-1">
                    <img class=" ls-is-cached lazyloaded" data-src="https://assets.pikiran-rakyat.com/crop/0x61:1355x844/191x114/webp/photo/2023/10/19/849226128.jpg" src="https://assets.pikiran-rakyat.com/crop/0x61:1355x844/191x114/webp/photo/2023/10/19/849226128.jpg" alt="Ganjar Pranowo: Hari Ini Masyarakat Butuh Banyak Lapangan Kerja" data-loaded="true">
                </a>
            </div>
            <div class="editors__box">
                <h4 class="editors__subtitle"><a href="https://www.pikiran-rakyat.com/nasional" tabindex="-1">Nasional</a></h4>
                <h2 class="editors__title">
                    <a href="https://www.pikiran-rakyat.com/nasional/pr-017368920/ganjar-pranowo-hari-ini-masyarakat-butuh-banyak-lapangan-kerja" class="editors__link" tabindex="-1">Ganjar Pranowo: Hari Ini Masyarakat Butuh Banyak Lapangan Kerja</a>
                </h2>
            </div>
        </div><div class="editors__item slick-slide slick-current slick-active" data-slick-index="3" aria-hidden="false" tabindex="-1" role="option" aria-describedby="slick-slide23" style="width: 224px;">
            <div class="editors__img">
                <a href="https://www.pikiran-rakyat.com/internasional/pr-017368810/tiktok-bereaksi-soal-viralnya-a-latter-to-america-susul-amukan-dari-gedung-putih" tabindex="0">
                    <img class=" lazyloaded" data-src="https://assets.pikiran-rakyat.com/crop/0x0:0x0/191x114/webp/photo/2023/03/24/2520102440.jpg" src="https://assets.pikiran-rakyat.com/crop/0x0:0x0/191x114/webp/photo/2023/03/24/2520102440.jpg" alt="TikTok Bereaksi Soal Viralnya 'a Latter to America', Susul Amukan dari Gedung Putih" data-loaded="true">
                </a>
            </div>
            <div class="editors__box">
                <h4 class="editors__subtitle"><a href="https://www.pikiran-rakyat.com/internasional" tabindex="0">Internasional</a></h4>
                <h2 class="editors__title">
                    <a href="https://www.pikiran-rakyat.com/internasional/pr-017368810/tiktok-bereaksi-soal-viralnya-a-latter-to-america-susul-amukan-dari-gedung-putih" class="editors__link" tabindex="0">TikTok Bereaksi Soal Viralnya 'a Latter to America', Susul Amukan dari Gedung Putih</a>
                </h2>
            </div>
        </div><div class="editors__item slick-slide slick-active" data-slick-index="4" aria-hidden="false" tabindex="-1" role="option" aria-describedby="slick-slide24" style="width: 224px;">
            <div class="editors__img">
                <a href="https://www.pikiran-rakyat.com/internasional/pr-017368684/penjajah-israel-sandera-5000-orang-di-rumah-sakit-gaza-wafa-kondisi-buruk" tabindex="0">
                    <img class=" lazyloaded" data-src="https://assets.pikiran-rakyat.com/crop/0x0:0x0/191x114/webp/photo/2023/11/16/1651609950.jpg" src="https://assets.pikiran-rakyat.com/crop/0x0:0x0/191x114/webp/photo/2023/11/16/1651609950.jpg" alt="Penjajah Israel Sandera 5.000 Orang di Rumah Sakit Gaza, WAFA: Kondisi Buruk" data-loaded="true">
                </a>
            </div>
            <div class="editors__box">
                <h4 class="editors__subtitle"><a href="https://www.pikiran-rakyat.com/internasional" tabindex="0">Internasional</a></h4>
                <h2 class="editors__title">
                    <a href="https://www.pikiran-rakyat.com/internasional/pr-017368684/penjajah-israel-sandera-5000-orang-di-rumah-sakit-gaza-wafa-kondisi-buruk" class="editors__link" tabindex="0">Penjajah Israel Sandera 5.000 Orang di Rumah Sakit Gaza, WAFA: Kondisi Buruk</a>
                </h2>
            </div>
        </div><div class="editors__item slick-slide slick-active" data-slick-index="5" aria-hidden="false" tabindex="-1" role="option" aria-describedby="slick-slide25" style="width: 224px;">
            <div class="editors__img">
                <a href="https://www.pikiran-rakyat.com/nasional/pr-017368660/cak-imin-balas-pantun-prabowo-masih-ada-rindu-di-antara-kita" tabindex="0">
                    <img class=" lazyloaded" data-src="https://assets.pikiran-rakyat.com/crop/0x0:0x0/191x114/webp/photo/2023/10/30/2345936482.jpg" src="https://assets.pikiran-rakyat.com/crop/0x0:0x0/191x114/webp/photo/2023/10/30/2345936482.jpg" alt="Cak Imin Balas Pantun Prabowo: Masih Ada Rindu di Antara Kita" data-loaded="true">
                </a>
            </div>
            <div class="editors__box">
                <h4 class="editors__subtitle"><a href="https://www.pikiran-rakyat.com/nasional" tabindex="0">Nasional</a></h4>
                <h2 class="editors__title">
                    <a href="https://www.pikiran-rakyat.com/nasional/pr-017368660/cak-imin-balas-pantun-prabowo-masih-ada-rindu-di-antara-kita" class="editors__link" tabindex="0">Cak Imin Balas Pantun Prabowo: Masih Ada Rindu di Antara Kita</a>
                </h2>
            </div>
        </div></div></div>
                
                
                
                
                
            <a href="#" class="arrow arrow--right slick-arrow slick-disabled" style="display: block;" aria-disabled="true"><span class="icon icon-angle-right"></span></a></div>
</section>
"""

soup = BeautifulSoup(html_content, 'html.parser')

# Extract editor's picks
editor_picks = soup.find('div', class_='editors__wrap')
editor_items = editor_picks.find_all('div', class_='editors__item')

editor_data = []
for item in editor_items:
    category = item.find('h4', class_='editors__subtitle').text.strip()
    image_src = item.find('img')['src']
    article_url = item.find('a', class_='editors__link')['href']
    title = item.find('h2', class_='editors__title').text.strip()

    editor_data.append({
        'Category': category,
        'ImageSrc': image_src,
        'ArticleURL': article_url,
        'Title': title
    })

# Print or process the extracted data as needed
print("Editor's Picks:")
print(editor_data)

# Create a DataFrame
df_editor = pd.DataFrame(editor_data)

# Save to CSV and JSON
df_editor.to_csv('pilihaneditor.csv', index=False)
df_editor.to_json('pilihaneditor.json', orient='records', lines=True)


# In[ ]:


#berita terkini 
import requests
from bs4 import BeautifulSoup
import pandas as pd

def extract_data_from_section(section):
    categories = []
    image_urls = []
    article_urls = []
    titles = []

    for item in section.find_all('div', class_='hl__b-item'):
        category = item.find('div', class_='hl__b-cat').text.strip()
        image_url = item.find('img')['src']
        article_url = item.find('h1', class_='hl__b-title').find('a')['href']
        title = item.find('h1', class_='hl__b-title').text.strip()

        categories.append(category)
        image_urls.append(image_url)
        article_urls.append(article_url)
        titles.append(title)

    return categories, image_urls, article_urls, titles

# URL of the web page
url = 'https://www.pikiran-rakyat.com/'

# Send an HTTP request
response = requests.get(url)

# Check if the request was successful (status code 200)
if response.status_code == 200:
    soup = BeautifulSoup(response.text, 'html.parser')

    # Find the "Berita Terkini" section
    latest_section = soup.find('section', class_='latest')

    # Extract data from the "Berita Terkini" section
    categories_latest, image_urls_latest, article_urls_latest, titles_latest = extract_data_from_section(latest_section)

    # Find the "headline" section
    headline_section = soup.find('section', class_='hl')

    # Extract data from the "headline" section
    categories_headline, image_urls_headline, article_urls_headline, titles_headline = extract_data_from_section(headline_section)

    # Combine data from both sections
    categories = categories_latest + categories_headline
    image_urls = image_urls_latest + image_urls_headline
    article_urls = article_urls_latest + article_urls_headline
    titles = titles_latest + titles_headline

    # Create a DataFrame
    df = pd.DataFrame({
        'Category': categories,
        'Image URL': image_urls,
        'Article URL': article_urls,
        'Title': titles
    })

    # Save the DataFrame to CSV and JSON files
    df.to_csv('editor_picks_combined.csv', index=False)
    df.to_json('editor_picks_combined.json', orient='records')

    print('Data berhasil di extracted and saved.')
else:
    print(f'Failed to retrieve the webpage. Status code: {response.status_code}')


# In[30]:


from bs4 import BeautifulSoup
import pandas as pd

html_content = """
    <!-- Start editors pick -->
<section class="editors mt3 clearfix">
    <h3 class="title3"><span>Pilihan Editor</span></h3>
    <div class="editors__wrap js--editors slick-initialized slick-slider"><a href="#" class="arrow arrow--left slick-arrow" aria-disabled="false" style="display: block;"><span class="icon icon-angle-left"></span></a>
                <div aria-live="polite" class="slick-list draggable"><div class="slick-track" role="listbox" style="opacity: 1; width: 1344px; transform: translate3d(-672px, 0px, 0px);"><div class="editors__item slick-slide" data-slick-index="0" aria-hidden="true" tabindex="-1" role="option" aria-describedby="slick-slide20" style="width: 224px;">
            <div class="editors__img">
                <a href="https://www.pikiran-rakyat.com/nasional/pr-017368543/populer-hari-ini-kpk-tahan-kajari-bondowoso-hingga-megawati-dianggap-aneh-tkn-prabowo-gibran" tabindex="-1">
                    <img class=" ls-is-cached lazyloaded" data-src="https://assets.pikiran-rakyat.com/crop/0x0:0x0/191x114/webp/photo/2023/11/16/1460266400.jpg" src="https://assets.pikiran-rakyat.com/crop/0x0:0x0/191x114/webp/photo/2023/11/16/1460266400.jpg" alt="POPULER HARI INI: KPK Tahan Kajari Bondowoso hingga Megawati Dianggap Aneh TKN Prabowo-Gibran" data-loaded="true">
                </a>
            </div>
            <div class="editors__box">
                <h4 class="editors__subtitle"><a href="https://www.pikiran-rakyat.com/nasional" tabindex="-1">Nasional</a></h4>
                <h2 class="editors__title">
                    <a href="https://www.pikiran-rakyat.com/nasional/pr-017368543/populer-hari-ini-kpk-tahan-kajari-bondowoso-hingga-megawati-dianggap-aneh-tkn-prabowo-gibran" class="editors__link" tabindex="-1">POPULER HARI INI: KPK Tahan Kajari Bondowoso hingga Megawati Dianggap Aneh TKN Prabowo-Gibran</a>
                </h2>
            </div>
        </div><div class="editors__item slick-slide" data-slick-index="1" aria-hidden="true" tabindex="-1" role="option" aria-describedby="slick-slide21" style="width: 224px;">
            <div class="editors__img">
                <a href="https://www.pikiran-rakyat.com/internasional/pr-017368460/terjemahan-bagian-1-surat-osama-bin-laden-a-letter-to-america-viral-bikin-as-ketar-ketir" tabindex="-1">
                    <img class=" ls-is-cached lazyloaded" data-src="https://assets.pikiran-rakyat.com/crop/0x0:0x0/191x114/webp/photo/2021/04/27/4005624653.jpg" src="https://assets.pikiran-rakyat.com/crop/0x0:0x0/191x114/webp/photo/2021/04/27/4005624653.jpg" alt="Terjemahan Bagian 1 Surat Osama bin Laden 'A Letter to America', Viral Bikin AS Ketar-ketir" data-loaded="true">
                </a>
            </div>
            <div class="editors__box">
                <h4 class="editors__subtitle"><a href="https://www.pikiran-rakyat.com/internasional" tabindex="-1">Internasional</a></h4>
                <h2 class="editors__title">
                    <a href="https://www.pikiran-rakyat.com/internasional/pr-017368460/terjemahan-bagian-1-surat-osama-bin-laden-a-letter-to-america-viral-bikin-as-ketar-ketir" class="editors__link" tabindex="-1">Terjemahan Bagian 1 Surat Osama bin Laden 'A Letter to America', Viral Bikin AS Ketar-ketir</a>
                </h2>
            </div>
        </div><div class="editors__item slick-slide" data-slick-index="2" aria-hidden="true" tabindex="-1" role="option" aria-describedby="slick-slide22" style="width: 224px;">
            <div class="editors__img">
                <a href="https://www.pikiran-rakyat.com/nasional/pr-017368920/ganjar-pranowo-hari-ini-masyarakat-butuh-banyak-lapangan-kerja" tabindex="-1">
                    <img class=" ls-is-cached lazyloaded" data-src="https://assets.pikiran-rakyat.com/crop/0x61:1355x844/191x114/webp/photo/2023/10/19/849226128.jpg" src="https://assets.pikiran-rakyat.com/crop/0x61:1355x844/191x114/webp/photo/2023/10/19/849226128.jpg" alt="Ganjar Pranowo: Hari Ini Masyarakat Butuh Banyak Lapangan Kerja" data-loaded="true">
                </a>
            </div>
            <div class="editors__box">
                <h4 class="editors__subtitle"><a href="https://www.pikiran-rakyat.com/nasional" tabindex="-1">Nasional</a></h4>
                <h2 class="editors__title">
                    <a href="https://www.pikiran-rakyat.com/nasional/pr-017368920/ganjar-pranowo-hari-ini-masyarakat-butuh-banyak-lapangan-kerja" class="editors__link" tabindex="-1">Ganjar Pranowo: Hari Ini Masyarakat Butuh Banyak Lapangan Kerja</a>
                </h2>
            </div>
        </div><div class="editors__item slick-slide slick-current slick-active" data-slick-index="3" aria-hidden="false" tabindex="-1" role="option" aria-describedby="slick-slide23" style="width: 224px;">
            <div class="editors__img">
                <a href="https://www.pikiran-rakyat.com/internasional/pr-017368810/tiktok-bereaksi-soal-viralnya-a-latter-to-america-susul-amukan-dari-gedung-putih" tabindex="0">
                    <img class=" lazyloaded" data-src="https://assets.pikiran-rakyat.com/crop/0x0:0x0/191x114/webp/photo/2023/03/24/2520102440.jpg" src="https://assets.pikiran-rakyat.com/crop/0x0:0x0/191x114/webp/photo/2023/03/24/2520102440.jpg" alt="TikTok Bereaksi Soal Viralnya 'a Latter to America', Susul Amukan dari Gedung Putih" data-loaded="true">
                </a>
            </div>
            <div class="editors__box">
                <h4 class="editors__subtitle"><a href="https://www.pikiran-rakyat.com/internasional" tabindex="0">Internasional</a></h4>
                <h2 class="editors__title">
                    <a href="https://www.pikiran-rakyat.com/internasional/pr-017368810/tiktok-bereaksi-soal-viralnya-a-latter-to-america-susul-amukan-dari-gedung-putih" class="editors__link" tabindex="0">TikTok Bereaksi Soal Viralnya 'a Latter to America', Susul Amukan dari Gedung Putih</a>
                </h2>
            </div>
        </div><div class="editors__item slick-slide slick-active" data-slick-index="4" aria-hidden="false" tabindex="-1" role="option" aria-describedby="slick-slide24" style="width: 224px;">
            <div class="editors__img">
                <a href="https://www.pikiran-rakyat.com/internasional/pr-017368684/penjajah-israel-sandera-5000-orang-di-rumah-sakit-gaza-wafa-kondisi-buruk" tabindex="0">
                    <img class=" lazyloaded" data-src="https://assets.pikiran-rakyat.com/crop/0x0:0x0/191x114/webp/photo/2023/11/16/1651609950.jpg" src="https://assets.pikiran-rakyat.com/crop/0x0:0x0/191x114/webp/photo/2023/11/16/1651609950.jpg" alt="Penjajah Israel Sandera 5.000 Orang di Rumah Sakit Gaza, WAFA: Kondisi Buruk" data-loaded="true">
                </a>
            </div>
            <div class="editors__box">
                <h4 class="editors__subtitle"><a href="https://www.pikiran-rakyat.com/internasional" tabindex="0">Internasional</a></h4>
                <h2 class="editors__title">
                    <a href="https://www.pikiran-rakyat.com/internasional/pr-017368684/penjajah-israel-sandera-5000-orang-di-rumah-sakit-gaza-wafa-kondisi-buruk" class="editors__link" tabindex="0">Penjajah Israel Sandera 5.000 Orang di Rumah Sakit Gaza, WAFA: Kondisi Buruk</a>
                </h2>
            </div>
        </div><div class="editors__item slick-slide slick-active" data-slick-index="5" aria-hidden="false" tabindex="-1" role="option" aria-describedby="slick-slide25" style="width: 224px;">
            <div class="editors__img">
                <a href="https://www.pikiran-rakyat.com/nasional/pr-017368660/cak-imin-balas-pantun-prabowo-masih-ada-rindu-di-antara-kita" tabindex="0">
                    <img class=" lazyloaded" data-src="https://assets.pikiran-rakyat.com/crop/0x0:0x0/191x114/webp/photo/2023/10/30/2345936482.jpg" src="https://assets.pikiran-rakyat.com/crop/0x0:0x0/191x114/webp/photo/2023/10/30/2345936482.jpg" alt="Cak Imin Balas Pantun Prabowo: Masih Ada Rindu di Antara Kita" data-loaded="true">
                </a>
            </div>
            <div class="editors__box">
                <h4 class="editors__subtitle"><a href="https://www.pikiran-rakyat.com/nasional" tabindex="0">Nasional</a></h4>
                <h2 class="editors__title">
                    <a href="https://www.pikiran-rakyat.com/nasional/pr-017368660/cak-imin-balas-pantun-prabowo-masih-ada-rindu-di-antara-kita" class="editors__link" tabindex="0">Cak Imin Balas Pantun Prabowo: Masih Ada Rindu di Antara Kita</a>
                </h2>
            </div>
        </div></div></div>
                
                
                
                
                
            <a href="#" class="arrow arrow--right slick-arrow slick-disabled" style="display: block;" aria-disabled="true"><span class="icon icon-angle-right"></span></a></div>
</section>
<!-- End editors pick -->
<!-- Start latest -->
<section class="latest mt3 clearfix">
    <h3 class="title"><span>Berita Terkini</span></h3>
    <div class="latest__wrap mail">
                        <div class="latest__item">
                        <div class="latest__img">
                <a href="https://www.pikiran-rakyat.com/gaya-hidup/pr-017369338/5-tips-jika-menemukan-rambut-di-makanan-anda-jangan-keburu-komplain-di-medsos">
                                        <img class=" lazyloaded" data-src="https://assets.pikiran-rakyat.com/crop/0x0:0x0/220x132/webp/photo/2023/11/17/2266764450.jpeg" src="https://assets.pikiran-rakyat.com/crop/0x0:0x0/220x132/webp/photo/2023/11/17/2266764450.jpeg" alt="5 Tips Jika Menemukan Rambut di Makanan Anda, Jangan Keburu Komplain di Medsos" data-loaded="true">
                </a>
            </div>
                        <div class="latest__right">
                <h4 class="latest__subtitle"><a href="https://www.pikiran-rakyat.com/gaya-hidup">Gaya Hidup</a></h4>
                <h2 class="latest__title">
                    <a href="https://www.pikiran-rakyat.com/gaya-hidup/pr-017369338/5-tips-jika-menemukan-rambut-di-makanan-anda-jangan-keburu-komplain-di-medsos" class="latest__link">5 Tips Jika Menemukan Rambut di Makanan Anda, Jangan Keburu Komplain di Medsos</a>
                </h2>
                                <date class="latest__date">17 November 2023, 10:22 WIB</date>
            </div>
        </div>
                                        <div class="latest__item">
                        <div class="latest__img">
                <a href="https://www.pikiran-rakyat.com/nasional/pr-017369327/firli-bahuri-minta-kepastian-hukum-soal-dugaan-pemerasan-terhadap-syahrul-yasin-limpo">
                                        <img class=" lazyloaded" data-src="https://assets.pikiran-rakyat.com/crop/0x0:0x0/220x132/webp/photo/2023/11/16/2580401334.jpg" src="https://assets.pikiran-rakyat.com/crop/0x0:0x0/220x132/webp/photo/2023/11/16/2580401334.jpg" alt="Firli Bahuri Minta Kepastian Hukum Soal Dugaan Pemerasan terhadap Syahrul Yasin Limpo" data-loaded="true">
                </a>
            </div>
                        <div class="latest__right">
                <h4 class="latest__subtitle"><a href="https://www.pikiran-rakyat.com/nasional">Nasional</a></h4>
                <h2 class="latest__title">
                    <a href="https://www.pikiran-rakyat.com/nasional/pr-017369327/firli-bahuri-minta-kepastian-hukum-soal-dugaan-pemerasan-terhadap-syahrul-yasin-limpo" class="latest__link">Firli Bahuri Minta Kepastian Hukum Soal Dugaan Pemerasan terhadap Syahrul Yasin Limpo</a>
                </h2>
                                <date class="latest__date">17 November 2023, 10:16 WIB</date>
            </div>
        </div>
                                        <div class="latest__item">
                        <div class="latest__img">
                <a href="https://www.pikiran-rakyat.com/internasional/pr-017369299/kenapa-banyak-anak-palestina-yang-mendekam-di-penjara-israel">
                                        <img class=" ls-is-cached lazyloaded" data-src="https://assets.pikiran-rakyat.com/crop/0x0:0x0/220x132/webp/photo/2023/11/17/3810368976.jpg" src="https://assets.pikiran-rakyat.com/crop/0x0:0x0/220x132/webp/photo/2023/11/17/3810368976.jpg" alt="Kenapa Banyak Anak Palestina yang Mendekam di Penjara Israel?" data-loaded="true">
                </a>
            </div>
                        <div class="latest__right">
                <h4 class="latest__subtitle"><a href="https://www.pikiran-rakyat.com/internasional">Internasional</a></h4>
                <h2 class="latest__title">
                    <a href="https://www.pikiran-rakyat.com/internasional/pr-017369299/kenapa-banyak-anak-palestina-yang-mendekam-di-penjara-israel" class="latest__link">Kenapa Banyak Anak Palestina yang Mendekam di Penjara Israel?</a>
                </h2>
                                <date class="latest__date">17 November 2023, 10:11 WIB</date>
            </div>
        </div>
                                        <div class="latest__item">
                        <div class="latest__img">
                <a href="https://www.pikiran-rakyat.com/nasional/pr-017369263/gibran-rakabuming-disebut-bukan-lulusan-s1-data-kemendikbudristek-berkata-lain">
                                        <img class=" ls-is-cached lazyloaded" data-src="https://assets.pikiran-rakyat.com/crop/0x0:0x0/220x132/webp/photo/2023/11/17/1696159466.jpg" src="https://assets.pikiran-rakyat.com/crop/0x0:0x0/220x132/webp/photo/2023/11/17/1696159466.jpg" alt="Gibran Rakabuming Disebut Bukan Lulusan S1, Data Kemendikbudristek Berkata Lain" data-loaded="true">
                </a>
            </div>
                        <div class="latest__right">
                <h4 class="latest__subtitle"><a href="https://www.pikiran-rakyat.com/nasional">Nasional</a></h4>
                <h2 class="latest__title">
                    <a href="https://www.pikiran-rakyat.com/nasional/pr-017369263/gibran-rakabuming-disebut-bukan-lulusan-s1-data-kemendikbudristek-berkata-lain" class="latest__link">Gibran Rakabuming Disebut Bukan Lulusan S1, Data Kemendikbudristek Berkata Lain</a>
                </h2>
                                <date class="latest__date">17 November 2023, 10:01 WIB</date>
            </div>
        </div>
                                        <div class="latest__item">
                        <div class="latest__img">
                <a href="https://www.pikiran-rakyat.com/nasional/pr-017369204/kurir-paket-tumis-cumi-isi-narkoba-ditangkap-di-lapas-tangerang">
                                        <img class=" ls-is-cached lazyloaded" data-src="https://assets.pikiran-rakyat.com/crop/0x56:700x452/220x132/webp/photo/2023/11/17/3989985902.jpg" src="https://assets.pikiran-rakyat.com/crop/0x56:700x452/220x132/webp/photo/2023/11/17/3989985902.jpg" alt="Kurir Paket Tumis Cumi Isi Narkoba Ditangkap di Lapas Tangerang" data-loaded="true">
                </a>
            </div>
                        <div class="latest__right">
                <h4 class="latest__subtitle"><a href="https://www.pikiran-rakyat.com/nasional">Nasional</a></h4>
                <h2 class="latest__title">
                    <a href="https://www.pikiran-rakyat.com/nasional/pr-017369204/kurir-paket-tumis-cumi-isi-narkoba-ditangkap-di-lapas-tangerang" class="latest__link">Kurir Paket Tumis Cumi Isi Narkoba Ditangkap di Lapas Tangerang</a>
                </h2>
                                <date class="latest__date">17 November 2023, 09:46 WIB</date>
            </div>
        </div>
                                <!-- ads square giant-->
<div class="ads mt2 clearfix">
    <div class="ads__box">
        <div id="div-gpt-ad-midCenter1" data-google-query-id="CKyJqJazyoIDFezFcwEdsQcKLg">
		  
		<div id="google_ads_iframe_/5197741/PikiranRakyat/_8__container__" style="border: 0pt none; display: inline-block; width: 728px; height: 90px;"><iframe frameborder="0" src="https://d88f9f4fb056e74320f36467fdb8be1c.safeframe.googlesyndication.com/safeframe/1-0-40/html/container.html" id="google_ads_iframe_/5197741/PikiranRakyat/_8" title="3rd party ad content" name="" scrolling="no" marginwidth="0" marginheight="0" width="728" height="90" data-is-safeframe="true" sandbox="allow-forms allow-popups allow-popups-to-escape-sandbox allow-same-origin allow-scripts allow-top-navigation-by-user-activation" allow="attribution-reporting" role="region" aria-label="Advertisement" tabindex="0" data-google-container-id="9" style="border: 0px; vertical-align: bottom;" data-load-complete="true"></iframe></div></div>
    </div>
</div>
        <div class="latest__item">
                        <div class="latest__img">
                <a href="https://www.pikiran-rakyat.com/internasional/pr-017369199/menlu-as-ke-penjajah-israel-yang-menggila-minimalkan-korban-sipil">
                                        <img class=" ls-is-cached lazyloaded" data-src="https://assets.pikiran-rakyat.com/crop/12x49:665x421/220x132/webp/photo/2023/11/15/4089081755.jpeg" src="https://assets.pikiran-rakyat.com/crop/12x49:665x421/220x132/webp/photo/2023/11/15/4089081755.jpeg" alt="Menlu AS ke Penjajah Israel yang Menggila: Minimalkan Korban Sipil" data-loaded="true">
                </a>
            </div>
                        <div class="latest__right">
                <h4 class="latest__subtitle"><a href="https://www.pikiran-rakyat.com/internasional">Internasional</a></h4>
                <h2 class="latest__title">
                    <a href="https://www.pikiran-rakyat.com/internasional/pr-017369199/menlu-as-ke-penjajah-israel-yang-menggila-minimalkan-korban-sipil" class="latest__link">Menlu AS ke Penjajah Israel yang Menggila: Minimalkan Korban Sipil</a>
                </h2>
                                <date class="latest__date">17 November 2023, 09:45 WIB</date>
            </div>
        </div>
                                        <div class="latest__item">
                        <div class="latest__img">
                <a href="https://www.pikiran-rakyat.com/internasional/pr-017369165/tentara-israel-bunuh-lansia-palestina-usai-difoto-untuk-propaganda">
                                        <img class=" ls-is-cached lazyloaded" data-src="https://assets.pikiran-rakyat.com/crop/0x0:0x0/220x132/webp/photo/2023/11/17/368774850.jpg" src="https://assets.pikiran-rakyat.com/crop/0x0:0x0/220x132/webp/photo/2023/11/17/368774850.jpg" alt="Tentara Israel Bunuh Lansia Palestina Usai Difoto untuk Propaganda" data-loaded="true">
                </a>
            </div>
                        <div class="latest__right">
                <h4 class="latest__subtitle"><a href="https://www.pikiran-rakyat.com/internasional">Internasional</a></h4>
                <h2 class="latest__title">
                    <a href="https://www.pikiran-rakyat.com/internasional/pr-017369165/tentara-israel-bunuh-lansia-palestina-usai-difoto-untuk-propaganda" class="latest__link">Tentara Israel Bunuh Lansia Palestina Usai Difoto untuk Propaganda</a>
                </h2>
                                <date class="latest__date">17 November 2023, 09:38 WIB</date>
            </div>
        </div>
                                        <div class="latest__item">
                        <div class="latest__img">
                <a href="https://www.pikiran-rakyat.com/entertainment/pr-017369119/coldplay-donasi-kapal-pembersih-sampah-untuk-indonesia-sungai-cisadane-jadi-fokus">
                                        <img class=" ls-is-cached lazyloaded" data-src="https://assets.pikiran-rakyat.com/crop/0x0:0x0/220x132/webp/photo/2023/11/17/3331455582.png" src="https://assets.pikiran-rakyat.com/crop/0x0:0x0/220x132/webp/photo/2023/11/17/3331455582.png" alt="Coldplay Donasi Kapal Pembersih Sampah untuk Indonesia: Sungai Cisadane Jadi Fokus" data-loaded="true">
                </a>
            </div>
                        <div class="latest__right">
                <h4 class="latest__subtitle"><a href="https://www.pikiran-rakyat.com/musik">Musik</a></h4>
                <h2 class="latest__title">
                    <a href="https://www.pikiran-rakyat.com/entertainment/pr-017369119/coldplay-donasi-kapal-pembersih-sampah-untuk-indonesia-sungai-cisadane-jadi-fokus" class="latest__link">Coldplay Donasi Kapal Pembersih Sampah untuk Indonesia: Sungai Cisadane Jadi Fokus</a>
                </h2>
                                <date class="latest__date">17 November 2023, 09:20 WIB</date>
            </div>
        </div>
                                        <div class="latest__item">
                        <div class="latest__img">
                <a href="https://www.pikiran-rakyat.com/kolom/pr-017369108/moderasi-beragama-dan-peran-lembaga-pendidikan-islam-studi-kasus-di-cirebon">
                                        <img class=" lazyloaded" data-src="https://assets.pikiran-rakyat.com/crop/0x0:0x0/220x132/webp/photo/2020/12/15/821070987.jpg" src="https://assets.pikiran-rakyat.com/crop/0x0:0x0/220x132/webp/photo/2020/12/15/821070987.jpg" alt="Moderasi Beragama dan Peran Lembaga Pendidikan (Islam): Studi Kasus di Cirebon" data-loaded="true">
                </a>
            </div>
                        <div class="latest__right">
                <h4 class="latest__subtitle"><a href="https://www.pikiran-rakyat.com/kolom">Kolom</a></h4>
                <h2 class="latest__title">
                    <a href="https://www.pikiran-rakyat.com/kolom/pr-017369108/moderasi-beragama-dan-peran-lembaga-pendidikan-islam-studi-kasus-di-cirebon" class="latest__link">Moderasi Beragama dan Peran Lembaga Pendidikan (Islam): Studi Kasus di Cirebon</a>
                </h2>
                                <date class="latest__date">17 November 2023, 09:19 WIB</date>
            </div>
        </div>
                                        <div class="latest__item">
                        <div class="latest__img">
                <a href="https://www.pikiran-rakyat.com/jawa-barat/pr-017369098/apbd-2023-majalengka-rp3041-triliun-hanya-12-persen-yang-berasal-dari-daerah">
                                        <img class=" lazyloaded" data-src="https://assets.pikiran-rakyat.com/crop/0x0:0x0/220x132/webp/photo/2020/06/30/4204956453.jpg" src="https://assets.pikiran-rakyat.com/crop/0x0:0x0/220x132/webp/photo/2020/06/30/4204956453.jpg" alt="APBD 2023 Majalengka Rp3,041 Triliun, Hanya 12 Persen yang Berasal dari Daerah" data-loaded="true">
                </a>
            </div>
                        <div class="latest__right">
                <h4 class="latest__subtitle"><a href="https://www.pikiran-rakyat.com/jawa-barat">Jawa Barat</a></h4>
                <h2 class="latest__title">
                    <a href="https://www.pikiran-rakyat.com/jawa-barat/pr-017369098/apbd-2023-majalengka-rp3041-triliun-hanya-12-persen-yang-berasal-dari-daerah" class="latest__link">APBD 2023 Majalengka Rp3,041 Triliun, Hanya 12 Persen yang Berasal dari Daerah</a>
                </h2>
                                <date class="latest__date">17 November 2023, 09:16 WIB</date>
            </div>
        </div>
                    </div>
</section>
<!-- End latest -->

                </div>
"""

soup = BeautifulSoup(html_content, 'html.parser')

# Extracting data from the "Berita Terkini" section
latest_news_section = soup.find('section', class_='latest')

# Initializing lists to store data
titles = []
categories = []
links = []
dates = []
images = []

# Looping through each item in the "Berita Terkini" section
for item in latest_news_section.find_all('div', class_='latest__item'):
    # Extracting data for each item
    title = item.find('h2', class_='latest__title').text.strip()
    category = item.find('h4', class_='latest__subtitle').text.strip()
    link = item.find('a', class_='latest__link')['href']
    date = item.find('date', class_='latest__date').text.strip()
    image = item.find('img')['src']

    # Appending data to the lists
    titles.append(title)
    categories.append(category)
    links.append(link)
    dates.append(date)
    images.append(image)

# Creating a DataFrame to store the extracted data
df = pd.DataFrame({
    'Title': titles,
    'Category': categories,
    'Link': links,
    'Date': dates,
    'Image': images
})

# Displaying the DataFrame
print(df)

# Create a DataFrame
df_editor = pd.DataFrame(df)

# Save to CSV and JSON
df_editor.to_csv('beritaterkita.csv', index=False)
df_editor.to_json('beritaterkita.json', orient='records', lines=True)


# In[31]:


import pandas as pd
from bs4 import BeautifulSoup

html_code = """
<section class="most mt2 clearfix" style="height: auto !important;">
    <h3 class="title title6"><span>Pemilu di Daerah</span></h3>
    <div class="most__wrap">
                <div class="most__item">
            <div class="most__number">1</div>
            <div class="most__right">
                <a href="https://lubuklinggau.pikiran-rakyat.com/politik/pr-2917366104/siap-perang-ini-daftar-calon-tetap-anggota-dprd-kabupaten-takalar-periode-2024-2029-dari-pdip?taging=pemilu-di-daerah&amp;utm_medium=pemilu2024&amp;utm_campaign=pemilu2024" class="most__link">
                    <h2 class="most__title">Siap Perang, Ini Daftar Calon Tetap Anggota DPRD Kabupaten Takalar periode 2024-2029 dari PDIP</h2>
                </a>
            </div>
        </div>
                        <div class="most__item">
            <div class="most__number">2</div>
            <div class="most__right">
                <a href="https://bogorraya.pikiran-rakyat.com/artikel/pr-3017369223/daftar-nama-caleg-perindo-kota-depok-lengkap-data-dct-kpu-dapil-1-2-3-4-5-dan-6?taging=pemilu-di-daerah&amp;utm_medium=pemilu2024&amp;utm_campaign=pemilu2024" class="most__link">
                    <h2 class="most__title">Daftar Nama Caleg Perindo Kota Depok Lengkap, Data DCT KPU Dapil 1 2 3 4 5 dan 6</h2>
                </a>
            </div>
        </div>
                        <div class="most__item">
            <div class="most__number">3</div>
            <div class="most__right">
                <a href="https://mediapurwodadi.pikiran-rakyat.com/purwodadi/pr-1867369115/bawaslu-grobogan-awasi-pencalonan-anggota-dprd-kabupaten-pada-pemilu-2024?taging=pemilu-di-daerah&amp;utm_medium=pemilu2024&amp;utm_campaign=pemilu2024" class="most__link">
                    <h2 class="most__title">Bawaslu Grobogan Awasi Pencalonan Anggota DPRD Kabupaten pada Pemilu 2024</h2>
                </a>
            </div>
        </div>
                        <div class="most__item">
            <div class="most__number">4</div>
            <div class="most__right">
                <a href="https://kabarwonosobo.pikiran-rakyat.com/wonosobo/pr-1567368279/belum-saatnya-kampanye-bawaslu-wonosobo-temukan-banyak-baliho-alat-peraga-sosialisasi-langgar-aturan?taging=pemilu-di-daerah&amp;utm_medium=pemilu2024&amp;utm_campaign=pemilu2024" class="most__link">
                    <h2 class="most__title">Belum Saatnya Kampanye, Bawaslu Wonosobo Temukan Banyak Baliho Alat Peraga Sosialisasi Langgar Aturan</h2>
                </a>
            </div>
        </div>
                        <div class="most__item">
            <div class="most__number">5</div>
            <div class="most__right">
                <a href="https://lubuklinggau.pikiran-rakyat.com/politik/pr-2917365569/ini-daftar-calon-tetap-anggota-dprd-kabupaten-takalar-periode-2024-2029-dari-partai-gerindra?taging=pemilu-di-daerah&amp;utm_medium=pemilu2024&amp;utm_campaign=pemilu2024" class="most__link">
                    <h2 class="most__title">Ini Daftar Calon Tetap Anggota DPRD Kabupaten Takalar periode 2024-2029 dari Partai Gerindra</h2>
                </a>
            </div>
        </div>
            </div><div class="google-auto-placed" style="width: 100%; height: auto; clear: none; text-align: center;"><ins data-ad-format="auto" class="adsbygoogle adsbygoogle-noablate" data-ad-client="ca-pub-3987315829323386" data-adsbygoogle-status="done" style="display: block; margin: 20px auto 10px; background-color: transparent; height: 0px;" data-ad-status="unfilled"><div id="aswift_3_host" style="border: none; height: 0px; width: 337px; margin: 0px; padding: 0px; position: relative; visibility: visible; background-color: transparent; display: inline-block; overflow: hidden; opacity: 0;" tabindex="0" title="Advertisement" aria-label="Advertisement"><iframe id="aswift_3" name="aswift_3" browsingtopics="true" style="left: 0px; position: absolute; top: 0px; border: 0px; width: 337px; height: 0px;" sandbox="allow-forms allow-popups allow-popups-to-escape-sandbox allow-same-origin allow-scripts allow-top-navigation-by-user-activation" width="337" height="0" frameborder="0" marginwidth="0" marginheight="0" vspace="0" hspace="0" allowtransparency="true" scrolling="no" allow="attribution-reporting" src="https://googleads.g.doubleclick.net/pagead/ads?gdpr=0&amp;client=ca-pub-3987315829323386&amp;output=html&amp;h=280&amp;adk=1025406284&amp;adf=2818074040&amp;pi=t.aa~a.1606768574~rp.4&amp;w=337&amp;fwrn=4&amp;fwrnh=100&amp;lmt=1700191844&amp;rafmt=1&amp;to=qs&amp;pwprc=8218215102&amp;format=337x280&amp;url=https%3A%2F%2Fwww.pikiran-rakyat.com%2F&amp;ea=0&amp;fwr=0&amp;pra=3&amp;rpe=1&amp;resp_fmts=3&amp;wgl=1&amp;fa=40&amp;uach=WyJXaW5kb3dzIiwiMTQuMC4wIiwieDg2IiwiIiwiMTE5LjAuNjA0NS4xNjAiLG51bGwsMCxudWxsLCI2NCIsW1siR29vZ2xlIENocm9tZSIsIjExOS4wLjYwNDUuMTYwIl0sWyJDaHJvbWl1bSIsIjExOS4wLjYwNDUuMTYwIl0sWyJOb3Q_QV9CcmFuZCIsIjI0LjAuMC4wIl1dLDBd&amp;dt=1700191844262&amp;bpp=1&amp;bdt=2814&amp;idt=-M&amp;shv=r20231109&amp;mjsv=m202311140101&amp;ptt=9&amp;saldr=aa&amp;abxe=1&amp;cookie=ID%3Dc6591f9338d91376%3AT%3D1700191384%3ART%3D1700191838%3AS%3DALNI_MYkCFdxZtajohnpWvwMzzc802DxJQ&amp;gpic=UID%3D00000c8accc6b231%3AT%3D1700191384%3ART%3D1700191838%3AS%3DALNI_MYNT8ZEZWjrLFZIkEBtpJleLUqGjg&amp;prev_fmts=0x0%2C337x280%2C1134x280&amp;nras=4&amp;correlator=5504629316476&amp;frm=20&amp;pv=1&amp;ga_vid=1590894287.1700191378&amp;ga_sid=1700191843&amp;ga_hid=2120572605&amp;ga_fc=1&amp;u_tz=420&amp;u_his=4&amp;u_h=1080&amp;u_w=1920&amp;u_ah=1032&amp;u_aw=1920&amp;u_cd=24&amp;u_sd=1&amp;dmc=8&amp;adx=765&amp;ady=3027&amp;biw=1134&amp;bih=911&amp;scr_x=0&amp;scr_y=700&amp;eid=44759875%2C44759926%2C31079606%2C31079628%2C44798934%2C44809316%2C31078297%2C31079756%2C44807764%2C44808149%2C44808285%2C44809056%2C31078663%2C31078665%2C31078668%2C31078670&amp;oid=2&amp;pvsid=47335097678357&amp;tmod=32634814&amp;uas=0&amp;nvt=3&amp;fc=1920&amp;brdim=0%2C0%2C0%2C0%2C1920%2C0%2C1920%2C1032%2C1151%2C911&amp;vis=1&amp;rsz=%7C%7Cs%7C&amp;abl=NS&amp;fu=128&amp;bc=31&amp;td=1&amp;psd=W251bGwsbnVsbCxudWxsLDNd&amp;nt=1&amp;ifi=4&amp;uci=a!4&amp;btvi=3&amp;fsb=1&amp;dtd=382" data-google-container-id="a!4" data-google-query-id="CN7cu5eMyoIDFbBHnQkdfoUIEA" data-load-complete="true"></iframe></div></ins></div>
</section>
"""

# Create a BeautifulSoup object
soup = BeautifulSoup(html_code, 'html.parser')

# Find the "Pemilu Daerah" section
pemilu_daerah_section = soup.find('section', class_='most')

# Extract information from each article in the "Pemilu Daerah" section
articles = pemilu_daerah_section.find_all('div', class_='most__item')

data = []

for article in articles:
    number = article.find('div', class_='most__number').text.strip()
    link = article.find('a')['href']
    title = article.find('h2', class_='most__title').text.strip()

    data.append({
        "Number": number,
        "Link": link,
        "Title": title
    })

# Create a DataFrame
df = pd.DataFrame(data)

# Save to CSV
df.to_csv('pemilu_daerah_data.csv', index=False)

# Save to JSON
df.to_json('pemilu_daerah_data.json', orient='records')

# Print the DataFrame
print(df)