# 增加全局扩展策略（ADD GLBEXTENDPOLICY）

- [命令功能](#ZH-CN_CONCEPT_0209678509__1.3.1.1)
- [注意事项](#ZH-CN_CONCEPT_0209678509__1.3.2.1)
- [操作用户权限](#ZH-CN_CONCEPT_0209678509__1.3.3.1)
- [参数说明](#ZH-CN_CONCEPT_0209678509__1.3.4.1)
- [使用实例](#ZH-CN_CONCEPT_0209678509__1.3.5.1)

#### [命令功能](#ZH-CN_CONCEPT_0209678509)

**适用NF：PGW-U、UPF**

该命令用于添加全局的扩展策略，其中包含扩展策略类型、业务属性、Tethering控制粒度和对应的策略。经过运营商的报文根据其匹配结果执行对应策略。

#### [注意事项](#ZH-CN_CONCEPT_0209678509)

- 该命令执行后对新数据流生效。
- 该命令最大记录数为55。
- 当SET TETHERDETGLBPARA的STATISTICMETHOD参数设为CONFIG时，每个用户下Tethering节点的最大个数，按照UserProfile下TetheringMaxNum参数配置值加1申请。

#### [操作用户权限](#ZH-CN_CONCEPT_0209678509)

G_1，管理员级别命令组；G_2，操作员级别命令组

#### [参数说明](#ZH-CN_CONCEPT_0209678509)

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| EXTENDPLYTYPE | 扩展策略类型 | 可选必选说明：必选参数<br>参数含义：该参数用于设置扩展策略类型。<br>数据来源：本端规划<br>取值范围：枚举类型。<br>- TETHERING：表示在没有超规格的情况下对Tethering前后台进行控制。<br>- EXCEED_TETHERING：表示在超规格情况下对Tethering前后台进行控制。<br>默认值：无<br>配置原则：根据部署的业务策略选择相应的策略类型。 |
| SRVPROPNAME | 业务属性名称 | 可选必选说明：可选参数<br>参数含义：该参数用于指定业务属性名称。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～63。不支持空格，不区分大小写。<br>默认值：无<br>配置原则：最多可以绑定10个SERVICEPROP。 |
| TETHERPLYTYPE | Tethering策略类型 | 可选必选说明：必选参数<br>参数含义：该参数用于设置Tethering策略类型。<br>数据来源：本端规划<br>取值范围：枚举类型。<br>- TETHERING_HOTSPOT：表示对tethering前台进行控制。<br>- TETHERING_TERMINAL：表示对没有超规格的tethering后台进行控制。<br>- EXCEED_TETHERING_TERMINAL：表示对超规格的tethering后台进行控制。<br>默认值：无<br>配置原则：根据部署的业务策略选择相应的策略类型。 |
| POLICYNAME | 策略名称 | 可选必选说明：必选参数<br>参数含义：该参数用于设置策略名称。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～31。不支持空格，不区分大小写。<br>默认值：无<br>配置原则：设置的POLICYNAME必须是已经存在的策略名称。当前只支持带宽控制策略。 |

#### [使用实例](#ZH-CN_CONCEPT_0209678509)

假如运营商希望增加一个全局扩展策略，扩展策略类型为TETHERING、业务属性为“srvprop”、Tethering策略类型为TETHERING_TERMINAL，对应的策略为“ply”：

```
ADD GLBEXTENDPOLICY: EXTENDPLYTYPE=TETHERING, SRVPROPNAME="srvprop", TETHERPLYTYPE=TETHERING_TERMINAL, POLICYNAME="ply";
```
