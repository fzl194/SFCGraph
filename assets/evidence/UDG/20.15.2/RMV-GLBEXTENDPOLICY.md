# 删除全局扩展策略（RMV GLBEXTENDPOLICY）

- [命令功能](#ZH-CN_CONCEPT_0209678531__1.3.1.1)
- [注意事项](#ZH-CN_CONCEPT_0209678531__1.3.2.1)
- [操作用户权限](#ZH-CN_CONCEPT_0209678531__1.3.3.1)
- [参数说明](#ZH-CN_CONCEPT_0209678531__1.3.4.1)
- [使用实例](#ZH-CN_CONCEPT_0209678531__1.3.5.1)

#### [命令功能](#ZH-CN_CONCEPT_0209678531)

**适用NF：PGW-U、UPF**

该命令用于删除全局扩展策略。

#### [注意事项](#ZH-CN_CONCEPT_0209678531)

- 该命令执行后对新数据流生效。
- 该命令不支持批量删除。

#### [操作用户权限](#ZH-CN_CONCEPT_0209678531)

G_1，管理员级别命令组；G_2，操作员级别命令组

#### [参数说明](#ZH-CN_CONCEPT_0209678531)

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| EXTENDPLYTYPE | 扩展策略类型 | 可选必选说明：必选参数<br>参数含义：该参数用于设置扩展策略类型。<br>数据来源：本端规划<br>取值范围：枚举类型。<br>- TETHERING：表示在没有超规格的情况下对Tethering前后台进行控制。<br>- EXCEED_TETHERING：表示在超规格情况下对Tethering前后台进行控制。<br>默认值：无<br>配置原则：根据部署的业务策略选择相应的策略类型。 |
| SRVPROPNAME | 业务属性名称 | 可选必选说明：可选参数<br>参数含义：该参数用于指定业务属性名称。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～63。不支持空格，不区分大小写。<br>默认值：无<br>配置原则：设置的SRVPROPNAME必须是已经存在的业务属性名称。 |
| TETHERPLYTYPE | Tethering策略类型 | 可选必选说明：必选参数<br>参数含义：该参数用于设置Tethering策略类型。<br>数据来源：本端规划<br>取值范围：枚举类型。<br>- TETHERING_HOTSPOT：表示对tethering前台进行控制。<br>- TETHERING_TERMINAL：表示对没有超规格的tethering后台进行控制。<br>- EXCEED_TETHERING_TERMINAL：表示对超规格的tethering后台进行控制。<br>默认值：无<br>配置原则：根据部署的业务策略选择相应的策略类型。 |

#### [使用实例](#ZH-CN_CONCEPT_0209678531)

假如运营商希望删除一条全局扩展策略，扩展策略类型为TETHERING、业务属性为“srvprop”、Tethering策略类型为TETHERING_TERMINAL：

```
RMV GLBEXTENDPOLICY: EXTENDPLYTYPE=TETHERING, SRVPROPNAME="srvprop", TETHERPLYTYPE=TETHERING_TERMINAL;
```
