
'''
The purpose of this file is to keep the HTML constants for 
selenium in one place for reuse and consistency. The user
and/or programmer does not need to see the xpath of a button
or element to utilize it.
'''

# the path to your systems chrome profile or person that you wish to use.
path_to_chrome_profile = "/home/switchblade/.config/google-chrome"

# html elements to interact with.
like_button = "/html/body/div[1]/div/div[1]/div/main/div[1]/div/div/div[1]/div[1]/div[2]/div[4]"
exit_match_button = "/html/body/div[1]/div/div[1]/div/main/div[2]/div/div/div[1]/div/div[4]/button"
close_super_like_option = "/html/body/div[2]/div/div/button[2]"

bio_text = "/html/body/div[1]/div/div[1]/div/main/div[1]/div/div/div[1]/div[1]/div[1]/div[3]/div[3]/div/div[2]/div/div"
bio_short = "//*[@id=\"t--771258051\"]/div/div[1]/div/main/div[1]/div/div/div[1]/div[1]/div[1]/div[3]/div[3]/div/div[2]/div/div"


bio_selector = "#t--771258051 > div > div.App__body.H\(100\%\).Pos\(r\).Z\(0\) > div > main > div.H\(100\%\) > div > div > div.recsCardboard.W\(100\%\).Mt\(a\).H\(100\%\)--s.Px\(4px\)--s.Pos\(r\) > div.recsCardboard__cardsContainer.H\(100\%\).Pos\(r\).Z\(1\) > div.recsCardboard__cards.Expand.Animdur\(\$fast\).Animtf\(eio\).Pos\(r\).CenterAlign > div.Toa\(n\).Wc\(\$transform\).Prs\(1000px\).Bfv\(h\).Ov\(h\).W\(100\%\).StretchedBox.Bgc\(\$c-placeholder\).Bdrs\(8px\) > div.Pos\(a\).D\(f\).Jc\(sb\).C\(\#fff\).Ta\(start\).B\(0\).W\(100\%\).Ai\(fe\).P\(16px\).P\(20px\)--l.Cur\(p\).focus-button-style > div > div:nth-child(2) > div > div"


bio_2 = "/html/body/div[1]/div/div[1]/div/div/main/div/div[1]/div[1]/div[1]/div[3]/div[3]/div/div[2]/div/div/text()"
