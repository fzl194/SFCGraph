# 增加IPv6前缀过滤器节点（ADD IPV6PREFIXFILTERNODE）

- [命令功能](#ZH-CN_CONCEPT_0000001550280694__1.3.1.1)
- [注意事项](#ZH-CN_CONCEPT_0000001550280694__1.3.2.1)
- [操作用户权限](#ZH-CN_CONCEPT_0000001550280694__1.3.3.1)
- [参数说明](#ZH-CN_CONCEPT_0000001550280694__1.3.4.1)
- [使用实例](#ZH-CN_CONCEPT_0000001550280694__1.3.5.1)

#### [命令功能](#ZH-CN_CONCEPT_0000001550280694)

该命令用于添加基于IPv6信息的前缀过滤器。

#### [注意事项](#ZH-CN_CONCEPT_0000001550280694)

- 该命令执行后立即生效。
- 该命令最大记录数为100000。

#### [操作用户权限](#ZH-CN_CONCEPT_0000001550280694)

G_1，管理员级别命令组；G_2，操作员级别命令组

#### [参数说明](#ZH-CN_CONCEPT_0000001550280694)

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| NAME | IPv6前缀列表名字 | 可选必选说明：必选参数<br>参数含义：IP前缀列表名字。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～169。<br>默认值：无<br>配置原则：不支持输入空格。 |
| NODESEQUENCE | IPv6前缀列表节点号 | 可选必选说明：必选参数<br>参数含义：IP前缀列表节点号。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围为1～4294967295。<br>默认值：无<br>配置原则：缺省情况下，该序号值按照配置先后顺序依次递增。 |
| MATCHMODE | IPv6前缀列表匹配模式 | 可选必选说明：必选参数<br>参数含义：IP前缀列表匹配模式。<br>数据来源：本端规划<br>取值范围：枚举类型。<br>- permit：允许。<br>- deny：拒绝。<br>默认值：无<br>配置原则：要求输入完全一致，如果为permit则通过前缀过滤器为允许，否则为不允许。 |
| ADDRESS | IPv6地址 | 可选必选说明：必选参数<br>参数含义：IPv6地址。<br>数据来源：本端规划<br>取值范围：IPv6地址类型。<br>默认值：无<br>配置原则：IPv6地址。 |
| MASKLENGTH | 掩码长度 | 可选必选说明：必选参数<br>参数含义：该参数用于表示IPv6路由的前缀长度。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围为0～128。<br>默认值：无 |
| MATCHNETWORK | 是否匹配网络地址 | 可选必选说明：可选参数<br>参数含义：是否匹配网络。<br>数据来源：本端规划<br>取值范围：布尔类型，输入格式为“TRUE”或者“FALSE”。<br>默认值：FALSE |
| GREATEREQUAL | 掩码长度匹配范围下限 | 可选必选说明：可选参数<br>参数含义：大于或等于。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围为0～128。<br>默认值：无<br>配置原则：<br>- GREATEREQUAL的意思是“大于等于”； LESSEQUAL的意思是“小于等于”。长度范围可以表达为MASKLENGTH <= GREATEREQUAL <= LESSEQUAL <= 128。<br>- 如果只指定了GREATEREQUAL，前缀范围为[GREATEREQUAL，128]。<br>- 当只指定LESSEQUAL时，前缀范围为[MASKLENGTH，LESSEQUAL]。 |
| LESSEQUAL | 掩码长度匹配范围上限 | 可选必选说明：可选参数<br>参数含义：小于或等于。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围为0～128。<br>默认值：无<br>配置原则：<br>- GREATEREQUAL的意思是“大于等于”； LESSEQUAL的意思是“小于等于”。长度范围是可以表达为MASKLENGTH <= GREATEREQUAL <= LESSEQUAL <= 128。<br>- 如果只指定了LESSEQUAL，前缀范围为[MASKLENGTH，LESSEQUAL]。<br>- 当只指定GREATEREQUAL时，前缀范围为[GREATEREQUAL，128]。 |

#### [使用实例](#ZH-CN_CONCEPT_0000001550280694)

增加IPv6前缀过滤器：

```
ADD IPV6PREFIXFILTERNODE:NAME="c",NODESEQUENCE=25,MATCHMODE=permit,ADDRESS="2001:DB8::",MASKLENGTH=128;
```
