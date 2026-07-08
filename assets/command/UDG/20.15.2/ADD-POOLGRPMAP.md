---
id: UDG@20.15.2@MMLCommand@ADD POOLGRPMAP
type: MMLCommand
name: ADD POOLGRPMAP（添加地址池组映射关系）
nf: UDG
version: 20.15.2
verb: ADD
object_keyword: POOLGRPMAP
command_category: 配置类
applicable_nf:
- PGW-U
- UPF
effect_mode: 对新用户生效
is_dangerous: false
max_records: 40000
category_path:
- 用户面服务管理
- 会话管理
- 会话地址管理
- 地址池组映射关系
status: active
---

# ADD POOLGRPMAP（添加地址池组映射关系）

## 功能

**适用NF：PGW-U、UPF**

该命令用于添加TAC-Group/LAC-Group、APN、SMF到地址池组的映射规则。

## 注意事项

- 该命令执行后只对新激活用户生效。
- 该命令最大记录数为40000。
- 在执行ADD POOLGRPMAP命令前，必须先执行命令ADD POOLGROUP配置地址池组，根据实际组网规划执行命令ADD TACGROUP/ADD LACGROUP配置TAC-Group/LAC-Group，ADD APN配置APN，ADD CPNODEID配置SMF。
- PoolGrpMap对象本身为SMF/APN/位置区组/位置区组+PLMN与地址池组之间的绑定关系，不支持修改。
- 可选参数中SMF/APN/LOCTIONTYPE +LOCATIONGRPNAME+PLMN（可选）至少选择输入一种。
- 地址池组中绑定的EXTERNAL类型地址池的白名单检查功能，只在地址池组与APN绑定时才生效。
- 通过映射关系查找到地址池组后，地址池组中的地址池配置的VPN实例与激活用户所在的APN配置的VPN实例必须相同时才能匹配，如果所有地址池都不匹配，则本映射查找失败。
- 相同的映射参数组合，只能和一个地址池组配置映射关系，不支持映射多个地址池组。
- 对于一条映射配置，所有配置的映射参数条件均满足的情况下，映射关系才生效，否则不生效。
- 当地址池组中绑定的LOCAL类型的地址池为SMF指定的地址池时，地址池组仅被APN单独绑定时生效。
- PLMN取值为消息中ULI信源中的TAI或LAI里携带的PLMN。
- 基于APN分地址的映射配置，不支持配置未绑定地址池的地址池组。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| MAPPINGNAME | 映射规则名称 | 可选必选说明：必选参数<br>参数含义：该参数用于指定映射规则名称。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～79。不支持空格及特殊字符“#”、“$”和“&”等，由“_”、“-”、数字、大小写字母和“.”组成，不能以“.”开头且不能出现连续两个“.”，不区分大小写。<br>默认值：无<br>配置原则：无 |
| LOCATIONGRPTYPE | 位置区组类型 | 可选必选说明：可选参数<br>参数含义：该参数用于指定映射地址池组的区域类型。<br>数据来源：本端规划<br>取值范围：枚举类型。<br>- LAC：LAC。<br>- TAC：TAC。<br>默认值：无<br>配置原则：无 |
| LOCATIONGRPNAME | 位置区组名称 | 可选必选说明：条件必选参数<br>前提条件：该参数在“LOCATIONGRPTYPE”配置为“TAC” 或 “LAC”时为必选参数。<br>参数含义：该参数用于指定位置组名称。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～32。<br>默认值：无<br>配置原则：该参数使用ADD TACGROUP或ADD LACGROUP命令配置生成。 |
| APN | APN名称 | 可选必选说明：可选参数<br>参数含义：该参数用于指定APN实例名。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～63。只能由“-”、数字、大小写字母和“.”组成，不能以“.”开头且不能出现连续两个“.”。不支持空格及“_”、“#”、“$”、“&”、“%”、“^”、“（”、“）”、“，”、“/”、“;”、“:”、“””、“`”特殊字符，不区分大小写。<br>默认值：无<br>配置原则：该参数使用ADD APN命令配置生成。 |
| SMF | SMF名称 | 可选必选说明：可选参数<br>参数含义：该参数用于指定SMF实例名称。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～255。只能由“_”、“-”、数字、大小写字母和“.”组成，不能以“.”开头且不能出现连续两个“.”，不区分大小写。<br>默认值：无<br>配置原则：该参数使用ADD CPNODEID命令配置生成。 |
| POOLGROUPNAME | 地址池组名称 | 可选必选说明：必选参数<br>参数含义：该参数用于指定地址池组名称。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～79。不支持空格及特殊字符“#”、“$”和“&”等，由“_”、“-”、数字、大小写字母和“.”组成，不能以“.”开头且不能出现连续两个“.”，不区分大小写。<br>默认值：无<br>配置原则：该参数使用ADD POOLGROUP命令配置生成。 |
| MCC | 移动国家码 | 可选必选说明：条件可选参数<br>前提条件：该参数在“LOCATIONGRPTYPE”配置为“LAC” 或 “TAC”时为可选参数。<br>参数含义：该参数用于指定移动国家码。<br>数据来源：全网规划<br>取值范围：字符串类型，为3位数字，000～999。<br>默认值：无<br>配置原则：无 |
| MNC | 移动网络号 | 可选必选说明：条件可选参数<br>前提条件：该参数在“LOCATIONGRPTYPE”配置为“LAC” 或 “TAC”时为可选参数。<br>参数含义：该参数用于指定移动网络号。<br>数据来源：全网规划<br>取值范围：字符串类型，可为2或3位数字，00~99或000~999。<br>默认值：无<br>配置原则：MNC有效配置长度为两位或三位。配置长度取决于PFCP Session Establishment Request消息ULI信元中携带的MNC有效值的长度，两位有效数字即配置两位，三位有效数字需配置三位。不受ADD MNCLEN影响。 |

## 操作的配置对象

- [[configobject/UDG/20.15.2/POOLGRPMAP]] · 地址池组映射关系（POOLGRPMAP）

## 关联任务

- [[UDG@20.15.2@Task@0-00047]]

## 使用实例

- 添加名为apn1.com的APN实例与名为poolgroup1的地址池组的映射，设置映射名为mapping1：
  ```
  ADD POOLGRPMAP: MAPPINGNAME="mapping1", APN="apn1.com", POOLGROUPNAME="poolgroup1";
  ```
- 添加名为smfnode1的SMF实例与名为poolgroup2的地址池组的映射，设置映射名为mapping2：
  ```
  ADD POOLGRPMAP: MAPPINGNAME="mapping2", SMF="smfnode1", POOLGROUPNAME="poolgroup2";
  ```
- 添加名为apn2.com的APN实例、名为tac1的TAC-Group与名为poolgroup3的地址池组的映射，设置映射名为mapping3：
  ```
  ADD POOLGRPMAP: MAPPINGNAME="mapping3", LOCATIONGRPTYPE=TAC, LOCATIONGRPNAME="tac1", APN="apn2.com", POOLGROUPNAME="poolgroup3";
  ```
- 添加值为460011的PLMN、名为tac1的TAC-Group与名为poolgroup4的地址池组的映射，设置映射名为mapping4：
  ```
  ADD POOLGRPMAP: MAPPINGNAME="mapping4", LOCATIONGRPTYPE=TAC, LOCATIONGRPNAME="tac1", POOLGROUPNAME="poolgroup4", MCC="460", MNC="011";
  ```

## 证据

- 原始手册：`evidence/UDG/20.15.2/ADD-POOLGRPMAP.md`
