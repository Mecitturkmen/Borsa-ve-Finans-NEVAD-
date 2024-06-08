import yfinance as yf
from stock_indicators.indicators.common.quote import Quote
from stock_indicators import indicators
from datetime import datetime
from datetime import timedelta
import pandas as pd
import os
from tqdm import tqdm
import decimal

# TimedeltaIndex uyarılarını devre dışı bırak
import warnings
warnings.filterwarnings('ignore', message="The 'unit' keyword in TimedeltaIndex construction is deprecated", category=FutureWarning)

# Dosya yolunu belirtin
dosya_klasoru = "C:/Users/q/Desktop/bılancolar/"

# Dosya klasöründeki tüm dosya isimlerini al
dosya_isimleri = os.listdir(dosya_klasoru)

# Tüm sinyalleri içeren DataFrame'i oluştur
all_signals = pd.DataFrame(columns=["Ticker", "RSI", "MACD","ADX","ADL","Alligator","ALMA","Aroon","ATR","ATR Stop","Awesome Oscillator","Basic Quotes",
                                    "Bollinger Bandı","BOP","CCI","Chaikin Oscillator","CHOP","CMF","CMO","Connors RSI","Correlation","Elder Ray","EMA",
                                    "EPMA","Fisher Transform","Force Index","Fractal","Gator Oscillator","HMA","HT Trendline","Hurst","KAMA","Keltner Channel",
                                    "KVO","MA Envelopes","MAMA","MFI","OBV","PMO","PVO","ROC","Slope","SMA","SMI","STARC-Bands","STC","STDEV","STDEV-Channels",
                                    "Stochastic RSI","T3","TEMA","TR","TRIX","TSI","Ulcer Index","Ultimate Oscillator","Volatility Stop","Vortex","VWAP","VWMA",
                                    "Williams %R","WMA"])

