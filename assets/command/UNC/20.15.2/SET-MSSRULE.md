---
id: UNC@20.15.2@MMLCommand@SET MSSRULE
type: MMLCommand
name: SET MSSRULE（设置匹配规则）
nf: UNC
version: 20.15.2
verb: SET
object_keyword: MSSRULE
command_category: 配置类
effect_mode: 立即生效
is_dangerous: false
category_path:
- 平台服务管理
- VNRS功能管理
- 操作维护
- 系统调测
- MSS
- 维测开关统计查询
status: active
---

# SET MSSRULE（设置匹配规则）

## 功能

该命令用于设置匹配规则。

用户只有设置规则后，才能绑定该规则对消息或者报文进行匹配，匹配规则是从消息、报文的偏移类型对应的位置加上偏移大小开始，比较“规则内容&规则掩码”和“报文内容&规则掩码”是否一致。

当前通信模块可通过DSP MSSCOMMSTAT命令查询匹配统计个数。

输入的规则内容和掩码应为字符串形式，只能是英文字母、数字的组合，英文字母只能是a～f，且不区分大小写，且字符个数只能是偶数个，输入不符合规范的字符串有错误信息“规则无效。”。

当规则ID被使用时无法删除或者修改，有错误信息“规则正在使用。”。

## 注意事项

该命令执行后立即生效。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| RUNAME | RU名称 | 可选必选说明：必选参数<br>参数含义：该参数用于指定RU名称。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～63。不支持空格，区分大小写。<br>默认值：无<br>配置原则：使用DSP RU查看RU名称。 |
| ENABLE | 使能 | 可选必选说明：必选参数<br>参数含义：该参数用于表示增加或者减少一条规则，增加规则时如果输入的规则ID已存在则覆盖该规则。<br>数据来源：本端规划<br>取值范围：枚举类型。<br>- FALSE：关闭。<br>- TRUE：打开。<br>默认值：无 |
| RULEID | 规则ID | 可选必选说明：条件必选参数<br>前提条件：该参数在“ENABLE”配置为“TRUE”时为必选参数。<br>可选必选说明：条件可选参数<br>前提条件：该参数在“ENABLE”配置为“FALSE”时为可选参数。<br>参数含义：该参数用于表示规则ID。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围为0～31。<br>默认值：无 |
| OFFSETTYPE | 偏移类型 | 可选必选说明：条件必选参数<br>前提条件：该参数在“ENABLE”配置为“TRUE”时为必选参数。<br>参数含义：该参数用于表示偏移类型。<br>数据来源：本端规划<br>取值范围：枚举类型。<br>- ufp-pkt-ctrl：UFP包控制块。<br>- ufp-pkt-data：UFP包数据区。<br>- vfp-pkt-ctrl：VFP包控制块。<br>- vfp-pkt-data：VFP包数据区。<br>- msg-ctrl：消息控制块。<br>- msg-data：消息数据区。<br>默认值：无 |
| OFFSET | 偏移 | 可选必选说明：条件必选参数<br>前提条件：该参数在“ENABLE”配置为“TRUE”时为必选参数。<br>参数含义：该参数用于表示偏移大小。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围为0～4294967295。<br>默认值：无 |
| PATTERN | 规则 | 可选必选说明：条件必选参数<br>前提条件：该参数在“ENABLE”配置为“TRUE”时为必选参数。<br>参数含义：该参数用于表示规则内容。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～128。<br>默认值：无 |
| MASK | 掩码 | 可选必选说明：条件必选参数<br>前提条件：该参数在“ENABLE”配置为“TRUE”时为必选参数。<br>参数含义：该参数用于表示掩码。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～128。<br>默认值：无 |

## 操作的配置对象

- [[configobject/UNC/20.15.2/MSSRULE]] · 匹配规则（MSSRULE）

## 使用实例

设置匹配规则：

```
SET MSSRULE:ENABLE=TRUE,RULEID=1,OFFSETTYPE=ufp-pkt-ctrl,OFFSET=0,PATTERN="FFFF",MASK="FFFF",RUNAME="VNODE_VNRS_VNFC_IPU_0066";
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/设置匹配规则（SET-MSSRULE）_00865565.md`
