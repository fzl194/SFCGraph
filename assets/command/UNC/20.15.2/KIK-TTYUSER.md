---
id: UNC@20.15.2@MMLCommand@KIK TTYUSER
type: MMLCommand
name: KIK TTYUSER（释放用户界面）
nf: UNC
version: 20.15.2
verb: KIK
object_keyword: TTYUSER
command_category: 调测类
effect_mode: 立即生效
is_dangerous: true
category_path:
- 平台服务管理
- VNRS功能管理
- 操作维护
- 接入配置管理
- TTY
- TTY用户信息
status: active
---

# KIK TTYUSER（释放用户界面）

## 功能

![](释放用户界面（KIK TTYUSER）_00441193.assets/notice_3.0-zh-cn_2.png)

本命令属于高危命令，操作不当会导致与指定用户界面的连接断开，请谨慎使用并联系华为技术支持协助操作。

该命令用于释放用户界面，用来断开与指定用户界面的连接。当管理员需要踢除某个用户界面时，可以使用该命令断开与某个用户界面的连接。

## 注意事项

- 该命令执行后立即生效。
- 该命令会断开与指定用户界面的连接。
- 该命令是高危命令，会断开与指定用户界面的连接。

## 权限

G_1，管理员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| INDEX | 接口编号 | 可选必选说明：必选参数<br>参数含义：该参数用于表示用户界面的接口编号。接口编号0到1为Console使用，接口编号34到54为VTY使用，接口编号100到119为SNetconf使用，接口编号200到229为MML使用。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围为0～229。<br>默认值：无 |

## 操作的配置对象

- [[configobject/UNC/20.15.2/TTYUSER]] · 用户信息（TTYUSER）

## 使用实例

释放用户界面：

```
KIK TTYUSER:INDEX=54;
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/释放用户界面（KIK-TTYUSER）_00441193.md`
