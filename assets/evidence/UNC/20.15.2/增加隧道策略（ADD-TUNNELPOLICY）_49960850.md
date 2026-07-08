# 增加隧道策略（ADD TUNNELPOLICY）

- [命令功能](#ZH-CN_CONCEPT_0000001549960850__1.3.1.1)
- [注意事项](#ZH-CN_CONCEPT_0000001549960850__1.3.2.1)
- [操作用户权限](#ZH-CN_CONCEPT_0000001549960850__1.3.3.1)
- [参数说明](#ZH-CN_CONCEPT_0000001549960850__1.3.4.1)
- [使用实例](#ZH-CN_CONCEPT_0000001549960850__1.3.5.1)

#### [命令功能](#ZH-CN_CONCEPT_0000001549960850)

该命令用于增加隧道策略。

#### [注意事项](#ZH-CN_CONCEPT_0000001549960850)

- 该命令执行后立即生效。
- 该命令最大记录数为65535。

#### [操作用户权限](#ZH-CN_CONCEPT_0000001549960850)

G_1，管理员级别命令组；G_2，操作员级别命令组

#### [参数说明](#ZH-CN_CONCEPT_0000001549960850)

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| TNLPOLICYNAME | 隧道策略名字 | 可选必选说明：必选参数<br>参数含义：该参数用于表示隧道策略名字。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～39。<br>默认值：无 |
| DESCRIPTION | 隧道策略描述 | 可选必选说明：可选参数<br>参数含义：该参数用于表示隧道策略描述。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～80。<br>默认值：无 |
| TNLPOLICYTYPE | 隧道策略类型 | 可选必选说明：必选参数<br>参数含义：该参数用于表示隧道策略类型。<br>数据来源：本端规划<br>取值范围：枚举类型。<br>- invalid：无效类型的隧道策略。<br>- tnlSelectSeq：隧道选择序列。<br>默认值：无 |
| LOADBALANCENUM | 负载均衡数 | 可选必选说明：条件必选参数<br>前提条件：该参数在“TNLPOLICYTYPE”配置为“tnlSelectSeq”时为必选参数。<br>参数含义：该参数用于表示负载均衡数。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围为1～64。<br>默认值：无 |
| SELTNLTYPE1 | 第一优选隧道类型 | 可选必选说明：条件必选参数<br>前提条件：该参数在“TNLPOLICYTYPE”配置为“tnlSelectSeq”时为必选参数。<br>参数含义：该参数用于表示选择隧道类型。<br>数据来源：本端规划<br>取值范围：枚举类型。<br>- lsp：LSP。<br>- gre：GRE。<br>默认值：无 |
| SELTNLTYPE2 | 第二优选隧道类型 | 可选必选说明：条件可选参数<br>前提条件：该参数在“TNLPOLICYTYPE”配置为“tnlSelectSeq”时为可选参数。<br>参数含义：该参数用于表示选择隧道类型。<br>数据来源：本端规划<br>取值范围：枚举类型。<br>- invalid：INVALID。<br>- lsp：LSP。<br>- gre：GRE。<br>默认值：invalid |

#### [使用实例](#ZH-CN_CONCEPT_0000001549960850)

增加隧道策略：

```
ADD TUNNELPOLICY:TNLPOLICYNAME="tp",TNLPOLICYTYPE=tnlSelectSeq,LOADBALANCENUM=50,SELTNLTYPE1=gre,SELTNLTYPE2=lsp;
```
