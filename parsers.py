lista=(input().split("\n"))

listaB=[['756', '381'], ['402', '138'], ['98', '844'], ['276', '282'], ['512', '593'], ['157', '422'], ['685', '528'], ['593', '514'], ['984', '897'], ['70', '842'], ['972', '43'], ['562', '859'], ['652', '245'], ['952', '408'], ['621', '592'], ['981', '320'], ['97', '892'], ['561', '142'], ['48', '553'], ['694', '660'], ['877', '11'], ['656', '746'], ['272', '695'], ['525', '74'], ['861', '889'], ['117', '671'], ['350', '802'], ['705', '567'], ['938', '297'], ['435', '41'], ['836', '940'], ['906', '117'], ['130', '341'], ['499', '593'], ['350', '739'], ['989', '128'], ['886', '685'], ['562', '229'], ['314', '125'], ['985', '24'], ['585', '572'], ['234', '178'], ['11', '734'], ['796', '242'], ['426', '286'], ['56', '908'], ['821', '74'], ['790', '270'], ['676', '740'], ['178', '927'], ['403', '943'], ['868', '835'], ['648', '704'], ['836', '883'], ['43', '286'], ['277', '894'], ['494', '366'], ['305', '122'], ['175', '474'], ['31', '44'], ['527', '662'], ['669', '691'], ['339', '108'], ['25', '378'], ['752', '337'], ['205', '952'], ['676', '728'], ['815', '238'], ['934', '735'], ['715', '234'], ['201', '820'], ['57', '132'], ['688', '160'], ['360', '77'], ['152', '457'], ['610', '97'], ['150', '848'], ['456', '825'], ['58', '344'], ['43', '267'], ['145', '415'], ['256', '116'], ['108', '824'], ['464', '797'], ['468', '773'], ['99', '937'], ['393', '711'], ['273', '940'], ['425', '578'], ['463', '904'], ['26', '947'], ['911', '324'], ['821', '402'], ['628', '467'], ['212', '206'], ['436', '329'], ['59', '919'], ['214', '952'], ['856', '897'], ['406', '242'], ['962', '286'], ['817', '912'], ['865', '587'], ['29', '178'], ['694', '603'], ['631', '493'], ['946', '464'], ['755', '379'], ['14', '236'], ['948', '322'], ['716', '428'], ['685', '730'], ['569', '680'], ['765', '784'], ['612', '460'], ['839', '242'], ['219', '27'], ['397', '633'], ['32', '979'], ['404', '812'], ['186', '25'], ['360', '455'], ['162', '822'], ['535', '742'], ['902', '591'], ['331', '513'], ['454', '747'], ['648', '624'], ['982', '746'], ['662', '663'], ['206', '193'], ['318', '963'], ['88', '489'], ['417', '84'], ['97', '95'], ['887', '248'], ['976', '89'], ['157', '964'], ['903', '903'], ['134', '438'], ['822', '586'], ['675', '735'], ['113', '855'], ['607', '515'], ['509', '684'], ['237', '859'], ['893', '696'], ['66', '559'], ['267', '300'], ['460', '829'], ['394', '981'], ['240', '199'], ['47', '62'], ['594', '914'], ['827', '188'], ['487', '911'], ['311', '271'], ['787', '965'], ['922', '697'], ['237', '874'], ['881', '378'], ['568', '917'], ['257', '831'], ['808', '967'], ['239', '215'], ['984', '988'], ['310', '100'], ['23', '14'], ['621', '45'], ['458', '719'], ['99', '12'], ['241', '125'], ['39', '447'], ['284', '571'], ['198', '127'], ['666', '401'], ['435', '610'], ['115', '339'], ['614', '673'], ['444', '816'], ['76', '561'], ['643', '598'], ['720', '549'], ['941', '210'], ['622', '365'], ['285', '681'], ['711', '876'], ['214', '924'], ['799', '829'], ['117', '163'], ['98', '644'], ['626', '730'], ['640', '710'], ['689', '173'], ['26', '240'], ['783', '663'], ['767', '290'], ['36', '979'], ['844', '281'], ['15', '400'], ['332', '847'], ['243', '731'], ['752', '29'], ['764', '984'], ['886', '132'], ['50', '725'], ['517', '293'], ['583', '34'], ['808', '230'], ['298', '655'], ['11', '470'], ['898', '249'], ['284', '827'], ['286', '827'], ['550', '309'], ['815', '572'], ['606', '509'], ['945', '660'], ['203', '421'], ['565', '28'], ['151', '77'], ['631', '401'], ['522', '68'], ['973', '933'], ['422', '661'], ['641', '158'], ['177', '892'], ['414', '407'], ['213', '614'], ['815', '436'], ['499', '487'], ['571', '933'], ['296', '808'], ['601', '514'], ['304', '581'], ['723', '63'], ['55', '143'], ['558', '771'], ['545', '279'], ['606', '547'], ['504', '500'], ['989', '10'], ['25', '20'], ['217', '312'], ['623', '813'], ['446', '496'], ['907', '957'], ['970', '44'], ['773', '64'], ['951', '376'], ['680', '438'], ['104', '700'], ['40', '171'], ['216', '825'], ['875', '251'], ['402', '900'], ['704', '827'], ['33', '829'], ['942', '532'], ['687', '80'], ['951', '614'], ['19', '320'], ['628', '113'], ['498', '964'], ['42', '943'], ['274', '440'], ['441', '463'], ['304', '203'], ['423', '628'], ['935', '859'], ['353', '294'], ['879', '978'], ['251', '854'], ['126', '366'], ['281', '465'], ['902', '561'], ['737', '153'], ['973', '964'], ['44', '377'], ['13', '757'], ['493', '190'], ['607', '102'], ['103', '900'], ['851', '165'], ['756', '273'], ['837', '562'], ['98', '231'], ['966', '597'], ['988', '10'], ['693', '321'], ['175', '798'], ['423', '984'], ['211', '211'], ['415', '537'], ['284', '835'], ['733', '659'], ['718', '305'], ['856', '900'], ['191', '167'], ['738', '172'], ['457', '951'], ['18', '839'], ['707', '985'], ['366', '478'], ['850', '190'], ['556', '640'], ['409', '764'], ['218', '732'], ['388', '26'], ['763', '809'], ['378', '741'], ['22', '967'], ['322', '68'], ['543', '147'], ['404', '331'], ['289', '746'], ['717', '497'], ['25', '776'], ['556', '826'], ['708', '278'], ['864', '230'], ['179', '946'], ['450', '557'], ['785', '985'], ['621', '494'], ['115', '948'], ['164', '406'], ['444', '678'], ['714', '477'], ['175', '66'], ['86', '980'], ['852', '336'], ['76', '919'], ['140', '884'], ['965', '363'], ['207', '696'], ['387', '73'], ['653', '884'], ['786', '721'], ['633', '256'], ['966', '790'], ['391', '843'], ['630', '883'], ['117', '93'], ['630', '351'], ['51', '681'], ['713', '148'], ['948', '843'], ['304', '491'], ['703', '915'], ['324', '144'], ['104', '91'], ['282', '262'], ['72', '907'], ['142', '149'], ['846', '432'], ['981', '209'], ['502', '439'], ['227', '558'], ['833', '34'], ['628', '549'], ['354', '153'], ['875', '675'], ['844', '182'], ['65', '484'], ['152', '929'], ['157', '861'], ['974', '931'], ['555', '69'], ['468', '426'], ['685', '105'], ['298', '624'], ['715', '810'], ['622', '474'], ['934', '343'], ['423', '77'], ['887', '515'], ['835', '719'], ['692', '680'], ['219', '176'], ['942', '953'], ['268', '243'], ['974', '123'], ['920', '313'], ['333', '824'], ['522', '117'], ['345', '311'], ['486', '942'], ['311', '843'], ['800', '418'], ['640', '616'], ['182', '748'], ['347', '145'], ['617', '767'], ['379', '380'], ['104', '772'], ['845', '979'], ['634', '696'], ['671', '550'], ['613', '869'], ['97', '206'], ['181', '42'], ['478', '297'], ['844', '807'], ['886', '724'], ['463', '467'], ['123', '316'], ['429', '652'], ['652', '488'], ['158', '151'], ['906', '668'], ['274', '874'], ['505', '484'], ['499', '102'], ['293', '928'], ['558', '564'], ['351', '854'], ['148', '129'], ['945', '124'], ['410', '877'], ['286', '454'], ['466', '851'], ['715', '500'], ['680', '463'], ['837', '336'], ['330', '650'], ['536', '982'], ['640', '395'], ['485', '563'], ['976', '457'], ['852', '582'], ['138', '719'], ['304', '569'], ['481', '803'], ['535', '32'], ['785', '29'], ['329', '930'], ['598', '270'], ['270', '932'], ['766', '671'], ['134', '98'], ['632', '676'], ['892', '174'], ['504', '692'], ['970', '390'], ['663', '314'], ['618', '402'], ['480', '964'], ['229', '582'], ['100', '532'], ['522', '150'], ['426', '777'], ['599', '762'], ['872', '123'], ['812', '814'], ['253', '373'], ['742', '514'], ['946', '236'], ['576', '185'], ['911', '141'], ['769', '908'], ['661', '592'], ['360', '984'], ['825', '464'], ['793', '44'], ['132', '796'], ['817', '128'], ['556', '801'], ['116', '136'], ['282', '123'], ['546', '798'], ['374', '576'], ['200', '659'], ['395', '293'], ['304', '822'], ['658', '239'], ['185', '325'], ['217', '736'], ['15', '273'], ['627', '233'], ['879', '252'], ['607', '186'], ['946', '188'], ['67', '829'], ['762', '469'], ['604', '85'], ['808', '708'], ['809', '578'], ['591', '558'], ['564', '298'], ['571', '334'], ['128', '79'], ['882', '908'], ['334', '949'], ['482', '382'], ['44', '968'], ['935', '219'], ['508', '890'], ['308', '747'], ['893', '622']]



for i in range (500):
    for j in range(2):
        listaB[i][j]=int(listaB[i][j])