# Her bir dosya için RSI ve MACD sinyallerini bul
for dosya_adi in tqdm(dosya_isimleri, desc="Hisse Senetleri İşleniyor"):
    # Dosya adının sonuna ".IS" ekleyerek ticker oluştur
    ticker = dosya_adi.split('.')[0] + '.IS'

    # Hisse verilerini indir
    today = datetime.now().date()
    data = yf.download(ticker, start="2022-01-01", end=today)

    if not data.empty:
        # Verileri Quote objesine dönüştür
        quotes = [Quote(date=row.Index, open=row.Open, high=row.High, low=row.Low, close=row.Close, volume=row.Volume) for row in data.itertuples()]

        # RSI hesapla
        rsi_results = indicators.get_rsi(quotes, lookback_periods=14)

        # MACD hesapla
        macd_results = indicators.get_macd(quotes)

        # ADX hesapla
        adx_results = indicators.get_adx(quotes)

        # ADL hesapla
        adl_results = indicators.get_adl(quotes)

        # Alligator hesapla
        alligator_results = indicators.get_alligator(quotes)

        # ALMA hesapla
        alma_results = indicators.get_alma(quotes)

        # Aroon hesapla
        aroon_results = indicators.get_aroon(quotes)

        # ATR hesapla
        atr_results = indicators.get_atr(quotes)

        # ATR Stop hesapla
        atr_stop_results = indicators.get_atr_stop(quotes)

        # Awesome Oscillator hesapla
        awesome_results = indicators.get_awesome(quotes)

        # Basic Quotes hesapla
        basic_quotes_results = indicators.get_basic_quote(quotes)

        # Bollinger Bandı hesapla
        bollinger_results = indicators.get_bollinger_bands(quotes)

        # BOP hesapla
        bop_results = indicators.get_bop(quotes)

        # CCI hesapla
        cci_results = indicators.get_cci(quotes)

        # Chaikin Oscillator hesapla
        chaikin_osc_results = indicators.get_chaikin_osc(quotes)

        # CHOP (Choppiness Index) hesapla
        chop_results = indicators.get_chop(quotes)

        # CMF (Chaikin Money Flow) hesapla
        cmf_results = indicators.get_cmf(quotes)

        # CMO (Chande Momentum Oscillator) hesapla
        cmo_results = indicators.get_cmo(quotes, lookback_periods = 20)

        # Connors RSI hesapla
        connors_rsi_results = indicators.get_connors_rsi(quotes)

        # Correlation hesapla
        correlation_results = indicators.get_correlation(quotes, quotes, lookback_periods = 20)

        # Elder Ray hesapla
        elder_ray_results = indicators.get_elder_ray(quotes, lookback_periods=13)

        # EMA hesapla
        ema_results = indicators.get_ema(quotes, lookback_periods=20)

        # EPMA hesapla
        epma_results = indicators.get_epma(quotes, lookback_periods=20)

        # Fisher Transform hesapla
        fisher_transform_results = indicators.get_fisher_transform(quotes, lookback_periods=10)

        # Force Index hesapla
        force_index_results = indicators.get_force_index(quotes, lookback_periods=13)

        # Fractal hesapla
        fractal_results = indicators.get_fractal(quotes)

        # Gator Oscillator hesapla
        gator_results = indicators.get_gator(quotes)

        # HMA hesapla
        hma_results = indicators.get_hma(quotes, lookback_periods=20)

        # HT Trendline hesapla
        ht_trendline_results = indicators.get_ht_trendline(quotes)

        # Hurst Exponent hesapla
        hurst_results = indicators.get_hurst(quotes, lookback_periods=20)

        # KAMA hesapla
        kama_results = indicators.get_kama(quotes)

        # Keltner Channels hesapla
        keltner_results = indicators.get_keltner(quotes, ema_periods=20, multiplier=2)

        # KVO hesapla
        kvo_results = indicators.get_kvo(quotes)

        # MA Envelopes hesapla
        ma_envelopes_results = indicators.get_ma_envelopes(quotes, lookback_periods=20, percent_offset=5)

        # MAMA hesapla
        mama_results = indicators.get_mama(quotes)

        # MFI hesapla
        mfi_results = indicators.get_mfi(quotes, lookback_periods=14)

        # OBV hesapla
        obv_results = indicators.get_obv(quotes)

        # PMO hesapla
        pmo_results = indicators.get_pmo(quotes)

        # PVO hesapla
        pvo_results = indicators.get_pvo(quotes)

        # ROC hesapla
        roc_results = indicators.get_roc(quotes, lookback_periods=14)

        # Slope hesapla
        slope_results = indicators.get_slope(quotes, lookback_periods=14)

        # SMA hesapla
        sma_results = indicators.get_sma(quotes, lookback_periods=14)

        # SMI hesapla
        smi_results = indicators.get_smi(quotes, lookback_periods=14)

        # Get-STARC-Bands hesapla
        starc_bands_results = indicators.get_starc_bands(quotes)

        # Get-STC hesapla
        stc_results = indicators.get_stc(quotes)

        # Get-STDEV hesapla
        stdev_results = indicators.get_stdev(quotes, lookback_periods=14)

        # Get-STDEV hesapla
        stdev_channels_results = indicators.get_stdev_channels(quotes, lookback_periods=14)

        # Stokastik RSI hesapla
        stoch_rsi_results = indicators.get_stoch_rsi(quotes, rsi_periods=14, stoch_periods=14, signal_periods=3)

        # T3 göstergesini hesapla
        t3_results = indicators.get_t3(quotes, lookback_periods=5, volume_factor=0.7)

        # TEMA göstergesini hesapla
        tema_results = indicators.get_tema(quotes, lookback_periods=14)

        # TR göstergesini hesapla
        tr_results = indicators.get_tr(quotes)

        # TRIX göstergesini hesapla
        trix_results = indicators.get_trix(quotes, lookback_periods=14)

        # TSI göstergesini hesapla
        tsi_results = indicators.get_tsi(quotes)

        # Ulcer Index göstergesini hesapla
        ulcer_index_results = indicators.get_ulcer_index(quotes, lookback_periods=14)

        # Ultimate Oscillator göstergesini hesapla
        ultimate_results = indicators.get_ultimate(quotes, short_periods=7, middle_periods=14, long_periods=28)

        # Örnek olarak Volatility Stop için:
        volatility_stop_results = indicators.get_volatility_stop(quotes, lookback_periods=14, multiplier=2)

        # Vortex göstergesini hesapla
        vortex_results = indicators.get_vortex(quotes, lookback_periods=14)

        # VWAP göstergesini hesapla
        vwap_results = indicators.get_vwap(quotes)

        # VWMA göstergesini hesapla
        vwma_results = indicators.get_vwma(quotes,lookback_periods=14)

        # Williams %R göstergesini hesapla
        williams_r_results = indicators.get_williams_r(quotes,lookback_periods=14)

        # WMA göstergesini hesapla
        wma_results = indicators.get_wma(quotes, lookback_periods=14)

        # En son geçerli RSI ve MACD sinyalini bul
        latest_rsi_signal = None
        latest_macd_signal = None
        latest_adx_signal = None
        latest_adl_signal = None
        latest_alligator_signal = None
        latest_alma_signal = None
        latest_aroon_signal = None
        latest_atr_signal = None
        latest_atr_stop_signal = None
        latest_awesome_signal = None
        latest_basic_quotes_signal = None
        latest_bollinger_signal = None
        latest_bop_signal = None
        latest_cci_signal = None
        latest_chaikin_osc_signal = None
        latest_chop_signal = None
        latest_cmf_signal = None
        latest_cmo_signal = None
        latest_connors_rsi_signal = None
        latest_correlation_signal = None
        latest_elder_ray_signal = None
        latest_ema_signal = None
        latest_epma_signal = None
        latest_fisher_transform_signal = None
        latest_force_index_signal = None
        latest_fractal_signal = None
        latest_gator_signal = None
        latest_hma_signal = None
        latest_ht_trendline_signal = None
        latest_hurst_signal = None
        latest_kama_signal = None
        latest_keltner_signal = None
        latest_kvo_signal = None
        latest_ma_envelopes_signal = None
        latest_mama_signal = None
        latest_mfi_signal = None
        latest_obv_signal = None
        latest_pmo_signal = None
        latest_pvo_signal = None
        latest_roc_signal = None
        latest_slope_signal = None
        latest_sma_signal = None
        latest_smi_signal = None
        latest_starc_bands_signal = None
        latest_stc_signal = None
        latest_stdev_signal = None
        latest_stdev_channels_signal= None
        latest_stoch_rsi_signal = None
        latest_t3_signal = None
        latest_tema_signal = None
        latest_tr_signal = None
        latest_trix_signal = None
        latest_tsi_signal = None
        latest_ulcer_index_signal = None
        latest_ultimate_signal = None
        latest_vwap = None
        latest_vortex_signal = None
        latest_volatility_stop_signal = None
        latest_vwma = None
        latest_williams_r = None
        latest_wma = None


        if wma_results:
            latest_wma = wma_results[-1].wma

        # Alım satım sinyali
        latest_wma_signal = None
        if latest_wma:
            # Güncel kapanış fiyatını al
            latest_close = quotes[-1].close
            # Alım veya satım sinyali üret
            if latest_close > latest_wma:
                latest_wma_signal = "Al"
            else:
                latest_wma_signal = "Sat"


        if williams_r_results:
            latest_williams_r = williams_r_results[-1].williams_r

        # Alım satım sinyali
        latest_williams_r_signal = None
        if latest_williams_r:
            # Williams %R değeri -20'nin üzerindeyse alım, -80'in altındaysa satış sinyali verebilir
            if latest_williams_r < -80:
                latest_williams_r_signal = "Al"
            elif latest_williams_r > -20:
                latest_williams_r_signal = "Sat"

        if vwma_results:
            latest_vwma = vwma_results[-1].vwma

        # Alım satım sinyali
        latest_vwma_signal = None
        if latest_vwma:
            # Güncel kapanış fiyatını al
            latest_close = quotes[-1].close
            # Alım veya satım sinyali üret
            if latest_close > latest_vwma:
                latest_vwma_signal = "Al"
            else:
                latest_vwma_signal = "Sat"

        # En son geçerli VWAP değerini al
        latest_vwap = None
        if vwap_results:
            latest_vwap = vwap_results[-1].vwap

        # Alım satım sinyali
        latest_vwap_signal = None
        if latest_vwap:
            # Güncel kapanış fiyatını al
            latest_close = quotes[-1].close
            # Alım veya satım sinyali üret
            if latest_close > latest_vwap:
                latest_vwap_signal = "Al"
            else:
                latest_vwap_signal = "Sat"


        # En son geçerli Vortex sinyali bul
        for result in reversed(vortex_results):
            if result.pvi is not None:
                # Vortex sonuçlarını kullanırken Quote nesnelerini kullanın
                quote = next((q for q in quotes if q.date == result.date), None)
                if quote:
                    # Burada sinyal üretmek için kendi kriterlerinize göre bir mantık oluşturabilirsiniz
                    # Örnek olarak: Vortex üzerindeki bir çizgiyi geçtiğinde alım yapabilirsiniz
                    if result.pvi > 1.0:
                        signal = "Al"
                    else:
                        signal = "Sat"
                    latest_vortex_signal = (result.date, result.pvi, signal)
                    break

        # En son geçerli Volatility Stop sinyali bul
        for result in reversed(volatility_stop_results):
            if result.is_stop is not None:
                # Volatility Stop sonuçlarını kullanırken Quote nesnelerini kullanın
                quote = next((q for q in quotes if q.date == result.date), None)
                if quote:
                    # Burada sinyal üretmek için kendi kriterlerinize göre bir mantık oluşturabilirsiniz
                    # Örnek olarak: Fiyat Volatility Stop seviyesinin üzerindeyse alım yapılabilir
                    if quote.close > result.is_stop:
                        signal = "Al"
                    else:
                        signal = "Sat"
                    latest_volatility_stop_signal = (result.date, result.is_stop, signal)
                    break

        for result in reversed(ultimate_results):
            if result.ultimate is not None:
                # Ultimate Oscillator sonuçlarını kullanırken Quote nesnelerini kullanın
                quote = next((q for q in quotes if q.date == result.date), None)
                if quote:
                    # Burada sinyal üretmek için kendi kriterlerinize göre bir mantık oluşturabilirsiniz
                    if result.ultimate > 50:
                        signal = "Al"
                    else:
                        signal = "Sat"
                    latest_ultimate_signal = (result.date, result.ultimate, signal)
                    break

        for result in reversed(ulcer_index_results):
            if result.ui is not None:
                # Ulcer Index sonuçlarını kullanırken Quote nesnelerini kullanın
                quote = next((q for q in quotes if q.date == result.date), None)
                if quote:
                    # Burada sinyal üretmek için kendi kriterlerinize göre bir mantık oluşturabilirsiniz
                    if result.ui > 50:
                        signal = "Al"
                    else:
                        signal = "Sat"
                    latest_ulcer_index_signal = (result.date, result.ui, signal)
                    break

        # En son geçerli TSI sinyali bul
        for result in reversed(tsi_results):
            if result.tsi is not None:
                # TSI sonuçlarını kullanırken Quote nesnelerini kullanın
                quote = next((q for q in quotes if q.date == result.date), None)
                if quote:
                    # TSI sonucunun kapanış fiyatını al
                    close = quote.close
                    # Burada sinyal üretmek için kendi kriterlerinize göre bir mantık oluşturabilirsiniz
                    if result.tsi > 0:
                        signal = "Al"
                    else:
                        signal = "Sat"
                    latest_tsi_signal = (result.date, close, result.tsi, signal)
                    break

        # En son geçerli TRIX sinyali bul
        for result in reversed(trix_results):
            if result.trix is not None:
                # TRIX sonuçlarını kullanırken Quote nesnelerini kullanın
                quote = next((q for q in quotes if q.date == result.date), None)
                if quote:
                    # TRIX sonucunun kapanış fiyatını al
                    close = quote.close
                    # Burada sinyal üretmek için kendi kriterlerinize göre bir mantık oluşturabilirsiniz
                    if result.trix > 0:
                        signal = "Al"
                    else:
                        signal = "Sat"
                    latest_trix_signal = (result.date, close, result.trix, signal)
                    break

        for result in reversed(tr_results):
            if result.tr is not None:
                quote = next((q for q in quotes if q.date == result.date), None)
                if quote:
                    close = quote.close
                    # TR sinyalini örnek olarak değerlendiriyoruz
                    # Burada alım veya satım sinyali üretmek için kendi kriterlerinize göre bir mantık oluşturabilirsiniz
                    if result.tr > close:
                        signal = "Al"
                    else:
                        signal = "Sat"
                    latest_tr_signal = (result.date, close, result.tr, signal)
                    break

        # En son geçerli RSI sinyali bul
        for result in reversed(rsi_results):
            if result.rsi is not None:
                if result.rsi < 30:
                    signal = "Al"
                elif result.rsi > 70:
                    signal = "Sat"
                else:
                    signal = "Bekle"
                quote = next((q for q in quotes if q.date == result.date), None)
                if quote:
                    latest_rsi_signal = (result.date, quote.close, result.rsi, signal)
                    break

        # En son geçerli MACD sinyali bul
        for result in reversed(macd_results):
            if result.macd is not None and result.signal is not None:
                if result.macd > result.signal:
                    signal = "Al"
                else:
                    signal = "Sat"
                quote = next((q for q in quotes if q.date == result.date), None)
                if quote:
                    latest_macd_signal = (result.date, quote.close, result.macd, result.signal, signal)
                    break

        # En son geçerli ADX sinyali bul
        for result in reversed(adx_results):
            if result.adx is not None:
                if result.adx > 25:
                    signal = "Güçlü Trend"
                else:
                    signal = "Zayıf Trend"
                quote = next((q for q in quotes if q.date == result.date), None)
                if quote:
                    latest_adx_signal = (result.date, quote.close, result.adx, signal)
                    break

        # En son geçerli ADL sinyali bul
        for result in reversed(adl_results):
            if result.adl is not None:
                adl_signal = "N/A"  # ADL için genellikle belirli bir al-sat sinyali kullanılmaz
                quote = next((q for q in quotes if q.date == result.date), None)
                if quote:
                    latest_adl_signal = (result.date, quote.close, result.adl, adl_signal)
                    
                    # Örnek al-sat stratejisi: ADL'nin fiyat hareketleriyle tersine dönme işaretleri
                    if result.adl > 0:  # Örnek alım sinyali
                        adl_signal = "Al"
                    elif result.adl < 0:  # Örnek satım sinyali
                        adl_signal = "Sat"
                    
                    latest_adl_signal = (result.date, quote.close, result.adl, adl_signal)
                    break

        # En son geçerli Alligator sinyali bul
        for result in reversed(alligator_results):
            if result.jaw is not None and result.teeth is not None and result.lips is not None:
                if result.jaw > result.teeth and result.teeth > result.lips:
                    signal = "Sat"
                elif result.jaw < result.teeth and result.teeth < result.lips:
                    signal = "Al"
                else:
                    signal = "Bekle"
                quote = next((q for q in quotes if q.date == result.date), None)
                if quote:
                    latest_alligator_signal = (result.date, quote.close, result.jaw, result.teeth, result.lips, signal)
                    break

        # En son geçerli ALMA sinyali bul
        for result in reversed(alma_results):
            if result.alma is not None:
                alma_signal = "N/A"  # ALMA için genellikle belirli bir al-sat sinyali kullanılmaz
                quote = next((q for q in quotes if q.date == result.date), None)
                if quote:
                    latest_alma_signal = (result.date, quote.close, result.alma, alma_signal)
                    
                    # Örnek al-sat stratejisi: ALMA çizgisi ile fiyat arasındaki ilişkiyi kullanma
                    if quote.close > result.alma:  # Fiyat ALMA'nın üzerindeyse alım sinyali
                        alma_signal = "Al"
                    elif quote.close < result.alma:  # Fiyat ALMA'nın altındaysa satım sinyali
                        alma_signal = "Sat"
                    
                    latest_alma_signal = (result.date, quote.close, result.alma, alma_signal)
                    break

        # En son geçerli Aroon sinyali bul
        for result in reversed(aroon_results):
            if result.aroon_up is not None and result.aroon_down is not None:
                if result.aroon_up > result.aroon_down:
                    signal = "Al"
                else:
                    signal = "Sat"
                quote = next((q for q in quotes if q.date == result.date), None)
                if quote:
                    latest_aroon_signal = (result.date, quote.close, result.aroon_up, result.aroon_down, signal)
                    break

        # En son geçerli ATR sinyali bul
        for result in reversed(atr_results):
            if result.atr is not None:
                signal = "N/A"  # ATR genellikle volatilite ölçmek için kullanılır, al-sat sinyali olarak kullanılmaz
                quote = next((q for q in quotes if q.date == result.date), None)
                if quote:
                    latest_atr_signal = (result.date, quote.close, result.atr, signal)
                    break

        # En son geçerli ATR Stop sinyali bul
        for result in reversed(atr_stop_results):
            try:
                if result.atr_stop is not None:
                    signal = "N/A"  # ATR Stop için genellikle belirli bir al-sat sinyali kullanılmaz
                    quote = next((q for q in quotes if q.date == result.date), None)
                    if quote:
                        latest_atr_stop_signal = (result.date, quote.close, result.atr_stop, signal)
                        break
            except decimal.InvalidOperation:
                continue  # Hatayı atla ve bir sonraki döngüye devam et

        # En son geçerli Awesome Oscillator sinyali bul
        for result in reversed(awesome_results):
            if result.oscillator is not None:
                if result.oscillator > 0:
                    signal = "Al"
                else:
                    signal = "Sat"
                quote = next((q for q in quotes if q.date == result.date), None)
                if quote:
                    latest_awesome_signal = (result.date, quote.close, result.oscillator, signal)
                    break

        # En son geçerli Basic Quotes sinyali bul
        for result in reversed(basic_quotes_results):
            quote = next((q for q in quotes if q.date == result.date), None)
            if quote:
                prev_quote = next((q for q in quotes if q.date == result.date - timedelta(days=1)), None)
                if prev_quote:
                    change = (quote.close - prev_quote.close) / prev_quote.close * 100
                    if change > 0:
                        signal = "Al"
                    elif change < 0:
                        signal = "Sat"
                    else:
                        signal = "Bekle"
                    latest_basic_quotes_signal = (result.date, quote.close, change, signal)
                    break

        # En son geçerli Bollinger Bandı sinyali bul
        for result in reversed(bollinger_results):
            try:
                if result.upper_band is not None and result.lower_band is not None:
                    signal = "N/A"  # Bollinger Bandı için genellikle belirli bir al-sat sinyali kullanılmaz
                    quote = next((q for q in quotes if q.date == result.date), None)
                    if quote:
                        # Upper ve lower band'ların arasındaki fark ile fiyat karşılaştırması yapabilirsiniz
                        if quote.close > result.upper_band:
                            signal = "Al"
                        elif quote.close < result.lower_band:
                            signal = "Sat"
                        latest_bollinger_signal = (result.date, quote.close, result.upper_band, result.lower_band, signal)
                        break
            except TypeError:
                continue  # Hatayı atla ve bir sonraki döngüye devam et

        # En son geçerli BOP sinyali bul
        for result in reversed(bop_results):
            if result.bop is not None:
                if result.bop > 0:
                    signal = "Al"
                elif result.bop < 0:
                    signal = "Sat"
                else:
                    signal = "Bekle"
                quote = next((q for q in quotes if q.date == result.date), None)
                if quote:
                    latest_bop_signal = (result.date, quote.close, result.bop, signal)
                    break

        # En son geçerli CCI sinyali bul
        for result in reversed(cci_results):
            if result.cci is not None:
                if result.cci > 100:
                    signal = "Aşırı Alım"
                elif result.cci < -100:
                    signal = "Aşırı Satım"
                else:
                    signal = "Bekle"
                quote = next((q for q in quotes if q.date == result.date), None)
                if quote:
                    latest_cci_signal = (result.date, quote.close, result.cci, signal)
                    break

        # En son geçerli Chaikin Oscillator sinyali bul
        for result in reversed(chaikin_osc_results):
            if result.oscillator is not None:
                if result.oscillator > 0:
                    signal = "Al"
                else:
                    signal = "Sat"
                quote = next((q for q in quotes if q.date == result.date), None)
                if quote:
                    latest_chaikin_osc_signal = (result.date, quote.close, result.oscillator, signal)
                    break

        # En son geçerli CHOP (Choppiness Index) sinyali bul
        for result in reversed(chop_results):
            if result.chop is not None:
                if result.chop > 61.8:
                    signal = "Al"
                elif result.chop < 38.2:
                    signal = "Sat"
                else:
                    signal = "Bekle"
                quote = next((q for q in quotes if q.date == result.date), None)
                if quote:
                    latest_chop_signal = (result.date, quote.close, result.chop, signal)
                    break

        # En son geçerli CMF (Chaikin Money Flow) sinyali bul
        for result in reversed(cmf_results):
            if result.cmf is not None:
                if result.cmf > 0:
                    signal = "Al"
                else:
                    signal = "Sat"
                quote = next((q for q in quotes if q.date == result.date), None)
                if quote:
                    latest_cmf_signal = (result.date, quote.close, result.cmf, signal)
                    break

        # En son geçerli CMO (Chande Momentum Oscillator) sinyali bul
        for result in reversed(cmo_results):
            if result.cmo is not None:
                if result.cmo > 50:
                    signal = "Al"
                elif result.cmo < -50:
                    signal = "Sat"
                else:
                    signal = "Bekle"
                quote = next((q for q in quotes if q.date == result.date), None)
                if quote:
                    latest_cmo_signal = (result.date, quote.close, result.cmo, signal)
                    break

        # En son geçerli Connors RSI sinyali bul
        for result in reversed(connors_rsi_results):
            if result.connors_rsi is not None:
                if result.connors_rsi > 70:
                    signal = "Sat"
                elif result.connors_rsi < 30:
                    signal = "Al"
                else:
                    signal = "Bekle"
                quote = next((q for q in quotes if q.date == result.date), None)
                if quote:
                    latest_connors_rsi_signal = (result.date, quote.close, result.connors_rsi, signal)
                    break

        # En son geçerli Correlation sinyali bul
        for result in reversed(correlation_results):
            if result.correlation is not None:
                if result.correlation > 0.8:
                    signal = "Pozitif Korelasyon"
                elif result.correlation < -0.8:
                    signal = "Negatif Korelasyon"
                else:
                    signal = "Zayıf Korelasyon"
                quote = next((q for q in quotes if q.date == result.date), None)
                if quote:
                    latest_correlation_signal = (result.date, quote.close, result.correlation, signal)
                    break

        # Elder Ray hesapla
        for result in reversed(elder_ray_results):
            if result.bull_power is not None and result.bear_power is not None:
                if result.bull_power > 0 and result.bear_power < 0:
                    signal = "Al"
                else:
                    signal = "Sat"
                latest_elder_ray_signal = (result.date, result.bull_power, result.bear_power, signal)
                break

        # EMA hesapla
        for result in reversed(ema_results):
            if result.ema is not None:
                if result.ema > quotes[-1].close:
                    signal = "Al"
                else:
                    signal = "Sat"
                latest_ema_signal = (result.date, quotes[-1].close, result.ema, signal)
                break

        # EPMA hesapla
        for result in reversed(epma_results):
            if result.epma is not None:
                if result.epma > quotes[-1].close:
                    signal = "Al"
                else:
                    signal = "Sat"
                latest_epma_signal = (result.date, quotes[-1].close, result.epma, signal)
                break

        # Fisher Transform hesapla
        for result in reversed(fisher_transform_results):
            if result.fisher is not None:
                if result.fisher > 0:
                    signal = "Al"
                else:
                    signal = "Sat"
                latest_fisher_transform_signal = (result.date, result.fisher, signal)
                break

        # Force Index hesapla
        for result in reversed(force_index_results):
            if result.force_index is not None:
                if result.force_index > 0:
                    signal = "Al"
                else:
                    signal = "Sat"
                latest_force_index_signal = (result.date, result.force_index, signal)
                break

        # Fractal hesapla
        for result in reversed(fractal_results):
            if result.fractal_bear is not None or result.fractal_bull is not None:
                if result.fractal_bull:
                    signal = "Al"
                elif result.fractal_bear:
                    signal = "Sat"
                latest_fractal_signal = (result.date, result.fractal_bull, result.fractal_bear, signal)
                break

        # Gator Oscillator hesapla
        for result in reversed(gator_results):
            if result.upper is not None and result.lower is not None:
                if result.upper > result.lower:
                    signal = "Al"
                else:
                    signal = "Sat"
                latest_gator_signal = (result.date, result.upper, result.lower, signal)
                break

        # HMA hesapla
        for result in reversed(hma_results):
            if result.hma is not None:
                if result.hma > quotes[-1].close:
                    signal = "Al"
                else:
                    signal = "Sat"
                latest_hma_signal = (result.date, quotes[-1].close, result.hma, signal)
                break

        # HT Trendline hesapla
        for result in reversed(ht_trendline_results):
            if result.trendline is not None:  # "result" üzerinden "trendline" özelliğine erişin
                if result.trendline > quotes[-1].close:
                    signal = "Al"
                else:
                    signal = "Sat"
                latest_ht_trendline_signal = (result.date, quotes[-1].close, result.trendline, signal)
                break

        # Hurst Exponent hesapla
        for result in reversed(hurst_results):
            if result.hurst_exponent is not None:  # Doğru özelliği kontrol edin
                if result.hurst_exponent > 0.5:  # Doğru özelliği kullanın
                    signal = "Al"
                else:
                    signal = "Sat"
                latest_hurst_signal = (result.date, result.hurst_exponent, signal)  # Doğru özelliği kullanın
                break

        # KAMA hesapla
        for result in reversed(kama_results):
            if result.kama is not None:
                if result.kama > quotes[-1].close:
                    signal = "Al"
                else:
                    signal = "Sat"
                latest_kama_signal = (result.date, quotes[-1].close, result.kama, signal)
                break

        # Keltner Channels hesapla
        for result in reversed(keltner_results):
            if result.center_line is not None and result.upper_band is not None and result.lower_band is not None:
                if quotes[-1].close > result.upper_band:
                    signal = "Sat"
                elif quotes[-1].close < result.lower_band:
                    signal = "Al"
                else:
                    signal = "Bekle"
                latest_keltner_signal = (result.date, quotes[-1].close, result.upper_band, result.lower_band, signal)
                break

        # KVO hesapla
        for result in reversed(kvo_results):
            if result.oscillator is not None:
                if result.oscillator > 0:
                    signal = "Al"
                else:
                    signal = "Sat"
                latest_kvo_signal = (result.date, result.oscillator, signal)
                break

        # MA Envelopes hesapla
        for result in reversed(ma_envelopes_results):
            if result.upper_envelope is not None and result.lower_envelope is not None:
                if quotes[-1].close > result.upper_envelope:
                    signal = "Sat"
                elif quotes[-1].close < result.lower_envelope:
                    signal = "Al"
                else:
                    signal = "Bekle"
                latest_ma_envelopes_signal = (result.date, quotes[-1].close, result.upper_envelope, result.lower_envelope, signal)
                break

        # MAMA hesapla
        for result in reversed(mama_results):
            if result.mama is not None:
                if result.mama > quotes[-1].close:
                    signal = "Al"
                else:
                    signal = "Sat"
                latest_mama_signal = (result.date, quotes[-1].close, result.mama, signal)
                break

        # MFI hesapla
        for result in reversed(mfi_results):
            if result.mfi is not None:
                if result.mfi > 80:
                    signal = "Aşırı Alım"
                elif result.mfi < 20:
                    signal = "Aşırı Satım"
                else:
                    signal = "Bekle"
                latest_mfi_signal = (result.date, result.mfi, signal)
                break

        # OBV hesapla
        for result in reversed(obv_results):
            if result.obv is not None:
                if result.obv > 0:
                    signal = "Al"
                else:
                    signal = "Sat"
                latest_obv_signal = (result.date, result.obv, signal)
                break

        # PMO hesapla
        for result in reversed(pmo_results):
            if result.pmo is not None:
                if result.pmo > 0:
                    signal = "Al"
                else:
                    signal = "Sat"
                latest_pmo_signal = (result.date, result.pmo, signal)
                break

        # PVO hesapla
        for result in reversed(pvo_results):
            if result.pvo is not None:
                if result.pvo > 0:
                    signal = "Al"
                else:
                    signal = "Sat"
                latest_pvo_signal = (result.date, result.pvo, signal)
                break

        # ROC hesapla
        for result in reversed(roc_results):
            if result.roc is not None:
                if result.roc > 0:
                    signal = "Al"
                else:
                    signal = "Sat"
                latest_roc_signal = (result.date, result.roc, signal)
                break

        # En son geçerli Slope sinyali bul
        for i, result in enumerate(reversed(slope_results)):
            if result.slope is not None:
                if result.slope  > 0:
                    signal = "Yukarı"
                else:
                    signal = "Aşağı"
                quote = next((q for q in quotes if q.date == quotes[i - len(slope_results)].date), None)
                if quote:
                    latest_slope_signal = (quote.date, quote.close, result.slope, signal)
                    break

        # En son geçerli SMA sinyali bul
        for i, result in enumerate(reversed(sma_results)):
            try:
                if result is not None:
                    if quotes[-1].close > result.sma:
                        signal = "Al"
                    else:
                        signal = "Sat"
                    quote = next((q for q in quotes if q.date == quotes[i - len(sma_results)].date), None)
                    if quote:
                        latest_sma_signal = (quote.date, quote.close, result.sma, signal)
                        break
            except TypeError:
                pass

        # En son geçerli SMI sinyali bul
        for i, result in enumerate(reversed(smi_results)):
            if result.smi is not None:
                if result.smi < 20:
                    signal = "Aşırı Sat"
                elif result.smi > 80:
                    signal = "Aşırı Al"
                else:
                    signal = "Bekle"
                quote = next((q for q in quotes if q.date == quotes[i - len(smi_results)].date), None)
                if quote:
                    latest_smi_signal = (quote.date, quote.close, result.smi, signal)
                    break

        # En son geçerli STARC-Bands sinyali bul
        for i, result in enumerate(reversed(starc_bands_results)):
            try:
                if result is not None:
                    if quotes[-1].close > result.upper_band:
                        signal = "Al"
                    elif quotes[-1].close < result.lower_band:
                        signal = "Sat"
                    else:
                        signal = "Bekle"
                    quote = next((q for q in quotes if q.date == quotes[i - len(starc_bands_results)].date), None)
                    if quote:
                        latest_starc_bands_signal = (quote.date, quote.close, signal)
                        break
            except TypeError:
                continue  # Hatayı atla ve bir sonraki döngüye devam et


        # En son geçerli STC sinyali bul
        for result in reversed(stc_results):
            try:
                if result is not None:
                    if result.stc > 80:
                        signal = "Al"  # Al sinyali
                    elif result.stc < 20:
                        signal = "Sat"  # Sat sinyali
                    else:
                        signal = "Bekle"  # Bekle sinyali
                    quote = next((q for q in quotes if q.date == result.date), None)
                    if quote:
                        latest_stc_signal = (quote.date, quote.close, signal)
                        break
            except TypeError:
                continue  # Hatayı atla ve bir sonraki döngüye devam et


        # En son geçerli STDEV sinyali bul
        for result in reversed(stdev_results):
            try:
                if result is not None:
                    if result.stdev > 1.5:
                        signal = "Al"  # Al sinyali
                    elif result.stdev < 0.5:
                        signal = "Sat"  # Sat sinyali
                    else:
                        signal = "Bekle"  # Bekle sinyali
                    quote = next((q for q in quotes if q.date == result.date), None)
                    if quote:
                        latest_stdev_signal = (quote.date, quote.close, signal)
                        break
            except TypeError:
                pass


        # STDEV kanalları sonuçları için sinyal belirleme
        for result in reversed(stdev_channels_results):
            try:
                if result is not None:
                    if result.upper_channel > 2:
                        signal = "Al"  # Al sinyali
                    elif result.lower_channel < 0.5:
                        signal = "Sat"  # Sat sinyali
                    else:
                        signal = "Bekle"  # Bekle sinyali
                    quote = next((q for q in quotes if q.date == result.date), None)
                    if quote:
                        latest_stdev_channels_signal = (quote.date, quote.close, signal)
                        break
            except TypeError:
                continue  # Hatanın olduğu durumu atla


        for result in reversed(stoch_rsi_results):
            if result.stoch_rsi is not None:
                if result.stoch_rsi < 0.2:
                    signal = "Aşırı Satım"
                elif result.stoch_rsi > 0.8:
                    signal = "Aşırı Alım"
                else:
                    signal = "Bekle"
                quote = next((q for q in quotes if q.date == result.date), None)
                if quote:
                    latest_stoch_rsi_signal = (result.date, quote.close, result.stoch_rsi, signal)
                    break

        # En son geçerli T3 sinyali bul
        for result in reversed(t3_results):
            if result.t3 is not None:
                # T3 sonuçlarını kullanırken Quote nesnelerini kullanın
                quote = next((q for q in quotes if q.date == result.date), None)
                if quote:
                    # T3 sonucunun kapanış fiyatını al
                    close = quote.close
                    if result.t3 > close:
                        signal = "Al"
                    else:
                        signal = "Sat"
                    latest_t3_signal = (result.date, close, result.t3, signal)
                    break

        # En son geçerli TEMA sinyali bul
        for result in reversed(tema_results):
            if result.tema is not None:
                # TEMA sonuçlarını kullanırken Quote nesnelerini kullanın
                quote = next((q for q in quotes if q.date == result.date), None)
                if quote:
                    # TEMA sonucunun kapanış fiyatını al
                    close = quote.close
                    if result.tema > close:
                        signal = "Al"
                    else:
                        signal = "Sat"
                    latest_tema_signal = (result.date, close, result.tema, signal)
                    break



        # Sonuçları DataFrame'e ekle
        if latest_rsi_signal:
            ticker_str = ticker.split('.')[0]  # .IS uzantısını kaldır
            rsi_date_str = latest_rsi_signal[0].date()
            rsi_close_price = float(latest_rsi_signal[1])
            rsi_value = latest_rsi_signal[2]
            rsi_signal = latest_rsi_signal[3]
            all_signals = pd.concat([all_signals, pd.DataFrame({"Ticker": [ticker_str], 
                                                                "RSI": latest_rsi_signal[3] if latest_rsi_signal is not None else None,
                                                                "MACD": latest_macd_signal[4] if latest_macd_signal is not None else None,
                                                                "ADX": latest_adx_signal[3] if latest_adx_signal is not None else None,
                                                                "ADL": latest_adl_signal[3] if latest_adl_signal is not None else None,
                                                                "Alligator": latest_alligator_signal[5] if latest_alligator_signal is not None else None,
                                                                "ALMA": latest_alma_signal[3] if latest_alma_signal is not None else None,
                                                                "Aroon": latest_aroon_signal[4] if latest_aroon_signal is not None else None,
                                                                "ATR": latest_atr_signal[2] if latest_atr_signal is not None else None,
                                                                "ATR Stop": latest_atr_stop_signal[2] if latest_atr_stop_signal is not None else None,
                                                                "Awesome Oscillator": latest_awesome_signal[3] if latest_awesome_signal is not None else None,
                                                                "Basic Quotes": latest_basic_quotes_signal[3] if latest_basic_quotes_signal is not None else None,
                                                                "Bollinger Bandı": latest_bollinger_signal[4] if latest_bollinger_signal is not None else None,
                                                                "BOP": latest_bop_signal[3] if latest_bop_signal is not None else None,
                                                                "CCI": latest_cci_signal[3] if latest_cci_signal is not None else None,
                                                                "Chaikin Oscillator": latest_chaikin_osc_signal[3] if latest_chaikin_osc_signal is not None else None,
                                                                "CHOP": latest_chop_signal[3] if latest_chop_signal is not None else None,
                                                                "CMF": latest_cmf_signal[3] if latest_cmf_signal is not None else None,
                                                                "CMO": latest_cmo_signal[3] if latest_cmo_signal is not None else None,
                                                                "Connors RSI": latest_connors_rsi_signal[3] if latest_connors_rsi_signal is not None else None,
                                                                "Correlation": latest_correlation_signal[3] if latest_correlation_signal is not None else None,
                                                                "Elder Ray": latest_elder_ray_signal[3] if latest_elder_ray_signal is not None else None,
                                                                "EMA": latest_ema_signal[3] if latest_ema_signal is not None else None,
                                                                "EPMA": latest_epma_signal[3] if latest_epma_signal is not None else None,
                                                                "Fisher Transform": latest_fisher_transform_signal[2] if latest_fisher_transform_signal is not None else None,
                                                                "Force Index": latest_force_index_signal[2] if latest_force_index_signal is not None else None,
                                                                "Fractal": latest_fractal_signal[3] if latest_fractal_signal is not None else None,
                                                                "Gator Oscillator": latest_gator_signal[3] if latest_gator_signal is not None else None,
                                                                "HMA": latest_hma_signal[3] if latest_hma_signal is not None else None,
                                                                "HT Trendline": latest_ht_trendline_signal[3] if latest_ht_trendline_signal is not None else None,
                                                                "Hurst": latest_hurst_signal[2] if latest_hurst_signal is not None else None,
                                                                "KAMA": latest_kama_signal[3] if latest_kama_signal is not None else None,
                                                                "Keltner Channel": latest_keltner_signal[4] if latest_keltner_signal is not None else None,
                                                                "KVO": latest_kvo_signal[2] if latest_kvo_signal is not None else None,
                                                                "MA Envelopes": latest_ma_envelopes_signal[4] if latest_ma_envelopes_signal is not None else None,
                                                                "MAMA": latest_mama_signal[3] if latest_mama_signal is not None else None,
                                                                "MFI": latest_mfi_signal[2] if latest_mfi_signal is not None else None,
                                                                "OBV": latest_obv_signal[2] if latest_obv_signal is not None else None,
                                                                "PMO": latest_pmo_signal[2] if latest_pmo_signal is not None else None,
                                                                "PVO": latest_pvo_signal[2] if latest_pvo_signal is not None else None,
                                                                "ROC": latest_roc_signal[2] if latest_roc_signal is not None else None,
                                                                "Slope": latest_slope_signal[3] if latest_slope_signal is not None else None,
                                                                "SMA": latest_sma_signal[3] if latest_sma_signal is not None else None,
                                                                "SMI": latest_smi_signal[3] if latest_smi_signal is not None else None,
                                                                "STARC-Bands": latest_starc_bands_signal[2] if latest_starc_bands_signal is not None else None,
                                                                "STC": latest_stc_signal[2] if latest_stc_signal is not None else None,
                                                                "STDEV": latest_stdev_signal[2] if latest_stdev_signal is not None else None,
                                                                "STDEV-Channels": latest_stdev_channels_signal[2] if latest_stdev_channels_signal is not None else None,
                                                                "Stochastic RSI": latest_stoch_rsi_signal[3] if latest_stoch_rsi_signal is not None else None,
                                                                "T3": latest_t3_signal[3] if latest_t3_signal is not None else None,
                                                                "TEMA": latest_tema_signal[3] if latest_tema_signal is not None else None,
                                                                "TR": latest_tr_signal[3] if latest_tr_signal is not None else None,
                                                                "TRIX": latest_trix_signal[3] if latest_trix_signal is not None else None,
                                                                "TSI": latest_tsi_signal[3] if latest_tsi_signal is not None else None,
                                                                "Ulcer Index": latest_ulcer_index_signal[2] if latest_ulcer_index_signal is not None else None,
                                                                "Ultimate Oscillator": latest_ultimate_signal[2] if latest_ultimate_signal is not None else None,
                                                                "Volatility Stop": latest_volatility_stop_signal[2] if latest_volatility_stop_signal is not None else None,
                                                                "Vortex": latest_vortex_signal[2] if latest_vortex_signal is not None else None,
                                                                "VWAP": latest_vwap_signal if latest_vwap_signal is not None else None,
                                                                "VWMA": latest_vwma_signal if latest_vwma_signal is not None else None,
                                                                "Williams %R": latest_williams_r_signal if latest_williams_r_signal is not None else None,
                                                                "WMA": latest_wma_signal if latest_wma_signal is not None else None
                                                             
                                                                })], ignore_index=True)
        else:
            print(f"RSI sinyali bulunamadı: {ticker}")

# Tüm sinyalleri içeren DataFrame'i Excel dosyasına yazdır
all_signals.to_excel("C:/Users/q/Desktop/bt/ındıcators_sinyalleri.xlsx", index=False)