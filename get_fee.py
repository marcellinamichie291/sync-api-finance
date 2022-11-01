import sys
from bs4 import BeautifulSoup
import requests


def main():
    obj = [
        ["AXS", "Ethereum", 0.41000000, 25, "Bitkub"],
        ["SAND", "Ethereum", 4.17000000, 25, "Bitkub"],
        ["IOST", "IOST", 1.00000000, 1, "Bitkub"],
        ["CTXC", "Cortex", 0.1, 300, "Bitkub"],
        ["JFIN", "Ethereum", 2.99000000, 25, "Bitkub"],
        ["ADA", "Cardano", 0.80000000, 20, "Bitkub"],
        ["BTC", "Bitcoin", 0.0002, 3, "Bitkub"],
        ["DOGE", "Dogecoin", 4.00000000, 2, "Bitkub"],
        ["MKR", "Ethereum", 0.00420000, 25, "Bitkub"],
        ["ENJ", "Ethereum", 8.25000000, 25, "Bitkub"],
        ["ABT", "Ethereum", 35, 25, "Bitkub"],
        ["MANA", "Ethereum", 5.52000000, 25, "Bitkub"],
        ["BAND", "Band Protocol", 0.01, 1, "Bitkub"],
        ["GLM", "Ethereum", 13.00000000, 25, "Bitkub"],
        ["FTT", "Ethereum", 0.14000000, 25, "Bitkub"],
        ["GF", "Ethereum", 10, 25, "Bitkub"],
        ["CHZ", "Ethereum", 17.00000000, 25, "Bitkub"],
        ["LYXE", "Ethereum", 1.5, 25, "Bitkub"],
        ["SOL", "Solana", 0.00800000, 5, "Bitkub"],
        ["FTM", "Fantom", 0.10000000, 5, "Bitkub"],
        ["LUNC", "Terra Classic", 70.00000000, 5, "Bitkub"],
        ["APE", "Ethereum", 0.80000000, 25, "Bitkub"],
        ["XTZ", "Tezos", 0.1, 1, "Bitkub"],
        ["SOLO", "Ripple", 1.0, 30, "Bitkub"],
        ["OP", "Optimism", 0.5, 1, "Bitkub"],
        ["KUB", "Ethereum", 2.70000000, 25, "Bitkub"],
        ["KUB", "Bitkub Chain", 0.01, 25, "Bitkub"],
        ["COMP", "Ethereum", 0.07500000, 25, "Bitkub"],
        ["XRP", "Ripple", 0.20000000, 1, "Bitkub"],
        ["ALPHA", "Ethereum", 31.00000000, 25, "Bitkub"],
        ["AAVE", "Ethereum", 0.04500000, 25, "Bitkub"],
        ["BCH", "Bitcoin Cash", 0.00080000, 3, "Bitkub"],
        ["SCRT", "Secret Network", 0.1, 1, "Bitkub"],
        ["YFI", "Ethereum", 0.00046000, 25, "Bitkub"],
        ["OMG", "Ethereum", 2.27000000, 25, "Bitkub"],
        ["KSM", "Kusama", 0.01, 1, "Bitkub"],
        ["ZRX", "Ethereum", 14.00000000, 25, "Bitkub"],
        ["DAI", "Ethereum", 10.00000000, 25, "Bitkub"],
        ["SNX", "Ethereum", 8.76000000, 25, "Bitkub"],
        ["BOBA", "Ethereum", 13.00000000, 25, "Bitkub"],
        ["GT", "Ethereum", 9.5, 25, "Bitkub"],
        ["DYDX", "Ethereum", 28.00000000, 25, "Bitkub"],
        ["TRX", "Tron", 1.0, 1, "Bitkub"],
        ["GAL", "Ethereum", 1.7600000, 25, "Bitkub"],
        ["1INCH", "Ethereum", 6.96, 25, "Bitkub"],
        ["CVC", "Ethereum", 30.00000000, 25, "Bitkub"],
        ["SIX", "Stellar", 1, 1, "Bitkub"],
        ["LTC", "Litecoin", 0.001, 4, "Bitkub"],
        ["BAT", "Ethereum", 12.00000000, 25, "Bitkub"],
        ["ZIL", "Zilliqa", 0.2, 1, "Bitkub"],
        ["DOT", "Polkadot", 0.08000000, 1, "Bitkub"],
        ["SUSHI", "Ethereum", 2.38000000, 25, "Bitkub"],
        ["BNB", "BNB Smart Chain", 0.00050000, 25, "Bitkub"],
        ["SNT", "Ethereum", 130.00000000, 25, "Bitkub"],
        ["OCEAN", "Ethereum", 21.00000000, 25, "Bitkub"],
        ["SGB", "Songbird", 0.01000000, 30, "Bitkub"],
        ["IMX", "Ethereum", 6.37000000, 25, "Bitkub"],
        ["ENS", "Ethereum", 0.22000000, 25, "Bitkub"],
        ["GRT", "Ethereum", 44.00000000, 25, "Bitkub"],
        ["MATIC", "Polygon", 0.1, 5, "Bitkub"],
        ["HBAR", "Hedera Hashgraph", 0.80000000, 1, "Bitkub"],
        ["CELO", "Celo", 0.001, 1, "Bitkub"],
        ["ALGO", "Algorand", 0.01, 1, "Bitkub"],
        ["BUSD", "BNB Smart Chain", 0.5, 15, "Bitkub"],
        ["LUNA", "Terra 2.0", 0.05000000, 5, "Bitkub"],
        ["ETH", "Ethereum", 0.00076800, 25, "Bitkub"],
        ["CRV", "Ethereum", 4.23000000, 25, "Bitkub"],
        ["LINK", "Ethereum", 0.48000000, 25, "Bitkub"],
        ["KNC", "Ethereum", 4, 25, "Bitkub"],
        ["XLM", "Stellar", 0.02, 1, "Bitkub"],
        ["BAL", "Ethereum", 0.55000000, 25, "Bitkub"],
        ["NEAR", "NEAR Protocol", 0.01, 1, "Bitkub"],
        ["POW", "Ethereum", 18.00000000, 25, "Bitkub"],
        ["USDT", "BNB Smart Chain", 0.8, 25, "Bitkub"],
        ["USDT", "Ethereum", 3.2, 25, "Bitkub"],
        ["USDC", "Ethereum", 3.20000000, 25, "Bitkub"],
        ["DON", "IOST", 0.82000000, 1, "Bitkub"],
        ["WAN", "Wanchain", 0.1, 30, "Bitkub"],
        ["UNI", "Ethereum", 0.54000000, 25, "Bitkub"],
        ["GALA", "Ethereum", 88.00000000, 25, "Bitkub"],
        ["ILV", "Ethereum", 0.05700000, 25, "Bitkub"],
        ["EXFI", "Songbird", 0.1, 30, "Bitkub"],
        ["AVAX", "Avalanche C-Chain", 0.00800000, 12, "Bitkub"],
        ["LRC", "Ethereum", 23.0, 0, "Bitkub"],
        ["ATOM", "Cosmos", 0.005, 10, "Bitkub"],
        ["LDO", "Ethereum", 1.97, 25, "Bitkub"],
        ["STG", "Ethereum", 5.94, 25, "Bitkub"],
        ["ADA","Cardano", 10.000000, 0.800000, "Satang Pro"],
        ["AION","Aion",0.20000000,0.10000000,"Satang Pro"],
        ["ALGO", "Algorand", 10.000000, 0.008000, "Satang Pro"],
        ["ANKR", "BNB Beacon Chain", 10.00000000, 5.47000000, "Satang Pro"],
        arpaARPA
        ARPA Chain
        Ethereum(ERC20)		12		214.00000000	107.00000000, "Satang Pro"],
        atomATOM
        Cosmos
        Cosmos		15		0.010000	0.004000, "Satang Pro"],
        avaxAVAX
        Avalanche
        AVAX C-Chain		12		0.10000000	0.00800000,"Satang Pro"],
        BNB Smart Chain(BEP20)		15		0.01000000	0.00510000,"Satang Pro"],
        Avalanche		1		0.10000000	0.01000000,"Satang Pro"],
        bandBAND
        BAND
            BAND		15		0.020000	0.010000, "Satang Pro"],
        batBAT
        Basic Attention Token
        Ethereum(ERC20)		12		24.00000000	12.00000000,"Satang Pro"],
        bchBCH
        Bitcoin Cash
        Bitcoin Cash		6		0.00200000	0.00080000,"Satang Pro"],
        bchaBCHA
        Bitcoin Cash ABC
        0 - -
        beamBEAM
        Beam
            Beam		70		0.20000000	0.10000000, "Satang Pro"],
        betaBETA
        Beta Finance
        Ethereum(ERC20)		12		86.00000000	43.00000000,"Satang Pro"],
        BNB Smart Chain(BEP20)		15		2.26000000	1.13000000,"Satang Pro"],
        bnbBNB
        BNB
        BNB Smart Chain(BEP20)		15		0.01000000	0.00050000,"Satang Pro"],
        BNB Beacon Chain(BEP2)		1		0.01000000	0.00050000,"Satang Pro"],
        btcBTC
        Bitcoin
        Bitcoin		2		0.00100000	0.00020000,"Satang Pro"],
        BNB Smart Chain(BEP20)		15		0.00000960	0.00000480,"Satang Pro"],
        btgBTG
        Bitcoin Gold
        Bitcoin Gold		70		0.00200000	0.00100000,"Satang Pro"],
        bttBTT
        BitTorrent
        0 - -
        busdBUSD
        BUSD
        Ethereum(ERC20)		12		40.00000000	3.90000000,"Satang Pro"],
        BNB Smart Chain(BEP20)		15		10.00000000	0.00000000,"Satang Pro"],
        cakeCAKE
        PancakeSwap
            BNB Smart Chain(BEP20)		15		0.04200000	0.02100000, "Satang Pro"],
        celrCELR
        Celer Network
        Ethereum(ERC20)		12		490.00000000	245.00000000,"Satang Pro"],
        chzCHZ
        Chiliz
        BNB Beacon Chain(BEP2)		1		1.50000000	0.75000000,"Satang Pro"],
        cocosCOCOS
        Cocos-BCX
        0 - -
        cosCOS
        Contentos
        BNB Beacon Chain(BEP2)		1		56.00000000	28.00000000,"Satang Pro"],
        cpyCPY
        Copytrack
            Ethereum(ERC20)		0		0.00000000	0.00000000, "Satang Pro"],
        ctxcCTXC
        Cortex
        Cortex		257		0.20000000	0.10000000,"Satang Pro"],
        cvcCVC
        Civic
        Ethereum(ERC20)		12		60.00000000	30.00000000,"Satang Pro"],
        daiDAI
        Dai
        Ethereum(ERC20)		12		30.00000000	10.00000000,"Satang Pro"],
        dashDASH
        Dash
        Dash		25		0.00400000	0.00160000,"Satang Pro"],
        dogeDOGE
        Dogecoin
        dogecoin		50		80.00000000	4.00000000,"Satang Pro"],
        dotDOT
        Polkadot
        Polkadot		3		1.50000000	0.08000000,"Satang Pro"],
        duskDUSK
        Dusk Network
            BNB Beacon Chain(BEP2)		1		2.44000000	1.22000000, "Satang Pro"],
        dydxDYDX
        DYDX
        Ethereum(ERC20)		12		56.00000000	28.00000000,"Satang Pro"],
        elecELEC
        Ethereum(ERC20)		0		0.00000000	0.00000000,"Satang Pro"],
        enjENJ
        Enjin Coin
        Ethereum(ERC20)		12		16.00000000	8.25000000,"Satang Pro"],
        eosEOS
        EOS
        EOS		1		0.2000	0.0800,"Satang Pro"],
        erdERD
        Elrond
            BNB Beacon Chain(BEP2)		1		3.00000000	0.00000000, "Satang Pro"],
        etcETC
        Ethereum Classic
        Ethereum Classic		500		0.02000000	0.00800000,"Satang Pro"],
        ethETH
        Ethereum
        Ethereum(ERC20)		12		0.00980000	0.00076800,"Satang Pro"],
        BNB Smart Chain(BEP20)		15		0.00012000	0.00006200,"Satang Pro"],
        etpETP
        Meteverse
            ETP		0		0.00000000	0.00000000, "Satang Pro"],
        fetFET
        Fetch.AI
        Ethereum(ERC20)		12		88.00000000	44.00000000,"Satang Pro"],
        flowFLOW
        Flow
        Flow		20		2.70000000	0.01000000,"Satang Pro"],
        ftmFTM
        Fantom
        BNB Beacon Chain(BEP2)		1		1.36000000	0.68000000,"Satang Pro"],
        fttFTT
        FTX Token
        Ethereum(ERC20)		12		0.28000000	0.14000000,"Satang Pro"],
        funFUN
        FunFair
        Ethereum(ERC20)		12		998.00000000	499.00000000,"Satang Pro"],
        hbarHBAR
        Hedera Hashgraph
        Hedera Hashgraph		1		2.00000000	0.80000000
        hcHC
        HyperCash
        HyperCash		30		0.01000000	0.00500000
        hotHOT
        Holo
        Ethereum(ERC20)		12		3, 692.00000000	1, 846.00000000
        icpICP
        Internet Computer
        Internet Computer		1		0.00100000	0.00030000
        icxICX
        ICON
        ICON		3		0.04000000	0.02000000
        iostIOST
        IOST
        IOST		80		2.00000000	1.00000000
        iotaIOTA
        MIOTA
        MIOTA		1		69.000000	0.500000
        iotxIOTX
        IoTeX
        IoTeX		1		1.00	0.10
        jfinJFIN
        JFIN Coin
        Ethereum(ERC20)		0		17.00000000	8.50000000
        kavaKAVA
        Kava
        KAVA		1		2.000000	0.010000
        kncKNC
        Kyber Network
        Ethereum(ERC20)		12		16.90000000	8.45000000
        linkLINK
        ChainLink
        Ethereum(ERC20)		12		0.96000000	0.48000000
        lskLSK
        Lisk
        Lisk		1		0.20000000	0.10000000
        ltcLTC
        Litecoin
        Litecoin		4		0.00200000	0.00100000
        ltoLTO
        LTO Network
        Ethereum(ERC20)		12		82.00000000	41.00000000
        lunaLUNA
        Terra
        Terra		1		10.000000	0.050000
        luncLUNC
        Terra Classic
        Terra Classic		1		30, 000.000000	2.266000
        manaMANA
        Decentraland
        Ethereum(ERC20)		12		11.00000000	5.52000000
        maticMATIC
        MATIC Network
        Ethereum(ERC20)		12		19.44000000	9.72000000
        mblMBL
        MovieBloc
        Ontology		5		7.06000000	3.53000000
        mcoMCO
        MCO
        0 - -
        mftMFT
        Mainframe
        Ethereum(ERC20)		12		1, 476.00000000	738.00000000
        nanoNANO
        NANO
        0 - -
        neoNEO
        NEO
        Neo Legacy		5		1.00000000	0.00000000
        nknNKN
        NKN
        Ethereum(ERC20)		12		82.00000000	41.00000000
        npxsNPXS
        Pundi X
        0 - -
        nulsNULS
        Nuls
        Nuls		30		0.02000000	0.01000000
        ognOGN
        OriginToken
        Ethereum(ERC20)		12		50.00000000	25.00000000
        omgOMG
        OmiseGO
        Ethereum(ERC20)		12		5.80000000	2.90000000
        oneONE
        Harmony
        Harmony		12		60.00000000	0.10000000
        ongONG
        Ontology Gas
        Ontology		5		0.06800000	0.03400000
        ontONT
        Ontology
        Ontology		5		2.00000000	1.00000000
        paxPAX
        Paxos Standard
        0 - -
        paxgPAXG
        PAX Gold
        Ethereum(ERC20)		12		0.00600000	0.00200000
        perlPERL
        Perlin
        Ethereum(ERC20)		12		372.00000000	186.00000000
        powrPOWR
        Power Ledger
        Ethereum(ERC20)		12		138.00000000	69.00000000
        qtumQTUM
        Qtum
        Qtum		24		0.020000	0.010000
        renREN
        Ren
        Ethereum(ERC20)		12		56.00000000	28.00000000
        rpxRPX
        Red Pulse Phoenix
        NEP5		0		0.00000000	0.00000000
        rvnRVN
        Ravencoin
        Ravencoin		200		2.00000000	1.00000000
        sandSAND
        The Sandbox
        Ethereum(ERC20)		12		8.34000000	4.17000000
        solSOL
        Solana
        Solana		1		0.02000000	0.00800000
        stptSTPT
        Standard Tokenization Protocol
        Ethereum(ERC20)		12		174.00000000	87.00000000
        stratSTRAT
        Stratis
        0 - -
        stxSTX
        Blockstack
        Stacks		8		5.0000	1.5000
        tfuelTFUEL
        Theta Fuel
        Theta Token		10		5.02000000	2.51000000
        thetaTHETA
        Theta Token
        Theta Token		10		0.24000000	0.12000000
        tomoTOMO
        TomoChain
        TomoChain		150		0.02000000	0.01000000
        troyTROY
        Troy
        BNB Beacon Chain(BEP2)		1		90.00000000	45.00000000
        trxTRX
        TRON
        Tron(TRC20)		1		2.000000	1.000000
        tusdTUSD
        TrueUSD
        Ethereum(ERC20)		12		30.00000000	6.00000000
        uniUNI
        Uniswap
        Ethereum(ERC20)		12		1.08000000	0.54000000
        BNB Smart Chain(BEP20)		15		0.02800000	0.01400000
        usdcUSDC
        USD Coin
        Ethereum(ERC20)		12		50.000000	3.200000
        usdtUSDT
        TetherUS
        Ethereum(ERC20)		12		50.000000	3.200000
        Tron(TRC20)		1		10.000000	0.800000
        BNB Smart Chain(BEP20)		15		10.000000	0.290000
        vetVET
        VeChain
        VeChain		12		40.00000000	20.00000000
        viteVITE
        VITE
        VITE		150		2.00000000	1.00000000
        wanWAN
        Wanchain
        Wanchain		30		0.20000000	0.10000000
        wavesWAVES
        Waves
        Waves		90		0.00320000	0.00160000
        waxWAX
        Ethereum(ERC20)		0		0.00000000	0.00000000
        winWIN
        WINK
        Tron(TRC20)		1		1, 194.000000	597.000000
        wrxWRX
        WazirX
        BNB Beacon Chain(BEP2)		1		1.54000000	0.77000000
        xlmXLM
        Stellar Lumens
        Stellar Network		1		40.0000000	0.0200000
        xmrXMR
        Monero
        Monero		3		0.00020000	0.00010000
        xrpXRP
        Ripple
        Ripple		1		30.000000	0.200000
        xtzXTZ
        Tezos
        Tezos		4		1.000000	0.100000
        xzcXZC
        Firo
        Firo		3		1.00010000	0.00010000
        zecZEC
        Zcash
        Zcash		20		0.01000000	0.00100000
        zilZIL
        Zilliqa
        Zilliqa		1		0.40000000	0.20000000
        zrxZRX
        0x
        Ethereum(ERC20)		12		28.00000000	14.00000000
    ]

    for i in obj:
        symbol = i[0]
        network = i[1]
        fee = i[2]
        block = i[3]
        description = i[4]
        url = "http://localhost:4041/api/v1/asset/fee"
        payload = f'asset_id={symbol}&block_chain_id={network}&fee={fee}&block_previous={block}&description={description}&is_active=true'
        headers = {
            'Authorization': 'Bearer enjtpZn4gVX8yCYKwZHWxOmo9-cQusziOfl60xgXNG2Wzzh6XM7VpXRaqpQt',
            'Content-Type': 'application/x-www-form-urlencoded'
        }

        response = requests.request("POST", url, headers=headers, data=payload)
        # print(response.json())
        print(
            f"Symbol: {symbol} Network: {network} Description: {description} Status: {response.status_code}")


if __name__ == "__main__":
    main()
    sys.exit(0)
