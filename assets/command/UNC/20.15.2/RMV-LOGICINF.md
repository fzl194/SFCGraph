---
id: UNC@20.15.2@MMLCommand@RMV LOGICINF
type: MMLCommand
name: RMV LOGICINF（删除逻辑接口）
nf: UNC
version: 20.15.2
verb: RMV
object_keyword: LOGICINF
command_category: 配置类
applicable_nf:
- SGW-C
- PGW-C
- SMF
effect_mode: 立即生效
is_dangerous: true
category_path:
- 业务服务管理
- 接口管理
- 计费和策略接口管理
- 逻辑接口
status: active
---

# RMV LOGICINF（删除逻辑接口）

## 功能

**适用NF：SGW-C、PGW-C、SMF**

![](删除逻辑接口（RMV LOGICINF）_09896725.assets/notice_3.0-zh-cn_2.png)

本命令属于高危命令，此操作会删除逻辑接口，可能导致相关业务中断。

该命令用于删除指定的逻辑接口。

## 注意事项

- 该命令执行后立即生效。
- 删除的逻辑接口需为系统中存在的逻辑接口，否则命令执行失败。
- 若逻辑接口被某些对象绑定时，则不允许被删除掉。
- 逻辑接口配置不支持在主备SMF之间自动同步，需要在主备SMF上分别配置。
- 此操作会删除逻辑接口，可能导致相关业务中断。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| NAME | 逻辑接口名称 | 可选必选说明：必选参数<br>参数含义：该参数用于配置逻辑接口名称，确保逻辑接口的唯一性。<br>数据来源：全网规划<br>取值范围：字符串类型，输入长度范围为1～63。<br>默认值：无<br>配置原则：字符串形式，用户输入形式例如：gaif1/0/0。其中gaif为逻辑接口类型；1/0/0中第一个数字为组号，第二个数字为实例类型；第三个数字为逻辑接口号，各逻辑接口类型有各自的配置范围。 |

## 操作的配置对象

- [[configobject/UNC/20.15.2/LOGICINF]] · 逻辑接口（LOGICINF）

## 使用实例

删除逻辑接口gxif1/0/1：

```
RMV LOGICINF: NAME="gxif1/0/1";
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/删除逻辑接口（RMV-LOGICINF）_09896725.md`
