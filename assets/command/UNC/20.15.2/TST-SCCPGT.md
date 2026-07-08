---
id: UNC@20.15.2@MMLCommand@TST SCCPGT
type: MMLCommand
name: TST SCCPGT（测试SCCP全局翻译码）
nf: UNC
version: 20.15.2
verb: TST
object_keyword: SCCPGT
command_category: 调测类
applicable_nf:
- SGSN
- MME
- SMSF
effect_mode: ''
is_dangerous: false
category_path:
- 业务服务管理
- Pre 5G接入业务管理
- 控制面管理
- 信令传输管理
- SCCP管理
- SCCP全局翻译码
status: active
---

# TST SCCPGT（测试SCCP全局翻译码）

## 功能

**适用网元：SGSN、MME、SMSF**

此命令用于测试SCCP GT码是否能被正确解析，对匹配的GT码输出翻译结果。

## 注意事项

- 系统会自行选取可用的信令进程（SPP/SGP），因此，执行该操作的时候要确保系统中有可用的信令进程。否则，操作将不能正常执行。
- 系统对输入的GT码进行最大匹配，匹配成功的输出翻译结果。

## 权限

manage-ug；system-ug；monitor-ug
G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| RUNAME | RU名称 | 可选必选说明：可选参数<br>参数含义：该参数用于指定SPU资源单元名。该参数可以通过<br>[DSP RU](../../../../../../平台服务管理/单体服务公共功能管理/系统管理/资源管理/RU管理/显示资源单元信息（DSP RU）_59103857.md)<br>命令查询。<br>取值范围：0~63 位字符串<br>默认值：无 |
| PT | 进程类型 | 可选必选说明：可选参数<br>参数含义：该参数用于指定进程的进程类型。<br>取值范围：<br>- “SPP(SPP)”<br>- “SGP(SGP)”<br>默认值：无 |
| PN | 进程号 | 可选必选说明：可选参数<br>参数含义：该参数用于指定进程号。<br>取值范围：0~20<br>默认值：无 |
| GTEXP | GT码表示语 | 可选必选说明：可选参数<br>参数含义：该参数用于指定GT码的类型。<br>取值范围：<br>- “FOUR（ITU四类）”<br>- “SIX（ANSI二类）”<br>默认值：<br>“FOUR（ITU四类）” |
| TT | 翻译类型 | 可选必选说明：可选参数<br>参数含义：该参数用于指定翻译类型。<br>前提条件：只有当<br>“GT码表示语”<br>为<br>“SIX（ANSI二类）”<br>时，该参数才有效。<br>取值范围：<br>- “ANSI9（ANSI 9类）”<br>- “ANSI10（ANSI 10类）”<br>默认值：<br>“ANSI9（ANSI 9类）” |
| NP | 编号计划 | 可选必选说明：可选参数<br>参数含义：该参数用于指编号计划。<br>前提条件：只有当<br>“GT码表示语”<br>为<br>“FOUR（ITU四类）”<br>时，该参数才有效。<br>取值范围：<br>- “ISDNP（ISDN/电话编号计划）”<br>- “DATA（数据编号计划）”<br>- “TELEX（Telex编号计划）”<br>- “SMS（海事移动编号计划）”<br>- “PMS（陆地移动编号计划）”<br>- “ISDNMS（ISDN/移动编号计划）”<br>默认值：<br>“ISDNP（ISDN/电话编号计划）” |
| ADDREXP | 地址性质表示语 | 可选必选说明：可选参数<br>参数含义：该参数用于指地址性质表示语。<br>前提条件：只有当<br>“GT码表示语”<br>为<br>“FOUR（ITU四类）”<br>时，该参数才有效。<br>取值范围：<br>- “FREE（空闲）”<br>- “SUBDN（用户号码）”<br>- “NSU（国内备用号码）”<br>- “NVU（国内有效号码）”<br>- “INTDN（国际号码）”<br>默认值：<br>“INTDN（国际号码）” |
| ADDR | 地址信息 | 可选必选说明：必选参数<br>参数含义：该参数用于指地址信息。<br>取值范围：长度不超过20的字符串<br>默认值：无 |

## 操作的配置对象

- [[configobject/UNC/20.15.2/SCCPGT]] · SCCP全局翻译码（SCCPGT）

## 使用实例

测试SCCP全局翻译码：

TST SCCPGT: ADDR="86139080210";

```
%%TST SCCPGT: ADDR="86139080210";%%
RETCODE = 0  操作成功。

测试SCCP模块GT码
----------------
      GT码索引  =  370
  GT码匹配长度  =  10
    匹配的GT码  =  4000114086139080210
  翻译结果类型  =  DPC + SSN
    网络指示语  =  国内网
目的信令点编码  =  0x80210
      子系统号  =  BSSAP+
    新GT码长度  =  0
        新GT码  =  NULL
(结果个数 = 1)
---    END
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/测试SCCP全局翻译码(TST-SCCPGT)_26306138.md`
