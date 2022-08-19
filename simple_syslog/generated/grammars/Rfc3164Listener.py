# Generated from grammars/Rfc3164.g4 by ANTLR 4.10.1
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .Rfc3164Parser import Rfc3164Parser
else:
    from Rfc3164Parser import Rfc3164Parser

#CHECKSTYLE:OFF
#
# Copyright 2018-2022 simple-syslog authors
# All rights reserved.
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#       http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#



# This class defines a complete listener for a parse tree produced by Rfc3164Parser.
class Rfc3164Listener(ParseTreeListener):

    # Enter a parse tree produced by Rfc3164Parser#octet_prefixed.
    def enterOctet_prefixed(self, ctx:Rfc3164Parser.Octet_prefixedContext):
        pass

    # Exit a parse tree produced by Rfc3164Parser#octet_prefixed.
    def exitOctet_prefixed(self, ctx:Rfc3164Parser.Octet_prefixedContext):
        pass


    # Enter a parse tree produced by Rfc3164Parser#syslogMsg.
    def enterSyslogMsg(self, ctx:Rfc3164Parser.SyslogMsgContext):
        pass

    # Exit a parse tree produced by Rfc3164Parser#syslogMsg.
    def exitSyslogMsg(self, ctx:Rfc3164Parser.SyslogMsgContext):
        pass


    # Enter a parse tree produced by Rfc3164Parser#syslogHeader.
    def enterSyslogHeader(self, ctx:Rfc3164Parser.SyslogHeaderContext):
        pass

    # Exit a parse tree produced by Rfc3164Parser#syslogHeader.
    def exitSyslogHeader(self, ctx:Rfc3164Parser.SyslogHeaderContext):
        pass


    # Enter a parse tree produced by Rfc3164Parser#headerPriority.
    def enterHeaderPriority(self, ctx:Rfc3164Parser.HeaderPriorityContext):
        pass

    # Exit a parse tree produced by Rfc3164Parser#headerPriority.
    def exitHeaderPriority(self, ctx:Rfc3164Parser.HeaderPriorityContext):
        pass


    # Enter a parse tree produced by Rfc3164Parser#headerPriorityValue.
    def enterHeaderPriorityValue(self, ctx:Rfc3164Parser.HeaderPriorityValueContext):
        pass

    # Exit a parse tree produced by Rfc3164Parser#headerPriorityValue.
    def exitHeaderPriorityValue(self, ctx:Rfc3164Parser.HeaderPriorityValueContext):
        pass


    # Enter a parse tree produced by Rfc3164Parser#headerHostName.
    def enterHeaderHostName(self, ctx:Rfc3164Parser.HeaderHostNameContext):
        pass

    # Exit a parse tree produced by Rfc3164Parser#headerHostName.
    def exitHeaderHostName(self, ctx:Rfc3164Parser.HeaderHostNameContext):
        pass


    # Enter a parse tree produced by Rfc3164Parser#headerTimeStamp.
    def enterHeaderTimeStamp(self, ctx:Rfc3164Parser.HeaderTimeStampContext):
        pass

    # Exit a parse tree produced by Rfc3164Parser#headerTimeStamp.
    def exitHeaderTimeStamp(self, ctx:Rfc3164Parser.HeaderTimeStampContext):
        pass


    # Enter a parse tree produced by Rfc3164Parser#headerTimeStamp3164.
    def enterHeaderTimeStamp3164(self, ctx:Rfc3164Parser.HeaderTimeStamp3164Context):
        pass

    # Exit a parse tree produced by Rfc3164Parser#headerTimeStamp3164.
    def exitHeaderTimeStamp3164(self, ctx:Rfc3164Parser.HeaderTimeStamp3164Context):
        pass


    # Enter a parse tree produced by Rfc3164Parser#date_month_short.
    def enterDate_month_short(self, ctx:Rfc3164Parser.Date_month_shortContext):
        pass

    # Exit a parse tree produced by Rfc3164Parser#date_month_short.
    def exitDate_month_short(self, ctx:Rfc3164Parser.Date_month_shortContext):
        pass


    # Enter a parse tree produced by Rfc3164Parser#date_day_short.
    def enterDate_day_short(self, ctx:Rfc3164Parser.Date_day_shortContext):
        pass

    # Exit a parse tree produced by Rfc3164Parser#date_day_short.
    def exitDate_day_short(self, ctx:Rfc3164Parser.Date_day_shortContext):
        pass


    # Enter a parse tree produced by Rfc3164Parser#full_date.
    def enterFull_date(self, ctx:Rfc3164Parser.Full_dateContext):
        pass

    # Exit a parse tree produced by Rfc3164Parser#full_date.
    def exitFull_date(self, ctx:Rfc3164Parser.Full_dateContext):
        pass


    # Enter a parse tree produced by Rfc3164Parser#date_fullyear.
    def enterDate_fullyear(self, ctx:Rfc3164Parser.Date_fullyearContext):
        pass

    # Exit a parse tree produced by Rfc3164Parser#date_fullyear.
    def exitDate_fullyear(self, ctx:Rfc3164Parser.Date_fullyearContext):
        pass


    # Enter a parse tree produced by Rfc3164Parser#date_month.
    def enterDate_month(self, ctx:Rfc3164Parser.Date_monthContext):
        pass

    # Exit a parse tree produced by Rfc3164Parser#date_month.
    def exitDate_month(self, ctx:Rfc3164Parser.Date_monthContext):
        pass


    # Enter a parse tree produced by Rfc3164Parser#date_mday.
    def enterDate_mday(self, ctx:Rfc3164Parser.Date_mdayContext):
        pass

    # Exit a parse tree produced by Rfc3164Parser#date_mday.
    def exitDate_mday(self, ctx:Rfc3164Parser.Date_mdayContext):
        pass


    # Enter a parse tree produced by Rfc3164Parser#full_time.
    def enterFull_time(self, ctx:Rfc3164Parser.Full_timeContext):
        pass

    # Exit a parse tree produced by Rfc3164Parser#full_time.
    def exitFull_time(self, ctx:Rfc3164Parser.Full_timeContext):
        pass


    # Enter a parse tree produced by Rfc3164Parser#partial_time.
    def enterPartial_time(self, ctx:Rfc3164Parser.Partial_timeContext):
        pass

    # Exit a parse tree produced by Rfc3164Parser#partial_time.
    def exitPartial_time(self, ctx:Rfc3164Parser.Partial_timeContext):
        pass


    # Enter a parse tree produced by Rfc3164Parser#time_hour.
    def enterTime_hour(self, ctx:Rfc3164Parser.Time_hourContext):
        pass

    # Exit a parse tree produced by Rfc3164Parser#time_hour.
    def exitTime_hour(self, ctx:Rfc3164Parser.Time_hourContext):
        pass


    # Enter a parse tree produced by Rfc3164Parser#time_minute.
    def enterTime_minute(self, ctx:Rfc3164Parser.Time_minuteContext):
        pass

    # Exit a parse tree produced by Rfc3164Parser#time_minute.
    def exitTime_minute(self, ctx:Rfc3164Parser.Time_minuteContext):
        pass


    # Enter a parse tree produced by Rfc3164Parser#time_second.
    def enterTime_second(self, ctx:Rfc3164Parser.Time_secondContext):
        pass

    # Exit a parse tree produced by Rfc3164Parser#time_second.
    def exitTime_second(self, ctx:Rfc3164Parser.Time_secondContext):
        pass


    # Enter a parse tree produced by Rfc3164Parser#time_secfrac.
    def enterTime_secfrac(self, ctx:Rfc3164Parser.Time_secfracContext):
        pass

    # Exit a parse tree produced by Rfc3164Parser#time_secfrac.
    def exitTime_secfrac(self, ctx:Rfc3164Parser.Time_secfracContext):
        pass


    # Enter a parse tree produced by Rfc3164Parser#time_offset.
    def enterTime_offset(self, ctx:Rfc3164Parser.Time_offsetContext):
        pass

    # Exit a parse tree produced by Rfc3164Parser#time_offset.
    def exitTime_offset(self, ctx:Rfc3164Parser.Time_offsetContext):
        pass


    # Enter a parse tree produced by Rfc3164Parser#time_numoffset.
    def enterTime_numoffset(self, ctx:Rfc3164Parser.Time_numoffsetContext):
        pass

    # Exit a parse tree produced by Rfc3164Parser#time_numoffset.
    def exitTime_numoffset(self, ctx:Rfc3164Parser.Time_numoffsetContext):
        pass


    # Enter a parse tree produced by Rfc3164Parser#msgAny.
    def enterMsgAny(self, ctx:Rfc3164Parser.MsgAnyContext):
        pass

    # Exit a parse tree produced by Rfc3164Parser#msgAny.
    def exitMsgAny(self, ctx:Rfc3164Parser.MsgAnyContext):
        pass


    # Enter a parse tree produced by Rfc3164Parser#msgUTF8.
    def enterMsgUTF8(self, ctx:Rfc3164Parser.MsgUTF8Context):
        pass

    # Exit a parse tree produced by Rfc3164Parser#msgUTF8.
    def exitMsgUTF8(self, ctx:Rfc3164Parser.MsgUTF8Context):
        pass


    # Enter a parse tree produced by Rfc3164Parser#msg_any.
    def enterMsg_any(self, ctx:Rfc3164Parser.Msg_anyContext):
        pass

    # Exit a parse tree produced by Rfc3164Parser#msg_any.
    def exitMsg_any(self, ctx:Rfc3164Parser.Msg_anyContext):
        pass


    # Enter a parse tree produced by Rfc3164Parser#msg_utf8.
    def enterMsg_utf8(self, ctx:Rfc3164Parser.Msg_utf8Context):
        pass

    # Exit a parse tree produced by Rfc3164Parser#msg_utf8.
    def exitMsg_utf8(self, ctx:Rfc3164Parser.Msg_utf8Context):
        pass


    # Enter a parse tree produced by Rfc3164Parser#bom.
    def enterBom(self, ctx:Rfc3164Parser.BomContext):
        pass

    # Exit a parse tree produced by Rfc3164Parser#bom.
    def exitBom(self, ctx:Rfc3164Parser.BomContext):
        pass


    # Enter a parse tree produced by Rfc3164Parser#utf_8_string.
    def enterUtf_8_string(self, ctx:Rfc3164Parser.Utf_8_stringContext):
        pass

    # Exit a parse tree produced by Rfc3164Parser#utf_8_string.
    def exitUtf_8_string(self, ctx:Rfc3164Parser.Utf_8_stringContext):
        pass


    # Enter a parse tree produced by Rfc3164Parser#octet.
    def enterOctet(self, ctx:Rfc3164Parser.OctetContext):
        pass

    # Exit a parse tree produced by Rfc3164Parser#octet.
    def exitOctet(self, ctx:Rfc3164Parser.OctetContext):
        pass


    # Enter a parse tree produced by Rfc3164Parser#sp.
    def enterSp(self, ctx:Rfc3164Parser.SpContext):
        pass

    # Exit a parse tree produced by Rfc3164Parser#sp.
    def exitSp(self, ctx:Rfc3164Parser.SpContext):
        pass


    # Enter a parse tree produced by Rfc3164Parser#printusascii.
    def enterPrintusascii(self, ctx:Rfc3164Parser.PrintusasciiContext):
        pass

    # Exit a parse tree produced by Rfc3164Parser#printusascii.
    def exitPrintusascii(self, ctx:Rfc3164Parser.PrintusasciiContext):
        pass


    # Enter a parse tree produced by Rfc3164Parser#printusasciinospecials.
    def enterPrintusasciinospecials(self, ctx:Rfc3164Parser.PrintusasciinospecialsContext):
        pass

    # Exit a parse tree produced by Rfc3164Parser#printusasciinospecials.
    def exitPrintusasciinospecials(self, ctx:Rfc3164Parser.PrintusasciinospecialsContext):
        pass


    # Enter a parse tree produced by Rfc3164Parser#nonzero_digit.
    def enterNonzero_digit(self, ctx:Rfc3164Parser.Nonzero_digitContext):
        pass

    # Exit a parse tree produced by Rfc3164Parser#nonzero_digit.
    def exitNonzero_digit(self, ctx:Rfc3164Parser.Nonzero_digitContext):
        pass


    # Enter a parse tree produced by Rfc3164Parser#zeroDigit.
    def enterZeroDigit(self, ctx:Rfc3164Parser.ZeroDigitContext):
        pass

    # Exit a parse tree produced by Rfc3164Parser#zeroDigit.
    def exitZeroDigit(self, ctx:Rfc3164Parser.ZeroDigitContext):
        pass


    # Enter a parse tree produced by Rfc3164Parser#nonZeroDigit.
    def enterNonZeroDigit(self, ctx:Rfc3164Parser.NonZeroDigitContext):
        pass

    # Exit a parse tree produced by Rfc3164Parser#nonZeroDigit.
    def exitNonZeroDigit(self, ctx:Rfc3164Parser.NonZeroDigitContext):
        pass


    # Enter a parse tree produced by Rfc3164Parser#capital.
    def enterCapital(self, ctx:Rfc3164Parser.CapitalContext):
        pass

    # Exit a parse tree produced by Rfc3164Parser#capital.
    def exitCapital(self, ctx:Rfc3164Parser.CapitalContext):
        pass


    # Enter a parse tree produced by Rfc3164Parser#lower.
    def enterLower(self, ctx:Rfc3164Parser.LowerContext):
        pass

    # Exit a parse tree produced by Rfc3164Parser#lower.
    def exitLower(self, ctx:Rfc3164Parser.LowerContext):
        pass



del Rfc3164Parser