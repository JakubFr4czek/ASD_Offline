from zad1testy import runtests 
import random
import string
'''

    Sprawdzam czy substring jest palindromem zaczynając sprawdzanie od
    jego środka do zewnątrz. Gdy natknę się na najmniejszy palindrom czyli
    przykładowo aba to sprawdzam czy znak przed aba jest równy znakowi po aba
    i tak dalej, a jeżeli są różne to kończe sprawdzanie i zapisuję długość
    palindromu. Mam wrażenie, że to około O(n^2).

'''




def ceasar_v2( s ):


    N = len(s)

    maks = 1

    for i in range(N):

        if i + 1 + maks < N and s[i] == s[i + 1 + maks]:

            cnt = 1

            x,y = i + 1, i + maks

            #w środku
            while x < y and s[x] == s[y]:
                #print(s1[x], s1[y])
                cnt += 2
                x+=1
                y-=1

            if x < y:
                continue

            x,y = i, i + 1 + maks

            #na zewnątrz
            while x >= 0 and y < N and s[x] == s[y]:
                cnt += 2
                x-=1
                y+=1

            if cnt > maks:
                maks = cnt

                

    return maks

def ceasar( s ):

    N = len(s)

    maks = 1 

    for i in range(1, N-1):

        x,y = i - 1, i + 1
        ile = 1

        while x >= 0 and y < N and s[x] == s[y]:
            ile+=2
            x-=1
            y+=1

        if ile > maks:
            maks = ile

    return maks

'''




'''

def manacher( s ):

    N = len(s)

    maks = 0

    mid = 0
    mirr = 0
    r = 0

    tab = [0 for _ in range(N)]

    for i in range(1,N):

        ile = 0
        mirr = mid - (i-mid)

        if i < r and mirr >= 0 and s[mirr] == s[i]:
            tab[i] = min(r-i,tab[mirr])
            ile = min(r-i,tab[mirr])

        x,y = i - (1 + ile) , i + 1 + ile

        while x >= 0 and y < N and s[x] == s[y]:
            ile+=1
            x-=1
            y+=1

        tab[i] = ile
        if ile > maks:
            maks = ile

        if i + ile > r:

            mid = i
            r = mid + ile

    #print(tab)
    return (maks * 2) + 1

#print(ceasar_v2("akontnoknonabcddcba"))
#print(manacher("akontnoknonabcddcba"))
# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( manacher , all_tests = True )


#for i in range(1000):

