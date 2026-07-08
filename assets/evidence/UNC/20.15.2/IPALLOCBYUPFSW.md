# 设置基于UPF的地址分配开关（SET IPALLOCBYUPFSW）

- [命令功能](#ZH-CN_MMLREF_0249644936__1.3.1)
- [注意事项](#ZH-CN_MMLREF_0249644936__1.3.2)
- [参数说明](#ZH-CN_MMLREF_0249644936__1.3.4)
- [使用实例](#ZH-CN_MMLREF_0249644936__1.3.5)

## [命令功能](#ZH-CN_MMLREF_0249644936)

**适用NF：PGW-C、SMF、GGSN**

配置基于UPF的IP地址分配功能开关。

## [注意事项](#ZH-CN_MMLREF_0249644936)

- 该命令执行后立即生效。

- 在每次执行ADD UPNODE命令时会自动为本命令增加一条记录，记录中参数的初始设置值如下：SWITCH：Inherit，NFINSTANCEID：UPNODE的NFINSTANCENAME。

#### [操作用户权限](#ZH-CN_MMLREF_0249644936)

G_1，管理员级别命令组；G_2，操作员级别命令组

## [参数说明](#ZH-CN_MMLREF_0249644936)

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| NFINSTANCEID | UPF实例标识 | 可选必选说明：必选参数<br>参数含义：该参数用于指定UPF实例标识。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围是0~255。<br>默认值：无。<br>配置原则：<br>该参数取值应与UPNODE中NFINSTANCENAME保持一致，使用该前需通过ADD UPNODE添加一组记录。 |
| SWITCH | 基于UPF的IPv4地址分配开关 | 可选必选说明：可选参数<br>参数含义：该参数用于指定基于UPF的IPv4地址分配功能开关。<br>数据来源：本端规划<br>取值范围：<br>- “DISABLE（去使能）”：不使用UPF所在的群组标识作为地址分配规则的匹配条件。<br>- “INHERIT（继承）”：继承SET IPALLOCBYUPFGLBSW命令的“基于UPF地址分配的全局开关”。<br>- “ENABLE（使能）”：使用UPF所在的群组标识作为地址分配规则的匹配条件。<br>默认值：无。执行命令并不输入该参数时，该参数保持系统当前配置不变，可通过LST IPALLOCBYUPFSW查询当前参数配置值。<br>配置原则：无 |
| IPV6SWITCH | 基于UPF的IPv6地址分配开关 | 可选必选说明：可选参数<br>参数含义：该参数用于指定基于UPF的IPV6地址分配功能开关。<br>数据来源：本端规划<br>取值范围：<br>- “DISABLE（去使能）”：不使用UPF所在的群组标识作为地址分配规则的匹配条件。<br>- “INHERIT（继承）”：继承SET IPALLOCBYUPFGLBSW命令的“基于UPF地址分配的全局开关”。<br>- “ENABLE（使能）”：使用UPF所在的群组标识作为地址分配规则的匹配条件。<br>默认值：无。执行命令并不输入该参数时，该参数保持系统当前配置不变，可通过LST IPALLOCBYUPFSW查询当前参数配置值。<br>配置原则：无 |

## [使用实例](#ZH-CN_MMLREF_0249644936)

使能名为“upf_instance_1”的UPF实例基于UPF分配地址：

```
SET IPALLOCBYUPFSW:NFINSTANCEID="upf_instance_1",SWITCH=ENABLE,IPV6SWITCH=ENABLE;
```
