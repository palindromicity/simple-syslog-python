# Generated from grammars/Rfc5424.g4 by ANTLR 4.10.1
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .Rfc5424Parser import Rfc5424Parser
else:
    from Rfc5424Parser import Rfc5424Parser

//CHECKSTYLE:OFF
/*
 * Copyright 2018-2022 simple-syslog authors
 * All rights reserved.
 * Licensed under the Apache License, Version 2.0 (the "License");
 * you may not use this file except in compliance with the License.
 * You may obtain a copy of the License at
 *
 *       http://www.apache.org/licenses/LICENSE-2.0
 *
 * Unless required by applicable law or agreed to in writing, software
 * distributed under the License is distributed on an "AS IS" BASIS,
 * WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
 * See the License for the specific language governing permissions and
 * limitations under the License.
 */



# This class defines a complete listener for a parse tree produced by Rfc5424Parser.
class Rfc5424Listener(ParseTreeListener):

    # Enter a parse tree produced by Rfc5424Parser#herokuHttpsMsg.
    def enterHerokuHttpsMsg(self, ctx:Rfc5424Parser.HerokuHttpsMsgContext):
        pass

    # Exit a parse tree produced by Rfc5424Parser#herokuHttpsMsg.
    def exitHerokuHttpsMsg(self, ctx:Rfc5424Parser.HerokuHttpsMsgContext):
        pass


    # Enter a parse tree produced by Rfc5424Parser#octet_prefixed.
    def enterOctet_prefixed(self, ctx:Rfc5424Parser.Octet_prefixedContext):
        pass

    # Exit a parse tree produced by Rfc5424Parser#octet_prefixed.
    def exitOctet_prefixed(self, ctx:Rfc5424Parser.Octet_prefixedContext):
        pass


    # Enter a parse tree produced by Rfc5424Parser#syslogMsg.
    def enterSyslogMsg(self, ctx:Rfc5424Parser.SyslogMsgContext):
        pass

    # Exit a parse tree produced by Rfc5424Parser#syslogMsg.
    def exitSyslogMsg(self, ctx:Rfc5424Parser.SyslogMsgContext):
        pass


    # Enter a parse tree produced by Rfc5424Parser#octet_prefix.
    def enterOctet_prefix(self, ctx:Rfc5424Parser.Octet_prefixContext):
        pass

    # Exit a parse tree produced by Rfc5424Parser#octet_prefix.
    def exitOctet_prefix(self, ctx:Rfc5424Parser.Octet_prefixContext):
        pass


    # Enter a parse tree produced by Rfc5424Parser#syslogHeader.
    def enterSyslogHeader(self, ctx:Rfc5424Parser.SyslogHeaderContext):
        pass

    # Exit a parse tree produced by Rfc5424Parser#syslogHeader.
    def exitSyslogHeader(self, ctx:Rfc5424Parser.SyslogHeaderContext):
        pass


    # Enter a parse tree produced by Rfc5424Parser#headerPriority.
    def enterHeaderPriority(self, ctx:Rfc5424Parser.HeaderPriorityContext):
        pass

    # Exit a parse tree produced by Rfc5424Parser#headerPriority.
    def exitHeaderPriority(self, ctx:Rfc5424Parser.HeaderPriorityContext):
        pass


    # Enter a parse tree produced by Rfc5424Parser#headerPriorityValue.
    def enterHeaderPriorityValue(self, ctx:Rfc5424Parser.HeaderPriorityValueContext):
        pass

    # Exit a parse tree produced by Rfc5424Parser#headerPriorityValue.
    def exitHeaderPriorityValue(self, ctx:Rfc5424Parser.HeaderPriorityValueContext):
        pass


    # Enter a parse tree produced by Rfc5424Parser#headerVersion.
    def enterHeaderVersion(self, ctx:Rfc5424Parser.HeaderVersionContext):
        pass

    # Exit a parse tree produced by Rfc5424Parser#headerVersion.
    def exitHeaderVersion(self, ctx:Rfc5424Parser.HeaderVersionContext):
        pass


    # Enter a parse tree produced by Rfc5424Parser#headerNilHostName.
    def enterHeaderNilHostName(self, ctx:Rfc5424Parser.HeaderNilHostNameContext):
        pass

    # Exit a parse tree produced by Rfc5424Parser#headerNilHostName.
    def exitHeaderNilHostName(self, ctx:Rfc5424Parser.HeaderNilHostNameContext):
        pass


    # Enter a parse tree produced by Rfc5424Parser#headerHostName.
    def enterHeaderHostName(self, ctx:Rfc5424Parser.HeaderHostNameContext):
        pass

    # Exit a parse tree produced by Rfc5424Parser#headerHostName.
    def exitHeaderHostName(self, ctx:Rfc5424Parser.HeaderHostNameContext):
        pass


    # Enter a parse tree produced by Rfc5424Parser#headerNilAppName.
    def enterHeaderNilAppName(self, ctx:Rfc5424Parser.HeaderNilAppNameContext):
        pass

    # Exit a parse tree produced by Rfc5424Parser#headerNilAppName.
    def exitHeaderNilAppName(self, ctx:Rfc5424Parser.HeaderNilAppNameContext):
        pass


    # Enter a parse tree produced by Rfc5424Parser#headerAppName.
    def enterHeaderAppName(self, ctx:Rfc5424Parser.HeaderAppNameContext):
        pass

    # Exit a parse tree produced by Rfc5424Parser#headerAppName.
    def exitHeaderAppName(self, ctx:Rfc5424Parser.HeaderAppNameContext):
        pass


    # Enter a parse tree produced by Rfc5424Parser#headerNilProcId.
    def enterHeaderNilProcId(self, ctx:Rfc5424Parser.HeaderNilProcIdContext):
        pass

    # Exit a parse tree produced by Rfc5424Parser#headerNilProcId.
    def exitHeaderNilProcId(self, ctx:Rfc5424Parser.HeaderNilProcIdContext):
        pass


    # Enter a parse tree produced by Rfc5424Parser#headerProcId.
    def enterHeaderProcId(self, ctx:Rfc5424Parser.HeaderProcIdContext):
        pass

    # Exit a parse tree produced by Rfc5424Parser#headerProcId.
    def exitHeaderProcId(self, ctx:Rfc5424Parser.HeaderProcIdContext):
        pass


    # Enter a parse tree produced by Rfc5424Parser#headerNilMsgId.
    def enterHeaderNilMsgId(self, ctx:Rfc5424Parser.HeaderNilMsgIdContext):
        pass

    # Exit a parse tree produced by Rfc5424Parser#headerNilMsgId.
    def exitHeaderNilMsgId(self, ctx:Rfc5424Parser.HeaderNilMsgIdContext):
        pass


    # Enter a parse tree produced by Rfc5424Parser#headerMsgId.
    def enterHeaderMsgId(self, ctx:Rfc5424Parser.HeaderMsgIdContext):
        pass

    # Exit a parse tree produced by Rfc5424Parser#headerMsgId.
    def exitHeaderMsgId(self, ctx:Rfc5424Parser.HeaderMsgIdContext):
        pass


    # Enter a parse tree produced by Rfc5424Parser#headerNilTimestamp.
    def enterHeaderNilTimestamp(self, ctx:Rfc5424Parser.HeaderNilTimestampContext):
        pass

    # Exit a parse tree produced by Rfc5424Parser#headerNilTimestamp.
    def exitHeaderNilTimestamp(self, ctx:Rfc5424Parser.HeaderNilTimestampContext):
        pass


    # Enter a parse tree produced by Rfc5424Parser#headerTimeStamp.
    def enterHeaderTimeStamp(self, ctx:Rfc5424Parser.HeaderTimeStampContext):
        pass

    # Exit a parse tree produced by Rfc5424Parser#headerTimeStamp.
    def exitHeaderTimeStamp(self, ctx:Rfc5424Parser.HeaderTimeStampContext):
        pass


    # Enter a parse tree produced by Rfc5424Parser#full_date.
    def enterFull_date(self, ctx:Rfc5424Parser.Full_dateContext):
        pass

    # Exit a parse tree produced by Rfc5424Parser#full_date.
    def exitFull_date(self, ctx:Rfc5424Parser.Full_dateContext):
        pass


    # Enter a parse tree produced by Rfc5424Parser#date_fullyear.
    def enterDate_fullyear(self, ctx:Rfc5424Parser.Date_fullyearContext):
        pass

    # Exit a parse tree produced by Rfc5424Parser#date_fullyear.
    def exitDate_fullyear(self, ctx:Rfc5424Parser.Date_fullyearContext):
        pass


    # Enter a parse tree produced by Rfc5424Parser#date_month.
    def enterDate_month(self, ctx:Rfc5424Parser.Date_monthContext):
        pass

    # Exit a parse tree produced by Rfc5424Parser#date_month.
    def exitDate_month(self, ctx:Rfc5424Parser.Date_monthContext):
        pass


    # Enter a parse tree produced by Rfc5424Parser#date_mday.
    def enterDate_mday(self, ctx:Rfc5424Parser.Date_mdayContext):
        pass

    # Exit a parse tree produced by Rfc5424Parser#date_mday.
    def exitDate_mday(self, ctx:Rfc5424Parser.Date_mdayContext):
        pass


    # Enter a parse tree produced by Rfc5424Parser#full_time.
    def enterFull_time(self, ctx:Rfc5424Parser.Full_timeContext):
        pass

    # Exit a parse tree produced by Rfc5424Parser#full_time.
    def exitFull_time(self, ctx:Rfc5424Parser.Full_timeContext):
        pass


    # Enter a parse tree produced by Rfc5424Parser#partial_time.
    def enterPartial_time(self, ctx:Rfc5424Parser.Partial_timeContext):
        pass

    # Exit a parse tree produced by Rfc5424Parser#partial_time.
    def exitPartial_time(self, ctx:Rfc5424Parser.Partial_timeContext):
        pass


    # Enter a parse tree produced by Rfc5424Parser#time_hour.
    def enterTime_hour(self, ctx:Rfc5424Parser.Time_hourContext):
        pass

    # Exit a parse tree produced by Rfc5424Parser#time_hour.
    def exitTime_hour(self, ctx:Rfc5424Parser.Time_hourContext):
        pass


    # Enter a parse tree produced by Rfc5424Parser#time_minute.
    def enterTime_minute(self, ctx:Rfc5424Parser.Time_minuteContext):
        pass

    # Exit a parse tree produced by Rfc5424Parser#time_minute.
    def exitTime_minute(self, ctx:Rfc5424Parser.Time_minuteContext):
        pass


    # Enter a parse tree produced by Rfc5424Parser#time_second.
    def enterTime_second(self, ctx:Rfc5424Parser.Time_secondContext):
        pass

    # Exit a parse tree produced by Rfc5424Parser#time_second.
    def exitTime_second(self, ctx:Rfc5424Parser.Time_secondContext):
        pass


    # Enter a parse tree produced by Rfc5424Parser#time_secfrac.
    def enterTime_secfrac(self, ctx:Rfc5424Parser.Time_secfracContext):
        pass

    # Exit a parse tree produced by Rfc5424Parser#time_secfrac.
    def exitTime_secfrac(self, ctx:Rfc5424Parser.Time_secfracContext):
        pass


    # Enter a parse tree produced by Rfc5424Parser#time_offset.
    def enterTime_offset(self, ctx:Rfc5424Parser.Time_offsetContext):
        pass

    # Exit a parse tree produced by Rfc5424Parser#time_offset.
    def exitTime_offset(self, ctx:Rfc5424Parser.Time_offsetContext):
        pass


    # Enter a parse tree produced by Rfc5424Parser#time_numoffset.
    def enterTime_numoffset(self, ctx:Rfc5424Parser.Time_numoffsetContext):
        pass

    # Exit a parse tree produced by Rfc5424Parser#time_numoffset.
    def exitTime_numoffset(self, ctx:Rfc5424Parser.Time_numoffsetContext):
        pass


    # Enter a parse tree produced by Rfc5424Parser#structured_data.
    def enterStructured_data(self, ctx:Rfc5424Parser.Structured_dataContext):
        pass

    # Exit a parse tree produced by Rfc5424Parser#structured_data.
    def exitStructured_data(self, ctx:Rfc5424Parser.Structured_dataContext):
        pass


    # Enter a parse tree produced by Rfc5424Parser#sdElement.
    def enterSdElement(self, ctx:Rfc5424Parser.SdElementContext):
        pass

    # Exit a parse tree produced by Rfc5424Parser#sdElement.
    def exitSdElement(self, ctx:Rfc5424Parser.SdElementContext):
        pass


    # Enter a parse tree produced by Rfc5424Parser#sdParam.
    def enterSdParam(self, ctx:Rfc5424Parser.SdParamContext):
        pass

    # Exit a parse tree produced by Rfc5424Parser#sdParam.
    def exitSdParam(self, ctx:Rfc5424Parser.SdParamContext):
        pass


    # Enter a parse tree produced by Rfc5424Parser#sd_id.
    def enterSd_id(self, ctx:Rfc5424Parser.Sd_idContext):
        pass

    # Exit a parse tree produced by Rfc5424Parser#sd_id.
    def exitSd_id(self, ctx:Rfc5424Parser.Sd_idContext):
        pass


    # Enter a parse tree produced by Rfc5424Parser#paramName.
    def enterParamName(self, ctx:Rfc5424Parser.ParamNameContext):
        pass

    # Exit a parse tree produced by Rfc5424Parser#paramName.
    def exitParamName(self, ctx:Rfc5424Parser.ParamNameContext):
        pass


    # Enter a parse tree produced by Rfc5424Parser#paramValue.
    def enterParamValue(self, ctx:Rfc5424Parser.ParamValueContext):
        pass

    # Exit a parse tree produced by Rfc5424Parser#paramValue.
    def exitParamValue(self, ctx:Rfc5424Parser.ParamValueContext):
        pass


    # Enter a parse tree produced by Rfc5424Parser#sd_name.
    def enterSd_name(self, ctx:Rfc5424Parser.Sd_nameContext):
        pass

    # Exit a parse tree produced by Rfc5424Parser#sd_name.
    def exitSd_name(self, ctx:Rfc5424Parser.Sd_nameContext):
        pass


    # Enter a parse tree produced by Rfc5424Parser#msgUTF8.
    def enterMsgUTF8(self, ctx:Rfc5424Parser.MsgUTF8Context):
        pass

    # Exit a parse tree produced by Rfc5424Parser#msgUTF8.
    def exitMsgUTF8(self, ctx:Rfc5424Parser.MsgUTF8Context):
        pass


    # Enter a parse tree produced by Rfc5424Parser#msg_utf8.
    def enterMsg_utf8(self, ctx:Rfc5424Parser.Msg_utf8Context):
        pass

    # Exit a parse tree produced by Rfc5424Parser#msg_utf8.
    def exitMsg_utf8(self, ctx:Rfc5424Parser.Msg_utf8Context):
        pass


    # Enter a parse tree produced by Rfc5424Parser#bom.
    def enterBom(self, ctx:Rfc5424Parser.BomContext):
        pass

    # Exit a parse tree produced by Rfc5424Parser#bom.
    def exitBom(self, ctx:Rfc5424Parser.BomContext):
        pass


    # Enter a parse tree produced by Rfc5424Parser#utf_8_string.
    def enterUtf_8_string(self, ctx:Rfc5424Parser.Utf_8_stringContext):
        pass

    # Exit a parse tree produced by Rfc5424Parser#utf_8_string.
    def exitUtf_8_string(self, ctx:Rfc5424Parser.Utf_8_stringContext):
        pass


    # Enter a parse tree produced by Rfc5424Parser#octet.
    def enterOctet(self, ctx:Rfc5424Parser.OctetContext):
        pass

    # Exit a parse tree produced by Rfc5424Parser#octet.
    def exitOctet(self, ctx:Rfc5424Parser.OctetContext):
        pass


    # Enter a parse tree produced by Rfc5424Parser#sp.
    def enterSp(self, ctx:Rfc5424Parser.SpContext):
        pass

    # Exit a parse tree produced by Rfc5424Parser#sp.
    def exitSp(self, ctx:Rfc5424Parser.SpContext):
        pass


    # Enter a parse tree produced by Rfc5424Parser#printusascii.
    def enterPrintusascii(self, ctx:Rfc5424Parser.PrintusasciiContext):
        pass

    # Exit a parse tree produced by Rfc5424Parser#printusascii.
    def exitPrintusascii(self, ctx:Rfc5424Parser.PrintusasciiContext):
        pass


    # Enter a parse tree produced by Rfc5424Parser#printusasciinospecials.
    def enterPrintusasciinospecials(self, ctx:Rfc5424Parser.PrintusasciinospecialsContext):
        pass

    # Exit a parse tree produced by Rfc5424Parser#printusasciinospecials.
    def exitPrintusasciinospecials(self, ctx:Rfc5424Parser.PrintusasciinospecialsContext):
        pass


    # Enter a parse tree produced by Rfc5424Parser#nonzero_digit.
    def enterNonzero_digit(self, ctx:Rfc5424Parser.Nonzero_digitContext):
        pass

    # Exit a parse tree produced by Rfc5424Parser#nonzero_digit.
    def exitNonzero_digit(self, ctx:Rfc5424Parser.Nonzero_digitContext):
        pass


    # Enter a parse tree produced by Rfc5424Parser#zeroDigit.
    def enterZeroDigit(self, ctx:Rfc5424Parser.ZeroDigitContext):
        pass

    # Exit a parse tree produced by Rfc5424Parser#zeroDigit.
    def exitZeroDigit(self, ctx:Rfc5424Parser.ZeroDigitContext):
        pass


    # Enter a parse tree produced by Rfc5424Parser#nonZeroDigit.
    def enterNonZeroDigit(self, ctx:Rfc5424Parser.NonZeroDigitContext):
        pass

    # Exit a parse tree produced by Rfc5424Parser#nonZeroDigit.
    def exitNonZeroDigit(self, ctx:Rfc5424Parser.NonZeroDigitContext):
        pass


    # Enter a parse tree produced by Rfc5424Parser#nilvalue.
    def enterNilvalue(self, ctx:Rfc5424Parser.NilvalueContext):
        pass

    # Exit a parse tree produced by Rfc5424Parser#nilvalue.
    def exitNilvalue(self, ctx:Rfc5424Parser.NilvalueContext):
        pass



del Rfc5424Parser