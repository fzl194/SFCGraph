---
id: UDG@20.15.2@MMLCommand@ADD BWMSERVICE
type: MMLCommand
name: ADD BWMSERVICE（增加带宽管理业务）
nf: UDG
version: 20.15.2
verb: ADD
object_keyword: BWMSERVICE
command_category: 配置类
applicable_nf:
- PGW-U
- UPF
effect_mode: 立即生效
is_dangerous: false
max_records: 1000
category_path:
- 用户面服务管理
- 业务控制策略
- 带宽控制
- 带宽管理业务
status: active
---

# ADD BWMSERVICE（增加带宽管理业务）

## 功能

**适用NF：PGW-U、UPF**

该命令用于增加一条带宽管理的业务范围，实现业务区分。该命令支持TOS类型业务，用报文的TOS区分业务，也支持非TOS类型业务，为带宽管理业务绑定一个分类属性、或者指定7层协议、或者绑定一个协议组来区分业务。

## 注意事项

- 该命令执行后立即生效。
- 该命令最大记录数为1000。当配置记录数大于规格的90%时，会上报“ALM-135602215 配置数量超阈值”告警。当配置记录数小于等于配置规格90%时，恢复“ALM-135602215 配置数量超阈值”告警。阈值可以通过MOD CFGTHRESHOLD命令修改。
- 一个带宽管理业务可以绑定在多个带宽管理规则下。
- 基于OSTYPE进行带宽控制场景，当用户的OSTYPE确定后，后续业务的OSTYPE发生变化，带宽策略不支持更新。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| BWMSERVICENAME | 带宽控制业务名称 | 可选必选说明：必选参数<br>参数含义：该参数用于配置带宽管理业务的名称。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～31。不支持空格，不区分大小写。<br>默认值：无<br>配置原则：无 |
| BWMSERVICETYPE | 业务类型 | 可选必选说明：必选参数<br>参数含义：该参数用于配置带宽管理业务的类型。<br>数据来源：本端规划<br>取值范围：枚举类型。<br>- TOS：TOS类型。<br>- NONTOS：非TOS类型。<br>默认值：无<br>配置原则：<br>- TOS：如果运营商希望设置该带宽管理业务按照报文的TOS类型区分时，则配置该参数。<br>- NONTOS：如果运营商希望设置该带宽管理业务基于非TOS区分，即分类属性、或者协议组、或者协议，则配置该参数。 |
| NONTOSSRVTYPE | 非TOS业务类型 | 可选必选说明：条件必选参数<br>前提条件：该参数在“BWMSERVICETYPE”配置为“NONTOS”时为必选参数。<br>参数含义：该参数用于配置带宽管理业务的非TOS类型。<br>数据来源：本端规划<br>取值范围：枚举类型。<br>- CATEGORY_PROP：基于分类属性的业务区分。<br>- PROTOCOLGROUP：基于协议组的业务区分。<br>- PROTOCOL：基于协议的业务区分。<br>默认值：无<br>配置原则：<br>- CATEGORY_PROP：如果运营商希望设置该带宽管理业务按照报文匹配到的内容计费规则来区分时，则配置该参数。<br>- PROTOCOLGROUP：如果运营商希望设置该带宽管理业务按照报文所属的7层协议组区分，则配置该参数。<br>- PROTOCOL：如果运营商希望设置该带宽管理业务按照报文的7层协议区分，则配置该参数。 |
| CATEPROPNAME | 分类属性名称 | 可选必选说明：条件必选参数<br>前提条件：该参数在“NONTOSSRVTYPE”配置为“CATEGORY_PROP”时为必选参数。<br>参数含义：该参数用于配置绑定在该带宽管理业务下的分类属性名称。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～31。不支持空格，不区分大小写。<br>默认值：无<br>配置原则：该参数使用ADD CATEGORYPROP命令配置生成。 |
| PROTGROUPNAME | 协议组名称 | 可选必选说明：条件必选参数<br>前提条件：该参数在“NONTOSSRVTYPE”配置为“PROTOCOLGROUP”时为必选参数。<br>参数含义：该参数用于配置绑定在该带宽管理业务下的协议组名称。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～31。不支持空格，不区分大小写。<br>默认值：无<br>配置原则：数据源为系统支持识别的所有类型的协议组，或者通过ADD PROTOCOLGROUP命令配置的协议组。 |
| PROTOCOLNAME | 协议名称 | 可选必选说明：条件必选参数<br>前提条件：该参数在“NONTOSSRVTYPE”配置为“PROTOCOL”时为必选参数。<br>参数含义：该参数用于配置绑定在该带宽管理业务下的协议名称。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～31。不支持空格，不区分大小写。<br>默认值：无<br>配置原则：数据源为系统支持识别的所有类型的协议、子协议。 |
| TOSCFGTYPE | Tos配置类型 | 可选必选说明：条件必选参数<br>前提条件：该参数在“BWMSERVICETYPE”配置为“TOS”时为必选参数。<br>参数含义：该参数用于配置TOS类型的配置方式。<br>数据来源：本端规划<br>取值范围：枚举类型。<br>- CLASS：使用TOS类别名称配置。<br>- TOS_VALUE：使用TOS值配置。<br>默认值：无<br>配置原则：<br>- CLASS：如果运营商希望设置以TOS类别名称配置TOS类型，则配置该参数。<br>- TOS_VALUE：如果运营商希望设置以TOS类别值配置TOS类型，则配置该参数。 |
| TOSCLASSTYPE | Tos分类类型 | 可选必选说明：条件必选参数<br>前提条件：该参数在“TOSCFGTYPE”配置为“CLASS”时为必选参数。<br>参数含义：该参数用于配置TOS类型业务的类别名，即IP报文中DSCP字段的Precedence（3bit）。<br>数据来源：本端规划<br>取值范围：枚举类型。<br>- BE：Precedence的值为000。<br>- AF1：Precedence的值为001。<br>- AF2：Precedence的值为010。<br>- AF3：Precedence的值为011。<br>- AF4：Precedence的值为100。<br>- EF：Precedence的值为101。<br>- CS6：Precedence的值为110。<br>- CS7：Precedence的值为111。<br>默认值：无<br>配置原则：无 |
| TOSVALUE | 服务类型 | 可选必选说明：条件必选参数<br>前提条件：该参数在“TOSCFGTYPE”配置为“TOS_VALUE”时为必选参数。<br>参数含义：该参数用于配置TOS类型业务的类别值，即IP报文中DSCP字段的Precedence。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围为0～7。<br>默认值：无<br>配置原则：TOS类型业务的类别名称与类别值的对应关系是：BE（0），AF1（1），AF2（2），AF3（3），AF4（4）， EF（5），CS6（6），CS7（7）。 |
| OSTYPE | 操作系统类型 | 可选必选说明：条件可选参数<br>前提条件：该参数在“BWMSERVICETYPE”配置为“NONTOS”时为可选参数。<br>参数含义：该参数用于配置绑定在该带宽管理业务下的操作系统类型。<br>数据来源：本端规划<br>取值范围：枚举类型。<br>- IOS：IOS操作系统。<br>- ANDROID：Android操作系统。<br>- WINDOWS：windows操作系统。<br>- OTHERS：其他操作系统类型。<br>默认值：无<br>配置原则：<br>- 如果运营商希望设置以操作系统类型匹配相应带宽控制策略，则配置该参数。<br>- 需要先设置SET GLBOSLELBWMSW、SET APNOSLELBWMSW和SET UPOSLELBWMSW命令，以开启操作系统带宽管理开关。 |
| CFGDOMAINNAME | 配置域名称 | 可选必选说明：可选参数<br>参数含义：该参数表示命令所属公共配置域的名称。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～31。<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [[configobject/UDG/20.15.2/BWMSERVICE]] · 带宽管理业务（BWMSERVICE）

## 关联任务

- [[UDG@20.15.2@Task@0-00034]]

## 使用实例

- 假如运营商需要增加带宽管理业务，业务名称为“testbwmservice1”，以报文的TOS类型为“BE”进行区分：
  ```
  ADD BWMSERVICE:BWMSERVICENAME="testbwmservice1",BWMSERVICETYPE=TOS,TOSCFGTYPE=CLASS,TOSCLASSTYPE=BE;
  ```
- 假如运营商需要增加带宽管理业务，业务名称为“TestBwmService2”，以报文的7层协议为“bt”进行区分：
  ```
  ADD BWMSERVICE:BWMSERVICENAME="testbwmservice2",BWMSERVICETYPE=NONTOS,NONTOSSRVTYPE=PROTOCOL,PROTOCOLNAME="bt";
  ```

## 证据

- 原始手册：`evidence/UDG/20.15.2/ADD-BWMSERVICE.md`
