# 设置本地分流共部署参数（SET COLOCATEDLBO）

- [命令功能](#ZH-CN_CONCEPT_0225895976__1.3.1.1)
- [注意事项](#ZH-CN_CONCEPT_0225895976__1.3.2.1)
- [操作用户权限](#ZH-CN_CONCEPT_0225895976__1.3.3.1)
- [参数说明](#ZH-CN_CONCEPT_0225895976__1.3.4.1)
- [使用实例](#ZH-CN_CONCEPT_0225895976__1.3.5.1)

#### [命令功能](#ZH-CN_CONCEPT_0225895976)

**适用NF：UPF**

![](设置本地分流共部署参数（SET COLOCATEDLBO）_25895976.assets/notice_3.0-zh-cn.png)

本命令属于高危命令，关闭ULCL分流功能ULCL分流会话会创建失败，业务不通。开启ULCL分流功能会导致设备性能下降。

该命令用于设置ULCL UPF和PSA UPF共部署的本地分流参数。此处PSA UPF可以是主锚点或辅锚点。

#### [注意事项](#ZH-CN_CONCEPT_0225895976)

- 该命令执行后只对之后发生承载更新的用户或者新激活用户生效。
- 该命令最大记录数为1。
- 设置ULCLSWITCH参数为ENABLE时，开启ULCL分流功能会导致UPF性能下降。
- 设置ULCLSWITCH参数为DISABLE时，会导致ULCL分流会话创建失败，业务不通。
- 该命令存在系统初始记录，参数的初始设置值如下表：

| 参数标识 | ULCLSWITCH |
| --- | --- |
| 初始值 | DISABLE |

#### [操作用户权限](#ZH-CN_CONCEPT_0225895976)

G_1，管理员级别命令组；G_2，操作员级别命令组

#### [参数说明](#ZH-CN_CONCEPT_0225895976)

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| ULCLSWITCH | ULCL功能开关 | 可选必选说明：可选参数<br>参数含义：该参数用于设置ULCL与PSA的共部署功能开关。<br>数据来源：本端规划<br>取值范围：枚举类型。<br>- DISABLE：不使能（关闭）。<br>- ENABLE：使能（开启）。<br>默认值：无<br>配置原则：无 |

#### [使用实例](#ZH-CN_CONCEPT_0225895976)

在需要配置ULCL和PSA合一设置功能时，执行该命令设置ULCL和PSA合一功能开启：

```
SET COLOCATEDLBO: ULCLSWITCH=ENABLE;
```
