---
id: UDG@20.15.2@MMLCommand@DSP ASSERTINFO
type: MMLCommand
name: DSP ASSERTINFO（显示RU断言信息）
nf: UDG
version: 20.15.2
verb: DSP
object_keyword: ASSERTINFO
command_category: 查询类
effect_mode: ''
is_dangerous: false
category_path:
- 平台服务管理
- 单体服务公共功能管理
- 操作维护
- 系统调测
- 异常信息
status: active
---

# DSP ASSERTINFO（显示RU断言信息）

## 功能

该命令用于显示当前是否存在断言信息。

## 注意事项

无。

## 权限

G_1，管理员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| RUNAME | RU名称 | 可选必选说明：可选参数<br>参数含义：该参数用于表示RU名称。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～63。不支持空格，区分大小写。<br>默认值：无<br>配置原则：当不输入时显示所有的资源单元的信息。使用<br>[**DSP RU**](../../../系统管理/资源管理/RU管理/显示资源单元信息（DSP RU）_59103857.md)<br>查看RU名称。 |
| SHOWNUM | 要查询的数据最大个数 | 可选必选说明：可选参数<br>参数含义：该参数用于表示每个资源单元能够显示的最大记录量。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围为1～100。<br>默认值：20<br>配置原则：当不输入时，若是某个资源单元的实际数据量达到此参数的默认值，则显示的数据量为此参数默认值，否则按实际数据量显示。当输入某个值时，若是某个资源单元的实际数据量达到此参数值，则显示的数据量为此参数值，否则按实际数据量显示。 |
| BEGININDEX | 记录起始位置 | 可选必选说明：可选参数<br>参数含义：该参数用于表示每个资源单元从第几条记录开始显示。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围为0～99。<br>默认值：无<br>配置原则：当不输入时，从最新的数据开始显示，否则从指定的起始数据索引开始显示。 |
| ISVERBOSE | 是否查询详细信息 | 可选必选说明：可选参数<br>参数含义：该参数用于表示是否显示详细信息。<br>数据来源：本端规划<br>取值范围：枚举类型。<br>- NO：否。<br>- YES：是。<br>默认值：NO |
| SERVICEINSTANCE | 服务实例 | 可选必选说明：必选参数<br>参数含义：该参数表示大颗粒服务实例名称。<br>数据来源：本端规划<br>取值范围：字符串类型，通过LST VNFC命令获取。<br>默认值：无<br>配置原则：只能填写通过LST VNFC命令查询到的管理代理标识，但不能填写0，0表示VNFP。 |

## 操作的配置对象

- [[configobject/UDG/20.15.2/ASSERTINFO]] · RU断言信息（ASSERTINFO）

## 使用实例

显示所有详细的断言信息：

```
DSP ASSERTINFO: ISVERBOSE=YES
,SERVICEINSTANCE="vnfc"
;
```

```
RETCODE = 0  操作成功

结果如下:
--------
RU名称                      断言发生时间           进程ID    进程名称            文件名        行号     附加信息     Fenix版本               Dopra版本                      补丁版本          调用栈
VNODE_CSLB_VNFC_OMU_0002     2016-04-15 10:19:01    1011      APPLocation10001    abc.c         32     NULL          FENIXV100R005C00B090    DOPRA SSP V300R002C50SPC070    V100R005MOD000    
liblocbase.so(VRP_Assert+0x75) [0x00007f77d866d2c5] 
compa.so(SSITP_Set_Compa_Triggerassertion+0x29) [0x00007f77d5261a59] 
libssitp.so(SSITP_Action_SetTestData+0x4f4) [0x00007f77d4bf9bc6] 
libssitp.so(SSITP_CFG_ParseActAtom+0x168) [0x00007f77d4bfbca4] 
libssitp.so(SSITP_CFG_ReceiveSmpActMsg+0x101) [0x00007f77d4bfbaa5] 
libssitp.so(SSITP_RECV_ProcSMPAppCfgiMsg+0xae) [0x00007f77d4bffe3f] 
libssitp.so(SSITP_COM_ReceiveMsg+0x140) [0x00007f77d4bffa34] 
libdefault.so(RTF_MsgProcessCbk+0x101) [0x00007f77dd6fc7a1] 
libdefault.so(rtfScmMessageSchedule+0x24d) [0x00007f77dd6fb7bd] 
libdefault.so(rtfScmCompScheKernelEntryFifo+0xda) [0x00007f77dd6fc55a] 
libdefault.so(rtfScmCompScheDefaultEntry+0x2fa) [0x00007f77dd6f8b6a] 
libdefault.so(tskAllTaskEntry+0x15f) [0x00007f77dd50deff]
VNODE_CSLB_VNFC_OMU_0002     2016-04-15 10:18:50    1010      APPLocation10001    abc.c         32    NULL           FENIXV100R005C00B090    DOPRA SSP V300R002C50SPC070    V100R005MOD000  
liblocbase.so(VRP_Assert+0x75) [0x00007f9990c062c5]
compa.so(SSITP_Set_Compa_Triggerassertion+0x29) [0x00007f998d7faa59] 
libssitp.so(SSITP_Action_SetTestData+0x4f4) [0x00007f998d192bc6] 
libssitp.so(SSITP_CFG_ParseActAtom+0x168) [0x00007f998d194ca4] 
libssitp.so(SSITP_CFG_ReceiveSmpActMsg+0x101) [0x00007f998d194aa5] 
libssitp.so(SSITP_RECV_ProcSMPAppCfgiMsg+0xae) [0x00007f998d198e3f] 
libssitp.so(SSITP_COM_ReceiveMsg+0x140) [0x00007f998d198a34] 
libdefault.so(RTF_MsgProcessCbk+0x101) [0x00007f9995c957a1] 
libdefault.so(rtfScmMessageSchedule+0x24d) [0x00007f9995c947bd] 
libdefault.so(rtfScmCompScheKernelEntryFifo+0xda) [0x00007f9995c9555a] 
libdefault.so(rtfScmCompScheDefaultEntry+0x2fa) [0x00007f9995c91b6a] 
libdefault.so(tskAllTaskEntry+0x15f) [0x00007f9995aa6eff] 
(结果个数 = 2)
---    END
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/显示RU断言信息（DSP-ASSERTINFO）_59103399.md`
