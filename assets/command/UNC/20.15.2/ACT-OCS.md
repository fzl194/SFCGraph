---
id: UNC@20.15.2@MMLCommand@ACT OCS
type: MMLCommand
name: ACT OCS（将备OCS的业务强制切换到主OCS）
nf: UNC
version: 20.15.2
verb: ACT
object_keyword: OCS
command_category: 动作类
applicable_nf:
- PGW-C
- SMF
effect_mode: 立即生效
is_dangerous: false
category_path:
- 业务服务管理
- 会话管理
- 计费管理
- 在线计费
- OCS Diameter连接
- OCS倒回
status: active
---

# ACT OCS（将备OCS的业务强制切换到主OCS）

## 功能

**适用NF：PGW-C、SMF**

该命令用于将备OCS的业务强制切换到主OCS。

## 注意事项

- 该命令执行后立即生效。
- 该命令只在OCS主备模式下生效。
- 指定的OCS必须是已经配置的OCS。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| OCSHOSTNAME | Ocs主机名称 | 可选必选说明：必选参数<br>参数含义：OCS主机名称。<br>数据来源：全网规划<br>取值范围：字符串类型，输入长度范围为1～127。不支持空格，由软参BIT150控制是否区分大小写。<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [[configobject/UNC/20.15.2/OCS]] · OCS（OCS）

## 使用实例

强制切换业务到名为“ocs-host-name”的主OCS：

```
ACT OCS:OCSHOSTNAME="ocs-host-name";
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/ACT-OCS.md`