#    letters = string.ascii_lowercase
#    s = ''.join(random.choice(letters) for i in range(random.randint(0,100000)))
#    if manacher(s) != ceasar(s): print(s)
#print(manacher("mphsognvqofwbyzmnhayiiafaijzhvhdocancsppvigyhdqsuqxmiudlcgvxealoaqlidaybnpynwmjxhqqubpebhjrzgrofhrppumrotsauilwwmaalbjitrphbcdqdoilhsfiaaobvtannuyyjmvupjcklckypquhsmjukxhjifelrvtjacaihqyjkslohdshrmoltgubjsuhgfmwqkfsdsnarcacfvjclpyzabuvmkdxikfdzmjpbvfufsdjhujzhzbtpjmiemlssgfsblzxiuzehjoysmobibuzfqnzmqqwouigezrnsscwmoihtivbcrmrkzmvraforrxawaypwkdbhxcfqfslhqkrxjaktnnrbkyhaahjkyalyxphzjpmnhwwmsseiotqnpdijfpqzlfubirpzdqoknkkhujdwhwixnocsyxafnmprzdacjqvgfonmlulvvmvojbdjlrcsmubskjrfutlkycymmefrrynlxenfzwqbnberrpwlqctzkazyhyjswoxdvvgmzhjkwdnbszyhwxlibtknridgiifolqljidnpahxkawvuadhahpvzfrpakfymrgtpovbaqzuiqfduaansiwsvhaugfxnlvehhweewhytfcgkhzfjnxgiurcxsnrtsnxjvrkyajevhmtolcysrbryebwycnqqiyfokggwbboaywkdaodkppfdzfdzygxyirphnidwsltbnjikuevwfuktlxrgfrnwzldlxdgmflfqqrmzaicnqpcwhhkxvedokibfxxufpligwxutzcirbwkfygvxsgmtttpytnefytnadiarotcyfccvqpogfbeyzvutqbmnejpcehjbejrfeezgvscowyemlhgnxdztyjthlinsyolgwcelvobmafgvvnlnqmpqecvadzayqpggrcxpssynpocndjfkwxeeytjskrzvnjwfuvwkbegyggxjhvjzzcdxnsrweccaarczmbvpmcwxlcncfoylqbryqlmfpeyuoioxkqudumxzwlbtifprojgpjjnnlspvoijaystfxxnlmeedhucvezdhfjzeyrwiemvfqnmbhshvgwoioggyjtuhqgowbhdprpuixbbtsqufpcnmleqaimoesosmvurqzswhlyfgqmmueltogucgteeijhbsjyjcatxvyzbpxcpszwmjlhcsfemuaetsowepykpapsyzglltawjdknwqafmpbxtkesgooiieapdfhznuxoousdcchyspnqlixkuhzewzmygvblcesyzodwjppeawiiuignyzuupxcjmofkfqvpvosrurgxoohsrckendutwgzkwlyjceoktlwojwwunoyqumaflioqksvtognwmbvqowafqqkcpppplexvebcifvjccvqrhfcanspwrdttmqdwyunbxweknfrfzovgpfaxyvcdujqylzckegdecgljazscjferyjuhczqdowavtuunbkwiamuljjogurkscuqkjzthjxrdkkmxrcofdpxyvqlgwgizxlvrdnuckwdmbvkjdxfzhawyrzejdhlvetblqmhicngonxkzulftpuzrbwwtiqnsxsrsvkrnydgksewcalfvuuqeoyiekdmvzhgjbvupdkgaxhqwwwsgqkldsradmdrujfxwfgkzrvqttdhgjfvidscqmcytftchtaxrnkfvwuqdcjategzieipzglnbhpomtmwsnwmmbrchpaojhmmnlmbmrkzfofnuepzjxidppobmdocrwisceecrdgnchvxxpujszuczcbwfevhojzbvxpcbkfivuvpaokqiawzanilegooszgkkjscfzrnoboqnbozmgxrjuipmqqkpqatdhnxzrxvmarfjpiyihzeznulwlcbxzhagncbzdbupybqxbkbvfejontkwzjlwlzcvkltefugzzhnqrlrannxxqpfmotrcwshulbjfosamxpbzbwevxaismfcpdwzzfghvtuvjzvhcpnjtcxdctwkvugrtoumbuuyhtgdhpvywkechjrcwrcgqgverixnhhgmqxnwhevtkgfbpmwwafgyoypvvopewiqsuokkvcclmrdohstzifwkvpsbxnmaggwjchjxnrqzcdxqednskrwepaydxrgqcpyepayfcgkyretdmwkctwjsulrsgqijnwzblukchzzuwksqyhurjlfuhihwvnxkvultmeawjjxxrfqwouixbzflwqcbreijpqhxuybrdkmjkusywszctkmfmmyvvgsbgyxeavignshiulxdftoekapaslbazyonqvajqtxossimcuuqhremzeujyhaexeoeujsuvqzpmnghkbsvhcubmwrboybtjelauvkebummjgzqyutwfhuzzjzcdngyyyghgkafnzcedwafzwsdcxzzyybtnccvsryxocscziaqwaaztqtcamfqrdukalfjlaqrnysskbuqybcuskhahzcujejnbapfbccxxharhzbaqvgsmlbhcmsiagjeffvbjdnjrmctbsprlnxpuqtyzcyjfafjsetvlwfanuuholklhvnmlhubhjcxakuhnbhxjigdghegocgvwppcmwdfymcxwkftrgnpqepjrvzkchlstkivdkzolmzuqjhjcsugqilfqzltrtwyqlztwyfebswslznlracebhgdlevkvwadavmaykzkjnnubnynhprstxmejsqvunosnwplimtlqblrhboonagprvbpdcxrbfnhtuallilnhubovceelqiafjggoetvnuxsbogfkhvpzbiviprnhscfmrrvstfruviyymfnbcasmcvgkwkoeipmcqlvkoxrsqburumiiskgalntupfcvbddrikfqtfsxafbqwnirejsoldubijuzwcqbmhuebzzjjibfixvwsiuvovvzfzjaabsoxhesmavvjmzqbutdhwkgsqsdqfpmjfylybyibtvwabmbbgqfjfwjarlystwinjmqjimukbhhaihtptxfkguhywpeftbzoqpdxaaomvchuinfjdtpmsosqqbtnxicyltogbershomftczgzsjqdhjypmsxvdovozusfbmuqfphizxnhjoewkzjiufcqhnueohbqythdyndsyzfvpmqwlljmyhphhgyiycrewolazzwrtrlwffoprqjfevgaxiqafkjbfbtwyikoboujwogjgmemefucsjtmcfmlrxxobfsxilskppmwmcuzovtdrjvsrgznlimbguggdgwfympziprrlsskdanmbburezemzifjvjfbtrkcymjpuxyarqwuyeezzrqpkengewakcscgghtejftqvzxaputdjkvpejmvuiqiiznjddxnrzotnhisduykkypixtrncxqihjzxhathgyfeabyshsmbllnrpegjrrrrbbbjkbvuwocmymdasaijhreuoygjxvhhutszlwahdizggyikhbvhktvaudbtvujmntxhiietrnodkyfqzjzeqaltsjrmljdcmcvzgtpkrqchdefjskxgywymbfgpwpvdabbxrhunxrcgpdwqyyyjzvzttqzvezdrflkldkktajnvwjuxpvqfaevzadcrtbouxzcszhjxlosajtamiowclcpzzbszpyiwtollepecwyjzijnjaslrfphbduqcedwmsjogxrfzuzotoitsbueuugtbsjnprwtduuepqrcirpybzjxjwscmayauniafznagutdulptuaepcyartqymqvfegollzkmdjlnkajcnytiuexzfjofeqgcjqhvsqztzreipxrhvqvgsbdqxufedchbrqwgiswniqhnnjxtbfpfvggwupgglyemmuxbvzmcprfkxzfmjhertgjvdfzltodtwextanahwbywiavicxgmootovfvjnyamccxxptvufkteplafscigovnsoewradmqcemqputpewugmdjrjdjsyccvsbrswmpyvrbvqajqirafrmujihvkhhtdpoqbajmchvfsagnkpaisqolinmnhrebozqdgtwsjsbycyoiclicaxuyozjyvjnugnzyyvnpxfupnduendsprsbgwdneumoxdsdvroxuoevjipctpujennubtkrfgtfwvpsohkoeggvcdebqpngqiotgksvhfmpqqgdgkjinvdurddohyvqjfaegqncgvsxhmgggjsjynlyuawscnlepegikjmgbefitvjyohjinszaplrmrqvudldawszseumlbnwidwdupxzysjrnpeydwjkipqnyibfftcnenftpfsafhmjfxeaonoxlirohtrjnzozjxjcspvxagigmzelcvdpqjlhixvumppzkgpyjeyjyyvgmrixxxrpucqzyamunatykeqwnduhimrmmiiejhpfxejdttgezicqrwkrzgxrvpjoskmgjzvtchszlhsbpinfhrjlilcbhqhnziqzzkkruwebzotltrmgxvuhcqoghkofrrotryqrtltxvvkxinzsctxhsfprjxbjvmqmexmleumkbhuengmmizlahytsdrxixxurfnryyuvljzlrimmupmselxzmnfzbcmitzqgbpzdqqdiernngjgmjjdzjglbzwattnihvagirqoslamdoxxwitcrcvtqaizgqqzgicdixxquvorikmlalxmqvyzebfcuhadoaujaclzvbfigfanjmczwxkdglepytzxdhqukquxsbkpvhxsllmafowhtaxvapvjscmsvuwmdwyrjnsbcpczjqxucwvzpxwymoolzccevltwfpfdywoqtknjtcgvjamfnfejkjgeytcaeqlcxdwjsoeskjommgyljlulcmcpxfybmsqgscfcwtuvkcmkzgfzegccrrqvrdaiofmolbmjqiwwnwpqovnkpvpvsjcywdrozpgoguzzmnwxuqxfgmhyohheyhoqyypsjltwchtghsawmatplgtpqppmjzsmfzxtbhhzlnyveyxbgvworwpazjcentpdtccpqzdlkcadvpnzlqwmtmdiipoozdngecyfmrgegpnvzxblegfedsgwdtnshcerqkwniuubhjqzauxwaaicpnglikmvegnhgkgpcwebljfypactuklxcqkkikpzswmkdllqquigazakrrsknhsuxzxupimogifttlsofmdjjcwlloqhwybrsdepucvftefzlflocvyubpegocetkjvfhyldgjgvxxqaftrvhxfbjjkzfsefblfwtdtyevizcrjdbggztiortuqqsoldcnquwxsqmgmjstvrvcopjxbulucwttdvqxrmjgeeqiblppblrnkpvkdqhiodiarcrtdtoxubtohcvpdwnmvckwuukgbrwpjmaxouibsfmkdrfhqxbuwfexkpcbaivqnxyfmgnvpsgiwqwjhcbzbzerkynzcxmkgpfrbdddsxgwcdugusagrhbpvgibkgyaixbwkqyzefdhadzrsvljttrsfzpxlxblbuavubdlhydfxvajglnmqxoddnvgbpbxsdohjmnlpaqqtvpnfxduercrmupqlxseuytmchlaikhhiiqnafabxufbzltmunpzhxffturezatlilqrtzdqsfsibekbfennnccojnezbhrhyexcofxbqerfbeoycnpwnfwvlpeoayndumylcadcorvtscjthladksuhzgzzcwbejvdffgpbzconqotpmihklwadfyarzbstawzypizndxvuoiwkegpyvupuggkzqcbhjqishirjcnhdaweqtwkvpgndkfpeoyyifyyiiyynaglqlswtsweoqkikbpqpyqofsvnhkxswgdeewclpejgzprozinhhygzswktmwpinwdzclotkwkrqfdypsizgikkaykdtdojlunvenanvmgpjobkgdeczdwhaqitbvsykoadqfborbysxmseegcpnpwuuefztdzynviobgyopiylmzlmdgcjilwgyganlrjgnueglkeujykdnllewiwmmvkgtmigaphimprmjggefdpnywmprpqpnjcmipmwigaguzjbvkjgoneflcnuofthfgpougplgqewiftofdrwjuexzaepmsfocttmeosopgtoqxxvspuqedtqouanwyhokppjoifyqmoiovvusjyqsuohdtxeqjeabcprftqxzbvdlxsuqkgqtegyfdsfckwcsjwiyuyovcgjgfognhdzkroshotpaagesvahjydtmhhqndjwoovsjesnjachbeqfhdpmlgoqjuloexdjilovrfqhegznrcrewntbkjundejnjlkkhoqzijwmsqbiytrdenmhwnhadaohcqjughcltirnnxkctrnfxpkktnhzewbdwbzybesjlvjillzwkhrlsmwpqyynpvuoerxhemrywqcpcqrooypmsccomkoiskmiqztewzsdcjvxkofnpdhhnktrzlxpnsbmeubhyhxzmmhgxuerwsbcqcaqmouhcjmfpfreihptfhwscyynnsdecpjmobsvytcnjvjqcicupskndsgzyruhfjgqnedtjxzpbdhjpkpnddgvimjmetxprknkwryzjmlzvtiitugpdsctqzszhakuldelykytvnztlopfxohveuvqxljrtinzkbnqutqeyetjduekkeuzicsyuguhngnybvfbbfpjwkyesnfudjhdnhxdmxjcbksvttbkumlggerkmjchkgkdvfzfkkrlgaetzirfsnqlwgtpifwvkennighatywlmwghyplplvejjgegbxwbsmzunerleabmpcoblanpywhsmcvlyyrtdriwzviiskcnpeqbixoekimmudyfuolqrzdjiylurmtlsblplnzntqsabuellphhzfzteninebihqglueqpizndngmslxsijnxgojomwuugnmqiufgfigwydcqnesgyrjldbyevuvpuioxmuvxtmkwbekuottezvpyvinhivhptiklygyxgeilxvepcxkiixycneeopcipftsumddtgyvismcaqwrzykpilhwqxtheqjjhssnnfqnjguaylhhyliocgndrfxqslrdbsttldwttkzahfdlgutngietgahrzzlurlollcostqbnvrnvqrnsjbdthoybmmwxkhhgzuelzoxjrvshaxjpnfjzmgmhzmhdvogzfouvccqbcvidvqojjqguxbezqkcmlrmkrwlmwulfbyswbmrpgbpigqhctyrpffnjktpfiwyfzudytvuweequfdiaxvnzsmrsrzxldwetehjrbwitpbqofuuxbmnohsocmasbgqshetxjmeckjdelmrtpcwgvkczcpnqhvhgixkfkmyqwgqwifhhuvjqjxijkhsmuiymwzpxginzobhjbnejqbyjrofrchgwygthkahtziynwbdxbldzogrbynhfvkwexbrvxyggvcuiwazlupjkbmfzavjboihagzycokhxrlovfxnjgubqwtgpnnkdhgcojecgqjunokazdbztovqsinqfvqsbotswamniuylzfsoxswjmuyigrxduiwdidvcffktcgsgzbpsklugzebrlpgcqjyqgndezfphqlpxftlnyqphrkypmzhjcoachjxsfuedcllzbqbnhfwmodtsccnduaggkzafucwhfsdzhmzdwylvrnslpjfabistvwagmkhijhlcilqmsjvauqhaiowfvudswnijnzyvfmopjthrrkiqrapvmlkhtqadvnvxfotrzmebyjfomdmwzbospoxbzcocasxqrxrsdvdqlhzlllpbnfjdtodmvofcyllprgyglxfetvtterynvegksrsznlipdfnytslssolmmcllinutcrcgqxdjjqbupbippnsmskvlroqyudznzzukvpqrrmelfpranzcpgliwkciqklakzpiauxtwhlaowvfahxnwxnusabysuwadosikdlpwktilkawlhbbkyeezslrrlksltnaghymhblfavxoyczsnqgjvfxvtwgdfnpgsowizcslnvoylcjsdqfsuohborlvkqdwzbylgylsjnphdbwqrctqwwyesndtoggolwyissvsowkckucfdzhzqtalzqkzjfewiznnbpgibokdtieczkqnhxpwcmixytukwlntnwyhxqcmktadoaolfskpvqlkszscuqdtklxwkqqtjoqcizqebxpynynroctdgybmxbvlmnlcljmsrpoesqtszfmrurbbzbwscosbfwsqpxclffvngduigamspgfwtzxxbdjpmpdxkewkljfaukrunrvvprloiswytzsuzrlfehymfhwyuozfpdxawyggpxuvdwnztwiqovpsmscoqdohwsudtxvihdzezyyjbusvhheljbtiprhfmgmjapydawzlgkunfrobpnvitmmighmzjhboanglzoaecfmmnlursuphtwodcmlyiprnybhbzufeobskjspvmnfgfzujcvnevetrdmdqtrggmpdjqbbipmqfxltofmuadvebwyqkizvdqdrsjaavvcbkplsqbbfmfsjyqjkjvssrvzyzbrrezqgoerieroafudrmkxufuhxwrmewbjwcrmkkgcwwbnlxvrqufuhalpjgsdfauucvefsrdmcvppdfluoqzhxdgezbrnheduwvwqhbwpschiwusxmlsrbmdrknrwznewmhvojlbtivrdvxszkqerwvjpqzixkcnxjjnzwexdxouwjbzzawiaiqoubugueasqucwksvwseampkmdkaybidgoozuoqzaphcrkpjibxxkkwusrfbqpsowtxcgrhxsniuxlkuiepaoarsxapkqavectqxhuvibrpfgwwezokhtvaefhqitmypvaysfmhaimbvyvcrekouxawwfrlfrkvgppmgvaorhwzwzgqnyapnggnutbbrpqmjdwbberowwltlfqiprywkgjuepyvanzjkipogzhhyreagtvgyxkgtnpmrnskcwtfrzuepxeutmzrbcpekifcxpgtwbafyfokszcdyakwrtalhybddxsimnseetujaxapifofspplulkddrzharnimnapvyrazyddvaimzedhwpxoiuhkgvthieaqineglefphhjhwzhbqzggqxaesxmtqvpmfnksvknltgzomrmzymvwsxfepuijlaxhrzahwqtlncunwvmwryxmogqenrotdlxgydcueoudymyfhyawbpqbfinscufofemhhopuyumgywdeniuijvqqsuvnuyrluxtkqvqamheunrzmufmhsxcipxlyvmumjwdbkapmbmqobzpjorbbjngvrfuboeyonvfkcbdocyyfjbyakcxdauiwtspysxmlayeuhaxduhqndxwsqyfsiebujrxwpsvfnpxkesztvkzaksziapdyesmifblryfobvlfzckdgiusmfumdhnpizusmopciecpftmmzmzmnslbedbvllkcsmxkentcgdozucsziutligysmwpvudbehdnbjfegzodzwiftbtydefrxkygbqjamrltjeipgzaefkdbentrjukrkniswqbgmbvvykbetmdnqbfijrlbtelrjqmnyanbmlxfddzeivhrfdqvkxxpaoypjiflmztrurdmlscsesbspdmvwqkjaqaoxjiwjoszwkwcbdwyxxnetvvuqtdfpenpfqlvttxvotihddazyutukxkczqnfxrlpxmereaxgizxxifblzxtdqbhpfzibfknytpfuqtvdlxjmpffuhdwpsgekqcwldhpkcrhwkyexwoodbpepilqmrcbimcyjrzevbmfyjhfemcqqppbpirhgkgyeqkfthspnhmdkkfchtopmhtwpnbpnzovplhexnypnrmzpvxmiikmxyosuryzpnobhdaztjqiydybxrcexzvitqfsepbptcpgiezaqbdthnrcolrvcpqwgwjsmoqolwmokvgryqrwvywannxnojqjatrhftvthsarpxqgliulezrogbruvpwqlkhifavoheebbnmuoghaxmhcxecqmqbhgdizikkadaxcrgliykqqpwfyinhckoclixxreezkqrnnxkmgnemtubagddjfltudeltdcyubakaakflalqfhxldtubwmcbtklwnkqrmtqownpamhfjhyqypvfmbcbjzlgicqyjlikedhwrognndxvoiuvcadrroywwhifhqidiqvjsubzybbevveeclegjrhygpnxzmqwemqbxsnvqlfxounjepoayysnutjadvixiedgoisbdikudnhabrehdhiwzrggvxclcbwivqwihelyvsyjqmvemkzcstwbefkidcygagmmugulflkdgjvswochrnwgfewvtvwftsnaceghxgfjdmxdttgjbdpyspmtthndzodedxweoylsrwqapcbpnjbmsyrvzxpunrnairozifoobyefgbdjzejijtnkprlyabavxrxmecyommwnmvztufejubvuwhhovdejqfxaxvzhucksskabnfzypxqvedmlrkomdnboysforizgjydylfztgbuvxcxxtryrqrhkabvtmvyaiwgypkasdstqutmczhpjzzbnmqnmniafcmnxzbpomdbwtvafolszpnypxzemroahlxfluwqphqyfcrjidhuoowrllrtxwcknidyvkpxfvizhbvouybqqwxaftlrgulsvhyyuxuqnvtifsnjagdwbxwqxutxcacsqkmmvevdaprndlbtniisvhenellxqitqfaomsbsejeyhiexjpjaidigdfmqxjoxhdwyliofxygurdmrpmytzqikpieyikcvdtjotqstzrhooezjnlliveyaxzafyxoqgzzxknexhrdohmztgpfkrsiokixqphiqssloagrmafrdtldimegxwltppgtpmvgzyoizdijagdthiuujkwmongotlyskcffqmjbouzkoiclaociogtxfivqiyndzcmqkixwxwiubkroejvvwzwvjcnnwhaaawjqxoigudzmpsmmyaqdpyywucbofcvjsjqyiwtonlpiaxmyroiarfkresadlfpeiffspwyjcczxjdnwmrfzhttpzxavilljbkvirbbujybtfvsmuvrygvachsscmljkapdacctgougwvynuwtypzgqeesknlydsfjnpgqkfrjdyznncivbvoapgwxkdgxrrcqacydrdfmvlcejceizytsfpcugznnuapftiizxqbeierrobzbmjiobalahaowuxhohipfcjcmyelnmekrwbpcofcsvkxnnikeojvamkzdubvzirruorazgjaigzfspyzndtlyovtzsohrnhtkmhafxjukjjyzymaazhoeipsxrrlbpqnjtnzygvmaaxyijbepjavoumxvcnlorgrigbtzurmytxqrazganxmrpfupscxezlrnsvkjdqhwabzzdudzhqtkxyybnsntakoubxawejhrrrohdckqxhhqcpcmvxmqpbiibrjtdnvjmuxihdwulmltrkiznimwbsmrziwtfmbmpuwrreizjewfsyiifurmytkztyqtwqixvqhouatebyuyczlkilroyghyhcegqzlsowleummatlyttajjxrfsvdfpagzotsyyndovysfinptdlgfbvsoauvklnlrlscvjdmjytqitlsseohbzqffrcctctnoyvgcbshqqypvvwrsjopvtodbhvwbeztserfxyehmaniggwkhegoewhrgtkpzloyqzaxooqvemtrgjmivlkuhoezfnsmivwsdsxcbchczkcszkfwwjjgjnvqbqwwrmnxfzldyqnygjfvwksphvswsgahzgtougmkaeqtqjldmanbejfhxfzlerpbxjnnqrhnwknsklrixatzfraqagmluxtpietbidoftxxhxlwcubptfimtcyglihrybpqscdirikhhojaldvhzgvpozcsegridpxreyfcrngzdrlqfcsmksqgphbachudjqecvdmdwzobctophqkujisczftrvtqzikybemimuoogazshomkzpluczfnxqretslwejbcahuwguyycclqeyynyknnvqjnismymcezhjhfgumqaibohaxvfhydvvpbohnpanduhczhiygnyozwjliebvlesddvgvlupksqpgnqzusjwmhqcnmkxeqhgeadsmkxknhbxblzchrqvakvfnteyguofcpisznaejsyescknogopogyvvhecuzcwvbcuqdodbptphgpcqtghkievzvjksheblesxrtlfudpcvuyykcjhwevoxtonarhfmeaduefdgksftcbayprhjukgwrrvsdbojzklrkaxvfrrfvrnebrzygenoczqarjofzbeandgvnusssstnwrbfighjnqurufkhhfbdxcwmsjycctvipznlhnmdeqlxwobhqrdtuhibjuczhwylzwouwhirmqsoaqewigcvdrirzmjlifnismxzeorqlqdugfflwaqpmhspjruswyehfidzwspszyvxkxkaqzxymciieknlppbbdtawmczsbwjsgwbvzoogjpubnyjbodtqbeadddcvcugfohcrzyrsvcokmzsetcsytywquxxsisjyqskhnawppmqzybrjzfkvboicmwvtxcfzfgyizcwjmnzouainukxugiucuavutyghfqjhnadndtyclkaymdlbsikiwcxrgaljlyoqimyjdqmowhjhezrhzpydvrimwfbyndpthwqhaakmeelezvgwbkzqgcrqoejxqxsddinpqbxwciequzynaxcrsjugrhkzwegpajweymanaiaxugwpbjwjqipfcijnzjmdjetowkkmechjfpjoployzdygdpbbqjssklffoxcowvewngqrtvtfekoujijumlcswkodjxsugjbjykfcetixcnqkimpvyxhkuiaogkvempatfburlmgdntduwccdjxyugyiwjiesvpwwkqudcrhoonvoxddwgtgtioeqczbbpidqntclpqgkpieavezzvymidnrxnxhhzfwegmiuzcmsurvbfftkfhnzyblhscskqafpdfibkwjyqclsqimoiyoyfvruvcxbkteybxhgswyuntvadhyetmqncmuqmtjqwrroaifwgnxhoailhpefscwtdpwkebagfsyncdgrssfdsilyrexsqjdvmpylmemttmoufhcybjvkxylmjnjtbeevgjxdwkrghxlghynbavjcwfjkqreexndrcustutwlqfuwaysvrphesmvfrlnacxgzmqhhdawnjzzmeqwsbnjosiuvzzrdinuwccfbybvqnrsuzfhzvlcdaqnpweouewsbhmkgcvbtgthmggepebqeocbhtxpibkqwxhxtiqqnpgsvfwpuluazmsoxjeyqkxcghvplbirakmzgotyeoqmgjgievlbxqmukeudhefqqdhcgpfgycbiyjkohiyhceqcuuqcgpovlqususzdunnwyjtpczrrrtoetuvlyymujlwsoxvgvzfwxbljlnsxwyrjldzhxfylvowztlvyvodselswrtftkmycvqublygsjssuwdesfqgklhajeruyvralrxbnaknodkrcmephorqvvyuntyneykwagxqhuqiptwcqixkigqcrnakgfwbzxykbmoyrydytcbuyfldxuylpvgdfxfdxhoqooauduaiprjfpnpebdstpbblwmuomncsuwjerooovpujabxlvxwpupdaujuszmimtijobdodwwkhtdyuhomzrmtufvfzrcamfscubapsiqeepzrbbvauyvubiyciiccqhkbwwxukembbvnvuekfxnprolsfkxbwxvgdyniurobfgzdkfyicmtiaalcpiboewggkuxbcjxrbfzqytwevynpwvcrcaafdovaebpiynbnddhgwrioydzernmqhndwwquaenujwxlxgtsczgkllqvavedjxaxkeezkhtdgmrcinusmbgyofoiqbjphchvobwfwrzsclperbtticalaamcqmasojujremgtaasezculpujcgnsapkpgbjcuhzqwiftrgsvicvvbpmrubcgxkwqmlsnznoltjkujlaretswkrvdqpvwmjafamplxpoomtswjpjpjphqjkfaksiafgfkytdeupwvpgcgxeikdzzrewjefepxkrsttdqjkngznqxbtlhoejghznckgqcqnvbkeafowlzezvelnlaroymgepguntxmlbukpflrxqgburwitehlzhkumdkegeumfmmudvwknoqextaihqhdjcbwykaygtedcgprxjyapsksvqqbxiwzynunggoemhwckjavrgzcpnnibxeveukbusbmkrphktjvkzruuyoquocvgfgcrqcwbawrnqktstovgbrgaauqnxcdgsqyqivgztdwfgegguvqizqtsdpszzaxintgetwqntcstmiprwfzbbczqqueblsdbfdmtjhbgvvboxhqmuuvvdyflfbpuouaiokhysoiqbofjsbnrqbypscefghsetcpvpvunyiigirncyyfdafmlwqarzikzsfvwjwgyjaajjaqjlhibrmbyfzyduoeczlataqnfvfwtqcdyawejihgndidvbnvchjsourjruxcxumjvaidtdxlvvxawqmgnylqzchviqqrmjdhjuwjdbevcmnzwgsbpapelhrupknkrxshzeujneogdtgikkwmqfnphehlzzssixwhrxbjzggpmoizrtjddwlismikmgsbenhriqliekrbipewaddbasfssrdctfughgyxnbhvfwoeawrgfdsgydysandtxkqsmqekeeszmdyuencxuuwupgvvacsyrdcxiehkokzoittsddslwbkrbsmvignphenpcijqqadiwuxlqsarwvuanoigauahwsfqlyffllmzollropmgeqaatezsldscfcarwcuyrzwthdrcegbuetqnxggccbbuudvmvtszfekgxlvfvmjeauokolrcaowebquvyccwmwmiaihebanmkucsxxsxgvuybviylbrmyfgbmfueullczcesmdvblimtdrvzzldhnymbxjucwephqmpqnfltmpingprqunxkrxkxakqjxoenouwnzrzauozynjgkmdokvgocjacztwokulmndefcvnwtyoqxxpevoohxarhjlzsmpgdvcdhynhgxkkdvwkcvkihdshmmhlbbdrirfuvpnwvvnddlebwkfyfbnybcxvazktdirromdxkapyryhkumytadgnrsdzirhimhviynhzevgggycmgesukklfybdordxonnhulsokocgdmwrqbqidfzyrcyebgrwkhkdktimmpmdqmfxjoylgxbfqxqydqydiqnbygyoaqzwixyqnbilrgsiriqxkwcmexvdrupcuxzygpucqdiahyfjiibtzdircownomvlwcxlthxlzrwxydggobaeboxasihxvxclellhnbireowqyxhxopprxqgwjxkzbwkpujoeeqtnfthrcfdpuoucnrrouippptowgmlugblwupfkkaqsbstfurbwvbwtyxfdisqtjkgkoxmshcctdiskjpexlwwbplbhpxkgwssaqegnymxfbwmvfvvmrwdlvsctxvbecdbgzmqyqmbjzybgovdintxnnntqcaanrquarnszjidygybfjqivoupniibggloxonpuszlbilrkgqgeuvdgqxbcdevpocklpkjlkfxedglblrjymgcizjlwufjidevuayevfjmdxcywnzsbcjegpntawigmltdjoccvcwcnfvtohtsfiroavnrzsxxnvbvmvcbdyxflhlyvizgtytyjddomncxvtkldwqpvbzmkobzayetsfaksuefqvqpsljgsdczszgsrbugvwhusxqmxyymurrolbfblpwhcmbvxduogctkuswzozocxzlofdvmglkufnqasqhswuhsatjrmgbwgfwhbhrwkdafphpqpobxlhqcxgjsoglewyvlgjfhezfrwrlifgjfokpawdyzuuptjvgsadtesmbexdsquuocraloaqzymknuupycgvwkxllxghhpqnleokoexskliqedglikednztsnehhmrwkqfvrrexwwafrzqcbltsvmaxvd"))
#print(manacher("testosteronowydon"))
#print(ceasar("testosteronowydon"))