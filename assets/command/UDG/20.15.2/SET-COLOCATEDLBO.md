---
id: UDG@20.15.2@MMLCommand@SET COLOCATEDLBO
type: MMLCommand
name: SET COLOCATEDLBO（设置本地分流共部署参数）
nf: UDG
version: 20.15.2
verb: SET
object_keyword: COLOCATEDLBO
command_category: 配置类
applicable_nf:
- UPF
effect_mode: ''
is_dangerous: true
max_records: 1
category_path:
- 用户面服务管理
- 业务控制策略
- 业务控制公共配置
- 共部署的本地分流开关
status: active
---

# SET COLOCATEDLBO（设置本地分流共部署参数）

## 功能

**适用NF：UPF**

![](设置本地分流共部署参数（SET COLOCATEDLBO）_25895976.assets/notice_3.0-zh-cn.png)

本命令属于高危命令，关闭ULCL分流功能ULCL分流会话会创建失败，业务不通。开启ULCL分流功能会导致设备性能下降。

该命令用于设置ULCL UPF和PSA UPF共部署的本地分流参数。此处PSA UPF可以是主锚点或辅锚点。

## 注意事项

- 该命令执行后只对之后发生承载更新的用户或者新激活用户生效。
- 该命令最大记录数为1。
- 设置ULCLSWITCH参数为ENABLE时，开启ULCL分流功能会导致UPF性能下降。
- 设置ULCLSWITCH参数为DISABLE时，会导致ULCL分流会话创建失败，业务不通。
- 该命令存在系统初始记录，参数的初始设置值如下表：

| 参数标识 | ULCLSWITCH |
| --- | --- |
| 初始值 | DISABLE |

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| ULCLSWITCH | ULCL功能开关 | 可选必选说明：可选参数<br>参数含义：该参数用于设置ULCL与PSA的共部署功能开关。<br>数据来源：本端规划<br>取值范围：枚举类型。<br>- DISABLE：不使能（关闭）。<br>- ENABLE：使能（开启）。<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [[configobject/UDG/20.15.2/COLOCATEDLBO]] · 本地分流共部署参数（COLOCATEDLBO）

## 使用实例

在需要配置ULCL和PSA合一设置功能时，执行该命令设置ULCL和PSA合一功能开启：

```
SET COLOCATEDLBO: ULCLSWITCH=ENABLE;
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/设置本地分流共部署参数（SET-COLOCATEDLBO）_25895976.md`
