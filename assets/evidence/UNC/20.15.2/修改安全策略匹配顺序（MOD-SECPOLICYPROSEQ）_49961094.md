# 修改安全策略匹配顺序（MOD SECPOLICYPROSEQ）

- [命令功能](#ZH-CN_CONCEPT_0000001549961094__1.3.1.1)
- [注意事项](#ZH-CN_CONCEPT_0000001549961094__1.3.2.1)
- [操作用户权限](#ZH-CN_CONCEPT_0000001549961094__1.3.3.1)
- [参数说明](#ZH-CN_CONCEPT_0000001549961094__1.3.4.1)
- [使用实例](#ZH-CN_CONCEPT_0000001549961094__1.3.5.1)

#### [命令功能](#ZH-CN_CONCEPT_0000001549961094)

该命令用来修改安全策略匹配顺序。

#### [注意事项](#ZH-CN_CONCEPT_0000001549961094)

- 该命令执行后立即生效。
- 该命令仅适用于非NP卡场景和NP卡非加速模式场景。

#### [操作用户权限](#ZH-CN_CONCEPT_0000001549961094)

G_1，管理员级别命令组；G_2，操作员级别命令组

#### [参数说明](#ZH-CN_CONCEPT_0000001549961094)

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| SECPOLICYID | 安全策略编号 | 可选必选说明：必选参数<br>参数含义：安全策略号。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围为1～30。<br>默认值：无 |
| SECPROSEQWL | 安全白名单匹配顺序 | 可选必选说明：必选参数<br>参数含义：安全白名单匹配顺序。<br>数据来源：本端规划<br>取值范围：枚举类型。<br>- First：匹配优先级高。<br>- Second：匹配优先级中。<br>- Third：匹配优先级低。<br>默认值：无<br>配置原则：SECPROSEQWL/SECPROSEQBL/SECPROSEQUF三个参数值不能相同。 |
| SECPROSEQBL | 安全黑名单匹配顺序 | 可选必选说明：必选参数<br>参数含义：安全黑名单匹配顺序。<br>数据来源：本端规划<br>取值范围：枚举类型。<br>- First：匹配优先级高。<br>- Second：匹配优先级中。<br>- Third：匹配优先级低。<br>默认值：无<br>配置原则：SECPROSEQWL/SECPROSEQBL/SECPROSEQUF三个参数值不能相同。 |
| SECPROSEQUF | 安全用户流匹配顺序 | 可选必选说明：必选参数<br>参数含义：安全用户自定义流。<br>数据来源：本端规划<br>取值范围：枚举类型。<br>- First：匹配优先级高。<br>- Second：匹配优先级中。<br>- Third：匹配优先级低。<br>默认值：无<br>配置原则：SECPROSEQWL/SECPROSEQBL/SECPROSEQUF三个参数值不能相同。 |

#### [使用实例](#ZH-CN_CONCEPT_0000001549961094)

修改安全策略匹配顺序：

```
MOD SECPOLICYPROSEQ:SECPOLICYID=1,SECPROSEQWL=Third,SECPROSEQBL=Second,SECPROSEQUF=First;
```
