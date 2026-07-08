# 删除配置MODELC/D组网的SCP原因码控制（RMV RESULTCODESCP）

- [命令功能](#ZH-CN_MMLREF_0000002181322862__1.3.1)
- [注意事项](#ZH-CN_MMLREF_0000002181322862__1.3.2)
- [参数说明](#ZH-CN_MMLREF_0000002181322862__1.3.4)
- [使用实例](#ZH-CN_MMLREF_0000002181322862__1.3.5)

## [命令功能](#ZH-CN_MMLREF_0000002181322862)

**适用NF：SMF、PGW-C、GGSN**

此命令用来删除指定组网场景结果码控制信息。

## [注意事项](#ZH-CN_MMLREF_0000002181322862)

该命令执行后立即生效。

#### [操作用户权限](#ZH-CN_MMLREF_0000002181322862)

G_1，管理员级别命令组；G_2，操作员级别命令组

## [参数说明](#ZH-CN_MMLREF_0000002181322862)

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| PCCTEMPLATE | PCC模板名称 | 可选必选说明：必选参数<br>参数含义：该参数用于设置该返回码所绑定的PCC模板。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围是1~63。<br>默认值：无<br>配置原则：<br>如果配置为“global”则表示全局配置。<br>如果配置为非“global”，则必须是已经通过ADD PCCTEMPLATE配置过的PCC模板名称。 |
| MODELTYPE | 组网场景 | 可选必选说明：必选参数<br>参数含义：该参数用于设置该返回码所应用的组网场景。<br>数据来源：本端规划<br>取值范围：<br>- “MODELC（组网场景为ModelC）”：组网场景为ModelC<br>- “MODELD（组网场景为ModelD）”：组网场景为ModelD。<br>- “MODELC_D（组网场景为ModelC和ModelD）”：组网场景为ModelC和ModelD。<br>默认值：无<br>配置原则：无 |
| N7RESULTCODEVAL | N7返回码 | 可选必选说明：必选参数<br>参数含义：本参数用于配置N7返回码。<br>数据来源：对端协商<br>取值范围：字符串类型，输入长度范围是1~3。300-599中的一个值或者3xx、4xx、5xx，不区分大小写。其中xx代表一个范围，例如3xx代表300~399。<br>默认值：无<br>配置原则：<br>配置的单个的返回码落在一个范围内时，单个的优先级高。 |
| ERRINFO | 故障码对应的Protocol or application Error信息 | 可选必选说明：必选参数<br>参数含义：该参数用于指定自定义的故障码对应的Protocol or application Error信息。<br>数据来源：全网规划<br>取值范围：字符串类型，输入长度范围是0~128。如果配置为星号（*），表示通配，对该异常码携带所有Protocol or application Error信息都生效。参考3GPP协议29.500的Protocol or application Error。<br>默认值：无<br>配置原则：<br>（1）该参数只能由字母（A-Z或者a-z）、数字（0-9）、下划线（_）、星号（*）组成。该参数不区分大小写。<br>（2）配置为“*”，表示该异常码动作对于所有的Protocol or application Error信息都生效。 |

## [使用实例](#ZH-CN_MMLREF_0000002181322862)

删除PCC模板“pcctemplate”、间接路由模式为ModelC、ERRINFO为*、N7返回码为5xx的RESULTCODESCP返回码的控制信息：

```
RMV RESULTCODESCP: PCCTEMPLATE="pcctemplate", MODELTYPE=MODELC, ERRINFO="*", N7RESULTCODEVAL="5xx";
```
